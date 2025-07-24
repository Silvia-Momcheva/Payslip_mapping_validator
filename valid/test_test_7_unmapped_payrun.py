import os
import pandas as pd
import json

def test_payrun_elements_have_mapping():
    folder = os.path.dirname(__file__)
    payrun = pd.read_excel(os.path.join(folder, 'Payrun.xlsx'))

    with open(os.path.join(folder, 'mapping.json')) as f:
        mapping = json.load(f)

    mapped = set(mapping['mappings'].keys())

    payrun.columns = [col.strip() for col in payrun.columns]

    # Filter columns starting from column 25, excluding unnamed and non-relevant
    excluded = {'Notes', 'Pay elements'}
    payrun_elements = [col for col in payrun.columns[25:]
                       if not col.startswith('Unnamed')
                       and col not in excluded]

    unmapped = [col for col in payrun_elements if col not in mapped]
    assert not unmapped, f"Payrun pay elements without mapping: {unmapped}"
