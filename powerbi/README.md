# Power BI dashboard

| File | Description |
|---|---|
| [`hr_attrition_dashboard.pbix`](hr_attrition_dashboard.pbix) | The dashboard (data imported from `data/processed/hr_attrition_scored.csv`) |
| [`screenshots/`](screenshots) | Screenshots of each report page |

## Data model

One table, `hr_attrition_scored`, with 10,000 rows (one row per employee), loaded from `data/processed/hr_attrition_scored.csv`. Band columns start with a number (`1. <60k`, `2. 60k-90k` and so on), so they sort in the right order. All columns are described in the [data dictionary](../docs/data_dictionary.md).

The measures are kept in a separate table called `Measures Table`.

## DAX measures

```DAX
Leavers             = SUM ( hr_attrition_scored[attrition_flag] )

Attrition Rate      = DIVIDE ( [Leavers], COUNT ( hr_attrition_scored[employee_id] ) )

High Risk Employees = CALCULATE ( COUNT ( hr_attrition_scored[employee_id] ), hr_attrition_scored[risk_points] >= 5 )
```

The Total Employees card counts `employee_id` and the Average Age card averages `age`. All measures react to the slicers, so selecting a department shows the attrition rate of that department.

## Pages

| Page | Content |
|---|---|
| **HR Overview** | Department buttons and business travel and overtime dropdowns (with a Clear all slicers button), cards for Total Employees, Leavers, High Risk Employees, Attrition Rate and Average Age, attrition-rate tables for job involvement, job satisfaction and work-life balance scores, charts by age band and by years since promotion, and a key findings panel |
| **Attrition Insights** | Charts by salary band and by distance from home, with a back button to page 1 |

## Validation

With no slicer selected, the cards match the Python results:

| Measure | Dashboard | Python |
|---|---|---|
| Total Employees | 10,000 | 10,000 |
| Leavers | 2,247 | 2,247 |
| Attrition Rate | 22.47% | 22.47% |
| High Risk Employees | 3,184 | 3,184 (5 or more risk points) |

## Reading the charts

The column charts by age band, years since promotion and salary band, and the line chart by distance from home, show the **number of leavers** in each group. Group sizes differ, so these counts do not show which group is riskier. For example, the 150k+ salary band has 2,912 employees against about 1,772 in each other band, so it has the most leavers, while its attrition rate is 22.6% against 22.4% for the other bands. Attrition **rates** are in the three score tables on page 1 and in the Python notebooks, where salary band (21.7% to 22.7%) and age band (21.2% to 23.2%) show almost no difference.

## Rebuild steps

1. **Home → Get data → Text/CSV**, load `data/processed/hr_attrition_scored.csv`, click **Load**.
2. **Home → Enter data** to create an empty table named `Measures Table`, then add the three measures above with **New measure**.
3. Build the visuals from the page table and the validation table above.
