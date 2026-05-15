import pandas as pd
import numpy as np
from pathlib import Path

path = "insurance.csv"

from pathlib import Path
import pandas as pd


def load_dataset(file):

    ext = Path(file.name).suffix.lower()
    if ext == ".csv":
        return pd.read_csv(file)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(file)
    elif ext == ".json":
        return pd.read_json(file)
    elif ext == ".parquet":
        return pd.read_parquet(file)
    elif ext == ".txt":
        return pd.read_table(file)
    else:

        raise ValueError(f"Unsupported file format: {ext}")


def data_clean(dataframe: pd.DataFrame) -> pd.DataFrame:
    df = dataframe.copy()
    df = df.dropna(how="all")
    df = df.drop_duplicates()
    df.columns = df.columns.str.strip()
    object_cols = df.select_dtypes(include=["object"]).columns

    for col in object_cols:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace("", pd.NA)
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df


def get_metadata(dataframe: pd.DataFrame) -> dict:
    numeric_cols = dataframe.select_dtypes(include="number")
    return {
        "rows": dataframe.shape[0],
        "columns": dataframe.shape[1],
        "column_names": dataframe.columns.tolist(),
        "dtypes": {col: str(dtype) for col, dtype in dataframe.dtypes.items()},
        "missing_values": dataframe.isnull().sum().to_dict(),
        "numeric_summary": (
            numeric_cols.describe().round(2).to_dict() if not numeric_cols.empty else {}
        ),
        "sample_data": dataframe.head(3).to_dict(orient="records"),
    }
