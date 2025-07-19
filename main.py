import argparse
import asyncio
from core.scanner import Scanner
from core.utils import setup_logging

async def main():
    parser = argparse.ArgumentParser(description="SmartRecon Pro - Advanced Recon Tool")
    parser.add_argument("target", help="Target URL, IP, or domain (e.g., http://127.0.0.1/dvwa)")
    parser.add_argument("--plugins", default="all", help="Plugins to run (e.g., subdomain,vuln,cloud,leak or all)")
    parser.add_argument("--stealth", action="store_true", help="Enable stealth mode")
    parser.add_argument("--output", default="reports/output", help="Output directory")
    args = parser.parse_args()

    logger = setup_logging()
    scanner = Scanner(args.target, args.plugins, args.stealth, args.output)
    await scanner.run()

if __name__ == "__main__":
    asyncio.run(main())