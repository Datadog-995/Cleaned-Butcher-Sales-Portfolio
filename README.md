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
