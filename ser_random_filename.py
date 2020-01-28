import os
import pandas as pd
import numpy as np
import csv

#files = os.listdir('C:/Users/AkkawutvanichC/Anaconda3/Projects/SER/mp3')
# selected = 0
# data = {
#     'Song_number' : files,
#     'Selected' : selected
#         }

data = pd.read_csv('ser_filename .csv')
# data['emotion'] = files

print (data)

def random_ser():
    file = []
    for i in range(0,3):
        chosen_idx = np.random.choice(len(data), replace=False, size=108)
        data_rand = data.iloc[chosen_idx]
        random_number = data_rand.iloc[:,:]

        file.append(random_number)
        print(random_number)

    return file

rand_file = random_ser()
file_setlist = []
for i in range(len(rand_file)):
    file_setlist.append(rand_file[i].iloc[:,0].values)

print (file_setlist)

with open('ser_setlist.csv','w', encoding='utf-8-sig',newline='') as f:
    fw = csv.writer(f) 
    fw.writerows(file_setlist)   