# Payslip Mapping Validation Suite

This repository provides a suite of unit tests to validate that customer payroll data has been correctly mapped into the Payslip format. Mapping accuracy is critical to ensure data integrity before ingestion into the Payslip system.

The tests are written in **Python** using **Pandas** and **Pytest**, and they verify the structure, consistency, and correctness of data between:

- A customer-format Excel file (`GTN.xlsx`)
- The mapped Payslip-format Excel file (`Payrun.xlsx`)
- A JSON mapping file (`mapping.json`) describing the relationship between columns

## Folder Structure

Each test is located in its own folder under `tests/` with:

- GTN.xlsx
- Payrun.xlsx
- mapping.json
- test\_\*.py

## Tests

(1) The File is of type excel
(2) The GTN file contains line breaks i.e. empty lines
(3) The GTN file header structure has changed e.g. there are two header rows instead of one
(4) Employees are Present in the Payrun File but missing in the GTN file.
(5) Employees are Present in the GTN but missing in the Payrun File.
(6) Pay Elements in the GTN file do not have a mapping in the Payrun File.
(7) Pay Elements in the Payrun file do not have a mapping in the GTN File.
(8) For Pay Elements in the GTN file, the values have a numeric type.

## Project Structure

├── tests/ ← Test datasets where each test is designed to FAIL
│ └── test_X_name/ ← One folder per test
├── valid/ ← Clean dataset that PASSES all tests
├── requirements.txt
└── README.md

## Test Descriptions

Each test verifies a specific condition required for correct data mapping:

## Test No. Name Description

1 File Type Verifies that both GTN.xlsx and Payrun.xlsx exist and are Excel files.
2 Blank Lines Checks that there are no completely blank rows in the GTN file.
3 Multiple Headers Ensures the GTN file does not have duplicate headers (e.g. repeated row).
4 Missing in GTN Checks that all employees in Payrun also exist in the GTN file.
5 Missing in Payrun Checks that all employees in GTN exist in the Payrun file.
6 Unmapped GTN Columns Ensures all GTN pay elements have a corresponding mapping.
7 Unmapped Payrun Columns Ensures all Payrun pay elements have a corresponding mapping.
8 Non-Numeric GTN Values Validates that mapped numeric GTN columns contain only numeric values.

## How to Run the Tests

1. Install dependencies:

pip install -r requirements.txt

2. Run the tests:

pytest tests/

You should see 8 failed tests when run on the tests/ folder.

3. Run on valid data:

pytest valid/

You should see all tests passing.

## Requirements

Python 3.8+

Main libraries:
pandas
pytest

See requirements.txt for full list.

## Notes

Each test folder under tests/ contains modified versions of the files that intentionally trigger the respective failure.

The valid/ folder contains correctly mapped files that serve as the passing baseline.
