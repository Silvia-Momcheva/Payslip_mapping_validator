import os
import pandas as pd
import json


gtn_blank = pd.DataFrame(employees)

# Уверяваме се, че има поне 3 реда (индекси 0, 1, 2)
while len(gtn_blank) < 3:
    gtn_blank.loc[len(gtn_blank)] = [None] * len(gtn_blank.columns)

# Зануляваме ред 3 (индекс 2)
gtn_blank.loc[2] = [None] * len(gtn_blank.columns)

# Записваме файловете
write_files("test_data/test_2_line_breaks", gtn_blank, pd.DataFrame(payrun), mapping)
