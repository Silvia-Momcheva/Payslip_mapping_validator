import os
import pandas as pd
import json

def test_gtn_has_no_blank_lines():
    folder = os.path.dirname(__file__)
    gtn = pd.read_excel(os.path.join(folder, 'GTN.xlsx'), keep_default_na=False)
    blank_rows = gtn.apply(lambda row: all(str(cell).strip() == '' for cell in row), axis=1).sum()
    assert blank_rows == 0, f"GTN contains {blank_rows} blank rows"
