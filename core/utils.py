import re
from urllib.parse import urlparse
import logging
import asyncio

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger()

async def validate_input(input_str: str) -> tuple[str, str, str]:
    logger = setup_logging()
    logger.info(f"Validating input: {input_str}")
    if not input_str:
        logger.error("Input cannot be empty")
        raise ValueError("Input cannot be empty")
    input_str = input_str.strip().lower()
    if input_str.startswith(('http://', 'https://')):
        parsed = urlparse(input_str)
        domain = parsed.hostname
        path = parsed.path
        if not domain:
            logger.error("No hostname found in URL")
            raise ValueError("Invalid URL: No hostname found")
    else:
        domain = input_str
        path = ''
    domain_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9\-\.]*\.[a-zA-Z]{2,}$'
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not (re.match(domain_pattern, domain) or re.match(ip_pattern, domain)):
        logger.error(f"Invalid domain or IP format: {domain}")
        raise ValueError("Invalid domain or IP format")
    logger.info(f"Validated: domain={domain}, path={path}")
    return domain, input_str, path