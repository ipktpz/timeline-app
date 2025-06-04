import streamlit as st
from streamlit_timeline import st_timeline
import pandas as pd

st.set_page_config(layout="wide")

# BEHG task data
df = pd.DataFrame([
    dict(Task="Einreichung des Überwachungsplans", Start='2025-01-01', Finish='2025-10-31'),
    dict(Task="Genehmigung des Überwachungsplans durch die DEHSt", Start='2025-01-01', Finish='2026-01-01'),
    dict(Task="Einreichung des Emissionsberichts für 2025", Start='2026-01-01', Finish='2026-01-31'),
    dict(Task="Einreichung des Prüfberichts", Start='2026-01-01', Finish='2026-03-31'),
    dict(Task="Abgabe der Emissionszertifikate", Start='2026-03-31', Finish='2026-04-30'),
    dict(Task="Einreichung des Überwachungsplans für 2026", Start='2026-01-01', Finish='2026-10-31'),
])

# Convert to timeline items
items = [
    {
        "id": i + 1,
        "content": row["Task"],
        "start": row["Start"],
        "end": row["Finish"]
    }
    for i, row in df.iterrows()
]

# Render interactive timeline
st.title("BEHG-Zeitplan")
timeline = st_timeline(items, groups=[], options={"stack": True, "showCurrentTime": True}, height="450px")

# Show selected task
st.subheader("Ausgewähltes Element")
st.write(timeline)

