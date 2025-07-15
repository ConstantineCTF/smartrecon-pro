from plugins.base import BasePlugin
import aiohttp
import subprocess
from core.stealth import StealthManager

class SubdomainEnumPlugin(BasePlugin):
    async def run(self, domain: str, session: aiohttp.ClientSession, stealth: bool, offline: bool) -> dict:
        results = {"subdomains": []}
        if offline:
            results["subdomains"] = self.run_local_amass(domain)
        else:
            results["subdomains"].extend(self.run_amass(domain))
            if stealth:
                await StealthManager().delay()
            try:
                async with session.get(f"https://crt.sh/?q={domain}&output=json") as resp:
                    data = await resp.json()
                    results["subdomains"].extend([entry["name_value"] for entry in data])
            except Exception:
                pass  # Fallback to local results
        return results

    def run_amass(self, domain: str) -> list:
        try:
            result = subprocess.run(["amass", "enum", "-d", domain], capture_output=True, text=True, timeout=300)
            return result.stdout.splitlines()
        except Exception:
            return []