"""Helper functions shared by the notebooks in this project."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "HR_Attrition_dataset.csv"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "outputs" / "figures"
TABLES = ROOT / "outputs" / "tables"

TARGET = "attrition_flag"   # 1 = employee left, 0 = employee stayed
ACCENT = "#d9534f"          # bars above the overall attrition rate
BASE = "#4c78a8"            # all other bars


# Factors used for the segment tables and the segment scatter plot (display name -> column)
SEGMENT_FACTORS = {
    "Department": "department",
    "Job role": "job_role",
    "Job level": "job_level",
    "Gender": "gender",
    "Marital status": "marital_status",
    "Education": "education",
    "Business travel": "business_travel",
    "Overtime": "overtime",
    "Environment satisfaction": "environment_satisfaction",
    "Work-life balance": "work_life_balance",
    "Job involvement": "job_involvement",
    "Job satisfaction": "job_satisfaction",
    "Years since promotion": "years_since_promotion",
    "Distance from home": "distance_band",
    "Age band": "age_band",
    "Salary band": "salary_band",
    "Tenure band": "tenure_band",
    "Salary hike band": "salary_hike_band",
}


def load_raw() -> pd.DataFrame:
    """Read the raw CSV. The file starts with a BOM, so utf-8-sig is required."""
    return pd.read_csv(RAW_FILE, encoding="utf-8-sig")


def load_clean() -> pd.DataFrame:
    return pd.read_csv(PROCESSED / "hr_attrition_clean.csv")


def rate_table(df: pd.DataFrame, col: str, target: str = TARGET) -> pd.DataFrame:
    """Employees, leavers, attrition rate (%) and lift for each value of `col`."""
    overall = df[target].mean()
    g = df.groupby(col, observed=True)[target].agg(employees="count", leavers="sum")
    g["attrition_rate_pct"] = (100 * g["leavers"] / g["employees"]).round(2)
    g["lift"] = ((g["leavers"] / g["employees"]) / overall).round(2)
    return g.reset_index()


def segment_table(df: pd.DataFrame, factors: dict, target: str = TARGET) -> pd.DataFrame:
    """Stack rate tables for many factors. `factors` maps a display name to a column."""
    total_leavers = df[target].sum()
    parts = []
    for name, col in factors.items():
        t = rate_table(df, col, target).rename(columns={col: "segment"})
        t["segment"] = t["segment"].astype(str)
        t.insert(0, "factor", name)
        parts.append(t)
    seg = pd.concat(parts, ignore_index=True)
    seg["share_of_leavers_pct"] = (100 * seg["leavers"] / total_leavers).round(2)
    seg["label"] = seg["factor"] + ": " + seg["segment"]
    return seg


def plot_rate(ax, table: pd.DataFrame, col: str, overall_pct: float, title: str, rotate: int = 0):
    """Bar chart of attrition rate with the overall rate as a dashed line."""
    rates = table["attrition_rate_pct"]
    colors = [ACCENT if r > overall_pct else BASE for r in rates]
    ax.bar(table[col].astype(str), rates, color=colors)
    ax.axhline(overall_pct, color="black", linestyle="--", linewidth=1)
    ax.set_title(title, fontsize=11, fontweight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Attrition rate (%)")
    for i, v in enumerate(rates):
        ax.text(i, v + 0.4, f"{v:.1f}", ha="center", fontsize=8)
    ax.tick_params(axis="x", rotation=rotate, labelsize=8)
    ax.set_ylim(0, max(rates.max() * 1.18, overall_pct * 1.5))


def savefig(fig, name: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / f"{name}.png", dpi=150, bbox_inches="tight")


def save_table(df: pd.DataFrame, name: str) -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    df.to_csv(TABLES / f"{name}.csv", index=False)
