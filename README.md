# <div align="center">AI Data Analyst</div>

<div align="center">

An AI-powered automated data analysis platform that generates visualizations, dashboards, and business insights from raw datasets using LLMs and Vision AI.

<br>

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit" />
<img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3f4f75?style=for-the-badge&logo=plotly" />
<img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Gemini-Vision%20AI-green?style=for-the-badge" />

</div>

---

# Preview

## Workflow

```text
Dataset Upload
      ↓
Data Cleaning
      ↓
Metadata Extraction
      ↓
LLM Chart Recommendation
      ↓
Automatic Chart Generation
      ↓
Dashboard Creation
      ↓
Vision AI Analysis
      ↓
Business Insights
```

---

# Features

<table>
<tr>
<td width="50%">

### Automated Data Processing

* Dataset cleaning
* Missing value handling
* Duplicate removal
* Metadata extraction
* Multi-format dataset support

</td>
<td width="50%">

### AI-Powered Analytics

* LLM-generated chart recommendations
* Automated dashboard generation
* Vision-based dashboard analysis
* Business insight generation
* Trend and anomaly detection

</td>
</tr>
</table>

---

# Supported File Formats

<div align="center">

| Format             | Supported |
| ------------------ | --------- |
| CSV                | Yes       |
| Excel (.xlsx/.xls) | Yes       |
| JSON               | Yes       |
| Parquet            | Yes       |
| TXT                | Yes       |

</div>

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* Python
* Pandas
* NumPy

## Visualization

* Plotly

## AI Models

* Groq LLM
* Gemini Vision

## Libraries

* LangChain
* Kaleido
* python-dotenv

---

# Project Structure

```bash
AI-Data-Analyst/
│
├── core/
│   ├── charts.py
│   ├── data_process.py
│   └── llm_engine.py
│
├── outputs/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/ItsMukundKumar/AI-Data-Analyst

cd AI-Data-Analyst
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Application Pipeline

<table>
<tr>
<th>Stage</th>
<th>Description</th>
</tr>

<tr>
<td>Dataset Upload</td>
<td>User uploads dataset through Streamlit UI</td>
</tr>

<tr>
<td>Data Cleaning</td>
<td>Removes duplicates, handles missing values, cleans columns</td>
</tr>

<tr>
<td>Metadata Extraction</td>
<td>Extracts dataset statistics and schema information</td>
</tr>

<tr>
<td>Chart Recommendation</td>
<td>Groq LLM recommends suitable visualizations</td>
</tr>

<tr>
<td>Chart Generation</td>
<td>Plotly creates interactive visualizations automatically</td>
</tr>

<tr>
<td>Dashboard Analysis</td>
<td>Gemini Vision analyzes dashboard screenshots</td>
</tr>

<tr>
<td>Business Insights</td>
<td>AI generates trends, anomalies, and recommendations</td>
</tr>

</table>

---

# Example AI Insights

The application can automatically generate:

* Trend analysis
* Correlation analysis
* Outlier detection
* Distribution insights
* Business recommendations
* Potential anomalies
* Suggested next analyses

---

# Future Improvements

* PDF report export
* Downloadable dashboards
* Chat with dataset
* SQL database integration
* Multi-file analysis
* Real-time analytics
* Advanced statistical engine
* RAG-based dataset querying

---

# Deployment

## Streamlit Community Cloud

Deploy directly using Streamlit Cloud.

1. Push project to GitHub
2. Open Streamlit Cloud
3. Connect repository
4. Add environment variables
5. Deploy

---

# Requirements

Example `requirements.txt`

```txt
streamlit
pandas
numpy
plotly
kaleido
python-dotenv
langchain
langchain-groq
langchain-google-genai
google-genai
openpyxl
pyarrow
```

---

# Author

<div align="center">

### Mukund Kumar

AI / ML Developer

</div>

---

# License

MIT License

---

# Star the Repository

If you found this project useful, consider giving it a star.
