import pickle
import numpy as np

with open('mats.pkl', 'rb') as f:
    data = pickle.load(f)

indices = []

corr = data[0]
p_vals = data[1]


print(p_vals.shape)

# for i in range(48):
# 	for j in range(48):
# 		if i == j:
# 			corr[i, j] = 0

# for counter in range(20):
# 	max = 0
# 	for i in range(48):
# 		for j in range(48):
# 			if corr[i, j] > max:
# 				max = corr[i, j]
# 				temp_i = i
# 				temp_j = j

# 	if temp_j > temp_i:
# 		indices.append((temp_i, temp_j))
# 	corr[temp_i, temp_j] = 0

# print(indices)




# for i in range(48):
# 	for j in range(48):
# 		if i == j:
# 			p_vals[i, j] = 100

# for counter in range(20):
# 	min = 9999999
# 	for i in range(48):
# 		for j in range(48):
# 			if p_vals[i, j] < min:
# 				min = p_vals[i, j]
# 				temp_i = i
# 				temp_j = j

# 	if temp_j > temp_i:
# 		indices.append((temp_i, temp_j))
# 	p_vals[temp_i, temp_j] = 100

# print(indices)
# print(p_vals)
