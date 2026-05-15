from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.data_process import get_metadata, load_dataset
from google import genai
from PIL import Image
from typing import List, Dict
import json
import os
import plotly.graph_objects as go
import streamlit as st
from google.genai import types
import io

load_dotenv()


def _load_groq_llm():
    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        api_key=st.secrets["GROQ_API_KEY"],  # type: ignore
        max_tokens=4000,
        max_retries=2,
    )


def generate_charts(metadata : dict) -> List[Dict]:
    llm = _load_groq_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are an expert data analyst and visualization recommendation engine.
                Your task is to analyze dataset metadata and return ONLY chart recommendations in STRICT JSON format.
                CRITICAL RULES:
                1. Return ONLY valid JSON
                2. Do NOT return markdown
                3. Do NOT return explanations
                4. Do NOT return comments
                5. Do NOT return text before or after JSON
                6. Output MUST be parseable using json.loads()
                7. Avoid duplicate or redundant charts
                8. Recommend only meaningful charts
                9. Use only columns present in metadata
                10. Use chart types only from the allowed list
                11. Never hallucinate column names
                12. Prefer high-information visualizations
                ALLOWED CHART TYPES:
                - line
                - bar
                - scatter
                - histogram
                - pie
                - box
                - heatmap
                CHART SELECTION RULES:
                1. scatter
                - Use ONLY for numeric vs numeric columns
                2. histogram
                - Use ONLY for a single numeric column
                3. line
                - Use ONLY when x-axis is datetime, sequential, or continuous numeric
                4. bar
                - Use for categorical vs numeric
                - Or categorical count comparison
                5. pie
                - Use ONLY for low-cardinality categorical columns
                - Avoid pie charts with many unique values
                6. box
                - Use for numeric distribution comparison
                - Prefer categorical vs numeric combinations
                7. heatmap
                - Use ONLY when multiple numeric columns exist
                - Use for correlation visualization
                STRICT OUTPUT FORMAT:
                [
                {{
                    "chart_type": "scatter",
                    "x_axis": "age",
                    "y_axis": "salary",
                    "title": "Age vs Salary"
                }},
                {{
                    "chart_type": "histogram",
                    "column": "salary",
                    "title": "Salary Distribution"
                }}
                ]
                FIELD RULES:
                1. scatter / line / bar / box
                Required fields:
                - chart_type
                - x_axis
                - y_axis
                - title
                2. histogram / pie
                Required fields:
                - chart_type
                - column
                - title
                3. heatmap
                Required fields:
                - chart_type
                - columns
                - title
                Example heatmap:
                {{
                "chart_type": "heatmap",
                "columns": ["age", "salary", "experience"],
                "title": "Correlation Heatmap"
                }}
                ADDITIONAL CONSTRAINTS:
                - Maximum 8 chart recommendations
                - Minimum 3 chart recommendations if possible
                - Do not recommend the same column combination twice
                - Titles must be concise and human readable
                - Prefer charts that reveal trends, relationships, distributions, or correlations
                - Ignore columns with extremely high missing values if metadata indicates it
                - Avoid charts using identifier columns like id, uuid, serial_number
                Dataset metadata:
                {metadata}""",
            )
        ]
    )
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"metadata": metadata})
    response = response.replace("```json", "")
    response = response.replace("```", "")
    
    charts = json.loads(response)

    return charts


client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

def analyze_dashboard(image_path: str) -> str:

    image = Image.open(image_path)

    # Convert image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="PNG")

    image_part = types.Part.from_bytes(
        data=img_byte_arr.getvalue(),
        mime_type="image/png"
    )

    prompt = """
    You are an expert data analyst.

    Analyze this dashboard and provide:

    1. Key trends
    2. Correlations
    3. Outliers
    4. Distribution insights
    5. Business insights
    6. Potential anomalies
    7. Suggested next analysis

    Keep the response structured and concise.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt,
            image_part
        ]
    )

    return response.text        # type: ignore
