# Data dictionary

## Source columns (renamed in notebook 01)

| Original name | Clean name | Meaning |
|---|---|---|
| `Employee_ID` | `employee_id` | Unique ID (1 to 10,000). Used only as a key |
| `Age` | `age` | Age in years (18-63) |
| `Attrition` | `attrition` | Yes = the employee left, No = the employee stayed |
| `Business_Travel` | `business_travel` | No Travel, Travel Rarely, Travel Frequently |
| `Department` | `department` | Cyber Security, Data Science, IT Services, Network Administration, Software Development |
| `Distance_From_Home` | `distance_from_home` | Distance from home to work (1-50, unit not stated) |
| `Education` | `education` | Below College, Degree, Graduation, Master's, PhD |
| `Environment_Satisfaction` | `environment_satisfaction` | Score 1-5 (assumed 5 = best) |
| `Gender` | `gender` | Female, Male |
| `Salary` | `salary` | Salary (30,078-199,989, currency and period not stated) |
| `Job_Involvement` | `job_involvement` | Score 1-5 (assumed 5 = best) |
| `Job_Level` | `job_level` | Level 1-8 |
| `Job_Role` | `job_role` | 12 roles, for example Developer, Manager, QA Analyst |
| `Job_Satisfaction` | `job_satisfaction` | Score 1-5 (assumed 5 = best) |
| `Marital_Status` | `marital_status` | Single, Married, Divorced |
| `Number_of_Companies_Worked_previously` | `companies_worked_before` | Number of earlier employers (0-10) |
| `Overtime` | `overtime` | Yes / No |
| `Salary_Hike_in_percent` | `salary_hike_pct` | Last salary hike in percent (0-100) |
| `Total_working_years_experience` | `total_experience_years` | Total years of work experience (0-20) |
| `Work_life_balance` | `work_life_balance` | Score 1-5 (assumed 5 = best) |
| `No_of_years_worked_at_current_company` | `years_at_company` | Years at the company (0-10) |
| `No_of_years_in_current_role` | `years_in_role` | Years in the current role (0-10) |
| `Years_since_last_promotion` | `years_since_promotion` | Years since the last promotion (0-8) |

## Columns added in notebook 01

| Column | Meaning |
|---|---|
| `attrition_flag` | **Target.** 1 = left, 0 = stayed |
| `flag_tenure_gt_experience` | 1 when years at the company are higher than total work experience |
| `flag_role_gt_tenure` | 1 when years in the role are higher than years at the company |
| `flag_promotion_gt_tenure` | 1 when years since promotion are higher than years at the company |
| `flag_experience_gt_working_age` | 1 when total experience is more than age minus 18 |
| `any_data_issue` | 1 when any of the four flags is 1 |
| `age_band` | 18-24, 25-34, 35-44, 45-54, 55+ |
| `salary_band` | <60k, 60k-90k, 90k-120k, 120k-150k, 150k+ |
| `tenure_band` | 0-1, 2-3, 4-5, 6-7, 8-10 years at the company |
| `distance_band` | <10, 10-19, 20-29, 30-39, 40+ |
| `promotion_band` | 0-1, 2-3, 4-5, 6-8 years since promotion |
| `salary_hike_band` | 0-24%, 25-49%, 50-74%, 75-100% |

Band labels start with a number (for example `1. <60k`) so they sort correctly in charts and in Power BI.

## Columns added in notebook 04

| Column | Meaning |
|---|---|
| `rf_low_environment_satisfaction` | 1 when environment satisfaction is 3 or lower |
| `rf_low_work_life_balance` | 1 when work-life balance is 2 or lower |
| `rf_low_job_involvement` | 1 when job involvement is 2 or lower |
| `rf_low_job_satisfaction` | 1 when job satisfaction is 2 or lower |
| `rf_no_recent_promotion` | 1 when 2 or more years since the last promotion |
| `rf_long_distance` | 1 when distance from home is 10 or more |
| `rf_frequent_travel` | 1 when the employee travels frequently |
| `rf_overtime` | 1 when the employee works overtime |
| `risk_points` | Sum of the eight `rf_` columns (0 to 8) |
| `risk_band` | Low (0-2), Medium (3-4), High (5-8) |
