import streamlit as st

def show_alerts():

    st.subheader("⚠ Climate Risk Intelligence")

    st.success(
        "Climate Monitoring System is Active."
    )

    st.info(
        "Forecast generated using Prophet Time Series Model."
    )

    st.warning(
        "High temperatures may indicate Heatwave conditions."
    )

    st.error(
        "Heavy rainfall may increase Flood Risk."
    )