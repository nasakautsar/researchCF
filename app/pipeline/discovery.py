from app.services.discovery.base import DiscoveryProvider


class DiscoveryPipeline:

    def __init__(self, provider: DiscoveryProvider):
        self.provider = provider

    def run(self, query: str, limit: int = 10) -> list[dict]:
        if not query.strip():
            return []

        return self.provider.search(
            query=query,
            limit=limit
        )