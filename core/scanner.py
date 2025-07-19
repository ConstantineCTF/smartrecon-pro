import re
import asyncio
import aiohttp
from core.utils import validate_input, setup_logging
from plugins.subdomain_enum import subdomain_scan
from plugins.vuln_scan import vuln_scan
from plugins.cloud_discovery import cloud_discovery
from plugins.leak_checker import leak_checker

class Scanner:
    def __init__(self, target, plugins, stealth, output_dir):
        self.logger = setup_logging()
        self.target = target
        self.plugins = plugins.split(',') if plugins != 'all' else ['subdomain', 'vuln', 'cloud', 'leak']
        self.stealth = stealth
        self.output_dir = output_dir
        self.domain = None
        self.full_target = None
        self.path = None

    async def initialize(self):
        self.domain, self.full_target, self.path = await validate_input(self.target)

    async def run(self):
        self.logger.info(f"Starting scan for {self.full_target} (stealth={self.stealth})")
        await self.initialize()
        results = {}
        async with aiohttp.ClientSession() as session:
            if 'subdomain' in self.plugins or 'all' in self.plugins:
                if re.match(r'^(\d{1,3}\.){3}\d{1,3}$', self.domain):
                    self.logger.info("Skipping subdomain scan for IP address")
                    results['subdomains'] = []
                else:
                    results['subdomains'] = await subdomain_scan(self.domain, session, self.stealth, offline=False)
            if 'vuln' in self.plugins or 'all' in self.plugins:
                results['vulns'] = await vuln_scan(self.full_target, session, self.stealth, offline=False)
            if 'cloud' in self.plugins or 'all' in self.plugins:
                results['cloud'] = await cloud_discovery(self.full_target, session, self.stealth, offline=False)
            if 'leak' in self.plugins or 'all' in self.plugins:
                results['leaks'] = await leak_checker(self.full_target, session, self.stealth, offline=False)
        self.logger.info(f"Scan completed: {results}")
        return results