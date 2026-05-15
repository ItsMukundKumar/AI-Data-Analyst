import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Dict
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from pathlib import Path


def create_charts(dataframe: pd.DataFrame, charts: List[Dict]) -> List[go.Figure]:

    figures = []
    for chart in charts:
        try:
            chart_type = chart.get("chart_type")
            if chart_type == "scatter":
                x = chart["x_axis"]
                y = chart["y_axis"]
                if x not in dataframe.columns or y not in dataframe.columns:
                    continue
                fig = px.scatter(dataframe, x=x, y=y, title=chart["title"])
                figures.append(fig)

            elif chart_type == "line":
                x = chart["x_axis"]
                y = chart["y_axis"]
                if x not in dataframe.columns or y not in dataframe.columns:
                    continue
                fig = px.line(dataframe, x=x, y=y, title=chart["title"])
                figures.append(fig)

            elif chart_type == "bar":
                x = chart["x_axis"]
                y = chart["y_axis"]
                if x not in dataframe.columns or y not in dataframe.columns:
                    continue
                fig = px.bar(dataframe, x=x, y=y, title=chart["title"])
                figures.append(fig)

            elif chart_type == "histogram":
                column = chart["column"]
                if column not in dataframe.columns:
                    continue
                fig = px.histogram(dataframe, x=column, title=chart["title"])
                figures.append(fig)

            elif chart_type == "pie":
                column = chart["column"]
                if column not in dataframe.columns:
                    continue
                fig = px.pie(dataframe, names=column, title=chart["title"])
                figures.append(fig)

            elif chart_type == "box":
                x = chart["x_axis"]
                y = chart["y_axis"]
                if x not in dataframe.columns or y not in dataframe.columns:
                    continue
                fig = px.box(dataframe, x=x, y=y, title=chart["title"])
                figures.append(fig)

            elif chart_type == "heatmap":
                columns = chart["columns"]
                valid_columns = [col for col in columns if col in dataframe.columns]
                if len(valid_columns) < 2:
                    continue
                corr = dataframe[valid_columns].corr()
                fig = ff.create_annotated_heatmap(
                    z=corr.values,
                    x=list(corr.columns),
                    y=list(corr.index),
                    annotation_text=corr.round(2).values,
                )
                fig.update_layout(title=chart["title"])
                figures.append(fig)

        except Exception:
            continue

    return figures


def combine_figures(figures):

    specs = []
    for fig in figures:
        trace_type = fig.data[0].type
        if trace_type == "pie":
            specs.append([{"type": "domain"}])
        else:
            specs.append([{"type": "xy"}])

    combined_fig = make_subplots(
        rows=len(figures),
        cols=1,
        specs=specs,
        subplot_titles=[fig.layout.title.text for fig in figures],
        vertical_spacing=0.08,
    )

    for i, fig in enumerate(figures, start=1):
        for trace in fig.data:
            combined_fig.add_trace(trace, row=i, col=1)

    combined_fig.update_layout(
        height=500 * len(figures), title="AI Data Analyst Dashboard", showlegend=False
    )

    return combined_fig


def save_dashboard(save_path: str, dashboard: go.Figure) -> str:

    save_dir = Path(save_path)
    save_dir.mkdir(parents=True, exist_ok=True)
    output_path = save_dir / "dashboard.png"
    dashboard.write_image(output_path)

    return str(output_path)
