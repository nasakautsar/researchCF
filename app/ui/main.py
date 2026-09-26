import streamlit as st

from app.pipeline.discovery import DiscoveryPipeline
from app.services.discovery.local import LocalDiscoveryProvider


st.set_page_config(
    page_title="ResearchCF",
    page_icon="🔎",
    layout="wide",
)


st.title("🔎 ResearchCF")
st.caption("Local research discovery engine")


query = st.text_input(
    "What are you looking for?",
    placeholder="e.g. AI Python jobs",
)


if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a search query.")
    else:
        provider = LocalDiscoveryProvider(
            "data/sample/sources.json"
        )

        pipeline = DiscoveryPipeline(provider)

        results = pipeline.run(
            query=query,
            limit=5,
        )

        st.subheader(f"Results for: {query}")

        if not results:
            st.info("No results found.")
        else:
          st.subheader(f"{len(results)} results found")

          for item in results:
             st.markdown("---")

             st.markdown(f"### {item.title}")

             st.write(item.snippet)

             st.caption(f"Source: {item.source}")
             st.caption(f"Score: {item.score}")

             if item.url:
                st.markdown(f"[View source]({item.url})")