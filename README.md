# Payslip Mapping Validation Suite

This repository provides unit tests to verify the integrity and correctness of payroll data mappings.

## Folder Structure

Each test is located in its own folder under `tests/` with:

- GTN.xlsx
- Payrun.xlsx
- mapping.json
- test\_\*.py

## Tests

1. File type is Excel
2. GTN file contains blank lines
3. GTN header has multiple rows
4. Missing employees in GTN
5. Missing employees in Payrun
6. GTN pay elements without mapping
7. Payrun elements without mapping
8. GTN pay elements with non-numeric values

## Usage

```bash
pip install -r requirements.txt
pytest
```
