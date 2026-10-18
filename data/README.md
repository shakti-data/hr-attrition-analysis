# Data

| File | Description |
|---|---|
| `raw/HR_Attrition_dataset.csv` | Original file: 10,000 rows, 23 columns. It starts with a byte order mark, so it is read with `encoding="utf-8-sig"` |
| `processed/hr_attrition_clean.csv` | Output of notebook 01: renamed columns, `attrition_flag`, bands and data quality flags |
| `processed/hr_attrition_scored.csv` | Output of notebook 04: the clean file plus the eight risk flags, `risk_points` and `risk_band`. Used by Power BI |

**Source:** [HR_Attrition_dataset](https://www.kaggle.com/datasets/ankitrajmishra/hr-attrition-dataset) on Kaggle (ankitrajmishra). Check the licence shown on the Kaggle page before reusing the data.

The file has no column documentation. Salary and distance from home have no unit, and the 1 to 5 scores have no scale description.

See [`../docs/data_dictionary.md`](../docs/data_dictionary.md) for every column.
