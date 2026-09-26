from app.services.discovery.local import LocalDiscoveryProvider
from app.pipeline.discovery import DiscoveryPipeline
from app.services.discovery.remote_ok import RemoteOKDiscoveryProvider


def test_local_discovery():
    provider = LocalDiscoveryProvider(
        "data/sample/sources.json"
    )

    results = provider.search(
        "AI Python",
        limit=5
    )

    assert isinstance(results, list)
    assert len(results) > 0


def test_discovery_pipeline():
    provider = LocalDiscoveryProvider(
        "data/sample/sources.json"
    )

    pipeline = DiscoveryPipeline(provider)

    results = pipeline.run(
        "AI Python",
        limit=5
    )

    assert isinstance(results, list)
    assert len(results) > 0

def test_remote_ok_discovery():
    provider = RemoteOKDiscoveryProvider()

    results = provider.search(
        "python",
        limit=5
    )

    assert isinstance(results, list)
    assert len(results) > 0
    assert all(item.url for item in results)