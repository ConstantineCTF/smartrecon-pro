import random
import aiohttp
import json
import os
from typing import Optional

class StealthManager:
    def __init__(self):
        self.proxies = ["http://proxy1.com", "http://proxy2.com"]  # Load from config.yaml
        ua_path = os.path.join(os.path.dirname(__file__), "../config/user_agents.json")
        with open(ua_path, "r") as f:
            self.user_agents = json.load(f)

    def configure_session(self, session: aiohttp.ClientSession) -> aiohttp.ClientSession:
        session.headers.update({"User-Agent": random.choice(self.user_agents)})
        if self.proxies:
            session.proxy = random.choice(self.proxies)
        return session

    async def delay(self) -> None:
        await asyncio.sleep(random.uniform(0.5, 5.0))  # Poisson-like delay