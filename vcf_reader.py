import csv
import pandas as pd
import numpy as np
import sys
import re
import matplotlib.pyplot as plt

# Calculate the ploidy of presented string like '1|0'
# Input: string
# Output: number of ploidy
def ploid_count_from_string(string_ploid):
	return string_ploid.count('/') + string_ploid.count('|') + 1

# Define if input string is heterozygote
# Input: string
# Output: Bool. Heterozygote or not
def is_hetero(input_string):
	split_symbols = ['/', '|']
	rezult = False
	if ploid_count_from_string(input_string) > 1:
		for i in split_symbols:
			input_string = input_string.replace(str(i), '')

	if len(set(input_string)) == 1:
		rezult = True

	return rezult

# parsing arg from cmd
default_value = ['vcf_reader.py', None, None]
for i in range(0, len(sys.argv)):
	default_value[i] = sys.argv[i]

file_path = default_value[1]
sample_name = default_value[2]

# check file name in cmd
if file_path is None:
	sys.exit()

# arr for data
data_arr = []

fixed_columns_names = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']

# read vcf file
with open(file_path, newline='') as csvfile:
	vcf_reader = csv.reader(csvfile, delimiter=' ')
	info_not_skipped = True

	for row in vcf_reader:
		# skip info
		if row[0] != '#CHROM' and info_not_skipped:
			continue
		# create array with columns titles
		if row[0] == '#CHROM':
			titles = row
			info_not_skipped = False
			continue
		data_arr.append(row)

np_arr = np.array(data_arr)
df_vcf = pd.DataFrame(np_arr, columns=titles)

# number of samples
samples_number = 0

for t in titles:
	if t not in fixed_columns_names:
		samples_number += 1

arr_of_ploid = []
pl_arr = []

for i in titles[-samples_number+1:]:
	# ploidy arr
	pl_arr.append([re.split(':', str(j))[0] for j in df_vcf[i]])

for i in pl_arr:
	arr_of_ploid.append([ploid_count_from_string(j) for j in i])

# suppose the ploidy of presented individuals is equal for all of them so we can get anyone element of array
print('The number of ploidy = ', arr_of_ploid[0][0])

# check sample name in cmd
if sample_name is None:
	sys.exit()

pl_arr = [re.split(':', str(j))[0] for j in df_vcf[sample_name]]
ar_pos = []

for p in range(0, len(pl_arr)):
	temp = is_hetero(str(pl_arr[p]))
	if temp:
		ar_pos.append(df_vcf['POS'][p])

ar_dist = []
for i in range(1, len(ar_pos)):
	ar_dist.append(int(ar_pos[i]) - int(ar_pos[i-1]))

print('Distance between heterozygotes in sample ', ar_dist)

plt.hist(ar_dist)
plt.title('Distance between heterozygotes in sample ' + str(sample_name))
plt.show()