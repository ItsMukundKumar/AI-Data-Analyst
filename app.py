import streamlit as st
import pandas as pd

from core.data_process import (
    load_dataset,
    data_clean,
    get_metadata,
)

from core.llm_engine import (
    generate_charts,
    analyze_dashboard,
)

from core.charts import (
    create_charts,
    combine_figures,
    save_dashboard,
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(page_title="AI Data Analyst", layout="wide")


# ---------------- TITLE ---------------- #

st.title("AI Data Analyst")
st.caption("Upload a dataset and generate AI-powered charts and insights.")


# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload Dataset", type=["csv", "xlsx", "xls", "json", "parquet"]
)


# ---------------- MAIN PIPELINE ---------------- #

if uploaded_file:

    try:

        # ---------- LOAD DATA ---------- #

        with st.spinner("Loading dataset..."):

            df = load_dataset(uploaded_file) # type: ignore

        st.success("Dataset loaded successfully.")

        # ---------- PREVIEW ---------- #

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        # ---------- CLEAN DATA ---------- #

        with st.spinner("Cleaning dataset..."):

            clean_df = data_clean(df)

        # ---------- METADATA ---------- #

        metadata = get_metadata(clean_df)

        # ---------- DATASET INFO ---------- #

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", metadata["rows"])
        col2.metric("Columns", metadata["columns"])
        col3.metric(
            "Numeric Columns", len(clean_df.select_dtypes(include="number").columns)
        )

        # ---------- GENERATE CHARTS ---------- #

        with st.spinner("Generating chart recommendations..."):

            chart_configs = generate_charts(metadata)

        st.subheader("Generated Chart Configurations")

        st.json(chart_configs)

        # ---------- CREATE CHARTS ---------- #

        with st.spinner("Creating charts..."):

            figures = create_charts(dataframe=clean_df, charts=chart_configs)

        # ---------- DISPLAY CHARTS ---------- #

        st.subheader("Generated Charts")

        for fig in figures:

            st.plotly_chart(fig, use_container_width=True)

        # ---------- COMBINE DASHBOARD ---------- #

        with st.spinner("Creating dashboard..."):

            dashboard = combine_figures(figures)

            dashboard_path = save_dashboard(save_path="outputs", dashboard=dashboard)

        # ---------- AI ANALYSIS ---------- #

        with st.spinner("Generating AI insights..."):

            analysis = analyze_dashboard(dashboard_path)

        # ---------- SHOW ANALYSIS ---------- #

        st.subheader("AI Dashboard Analysis")

        st.markdown(analysis)

    except Exception as e:

        st.error(f"Error: {str(e)}")
