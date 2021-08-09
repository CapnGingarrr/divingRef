
# Packages
import os
import pandas as pd

# https://www.youtube.com/watch?v=SSW9LzOJSus

# Video Preprocessing

# List all videos in raw video folder
path = 'vid_raw/'
vids = os.listdir(path)

f_name_df = pd.DataFrame(columns=['Title'])

f_name_df['Title'] = vids
f_name_df['ID'] = f_name_df.index
f_name_df['Title'] = f_name_df['Title'].map(lambda x: x.rstrip('.mp4'))

# Read Data and Label Details
reference = pd.read_json('annotations/Diving48_vocab.json')
reference = reference.reset_index()
reference.columns = ['ID', 'TakeOff', 'Somersault', 'Twist', 'FlightPosition']

data1 = pd.read_json('annotations/Diving48_V2_train.json')
data2 = pd.read_json('annotations/Diving48_V2_test.json')

# Combine datasets into 1 dataset
d = [data1, data2]
data = pd.concat(d)
data.columns = ['Title', 'Dive', 'Start', 'End']

data = data.merge(f_name_df, how='left', on='Title')
d_check = data.dropna().copy()
d_check['ID'] = d_check['ID'].astype('int64')

# Rename all videos in file to match new ID - mainly to help any manual validation that must be performed
for index, video in enumerate(vids):
    os.rename(os.path.join(path, video), os.path.join(path, ''.join([str(index), '.mp4'])))


