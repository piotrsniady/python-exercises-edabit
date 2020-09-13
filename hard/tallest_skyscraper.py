import numpy as np


data = [
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1]
]


skyline = np.array(data)
max_sum = skyline.sum(axis=0)
# max value
print(max_sum.max())
# index of max value
print(max_sum.argmax())
