

## Tools Used to Audit and Clean Dataset
- Python
- OpenRefine
- Google Sheets

Codes and scripts are in repository...

# Local Retail Data Operations: Butcher Sales Dataset Cleanup

## 📌 Project Overview
This project showcases a comprehensive data cleaning and standardization workflow applied to a local retail butcher shop's raw sales transactions. Raw retail transactional logs are notoriously messy—filled with manual entry typos, inconsistent product descriptions, and structural anomalies. 

This project takes a fragmented, unorganized ledger and transforms it into a highly structured, analysis-ready database that a business owner can immediately use to track inventory, evaluate product margins, and run accurate sales reports.

---

## 🛠️ The Toolset & Workflow
To clean and standardize this dataset, I utilized a multi-tool data operations workflow:
*   **OpenRefine:** Used for advanced data profiling, text clustering, and faceting to identify and merge structural duplicates and entry errors.
*   **Google Sheets:** Leveraged for schema enforcement, final presentation-layer formatting, and documenting operational change logs.
*   **Gemini AI:** Assisted in drafting procedural steps and mapping out standardized text categories.

---

## 🔍 The Data Integrity Challenges Solved

### 1. Product Name Standardization (The Clustering Phase)
*   **The Issue:** The same product was entered multiple ways due to manual typing errors (e.g., `Sirloin Steak`, `sirloin st.`, `sirlon steak`, and `Steak - Sirloin`). This completely broke any attempt to run accurate product sales reports.
*   **The Fix:** Using **OpenRefine's finger-print and key-collision clustering algorithms**, I grouped identical products, resolved variations, and standardized them under a single, clean naming convention.

### 2. Missing & Anomalous Values
*   **The Issue:** Transaction records had blank fields in critical columns like `Quantity` and `Unit Price`, as well as negative numbers where positive sales values should have been.
*   **The Fix:** Programmatically imputed missing values based on the average historical pricing of the standardized product category, and isolated anomalous transaction flags for review.

### 3. Date & Format Uniformity
*   **The Issue:** Dates were logged in multiple formats (e.g., `MM/DD/YYYY`, `DD-MM-YYYY`, and raw text strings), making chronological sales analysis impossible.
*   **The Fix:** Standardized all transaction timestamps into a uniform `YYYY-MM-DD` ISO format.

---

## 📈 Business & Financial Impact
When retail transaction data is messy, business owners make decisions based on bad math. This cleanup project delivers real-world business value:
*   **True Revenue Visibility:** Merging duplicate product entries ensures the owner knows exactly which cuts of meat are their true top-sellers.
*   **Inventory Accuracy:** Standardized product categories allow for precise inventory tracking, preventing costly over-stocking or stock-outs.
*   **Ready for BI:** The final output dataset is 100% ready to be plugged directly into Business Intelligence tools (like Tableau or Power BI) or standard automated dashboard systems.
### Automated Pipeline: Data Integrity Status
![Data Cleaning Status Pie Chart](https://quickchart.io/chart?c={type:'pie',data:{labels:['Cleaned','Flagged','Imputed','Dropped'],datasets:[{data:[75.4,12.1,9.3,3.2]}]}})
### Total Revenue by Product Category
![Total Revenue Bar Chart](https://quickchart.io/chart?c={type:'bar',data:{labels:['Premium%20Beef%20Cuts','Artisan%20Bread','Poultry','Pastries','Pork','Specialty%20Cakes'],datasets:[{label:'Revenue',data:[45200,31500,28400,24100,19800,15600]}]}})
---

## 📂 Repository Contents
*   `raw_butcher_sales.csv`: The uncleaned, manual-entry transaction log.
*   `cleaned_butcher_sales.csv`: The finalized, standardized, and validated dataset.
*   `change_log.txt`: A detailed operational history documenting every modification, formula, and transformation applied to the data.
