""" Splits data into train test and validation sets """
import numpy as np
import random
np.random.seed(2)

maxLen = 12000 #length of the dataset
data = range(1, maxLen)
# random.shuffle(data)

testSize = int(maxLen * 0.1) # 10percent data as test set
validSize = int(maxLen * 0.05) # 5percent data as validation set
test_ = random.sample(data, testSize)
valid_ = random.sample(data, validSize)

test_nos = np.sort(test_)
valid_nos = np.sort(valid_)

print(test_nos)
print(valid_nos)
f = open("all_data.txt", 'r')
f1 = open('test.txt', 'a')
f2 = open('valid.txt', 'a')
f3 = open('train_new.txt', 'a') #stores all the data not in valid.txt or test.txt

t = 0
v = 0
i = 0

for line in f:
    if(t < testSize and i == test_nos[t]):
        f1.write(line)
        t += 1
    if(v < validSize and i == valid_nos[v]):
        f2.write(line)
        v += 1
    else:
        f3.write(line)
    i += 1

f.close()
f1.close()
f2.close()
f3.close()