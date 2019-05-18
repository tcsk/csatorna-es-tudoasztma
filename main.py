import pandas as pan
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure

csatorna = pan.read_excel('./data/2_3_8i.xls', skiprows = [0, 1, 2, 3], sheet_name = '2.3.8.')
csatorna = csatorna.drop(csatorna.columns[[1, 2, 3, 4, 5, 7, 8]], axis = 1)
csatorna = csatorna.rename(index = str, columns = {csatorna.columns[0]: 'ev', csatorna.columns[1]: 'kozseg%'})
print(csatorna)

figure(num = None, figsize = (8, 8), dpi = 80, facecolor = 'w', edgecolor = 'k')
plot.clf()
plot.xlabel('Ev')
plot.ylabel('Kozuzemi szennyvizgyujto-halozattal ellatott kozsegi lakasok aranya [%]')
plot.plot(csatorna['ev'], csatorna['kozseg%'])
plot.show()

asztma = pan.read_excel('./data/2_4_5i.xls', skiprows = [0, 1], sheet_name = '2.4.5.')
asztma = asztma.drop(asztma.columns[[1, 2, 3, 4, 5, 6, 7, 9]], axis = 1)
asztma = asztma.rename(index = str, columns = {asztma.columns[0]: 'ev', asztma.columns[1]: 'asztmasokSzama'})
print(asztma)

figure(num = None, figsize = (8, 8), dpi = 80, facecolor = 'w', edgecolor = 'k')
plot.clf()
plot.xlabel('Ev')
plot.ylabel('Nyilvantartott tudoasztmasok szama')
plot.plot(asztma['ev'], asztma['asztmasokSzama'])
plot.show()