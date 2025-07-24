import os
import pandas as pd

def test_gtn_has_single_header():
    folder = os.path.dirname(__file__)
    gtn_path = os.path.join(folder, 'GTN.xlsx')
    
    # Зареждаме без зададен header – всички редове стават част от dataframe-а
    df = pd.read_excel(gtn_path, header=None)

    # Вземаме първия ред като header
    header = [str(cell).strip().lower() if pd.notnull(cell) else '' for cell in df.iloc[0]]

    # Сравняваме всеки от следващите 5 реда дали дублира header реда
    for i in range(1, min(5, len(df))):
        row = [str(cell).strip().lower() if pd.notnull(cell) else '' for cell in df.iloc[i]]
        if header == row:
            raise AssertionError(f"GTN file likely contains multiple header rows: duplicate found at row {i+1}")
