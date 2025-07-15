import aiodns
import asyncio
from typing import Optional

async def validate_domain(domain: str) -> str:
    resolver = aiodns.DNSResolver()
    try:
        await resolver.query(domain, "A")
        return domain
    except Exception as e:
        raise ValueError(f"Invalid domain: {domain} ({str(e)})")