import pytest
import asyncio
from core.scanner import SmartRecon

@pytest.mark.asyncio
async def test_scanner_init():
    recon = SmartRecon("example.com", stealth=True, output_dir="./reports/output")
    assert recon.domain == "example.com"
    assert recon.stealth is True

@pytest.mark.asyncio
async def test_scan():
    recon = SmartRecon("example.com", offline=True)
    await recon.scan()
    assert isinstance(recon.results, dict)