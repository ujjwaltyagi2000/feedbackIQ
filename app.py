# UI will be built here using Streamlit

import streamlit as st
import pandas as pd
import numpy as np

st.title("FeedbackIQ")

import streamlit as st

pages = [
    st.Page("pages/streaming.py", title="Feedback Streaming", icon="🚀"),
    st.Page("pages/agent.py", title="Agent", icon="🤖"),
    st.Page("pages/analytics.py", title="Insights", icon="📊"),
]

pg = st.navigation(pages, position="top")

pg.run()