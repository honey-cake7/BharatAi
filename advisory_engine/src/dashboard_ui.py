import streamlit as st
import json
import os

st.set_page_config(page_title="Edge QC Assistant", layout="wide")
st.title("Edge Quality Control Assistant Dashboard")

log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../shared/telemetry_stream.jsonl"))

col1, col2 = st.columns(2)
col1.subheader("Live Telemetry Events")
col2.subheader("Operator Guidance")

if os.path.exists(log_path):
    with open(log_path, "r") as f:
        events = [json.loads(line) for line in f.readlines() if line.strip()]
    if events:
        latest = events[-1]
        col1.json(latest)
        col2.metric("Anomaly Score", latest["anomaly_score"])
        col2.warning(f"Detected Defect: {latest['defect_characteristics']['category']}")
    else:
        st.info("No defect events registered yet.")
else:
    st.info("Waiting for vision pipeline to initialize...")
