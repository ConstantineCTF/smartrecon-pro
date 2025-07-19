from plugins.base import BasePlugin
import aiohttp
import json
import os
from core.stealth import StealthManager
from bs4 import BeautifulSoup

class VulnScanPlugin(BasePlugin):
    async def run(self, target: str, session: aiohttp.ClientSession, stealth: bool, offline: bool) -> dict:
        logger = self.logger
        logger.info(f"Starting vuln scan on {target} (stealth={stealth}, offline={offline})")
        results = {"vulns": []}
        nvd_path = os.path.join(os.path.dirname(__file__), "../data/nvd.json")
        if offline and os.path.exists(nvd_path):
            with open(nvd_path, "r") as f:
                results["vulns"] = json.load(f)[:10]
        else:
            if stealth:
                await StealthManager().delay()
            try:
                async with session.get(target, timeout=10 if stealth else 30) as resp:
                    if resp.status == 200:
                        html = await resp.text()
                        soup = BeautifulSoup(html, 'html.parser')
                        if soup.find('title', string='DVWA'):
                            results["vulns"].append({'vuln': 'DVWA detected', 'url': target, 'cvss_score': 7.5, 'public_poc': False})
                    else:
                        logger.warning(f"Failed to access {target}: Status {resp.status}")
            except Exception as e:
                logger.error(f"Vuln scan error on {target}: {e}")
        logger.info(f"Vuln scan completed: {results}")
        return results