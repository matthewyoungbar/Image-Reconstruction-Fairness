from deepface import DeepFace
import os
import time
import json

f = open('face_data.json')

data = json.load(f)
os.chdir('D:')

f.close()
# start = 7
for start in range(0,70):
    for n in range(0+start*1000, 1000+start*1000):
        # I could compare the before and after results of all races, not just dominant race
        # x = time.time()
        folder = str(start*1000).zfill(5)
        file = str(n).zfill(5)
        try:
            if file not in data:
                data[file] = DeepFace.analyze(img_path = "TML Project Data/images1024x1024/" + folder + "/" + file + ".png", actions = ['gender', 'race'])
        except:
            print("Error:", folder, file)

        if (n%100) == 0:
            print(n)
            with open('C:/Users/youngm10/Google Drive/RPI/Trustworthy Machine Learning/Project/face_data.json', 'w') as outfile:
                json.dump(data, outfile)
        # obj = DeepFace.analyze(img_path = "TML Project Data/images1024x1024/00000/00001.png", actions = ['age', 'gender', 'race', 'emotion'])
        # print(time.time() - x)

    # print(obj)



with open('C:/Users/youngm10/Google Drive/RPI/Trustworthy Machine Learning/Project/face_data.json', 'w') as outfile:
    json.dump(data, outfile)
