import pandas as pan
csatorna = pan.read_excel('./data/2_3_8i.xls', skiprows = [0, 1, 2, 3], sheet_name = '2.3.8.')
csatorna = csatorna.drop(csatorna.columns[[1, 2, 3, 4, 5, 7, 8]], axis = 1)
print(csatorna)