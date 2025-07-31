import re
import sys

Title = []
with open(sys.argv[1]) as secFILE:
	for line in secFILE:
		line = line.rstrip()
		if re.match('@', line) and re.search(' ', line):
			Line = line.split(' ')
			title = Line[0][1:]
			Title.append(title)

Length = {}
End_reason = {}
with open(sys.argv[2]) as firFILE:
	for line in firFILE:
		if not re.match('filename', line):
			Line = line.rstrip().split('\t')
			if Line[4] in Title:
				Length[Line[4]] = int(Line[15])
				End_reason[Line[4]] = Line[-1]

print('category\tnumber\tsum\tmean\tmedian\tN50')
for i in ('signal_positive', 'signal_negative', 'data_service_unblock_mux_change', 'unblock_mux_change'):
	List = []
	for j in End_reason.keys():
		if End_reason[j] == i:
			List.append(Length[j])
	sum_length = sum(List)
	number = len(List)
	if number > 0:
		mean = int(sum_length / number)
		List_sorted = sorted(List, reverse = True)
		median = List_sorted[int(number/2)]
		sum_temp = 0
		for k in range(0,number):
			sum_temp += List_sorted[k]
			if sum_temp > sum_length / 2:
				N50 = List_sorted[k]
				break
	else:
		mean = median = N50 = 0
	print(i + '\t' + str(number) + '\t' + str(sum_length) + '\t' + str(mean) + '\t' + str(median) + '\t' + str(N50))