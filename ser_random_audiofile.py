import os
import pandas as pd
import numpy as np
import csv

files = os.listdir('C:/Users/AkkawutvanichC/Anaconda3/Projects/SER/mp3')
selected = 0
data = {
    'Song_number' : files,
    'Selected' : selected
        }

# data = pd.read_csv('ser_filename .csv')
# # data['emotion'] = files


def random_song():
    song_name = []
    for i in range(0,20):
        df = pd.DataFrame(data)
        #print ('Round %d ' %(i+1))
        
        for j in range(0,2):
            chosen_idx = np.random.choice(len(df), replace = False, size = 55) 
            df_rand = df.iloc[chosen_idx] 
            df = df.drop(df_rand.index)
            random_number = df_rand.iloc[:,:]

            song_name.append(random_number)
            
            #print (random_number )
    return song_name
        
song = random_song()

songset = []
for i in range(len(song)):
    songset.append(song[i].iloc[:,0].values)

with open('Songset_for_ser.csv','w', encoding='utf-8-sig',newline='') as f:
    fw = csv.writer(f) 
    fw.writerows(songset)   