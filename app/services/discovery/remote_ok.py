from app.models.source import ResearchSource
from app.services.discovery.base import DiscoveryProvider
from app.services.sources.remote_ok import RemoteOKSource


class RemoteOKDiscoveryProvider(DiscoveryProvider):
    def __init__(self):
        self.source = RemoteOKSource()

    def search(
        self,
        query: str,
        limit: int = 10
    ) -> list[ResearchSource]:

        if not query.strip():
            return []

        sources = self.source.fetch(limit=100)

        query_words = query.lower().split()
        results = []

        for item in sources:
            text = f"{item.title} {item.snippet}".lower()

            score = 0
            for word in query_words:
                if word in item.title.lower():
                    score += 3

                if word in item.snippet.lower():
                    score += 1

            if score > 0:
                item.score = score
                results.append(item)

        results.sort(
            key=lambda x: x.score,
            reverse=True
        )

        return results[:limit]