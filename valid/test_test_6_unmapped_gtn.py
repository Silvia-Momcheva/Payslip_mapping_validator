import os
import pandas as pd
import json

def test_gtn_elements_have_mapping():
    folder = os.path.dirname(__file__)
    gtn = pd.read_excel(os.path.join(folder, 'GTN.xlsx'))

    with open(os.path.join(folder, 'mapping.json')) as f:
        mapping = json.load(f)

    # Get mapped + not_used elements
    mapped = {v['vendor'] for v in mapping['mappings'].values() if v['map']}
    not_used = {v['vendor'] for v in mapping.get('not_used', [])}
    allowed = mapped.union(not_used)

    gtn.columns = [col.strip() for col in gtn.columns]
    gtn_elements = gtn.columns[4:]  # Elements expected after column 4

    unmapped = [col for col in gtn_elements if col not in allowed]
    assert not unmapped, f"GTN pay elements without mapping: {unmapped}"
