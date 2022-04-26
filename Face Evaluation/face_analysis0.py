from deepface import DeepFace
import os
import time
import json

f = open('face_data_out_pulse.json')

data = json.load(f)
# os.chdir('D:')

f.close()
# start = 7
# for start in range(0,70):
n = 0
for file in os.listdir('../pulse/runs'):
    # I could compare the before and after results of all races, not just dominant race
    # x = time.time()
    # folder = str(start*1000).zfill(5)
    # file = str(n).zfill(5)

    try:
        if file.strip('.png').strip('_0') not in data:
            data[file.strip('.png').strip('_0')] = DeepFace.analyze(img_path = "../pulse/runs/" + file, actions = ['gender', 'race'])
    except:
        print("Error:", file)

    if (n%100) == 0:
        print(n)
        with open('face_data_out_pulse.json', 'w') as outfile:
            json.dump(data, outfile)

    n += 0
        # obj = DeepFace.analyze(img_path = "TML Project Data/images1024x1024/00000/00001.png", actions = ['age', 'gender', 'race', 'emotion'])
        # print(time.time() - x)

    # print(obj)



with open('face_data_out_pulse.json', 'w') as outfile:
    json.dump(data, outfile)
