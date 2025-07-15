import asyncio
import aiohttp
from typing import List, Dict
from plugins.base import BasePlugin
from core.risk_scorer import RiskScorer
from core.stealth import StealthManager
from core.report_generator import ReportGenerator
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class SmartRecon:
    def __init__(self, domain: str, stealth: bool = False, output_dir: str = "./reports/output",
                 plugins: List[str] = ["all"], offline: bool = False):
        self.domain = domain
        self.stealth = stealth
        self.output_dir = output_dir
        self.offline = offline
        self.plugins: List[BasePlugin] = self.load_plugins(plugins)
        self.risk_scorer = RiskScorer()
        self.stealth_manager = StealthManager()
        self.results: Dict = {"subdomains": [], "vulns": [], "assets": [], "leaks": []}
        logging.info(f"Initialized SmartRecon for {domain} (stealth={stealth}, offline={offline})")

    def load_plugins(self, plugins: List[str]) -> List[BasePlugin]:
        from plugins import subdomain_enum, vuln_scan, cloud_discovery, leak_checker
        available = {
            "subdomain": subdomain_enum.SubdomainEnumPlugin(),
            "vuln": vuln_scan.VulnScanPlugin(),
            "cloud": cloud_discovery.CloudDiscoveryPlugin(),
            "leaks": leak_checker.LeakCheckerPlugin()
        }
        return [available[p] for p in plugins if p != "all"] or list(available.values())

    async def scan(self):
        async with aiohttp.ClientSession() as session:
            session = self.stealth_manager.configure_session(session)
            tasks = [plugin.run(self.domain, session, self.stealth, self.offline)
                     for plugin in self.plugins]
            plugin_results = await asyncio.gather(*tasks, return_exceptions=True)

            for result in plugin_results:
                if isinstance(result, dict):
                    self.results["subdomains"].extend(result.get("subdomains", []))
                    self.results["vulns"].extend(result.get("vulns", []))
                    self.results["assets"].extend(result.get("assets", []))
                    self.results["leaks"].extend(result.get("leaks", []))

            self.results["vulns"] = [self.risk_scorer.score(vuln) for vuln in self.results["vulns"]]
            logging.info(f"Scan completed: {len(self.results['subdomains'])} subdomains, "
                        f"{len(self.results['vulns'])} vulns, {len(self.results['assets'])} assets")

    def generate_report(self):
        generator = ReportGenerator(self.results, self.output_dir, self.domain)
        generator.generate_pdf()
        generator.generate_markdown()
        logging.info(f"Reports generated in {self.output_dir}")