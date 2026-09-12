from abc import ABC, abstractmethod


class DiscoveryProvider(ABC):

    @abstractmethod
    def search(self, query: str, limit: int = 10) -> list[dict]:
        """Search for sources relevant to a research query."""
        pass