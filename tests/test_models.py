from app.models.source import ResearchSource

def test_research_source():
    source = ResearchSource(
        title="Python Engineer",
        url="https://example.com/python",
        snippet="Python engineering position",
        source="sample",
        score=3,
    )

    assert source.title == "Python Engineer"
    assert source.url == "https://example.com/python"
    assert source.score == 3