import re
import asyncio

async def validate_domain(domain: str) -> str:
    if not domain:
        raise ValueError("Domain cannot be empty")
    domain = domain.strip().lower()
    if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9\-\.]*\.[a-zA-Z]{2,}$', domain):
        raise ValueError("Invalid domain format")
    return domain