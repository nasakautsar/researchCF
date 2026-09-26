import re
import requests

from app.models.source import ResearchSource


class RemoteOKSource:
    API_URL = "https://remoteok.com/api"

    @staticmethod
    def clean_html(text: str) -> str:
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def fetch(self, limit: int = 20) -> list[ResearchSource]:
        response = requests.get(
            self.API_URL,
            headers={
                "User-Agent": "ResearchCF/1.0"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        results = []

        for item in data:
            # first item not job
            if "position" not in item:
                continue

            results.append(
                ResearchSource(
                    title=item.get("position", ""),
                    url=item.get("url", ""),
                    snippet=self.clean_html(
                        item.get("description", "")
                    ),
                    source="Remote OK",
                    score=0
                )
            )

            if len(results) >= limit:
                break

        return results