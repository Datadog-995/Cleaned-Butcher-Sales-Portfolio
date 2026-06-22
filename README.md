### 📍 Project Roadmap & Navigation

To provide full visibility into this data audit and cleaning lifecycle, please follow this step-by-step roadmap:

* **Step 1: Inspect the Full Dataset (100k+ Rows)** – Due to the large volume of production records, the interactive cleaning sandbox is hosted externally.
    * 👉 [Access the Interactive Google Sheets Sandbox](https://docs.google.com/spreadsheets/d/12dPNYDKRLjWn3hQruQNvAbuJ9qVUmFiw_45jtcc-fhA/edit?usp=sharing)*(Review the 'Before' and 'After' tabs to see structural transformations).*
* **Step 2: Review Technical Rules & Scope** – Scroll down this page to view the explicit data validation criteria, schema enforcement rules, and business case.
* **Step 3: View the Programmatic Pipeline** – Open the [`Cleaned-Butcher_sales.ipynb`](Cleaned-Butcher_sales.ipynb) notebook in this repository to review the Python/Pandas code that automates these checks.

---

# Retail Data Integrity & Quality Engineering Pipeline

## 📊 Business Case & Project Overview
In retail operations, messy transactional data can severely skew revenue forecasting, supply chain planning, and financial audits. This portfolio project showcases a production-ready data cleaning and validation pipeline built to ingest, audit, and clean an unformatted retail dataset containing **3,600+ historical butcher shop transactions**.

The primary objective was to transform raw, anomaly-ridden CSV text into a reliable database asset by programmatically isolating structural errors, enforcing data types, and flagging missing operational audit checkpoints.

---

## 🛠️ Technical Stack & Tools
* **Python (Pandas):** Engineered the core automated data validation masks and conditional flagging architecture.
* **OpenRefine (JSON Architecture):**基因 Generated structural mapping arrays used during the initial mass schema restructuring, string alignment, and whitespace trimming.
* **Google Colab:** Used as an interactive notebook environment for step-by-step pipeline execution and analysis.
* **GitHub:** Maintained version control and hosted the public-facing interactive data assets for client review.

---

## 🚀 Data Quality Rules Enforced

### 1. Automated Anomaly Tracking (Boolean Masking)
Instead of drop-deleting critical financial transactions that were missing operational dates—which would result in unrecorded revenue—the pipeline applies a custom Python Boolean mask to isolate empty or null values:
```python
missing_date_mask = df['Date'].isna() | (df['Date'].astype(str).str.strip() == '')
df.loc[missing_date_mask, 'Audit Notes'] = '🚨 Missing Date - Flagged for Review'# data--quality--portfolio

crm data audit & cleaning portfolio using Python Pandas, Openrefine ,and Google Sheets .

## Butcher Shop Sales Data Transformation

Demonstrating data cleaning and enrichment for the butcher shop sales dataset.

### Data Comparison: Before vs After

| Data Quality Category | State | Date | Store | Product | Price | Qty | Total Sales | Audit Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Mathematical & Financial Reconciliation** | Raw | 2025-12-30 | The Little Bull | Skirt Steak | $105.09 | 3 | | |
| | Cleaned | 2025-12-30 | The Little Bull | Skirt Steak | $105.09 | 3 | $315.27 | Calculated missing Total Sales |
| **2. Missing Structural Data** | Raw | 2025-12-31 | Unknown | Ribeye | $85.00 | 2 | $170.00 | |
| | Cleaned | 2025-12-31 | Happy Cow | Ribeye | $85.00 | 2 | $170.00 | Resolved 'Unknown' store |
| **3. Schema & Syntax Standardization** | Raw | 2026-01-01 |  butcher shop  | filet mignon | $50.00 | 1 | $50.00 | |
| | Cleaned | 2026-01-01 | Butcher Shop | Filet Mignon | $50.00 | 1 | $50.00 | Standardized casing & spaces |

### Detailed Step-by-Step Data Transformation Breakdown

1. **Store Name Cleanup (Whitespace):** `value.trim()` - Removes leading and trailing spaces from store names to ensure consistent grouping.
2. **Store Name Standardization (Casing):** `value.toTitlecase()` - Converts store names to Title Case for uniform presentation.
3. **Product Name Cleanup (Whitespace):** `value.trim()` - Eliminates accidental spaces in product entries.
4. **Product Name Standardization (Casing):** `value.toTitlecase()` - Standardizes product labels across the dataset.
5. **Reverse-Engineering Price:** `cells["Total Sales"].value / cells["Quantity"].value` - Recalculates unit prices where the original price field was missing but total sales and quantity were present.
6. **Conditional Total Sales Calculation:** `if(isNull(value), cells["Price"].value * cells["Quantity"].value, value)` - Dynamically populates missing Total Sales values only when the cell is empty, using the product of Price and Quantity.
7. **Currency Character Removal:** `value.replace("$", "").replace(",", "")` - Strips non-numeric characters from price strings to allow for mathematical operations.
8. **Numeric Type Conversion:** `value.toNumber()` - Casts string-based currency values into numeric formats for calculation.
9. **Currency Re-formatting:** `"$ " + value.format("%.2f")` - Restores the currency symbol and ensures two-decimal place precision for financial reporting.
10. **Audit Note Generation:** `if(cells["Total Sales"].value == null, "Calculated missing Total Sales", "Verified")` - Flagging rows where transformations were applied for audit transparency.

## Business Impact & ROI Analysis

By implementing automated data quality audits, the organization can achieve:
- **Reduced Operational Costs:** Minimizing manual data cleaning efforts.
- **Improved Decision Making:** Providing high-integrity data for executive reporting.
- **Risk Mitigation:** Identifying and correcting errors before they affect downstream pipelines.
