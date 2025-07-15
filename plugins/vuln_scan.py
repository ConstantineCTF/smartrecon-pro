from plugins.base import BasePlugin
import aiohttp
import json
import os
from core.stealth import StealthManager

class VulnScanPlugin(BasePlugin):
    async def run(self, domain: str, session: aiohttp.ClientSession, stealth: bool, offline: bool) -> dict:
        results = {"vulns": []}
        nvd_path = os.path.join(os.path.dirname(__file__), "../data/nvd.json")
        if offline and os.path.exists(nvd_path):
            with open(nvd_path, "r") as f:
                results["vulns"] = json.load(f)[:10]  # Simulate offline CVE data
        else:
            if stealth:
                await StealthManager().delay()
            try:
                async with session.get(f"https://services.nvd.nist.gov/rest/json/cves/2.0") as resp:
                    data = await resp.json()
                    results["vulns"] = [
                        {"cve_id": item["cve"]["id"], "cvss_score": 7.5, "asset": domain, "public_poc": False}
                        for item in data["vulnerabilities"]
                    ][:10]  # Limit for demo
            except Exception:
                pass
        return results