
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mpl
import numpy as np


VersaoOriginal = [
[0.0020660000, 0.0015960000, 0.0012340000, 0.0012280000, 0.0010580000, 0.0010830000, 0.0010280000, 0.0010600000, 0.0009920000, 0.0010660000, 0.0010110000, 0.0010520000, 0.0014560000, 0.0009930000, 0.0009920000, 0.0010010000, 0.0023760000, 0.0013360000, 0.0009820000, 0.0009960000, 0.0009960000, 0.0010020000, 0.0009800000, 0.0009870000, 0.0013060000, 0.0010040000, 0.0010710000, 0.0009910000, 0.0009880000, 0.0009930000],
[0.0083030000, 0.0091290000, 0.0080250000, 0.0081890000, 0.0084460000, 0.0081460000, 0.0079180000, 0.0078960000, 0.0081610000, 0.0079100000, 0.0078940000, 0.0080120000, 0.0079050000, 0.0080040000, 0.0079310000, 0.0078840000, 0.0078970000, 0.0080370000, 0.0080350000, 0.0080390000, 0.0078650000, 0.0080040000, 0.0079140000, 0.0079100000, 0.0079040000, 0.0078790000, 0.0079170000, 0.0079530000, 0.0078620000, 0.0085610000],
[0.0270000000, 0.0265390000, 0.0265460000, 0.0264950000, 0.0267910000, 0.0265840000, 0.0267690000, 0.0265990000, 0.0270530000, 0.0264760000, 0.0264570000, 0.0269420000, 0.0286650000, 0.0367610000, 0.0279750000, 0.0276340000, 0.0277160000, 0.0271770000, 0.0271340000, 0.0281770000, 0.0266030000, 0.0264670000, 0.0266050000, 0.0267020000, 0.0265100000, 0.0269580000, 0.0269040000, 0.0264940000, 0.0264320000, 0.0265530000],
[0.1234470000, 0.1231200000, 0.1239500000, 0.1225290000, 0.1224760000, 0.1238180000, 0.1237390000, 0.1226870000, 0.1240700000, 0.1232360000, 0.1238640000, 0.1231620000, 0.1221850000, 0.1239120000, 0.1230190000, 0.1236640000, 0.1237480000, 0.1235000000, 0.1237520000, 0.1234700000, 0.1233980000, 0.1233860000, 0.1230870000, 0.1235240000, 0.1235330000, 0.1232320000, 0.1239680000, 0.1230360000, 0.1233860000, 0.1230150000]
]

Versao1 = [
[0.0010180000, 0.0010100000, 0.0010120000, 0.0010030000, 0.0010130000, 0.0010020000, 0.0010030000, 0.0010030000, 0.0010030000, 0.0010020000, 0.0010090000, 0.0011040000, 0.0010070000, 0.0010090000, 0.0009970000, 0.0010050000, 0.0009980000, 0.0010000000, 0.0010050000, 0.0010490000, 0.0010570000, 0.0009980000, 0.0010060000, 0.0009980000, 0.0010120000, 0.0011140000, 0.0009980000, 0.0010130000, 0.0010000000, 0.0010090000],
[0.0084270000, 0.0081880000, 0.0083710000, 0.0083730000, 0.0085570000, 0.0083490000, 0.0081650000, 0.0082130000, 0.0082730000, 0.0082600000, 0.0081920000, 0.0083020000, 0.0082130000, 0.0082250000, 0.0082050000, 0.0084900000, 0.0083640000, 0.0083760000, 0.0083830000, 0.0083240000, 0.0082900000, 0.0083000000, 0.0082320000, 0.0083450000, 0.0084420000, 0.0083240000, 0.0082740000, 0.0082480000, 0.0082690000, 0.0082850000],
[0.0278810000, 0.0278740000, 0.0275240000, 0.0275650000, 0.0276610000, 0.0276390000, 0.0275130000, 0.0275770000, 0.0276260000, 0.0280360000, 0.0275610000, 0.0276170000, 0.0275400000, 0.0275750000, 0.0278170000, 0.0275640000, 0.0275500000, 0.0276200000, 0.0275320000, 0.0275320000, 0.0274770000, 0.0277070000, 0.0275830000, 0.0275020000, 0.0275370000, 0.0275230000, 0.0275810000, 0.0280920000, 0.0277150000, 0.0279970000],
[0.1286020000, 0.1282320000, 0.1284480000, 0.1308740000, 0.1296410000, 0.1311650000, 0.1284550000, 0.1302000000, 0.1285250000, 0.1287870000, 0.1285490000, 0.1308580000, 0.1294930000, 0.1278090000, 0.1294010000, 0.1289380000, 0.1289940000, 0.1291090000, 0.1282300000, 0.1286310000, 0.1292060000, 0.1298480000, 0.1294580000, 0.1290930000, 0.1285060000, 0.1286590000, 0.1287970000, 0.1295080000, 0.1284390000, 0.1298210000]
]

