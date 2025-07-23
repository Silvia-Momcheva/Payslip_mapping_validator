import os
import pandas as pd
import json

def test_payrun_elements_have_mapping():
    folder = os.path.dirname(__file__)
    gtn = pd.read_excel(os.path.join(folder, 'GTN.xlsx'))
    payrun = pd.read_excel(os.path.join(folder, 'Payrun.xlsx'))
    with open(os.path.join(folder, 'mapping.json')) as f:
        mapping = json.load(f)
    mapped = set(mapping['mappings'].keys())
    payrun_elements = payrun.columns[25:]
    unmapped = [col for col in payrun_elements if col not in mapped]
    assert not unmapped, f"Payrun pay elements without mapping: {unmapped}"
