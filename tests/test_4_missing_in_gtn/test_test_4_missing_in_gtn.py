import os
import pandas as pd
import json

def test_employees_missing_in_gtn():
    folder = os.path.dirname(__file__)
    gtn = pd.read_excel(os.path.join(folder, 'GTN.xlsx'))
    payrun = pd.read_excel(os.path.join(folder, 'Payrun.xlsx'))
    with open(os.path.join(folder, 'mapping.json')) as f:
        mapping = json.load(f)
    missing = set(payrun['Employee_ID'].astype(str)) - set(gtn['employee_id'].astype(str))
    assert not missing, f"Employees in Payrun but missing in GTN: {missing}"