Versao2 = [
[0.0059080000, 0.0059370000, 0.0054100000, 0.0056620000, 0.0052600000, 0.0052690000, 0.0050810000, 0.0057290000, 0.0054290000, 0.0052120000, 0.0065010000, 0.0070700000, 0.0077580000, 0.0052330000, 0.0050800000, 0.0053370000, 0.0069460000, 0.0066560000, 0.0051980000, 0.0064430000, 0.0051360000, 0.0064500000, 0.0051660000, 0.0066130000, 0.0072700000, 0.0066720000, 0.0066840000, 0.0065930000, 0.0072620000, 0.0067490000],
[0.0431790000, 0.0420980000, 0.0410090000, 0.0428650000, 0.0462570000, 0.0623800000, 0.0533920000, 0.0449050000, 0.0479120000, 0.0423290000, 0.0433650000, 0.0525380000, 0.0431030000, 0.0435320000, 0.0485170000, 0.0415850000, 0.0436630000, 0.0444580000, 0.0436260000, 0.0446180000, 0.0515090000, 0.0485740000, 0.0480210000, 0.0455640000, 0.0487900000, 0.0477580000, 0.0441860000, 0.0419260000, 0.0398420000, 0.0459890000],
[0.1450400000, 0.1445380000, 0.1578570000, 0.1459880000, 0.1615480000, 0.1435620000, 0.1428160000, 0.1487110000, 0.1447070000, 0.1503590000, 0.1504610000, 0.1449330000, 0.1474920000, 0.1427320000, 0.1461920000, 0.1452790000, 0.1481440000, 0.1417240000, 0.1437400000, 0.1500500000, 0.1438790000, 0.1457340000, 0.1442700000, 0.1502030000, 0.1466060000, 0.1521320000, 0.1492590000, 0.1511680000, 0.1507680000, 0.1724530000],
[0.7759610000, 0.7600260000, 0.7629880000, 0.7382150000, 0.7387830000, 0.7329550000, 0.7387340000, 0.7375500000, 0.7346810000, 0.7321820000, 0.7422270000, 0.7535060000, 0.7470070000, 0.7457270000, 0.7714930000, 0.7463900000, 0.8263800000, 0.7476010000, 0.7455890000, 0.7482170000, 0.7440520000, 0.7448650000, 0.7655790000, 0.7410440000, 0.7402910000, 0.7501110000, 0.7329710000, 0.7315400000, 0.7280240000, 0.7267110000]
]

Versao3 = [
[0.0013600000, 0.0013670000, 0.0013630000, 0.0013620000, 0.0013700000, 0.0013450000, 0.0013720000, 0.0013480000, 0.0013650000, 0.0013450000, 0.0013860000, 0.0014330000, 0.0013420000, 0.0013560000, 0.0013360000, 0.0013530000, 0.0013560000, 0.0013500000, 0.0013970000, 0.0013490000, 0.0013740000, 0.0013860000, 0.0013520000, 0.0014090000, 0.0013940000, 0.0014160000, 0.0014020000, 0.0013520000, 0.0013910000, 0.0013510000],
[0.0108300000, 0.0108380000, 0.0107320000, 0.0107900000, 0.0107110000, 0.0107630000, 0.0107140000, 0.0107510000, 0.0107360000, 0.0112220000, 0.0113080000, 0.0109920000, 0.0110140000, 0.0107460000, 0.0111220000, 0.0109370000, 0.0108730000, 0.0106810000, 0.0107230000, 0.0107270000, 0.0109150000, 0.0109400000, 0.0109900000, 0.0109540000, 0.0108840000, 0.0109520000, 0.0107270000, 0.0108440000, 0.0108430000, 0.0108210000],
[0.0381670000, 0.0376760000, 0.0382640000, 0.0378630000, 0.0389090000, 0.0376760000, 0.0387950000, 0.0383800000, 0.0396700000, 0.0381620000, 0.0382190000, 0.0382430000, 0.0390060000, 0.0383350000, 0.0386000000, 0.0383630000, 0.0382350000, 0.0385630000, 0.0379670000, 0.0384820000, 0.0383100000, 0.0380400000, 0.0381430000, 0.0381560000, 0.0382690000, 0.0382290000, 0.0380970000, 0.0382060000, 0.0380470000, 0.0379380000],
[0.1833910000, 0.1815950000, 0.1811860000, 0.1825350000, 0.1797620000, 0.1831350000, 0.1837050000, 0.1831280000, 0.1786130000, 0.1873710000, 0.1779840000, 0.1845290000, 0.2511190000, 0.1843690000, 0.1803490000, 0.1771370000, 0.1840240000, 0.1947090000, 0.2013620000, 0.1971680000, 0.1852430000, 0.1860590000, 0.1822130000, 0.1806470000, 0.1795330000, 0.1795160000, 0.1798900000, 0.1845220000, 0.1842050000, 0.1812380000]
]


