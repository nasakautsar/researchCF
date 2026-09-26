from app.services.discovery.base import DiscoveryProvider
from app.models.source import ResearchSource


class DiscoveryPipeline:

    def __init__(self, provider: DiscoveryProvider):
        self.provider = provider

    def run(self, query: str, limit: int = 10) -> list[ResearchSource]:
        if not query.strip():
            return []

        return self.provider.search(
            query=query,
            limit=limit
        )