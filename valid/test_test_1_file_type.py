import os
import pandas as pd
import json

def test_file_type():
    folder = os.path.dirname(__file__)
    gtn = pd.read_excel(os.path.join(folder, 'GTN.xlsx'))
    payrun = pd.read_excel(os.path.join(folder, 'Payrun.xlsx'))
    with open(os.path.join(folder, 'mapping.json')) as f:
        mapping = json.load(f)
    assert os.path.splitext('GTN.xlsx')[-1] in ['.xlsx', '.xls']
