import matplotlib.pyplot as plt
import json

# FIND PERCENTAGE OF EACH RACE THAT PULSE DID NOT FIND AN IMAGE FOR


data = json.load(open('face_data_out_pulse.json'))

orig = json.load(open('face_data.json'))

averages = dict()
dominant_race_correct = dict()
genders = dict()
counts = dict()
gender_counts = dict()
for image in data:
    # print(image)
    img = image.zfill(5)
    diff = 0
    if img not in orig:
        continue
    for race in data[image]["race"]:
        diff += abs(data[image]["race"][race] - orig[img]["race"][race])
    if orig[img]["dominant_race"] in averages:
        averages[orig[img]["dominant_race"]] += diff/len(data[image]["race"])
        counts[orig[img]["dominant_race"]] += 1
    else:
        averages[orig[img]["dominant_race"]] = diff/len(data[image]["race"])
        counts[orig[img]["dominant_race"]] = 1

    if orig[img]["dominant_race"] == data[image]["dominant_race"]:
        if orig[img]["dominant_race"] in dominant_race_correct:
            dominant_race_correct[orig[img]["dominant_race"]] += 1
        else:
            dominant_race_correct[orig[img]["dominant_race"]] = 1
    if orig[img]["gender"] in gender_counts:
        gender_counts[orig[img]["gender"]] += 1
    else:
        gender_counts[orig[img]["gender"]] = 1
    if orig[img]["gender"] == data[image]["gender"]:
        if orig[img]["gender"] in genders:
            genders[orig[img]["gender"]] += 1

        else:
            genders[orig[img]["gender"]] = 1

for race in averages:
    averages[race] /= counts[race]
    if race not in dominant_race_correct:
        dominant_race_correct[race] = 0
    dominant_race_correct[race] /= counts[race]

for gender in genders:
    genders[gender] /= gender_counts[gender]
print(averages)
print(dominant_race_correct)
print(genders)

failures = dict()
fail_counts = dict()
fail_genders = dict()
fail_gender_counts = dict()
for num in range(1000):
    n = str(num)
    n2 = n.zfill(5)
    if n not in data and n2 in orig:
        if orig[n2]["dominant_race"] in failures:
            failures[orig[n2]["dominant_race"]] += 1
        else:
            failures[orig[n2]["dominant_race"]] = 1
        if orig[n2]["gender"] in fail_genders:
            fail_genders[orig[n2]["gender"]] += 1
        else:
            fail_genders[orig[n2]["gender"]] = 1

    if n2 in orig:
        if orig[n2]["dominant_race"] in fail_counts:
            fail_counts[orig[n2]["dominant_race"]] += 1
        else:
            fail_counts[orig[n2]["dominant_race"]] = 1

        if orig[n2]["gender"] in fail_gender_counts:
            fail_gender_counts[orig[n2]["gender"]] += 1
        else:
            fail_gender_counts[orig[n2]["gender"]] = 1

for race in failures:
    failures[race] /= fail_counts[race]

for gender in fail_genders:
    fail_genders[gender] /= fail_gender_counts[gender]

print(failures)
print(fail_genders)

plt.bar(averages.keys(), averages.values(), color ='blue', width = 0.4)

plt.xlabel("Race")
plt.ylabel("Disparity")
plt.title("Disparity of Deepface Results of Input and Output Images for PULSE")
plt.show()

plt.bar(dominant_race_correct.keys(), dominant_race_correct.values(), color ='pink', width = 0.4)
plt.xlabel("Race")
plt.ylabel("Matching Percentage")
plt.title("Percentage of Input Images whose \"Primary Race\" matches that of Output")
plt.show()

plt.bar(genders.keys(), genders.values(), color ='green', width = 0.4)
plt.xlabel("Gender")
plt.ylabel("Matching Percentage")
plt.title("Percentage of Input Images whose Gender matches that of Output")
plt.axis([-1, 2, 0, 1])
plt.show()

failures.update(fail_genders)

plt.bar(failures.keys(), failures.values(), color ='purple', width = 0.4)
plt.xlabel("Race")
plt.ylabel("Percentage Success")
plt.title("Success Rates of Generating an Image from Input")
# plt.axis([-1, 2, 0, 1])
plt.show()
#
# plt.bar(fail_genders.keys(), fail_gendersgender.values(), color ='green', width = 0.4)
# plt.xlabel("Gender")
# plt.ylabel("Matching Percentage")
# plt.title("Success Rates of Generating an Image from Input")
# plt.axis([-1, 2, 0, 1])
# plt.show()
