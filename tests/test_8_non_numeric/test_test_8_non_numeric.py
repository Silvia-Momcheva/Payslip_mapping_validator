import os
import pandas as pd
import json

def test_gtn_values_are_numeric():
    folder = os.path.dirname(__file__)
    gtn = pd.read_excel(os.path.join(folder, 'GTN.xlsx'))
    payrun = pd.read_excel(os.path.join(folder, 'Payrun.xlsx'))
    with open(os.path.join(folder, 'mapping.json')) as f:
        mapping = json.load(f)

    mapped = {v['vendor'] for v in mapping['mappings'].values() if v['map']}
    non_numeric = []
    for col in mapped:
        if col in gtn.columns:
            if not pd.to_numeric(gtn[col], errors='coerce').notnull().all():
                non_numeric.append(col)

    assert not non_numeric, f"GTN elements not numeric: {non_numeric}"

