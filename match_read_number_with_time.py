import re
import sys

Time = {}
Length = {}
Adaptive_match = {}
Control_match = {}
print('min\tAdaptive_read_count\tControl_read_count\tAdaptive_base_count\tControl_base_count')

with open(sys.argv[1]) as firFILE:
	for line in firFILE:
		line = line.rstrip()
		if not re.match('filename_fastq', line):
			Line = line.split('\t')
			Time[Line[4]] = float(Line[9])

with open(sys.argv[2]) as secFILE:
	for line in secFILE:
		line = line.rstrip()
		if not re.match('@', line):
			Line = line.split('\t')
			if Line[0] not in Length.keys():
				Length[Line[0]] = len(Line[9])
			if Line[2] == '*':
				Adaptive_match[Line[0]] = 0
			else:
				Adaptive_match[Line[0]] = 1

with open(sys.argv[3]) as thiFILE:
	for line in thiFILE:
		line = line.rstrip()
		if not re.match('@', line):
			Line = line.split('\t')
			Length[Line[0]] = len(Line[9])
			if Line[2] == '*':
				Control_match[Line[0]] = 0
			else:
				Control_match[Line[0]] = 1

for i in range(900, 172801, 900):
	Adaptive_read_count = 0
	Adaptive_base_count = 0
	for j in Adaptive_match.keys():
		if Adaptive_match[j] == 1 and Time[j] < i:
			Adaptive_read_count += 1
			Adaptive_base_count += Length[j]
	Control_read_count = 0
	Control_base_count = 0
	for j in Control_match.keys():
		if Control_match[j] == 1 and Time[j] < i:
			Control_read_count += 1
			Control_base_count += Length[j]
	print(str(i) + '\t' + str(Adaptive_read_count) + '\t' + str(Control_read_count) + '\t' + str(Adaptive_base_count) + '\t' + str(Control_base_count))
