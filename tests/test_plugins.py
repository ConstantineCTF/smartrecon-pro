import pytest
import asyncio
from plugins.subdomain_enum import SubdomainEnumPlugin
from plugins.base import BasePlugin
import aiohttp

@pytest.mark.asyncio
async def test_subdomain_enum():
    plugin = SubdomainEnumPlugin()
    async with aiohttp.ClientSession() as session:
        result = await plugin.run("example.com", session, stealth=False, offline=True)
        assert isinstance(result, dict)
        assert "subdomains" in result