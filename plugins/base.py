from abc import ABC, abstractmethod
import aiohttp
from typing import Dict

class BasePlugin(ABC):
    @abstractmethod
    async def run(self, domain: str, session: aiohttp.ClientSession, stealth: bool, offline: bool) -> Dict:
        pass