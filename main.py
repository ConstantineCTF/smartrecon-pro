import asyncio
import argparse
from core.scanner import SmartRecon
from core.utils import validate_domain

async def main():
    parser = argparse.ArgumentParser(description="SmartRecon Pro: Enterprise-grade reconnaissance tool")
    parser.add_argument("domain", help="Target domain (e.g., target.com)")
    parser.add_argument("--stealth", action="store_true", help="Enable stealth mode")
    parser.add_argument("--output-dir", default="./reports/output", help="Output directory for reports")
    parser.add_argument("--plugins", default="all", help="Comma-separated plugins (e.g., subdomain,vuln)")
    parser.add_argument("--offline", action="store_true", help="Run in offline mode")
    args = parser.parse_args()

    try:
        domain = await validate_domain(args.domain)  # Fixed: Added await here
        recon = SmartRecon(
            domain=domain,
            stealth=args.stealth,
            output_dir=args.output_dir,
            plugins=args.plugins.split(",") if args.plugins != "all" else ["all"],
            offline=args.offline
        )
        await recon.scan()
        recon.generate_report()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())