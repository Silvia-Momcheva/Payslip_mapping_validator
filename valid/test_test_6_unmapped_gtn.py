import os
import pandas as pd
import json

def test_gtn_elements_have_mapping():
    folder = os.path.dirname(__file__)
    gtn = pd.read_excel(os.path.join(folder, 'GTN.xlsx'))
    payrun = pd.read_excel(os.path.join(folder, 'Payrun.xlsx'))
    with open(os.path.join(folder, 'mapping.json')) as f:
        mapping = json.load(f)
    mapped = {v['vendor'] for v in mapping['mappings'].values() if v['map']}
    gtn_elements = gtn.columns[4:]
    unmapped = [col for col in gtn_elements if col not in mapped]
    assert not unmapped, f"GTN pay elements without mapping: {unmapped}"