mediaVersaoOriginal = []
stdVersaoOriginal = []
mediaVersao1 = []
stdVersao1 = []

mediaVersao2 = []
stdVersao2 = []
mediaVersao3 = []
stdVersao3 = []

for i in range(4):
	mediaVersaoOriginal.append(np.mean(VersaoOriginal[i]))
	stdVersaoOriginal.append(np.std(VersaoOriginal[i]))
	mediaVersao1.append(np.mean(Versao1[i]))
	stdVersao1.append(np.std(Versao1[i]))

	mediaVersao2.append(np.mean(Versao2[i]))
	stdVersao2.append(np.std(Versao2[i]))
	mediaVersao3.append(np.mean(Versao3[i]))
	stdVersao3.append(np.std(Versao3[i]))

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(111)


## Média e desvio padrão ##

plt.errorbar(np.array(range(len(mediaVersaoOriginal)))*2, mediaVersaoOriginal, stdVersaoOriginal,label=r'Versão Original', color='#1F77B4', fmt='o', lw=1, capsize=4, markersize=8, markeredgecolor='#1F77B4', markerfacecolor='#8FBBD9')
plt.plot(np.array(range(len(mediaVersaoOriginal)))*2, mediaVersaoOriginal, color='#1F77B4',lw=2)

# plt.errorbar(np.array(range(len(mediaVersao1)))*2, mediaVersao1, stdVersao1,label=r'Versão 1', color='#D62728', fmt='s', lw=1, capsize=4, markersize=8, markeredgecolor='#D62728', markerfacecolor='#EA9393')
# plt.plot(np.array(range(len(mediaVersao1)))*2, mediaVersao1, color='#D62728',lw=2)


# plt.errorbar(np.array(range(len(mediaVersao2)))*2, mediaVersao2, stdVersao2,label=r'Versão 2', color='#2CA02C', fmt='v', lw=1, capsize=4, markersize=8, markeredgecolor='#2CA02C', markerfacecolor='#95CF95')
# plt.plot(np.array(range(len(mediaVersao2)))*2, mediaVersao2, color='#2CA02C',lw=2)

# plt.errorbar(np.array(range(len(mediaVersao3)))*2, mediaVersao3, stdVersao3,label=r'Versão 3', color='#FF7F0E', fmt='D', lw=1, capsize=4, markersize=8, markeredgecolor='#FF7F0E', markerfacecolor='#FFBF86')
# plt.plot(np.array(range(len(mediaVersao3)))*2, mediaVersao3, color='#FF7F0E',lw=2)



ax1.yaxis.grid(True, linestyle='-', linewidth=0.5, which='major', color='lightgrey',alpha=1.0)
# ax1.xaxis.grid(True, linestyle='-', linewidth=0.5, which='major', color='lightgrey',alpha=1.0)

fontSize=12

ax1.set_axisbelow(True)
# ax1.set_title('Titulo', fontsize=fontSize+3, fontweight='bold')
ax1.set_xlabel(r'Tamanho matriz', fontsize=fontSize+2)
ax1.set_ylabel('Tempo médio (em seg)', fontsize=fontSize+2)
ax1.xaxis.set_label_coords(0.5, -0.08)
ax1.set_facecolor('white')


handles, labels = ax1.get_legend_handles_labels()
leg = ax1.legend(handles, labels, bbox_to_anchor=(0.01, 0.98), loc=2, borderaxespad=0., fontsize=fontSize)
leg.get_frame().set_facecolor('#FFFFFF')
# plt.legend(title=r'Compilador')




ticks = ['500', '1000', '10000', '100000']
plt.xticks(range(0, len(ticks)*2, 2), ticks, fontsize=fontSize)
plt.yticks(fontsize=fontSize)
plt.xlim(-1, len(ticks)*2-1)
#plt.ylim(-10, 40)


plt.tight_layout()
# plt.show()

plt.savefig('GraficoPratica1.pdf',bbox_inches='tight')