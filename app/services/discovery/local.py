import json
from pathlib import Path

from .base import DiscoveryProvider


class LocalDiscoveryProvider(DiscoveryProvider):

    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)

    def search(self, query: str, limit: int = 10) -> list[dict]:
        with open(self.dataset_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        query_words = query.lower().split()

        results = []

        for item in data:
            text = " ".join([
                item.get("title", ""),
                item.get("snippet", "")
            ]).lower()

            score = sum(
                1 for word in query_words
                if word in text
            )

            if score > 0:
                results.append({
                    **item,
                    "score": score
                })

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results[:limit]