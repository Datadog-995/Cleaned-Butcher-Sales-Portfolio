
# Client Review: Script Summary of Data Cleaning & Validation

This document outlines the data cleaning process applied to the `Sheet 1-1-RAW_DATA_ORIGINAL no-shows.csv` dataset. The goal of this cleaning pipeline is to ensure data quality, consistency, and readiness for further analysis or model building.

---

#### 1. Data Loading and Initial Setup

*   **Cell `HxwBFZpvKY6Q`**: Downloads the raw dataset from KaggleHub and loads it into `df_raw`. This ensures we start with the original data.
*   **Cell `3jMss6cJMcz_`**: Uploads the user-cleaned CSV (e.g., from OpenRefine) into `df_openrefine`, which is our primary working DataFrame.

---

#### 2. Core Data Cleaning and Standardization

*   **Cell `h0azHjo9NFW9`**: Formats the `PatientId` column to ensure it is a clean string, converting from potential float or scientific notation.
*   **Cell `mrOw6zsfNaOA`**: Extracts `Appointment_Date` and `Appointment_Time` from the original `AppointmentDay` column.
*   **Cell `JCHqDAIhNrM_`**: Standardizes the `AppointmentDay` column itself to contain only the date part.
*   **Cell `b7534446`**: Splits `ScheduledDay` into `Scheduled_Date` and `Scheduled_Time` columns.
*   **Cell `f1a90d4d`**: Removes the original `ScheduledDay` column, as its components are now in separate, more usable columns.
*   **Cell `1fZZSj1_N8iS`**: Adds an `Audit Age` column, initially copying `Age`, to prepare for anomaly flagging.
*   **Cell `KdU83HPvPZ1g`**: Filters the `Audit Age` column to flag only ages that are less than 0 or greater than 100, setting others to `None`.
*   **Cell `XxF4YgvvQFmW`**: Standardizes the `Neighbourhood` column by stripping whitespace, converting to Title Case, and renaming it to `Neighborhood`.
*   **Cell `fq5bg8v0SdU1`**: Creates and refines a `Wait Time Audit` column to specifically flag operational errors where the appointment day occurred before the scheduled day.
*   **Cell `sN17AjPPRtXF`**: Renames `Handcap` to `Handicap` and standardizes its values to binary (0 or 1).

---

#### 3. Data Validation and Overview

*   **Cell `2b3857b8`**: Displays descriptive statistics for all numerical columns in `df_openrefine`, providing a quantitative summary.
*   **Cell `8cdbf8f0`**: Shows value counts for key categorical columns, helping to identify distribution and potential inconsistencies.
*   **Cell `c85770d3`**: Verifies the data types of all columns in `df_openrefine`.
*   **Cell `1d50970c`**: Performs a final check for any remaining missing values (`NaN` or 'N/A' strings), confirming the effectiveness of our imputation steps.
*   **Cell `0a7dea7a`**: Generates visualizations (count plots) for top categories in categorical columns to visually inspect distributions.

### **1. Data Loading and Initial Setup**

**Description**: This step mounts Google Drive and loads the raw dataset into a DataFrame named `df`.

### **2. `PatientId` Standardization**

**Description**: The `PatientId` column was converted from a float type (which can appear in scientific notation) to an integer and then to a string to ensure consistent identification.

### **3. `AppointmentDay` Splitting and Removal**

**Description**: The original `AppointmentDay` column, which contained both date and time information, was split into separate `Appointment_Date` and `Appointment_Time` columns. The original column was then removed.

### **4. `Gender` Cleaning**

**Description**: Whitespace was stripped from `Gender` entries, and they were converted to uppercase. A check was performed to ensure only 'F' and 'M' values were present.

**Impact**: No invalid gender entries were found; all were 'F' or 'M'.

### **5. `Age > 99` Anomaly Flagging**

**Description**: An `Audit Age` column was created to flag rows where the `Age` was found to be greater than 99, indicating potential outliers or data entry errors.

**Impact**: 11 rows were flagged with `Age > 99`.

### **6. `Neighbourhood` Cleaning**

**Description**: The `Neighbourhood` column was cleaned by stripping whitespace and converting entries to Title Case for consistency. It also checked for and filled any empty cells.

**Impact**: No empty cells were found in `Neighbourhood`.

### **7. `No-show` Validation**

**Description**: The `No-show` column was standardized by stripping whitespace and converting entries to Title Case. It then validated that all entries were either 'Yes' or 'No'.

**Impact**: All entries in `No-show` were confirmed to be 'Yes' or 'No'; no invalid values were found.

### **8. Remaining Empty Cells Check**

**Description**: A final sweep was performed across all remaining columns to identify and fill any `NaN` values. Numeric columns were filled with their median, and categorical columns with 'Unknown'.

**Impact**: "No empty cells found in the remaining columns," indicating the data was already quite clean or previous steps handled most missing values.

### **9. Column Renaming for Consistency**

**Description**: Typographical errors in column names were corrected: `Hipertension` was renamed to `Hypertension`, and `Handcap` to `Handicap`.

### **10. `Age = 0` Anomaly Flagging**

**Description**: A new `Audit_Age_Zero` column was created to specifically flag rows where the `Age` was exactly 0, as this is an unusual value for medical appointment data.

**Impact**: 3539 rows were flagged with `Age = 0`.

### **11. Column Name Standardization to Snake_Case**

**Description**: All column names in the DataFrame were converted to `snake_case` (e.g., `PatientId` became `patient_id`, `No-show` became `no_show`). This step included a corrected function to prevent unintended extra underscores.

**Impact**: All 18 columns were successfully converted to snake_case. The final column names are: `['patient_id', 'appointment_id', 'gender', 'age', 'audit_age_zero', 'audit_age', 'neighbourhood', 'scholarship', 'hypertension', 'diabetes', 'alcoholism', 'handicap', 'sms_received', 'no_show', 'scheduled_date', 'scheduled_time', 'appointment_date', 'appointment_time']`.

### **12. Data Export**

**Description**: The fully cleaned DataFrame was saved to a CSV file named `cleaned_noshowappointments.csv`. This file was then backed up to your Google Drive and made available for direct download to your local machine.

---

This concludes the summary of the cleaning process and the corresponding code snippets. Let me know if you have any other questions!

