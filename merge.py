# This script aims to update the final.csv file 
# this file can then be used to show infant mortality
# rate on a map (eg. a heatmap for infant mortality rate)

import pandas

count = 1
final_file = pandas.read_csv("data/final.csv")
infant_file = pandas.read_csv("data/infant_mortality_rate.csv")
regions_values = {}


for index_infant, row_infant in infant_file.iterrows():
	if row_infant['region'] in regions_values:
			regions_values[row_infant['region']] += \
			float(row_infant['infant mortality rate'])
	else:
		regions_values[row_infant['region']] = \
		float(row_infant['infant mortality rate'])


for index_final, row_final in final_file.iterrows():
	for key, value in regions_values.iteritems():
		region = str(row_final['region']).strip()
		key = key.strip()
		if region == key:
			print row_final['region'] + ',' + str(value)
			