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

DATASET_PATH = "insurance.csv"
OUTPUT_DIR = "dashboard"

print("\nLoading dataset...")

df = load_dataset(file=DATASET_PATH)

print("Dataset loaded successfully.")

print("\nCleaning dataset...")

clean_df = data_clean(df)

print("Dataset cleaned successfully.")


print("\nGenerating metadata...")

metadata = get_metadata(clean_df)

print("Metadata generated successfully.")


print("\nGenerating chart recommendations using LLM...")

chart_configs = generate_charts(metadata=metadata)

print(f"{len(chart_configs)} chart recommendations generated.")


print("\nCreating charts...")

figures = create_charts(dataframe=clean_df, charts=chart_configs)

print(f"{len(figures)} charts created successfully.")


print("\nCombining charts into dashboard...")

dashboard = combine_figures(figures)

print("Dashboard created successfully.")


print("\nSaving dashboard image...")

dashboard_path = save_dashboard(save_path=OUTPUT_DIR, dashboard=dashboard)

print(f"Dashboard saved at: {dashboard_path}")

print("\nAnalyzing dashboard using Vision LLM...")

analysis = analyze_dashboard(dashboard_path)

print("\nDashboard Analysis:\n")

print(analysis)
