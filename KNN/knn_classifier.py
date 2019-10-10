import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Input data - [SAT Score, GPA]
data = [[1360,2.4 ], [1540,2.7], [1600,2.6], [1400,2.5], [1520,2.5], [1380,2.1], [1420,2.3], [1490,2.3], [1510,2.4],
     [1350,3.9], [1500,2.9], [1440,2.5], [1380,3.7], [1430,2.1], [1420,3.9], [1430,3.4], [1450,3.7], [1350,2.0],
     [1430,3.0], [1540,3.7], [1370,3.8], [1490,3.7], [1520,3.5], [1300,3.1], [1360,2.9], [1460,3.3], [1510,3.4],
     [1340,2.9], [1590,2.9], [1320,2.5], [1380,2.6], [1400,2.1], [1540,2.4], [1310,2.7], [1410,2.1], [1305,2.5],
     [1590,3.9], [1360,3.7], [1300,3.5], [1320,3.6], [1400,2.7], [1540,3.4], [1350,3.1], [1560,3.3], [1305,3.9], 
     [1460,2.7], [1440,2.3], [1600,3.6], [1320,2.5], [1410,3.6], [1590,2.7], [1560,2.3], [1310,2.1], [1460,3.2]]

# Labels - Accepted or Rejected
label = ['rejected','accepted','accepted','rejected','accepted','rejected','rejected','accepted','accepted',
     'accepted','rejected','rejected','accepted','rejected','accepted','accepted','accepted','rejected',
     'rejected','accepted','rejected','accepted','accepted','rejected','rejected','accepted','accepted',
     'rejected','accepted','rejected','rejected','rejected','accepted','rejected','rejected','rejected',
     'accepted','accepted','accepted','rejected','rejected','accepted','rejected','accepted','rejected',
     'rejected','rejected','accepted','rejected','accepted','accepted','accepted','rejected','accepted']

datas = pd.DataFrame()
datas['data'] = data
datas['label'] = label
# print(datas)

datas_copy = datas.copy()
data_train = datas_copy.sample(frac=0.70, random_state=0)
data_test = datas_copy.drop(data_train.index)
print ('Data Training')
print (data_train)
print ('\nData Test')
print (data_test)


for i in range(len(data)):
    if label[i] == 'accepted':
        plt.scatter(data[i][0], data[i][1], linewidths = 2, color='red')
    else:
        plt.scatter(data[i][0], data[i][1], linewidths = 2, color='blue')
        
plt.plot()
plt.show()

def distance(data, label, x) :
  
    neigh = []
    for i in range(len(data)) :
        dis = np.sqrt(((x[0] - data[i][0]) ** 2) + ((x[1] - data[i][1]) ** 2))
        neigh.append([data[i][0], data[i][1], dis])
        arr_dis = sorted(neigh, key=lambda x: x[2])
    return arr_dis

def knn(data, label, x, k) :
    neighbor = []
    acc = 0
    rej = 0
    lab = []
    for i in range(k) :
        neighbor.append([distance(data,label,x)[i][0], distance(data,label,x)[i][1]])
    for j in range (len(neighbor)) :
        l = 0
        while (neighbor[j] != data[l]) and (l <= len(data)) :
            l += 1
        if (neighbor[j] == data[l]) :
            if (label[l] == 'accepted') :
                acc += 1
            else :
                rej += 1
    if acc > rej :
        return ("accepted")
    else :
        return ("rejected")
    return acc,rej

x = [1579, 3.0]
k = 3
print(knn(data,label,x,k))
