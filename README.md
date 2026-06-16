# data--quality--portfolio

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
