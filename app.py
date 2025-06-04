import streamlit as st
from streamlit_antd_components import timeline

st.set_page_config(layout="wide")
st.title("Timeline of Events")

# Define events with descriptions and optional color/status
events = [
    {'content': 'Event B — 2022-10-09', 'color': 'red'},
    {'content': 'Event D — 2022-10-16', 'color': 'orange'},
    {'content': 'Event C — 2022-10-18', 'color': 'green'},
    {'content': 'Event A — 2022-10-20', 'color': 'blue'},
    {'content': 'Event E — 2022-10-25', 'color': 'cyan'},
    {'content': 'Event F — 2022-10-27', 'color': 'purple'},
]

st.subheader("Phase 1: Planning")
timeline([
    {'content': 'Kickoff Meeting — 2022-10-09'},
    {'content': 'Needs Assessment — 2022-10-16'},
])

st.subheader("Phase 2: Execution")
timeline([
    {'content': 'Deployment — 2022-10-20'},
    {'content': 'Testing — 2022-10-25'},
])

# Render timeline (newest at top with reverse=True)
timeline(items=events, reverse=True)


