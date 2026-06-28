# Data Integrity Case Study: Butcher Shop Sales Optimization

## Executive Project Impact Summary
* **100% Data Integrity Enforced:** Zero transactional or revenue records were dropped or misclassified during programmatic processing.
* **Rapid Scale Execution:** Ingested, validated, and structural masks applied to the entire historical dataset in under 5 seconds.
* **Anomaly Resolution:** Successfully detected and flagged missing operational attributes across 3,600+ historical records without mutating core financial values.

## Pipeline Architecture
The pipeline ingests raw, unformatted transactional data from decentralized CSV exports, routing them through a multi-stage validation framework:
1. **Ingestion & Typage Enforcement:** Explicit schema casting to standardize currency, dates, and item IDs.
2. **Boolean Masking Matrix:** Multi-conditional logical checks to automatically isolate missing elements.
3. **Audit Log Generation:** Appends robust data quality flags to target rows for downstream operational review.

## 🔍 Visual Data Audit (Before & After Cleaning)
The images below illustrate the structural and categorical anomalies identified during the initial discovery phase alongside the successfully normalized production output.

### ❌ BEFORE: Raw Data Diagnostic
Look closely at the raw export below. The primary discovery pass flagged several critical structural and data-entry vulnerabilities:
* **Missing Operational Attributes:** Multiple records missing critical operational categories and IDs.
* **Inconsistent Records:** Inconsistent structural formatting across transactional sequences.

<img width="645" height="911" alt="Screenshot 2026-06-27 at 9 36 11 PM" src="https://github.com/user-attachments/assets/c7c2d681-1839-4c30-9c84-edea36f09499" />

###  AFTER: Normalized Production Output
The programmatic validation pipeline flawlessly restructured the dataset into a strict corporate master record:
* **Enforced Schema Integrity:** Standardized all transactional fields and missing elements cleanly resolved.
* **Production Readiness:** Operational attribute alignment completed without mutating core financial values.

<img width="759" height="941" alt="Screenshot 2026-06-27 at 9 35 13 PM" src="https://github.com/user-attachments/assets/40fd17be-7242-49a9-ac48-146cefdf0d7f" />
