import os
import pandas as pd

def test_employees_missing_in_gtn():
    folder = os.path.dirname(__file__)
    gtn = pd.read_excel(os.path.join(folder, 'GTN.xlsx'))
    payrun = pd.read_excel(os.path.join(folder, 'Payrun.xlsx'))

    # Normalize column names
    gtn.columns = [col.strip().lower().replace(" ", "_") for col in gtn.columns]
    payrun.columns = [col.strip().lower().replace(" ", "_") for col in payrun.columns]

    # Ensure column exists after normalization
    assert 'employee_id' in gtn.columns, "Missing 'employee_id' in GTN"
    assert 'employee_id' in payrun.columns, "Missing 'employee_id' in Payrun"

    # Normalize ID values: to string, removing NaNs
    gtn_ids = pd.to_numeric(gtn['employee_id'], errors='coerce').dropna().astype(int).astype(str)
    payrun_ids = pd.to_numeric(payrun['employee_id'], errors='coerce').dropna().astype(int).astype(str)

    missing = set(payrun_ids) - set(gtn_ids)
    assert not missing, f"Employees in Payrun but missing in GTN: {missing}"
