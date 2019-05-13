from os import listdir
from os.path import isfile, join
import os, random
import sys

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

# parameters

current_dir = sys.argv[1]
print(current_dir)

percentage_test = 0.2


filenames = [f for f in listdir(current_dir) if isfile(join(current_dir, f)) and (f.endswith('.png') or f.endswith('.jpg'))]

filenames.sort()  # make sure that the filenames have a fixed order before shuffling
random.seed(230)
random.shuffle(filenames) # shuffles the ordering of filenames (deterministic given the chosen seed)

split_1 = int(percentage_test * len(filenames))
test_filenames = filenames[:split_1]
train_filenames = filenames[split_1:]

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')


for file_ in test_filenames:
        file_test.write(current_dir + "/" + file_ + "\n")

for file_ in train_filenames:
        file_train.write(current_dir + "/" + file_ + "\n")
