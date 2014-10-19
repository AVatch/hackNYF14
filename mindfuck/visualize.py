import csv
import numpy as np
import matplotlib.pyplot as plt

chill03 = np.array(list(csv.reader(
                        open('chill03.csv'), delimiter=',')))
chill04 = np.array(list(csv.reader(
                        open('chill04.csv'), delimiter=',')))
chill05 = np.array(list(csv.reader(
                        open('chill05.csv'), delimiter=',')))
chill06 = np.array(list(csv.reader(
                        open('chill06.csv'), delimiter=',')))
chill07 = np.array(list(csv.reader(
                        open('chill07.csv'), delimiter=',')))

chill03_attn = []
for i in chill03:
    if i == []:
        continue
    chill03_attn.append(i[1])

chill04_attn = []
for i in chill04:
    if i == []:
        continue
    chill04_attn.append(i[1])

chill05_attn = []
for i in chill05:
    if i == []:
        continue
    chill05_attn.append(i[1])

chill06_attn = []
for i in chill06:
    if i == []:
        continue
    chill06_attn.append(i[1])

chill07_attn = []
for i in chill07:
    if i == []:
        continue
    chill07_attn.append(i[1])


###################################################

strain01 = np.array(list(csv.reader(
                        open('strain01.csv'), delimiter=',')))
strain03 = np.array(list(csv.reader(
                        open('strain03.csv'), delimiter=',')))
strain04 = np.array(list(csv.reader(
                        open('strain04.csv'), delimiter=',')))
strain05 = np.array(list(csv.reader(
                        open('strain05.csv'), delimiter=',')))
strain06 = np.array(list(csv.reader(
                        open('strain06.csv'), delimiter=',')))

strain01_attn = []
for i in strain01:
    if i == []:
        continue
    strain01_attn.append(i[1])

strain03_attn = []
for i in strain03:
    if i == []:
        continue
    strain03_attn.append(i[1])

strain04_attn = []
for i in strain04:
    if i == []:
        continue
    strain04_attn.append(i[1])

strain05_attn = []
for i in strain05:
    if i == []:
        continue
    strain05_attn.append(i[1])

strain06_attn = []
for i in strain06:
    if i == []:
        continue
    strain06_attn.append(i[1])



plt.plot(chill03_attn, label="chill 03")
plt.plot(chill04_attn, label="chill 04")
plt.plot(chill05_attn, label="chill 05")
plt.plot(chill06_attn, label="chill 06")


plt.plot(strain01_attn, label="strain 03")
plt.plot(strain03_attn, label="strain 04")
plt.plot(strain04_attn, label="strain 05")
plt.plot(strain05_attn, label="strain 06")


plt.legend(loc=1)
plt.grid()

plt.show()