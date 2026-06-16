# data--quality--portfolio
crm data audit & cleaning portfolio using Python Pandas, Openrefine ,and Google Sheets .

## Butcher Shop Sales Data Transformation
Demonstrating data cleaning and enrichment for the butcher shop sales dataset.

### Data Comparison: Before vs After

**Before (Raw Uncleaned Data)**
| Date | Store | Product | Price | Quantity | Total Sales |
|---|---|---|---|---|---|
| 2025-12-30 | The Little Bull | Skirt Steak | $105.09 | 3 | |

**After (Cleaned Data)**
| Date | Store | Product | Price | Quantity | Total Sales | Audit Notes |
|---|---|---|---|---|---|---|
| 2025-12-30 | The Little Bull | Skirt Steak | $105.09 | 3 | $315.27 | Calculated missing Total Sales |

### Detailed Step-by-Step Data Transformation Breakdown

1. **Store Name Cleanup (Whitespace):** `value.trim()` - Removes leading and trailing spaces from store names to ensure consistent grouping.
2. **Store Name Standardization (Casing):** `value.toTitlecase()` - Converts store names to Title Case for uniform presentation.
3. **Product Name Cleanup (Whitespace):** `value.trim()` - Eliminates accidental spaces in product entries.
4. **Product Name Standardization (Casing):** `value.toTitlecase()` - Standardizes product labels across the dataset.
5. **Reverse-Engineering Price:** `cells["Total Sales"].value / cells["Quantity"].value` - Recalculates unit prices where the original price field was missing but total sales and quantity were present.
6. **Conditional Total Sales Calculation:** `if(isNull(value), cells["Price"].value * cells["Quantity"].value, value)` - Dynamically populates missing Total Sales values only when the cell is empty, using the product of Price and Quantity.
7. **Currency Character Removal:** `value.replace("$", "").replace(",", "")` - Strips non-numeric characters from price strings to allow for mathematical operations.
8. **Numeric Type Conversion:** `value.toNumber()` - Casts string-based currency values into numeric formats for calculation.
9. **Currency Re-formatting:** ` "$" + value.format("%.2f")` - Restores the currency symbol and ensures two-decimal place precision for financial reporting.
10. **Audit Note Generation:** `if(cells["Total Sales"].value == null, "Calculated missing Total Sales", "Verified")` - Flagging rows where transformations were applied for audit transparency.
