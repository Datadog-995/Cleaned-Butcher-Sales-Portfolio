# Quality Data Solutions: Butcher Shop Sales Data Cleaning & Audit

This repository contains a comprehensive data cleaning pipeline for a retail butcher shop sales dataset. It demonstrates how to transform raw, inconsistent daily sales logs into a clean, structured format ready for inventory analysis and revenue reporting.

## 📊 Repository Structure & Components

### 1. Raw Dataset (`raw_butcher_sales.csv`)
* **Status:** Untouched / Raw Input Data
* **Description:** The original, uncleaned daily sales logs containing missing values, inconsistent formatting, and unstandardized inventory categories (e.g., mixed text cases for meat cuts).

### 2. Cleaned Output (`cleaned_butcher_sales.csv`)
* **Status:** Pristine / Production-Ready Output
* **Description:** The final polished dataset. All product names are standardized to Title Case, missing entries are resolved, whitespace is stripped, and formatting anomalies have been fully removed.

---

## 🛠️ Data Cleaning Footprint

The core data integrity steps applied to this dataset include:
* **Text Standardization:** Applied whitespace trimming and standardized product categories (e.g., merging inconsistent manual entries into uniform product families).
* **Data Auditing:** Flagged and cleaned anomalous weight and price entries to ensure accurate downstream revenue calculations.
* **Formatting:** Restructured the file into a clean, strictly formatted CSV ready for direct database upload or BI tool ingestion.
