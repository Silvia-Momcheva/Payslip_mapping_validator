import os
import pandas as pd

def test_gtn_has_single_header():
    folder = os.path.dirname(__file__)
    gtn_path = os.path.join(folder, 'GTN.xlsx')
    
    df = pd.read_excel(gtn_path, header=None)
 
    header = [str(cell).strip().lower() if pd.notnull(cell) else '' for cell in df.iloc[0]]
 
    for i in range(1, min(5, len(df))):
        row = [str(cell).strip().lower() if pd.notnull(cell) else '' for cell in df.iloc[i]]
        if header == row:
            raise AssertionError(f"GTN file likely contains multiple header rows: duplicate found at row {i+1}")
