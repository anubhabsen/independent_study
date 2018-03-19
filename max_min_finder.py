import pickle
import numpy as np

with open('mats.pkl', 'rb') as f:
    data = pickle.load(f)

indices = []

corr = data[0]
p_vals = data[1]


fields = ["Results Pitch", "Results Time", "Age", "Gender","WAIS_vocabularyRP","WAIS_vocabularySP","WAIS_similaritiesRP","WAIS_similaritiesSP","WAIS_informationRP","WAIS_informationSP","WAIS_picturecompletionRP","WAIS_picturecompletionSP","WAIS_digitsymbolcodingRP","WAIS_digitsymbolcodingSP","WAIS_blockdesignRP","WAIS_blockdesignSP","WAIS_matrixreasoningRP","WAIS_matrixreasoningSP","WAIS_symbolsearchRP","WAIS_symbolsearchSP","WAIS_VCI_verbal_comprehension_index","WAIS_POI_perceptual_organization_index","WAIS_PSI_processing_speed_index","WMS_letternumbersequenceRP","WMS_letternumbersequenceSP","WMS_spatialspanRP","WMS_spatialspanSP","WMS_word_lists1RP","WMS_word_lists1SP","WMS_word_lists2RP","WMS_word_lists2SP","WMS_wordlists_recognitionRP","WMS_wordlists_recognitionSP","WMS_workingmemoryindex","TrailMakingA_time_in_seconds","TrailMakingA_percentile","TrailMakingA_numberoferrors","TrailMakingB_time_in_seconds","TrailMakingB_percentile","TrailMakingB_numberoferrors","TrailMaking_difference_percentile","TrailMaking_ratiopercentile","Stroop_word_reading_time","Stroop_word_reading_no_of_errors","Stroop_colournaming_time","Stroop_colournaming_nooferrors","Stroop_interference_time","Stroop_interference_nooferrors"]
counter = 0

# Correlation
# for i in range(48):
# 	for j in range(48):
# 		if i == j:
# 			corr[i, j] = 0

# while counter < 10:
# 	max = 0
# 	for i in range(48):
# 		for j in range(48):
# 			if corr[i, j] > max and (i == 1 or j == 1):
# 				max = corr[i, j]
# 				temp_i = i
# 				temp_j = j

# 	if temp_j > temp_i and abs(temp_j - temp_i) > 1:
# 		indices.append((temp_i, temp_j))
# 		counter += 1
# 	corr[temp_i, temp_j] = 0


# The p values
for i in range(48):
	for j in range(48):
		if i == j:
			p_vals[i, j] = 100

while counter < 10:
	min = 9999999
	for i in range(48):
		for j in range(48):
			if p_vals[i, j] < min and (i == 1 or j == 1):
				min = p_vals[i, j]
				temp_i = i
				temp_j = j

	if temp_j > temp_i and abs(temp_i - temp_j) > 1:
		indices.append((temp_i, temp_j))
		counter += 1
	p_vals[temp_i, temp_j] = 100


for indexes in indices:
	print(fields[indexes[0]],"and", fields[indexes[1]])
