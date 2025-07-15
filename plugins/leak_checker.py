from plugins.base import BasePlugin
import aiohttp
from core.stealth import StealthManager

class LeakCheckerPlugin(BasePlugin):
    async def run(self, domain: str, session: aiohttp.ClientSession, stealth: bool, offline: bool) -> dict:
        results = {"leaks": []}
        if offline:
            return results  # No leaks in offline mode
        if stealth:
            await StealthManager().delay()
        try:
            # Placeholder: Check Pastebin for leaks
            async with session.get(f"https://pastebin.com/api_scraping.php?query={domain}") as resp:
                data = await resp.json()
                results["leaks"] = [
                    {"source": "pastebin", "content": item["full_content"], "date": item["date"]}
                    for item in data if domain in item["full_content"]
                ]
        except Exception:
            pass
        return results