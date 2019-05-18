import pandas as pan
csatorna = pan.read_excel('./data/2_3_8i.xls', skiprows = [0, 1, 2, 3], sheet_name = '2.3.8.')
print(csatorna)