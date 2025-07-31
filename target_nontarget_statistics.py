import re
import sys

Dict = {}
total_read_count = 0
total_base_count = 0
with open(sys.argv[1]) as firFILE:
	for line in firFILE:
		line = line.rstrip()
		if re.match('>', line):
			title = line.split(' ')[0][1:]
		else:
			Dict[title] = line
			total_read_count += 1
			total_base_count += len(line)
print('total read count: ' + str(total_read_count))
print('total base count: ' + str(total_base_count))

Target = {}
with open(sys.argv[2]) as secFILE:
	for line in secFILE:
		line = line.rstrip()
		if not re.match('@', line):
			title = line.split('\t')[0]
			if line.split('\t')[2] != '*':
				Target[title] = 1
			else:
				Target[title] = 0

Nontarget = {}
with open(sys.argv[3]) as secFILE:
	for line in secFILE:
		line = line.rstrip()
		if not re.match('@', line):
			title = line.split('\t')[0]
			if line.split('\t')[2] != '*':
				Nontarget[title] = 1
			else:
				Nontarget[title] = 0

target_read_count = target_base_count = nontarget_read_count = nontarget_base_count = both_read_count = both_base_count = 0

for i in Dict.keys():
	if Target[i] == 1 and Nontarget[i] == 0:
		target_read_count += 1
		target_base_count += len(Dict[i])
	elif Target[i] == 0 and Nontarget[i] == 1:
		nontarget_read_count += 1
		nontarget_base_count += len(Dict[i])
	elif Target[i] == 1 and Nontarget[i] == 1:
		both_read_count += 1
		both_base_count += len(Dict[i])

print('target read count: ' + str(target_read_count))
print('target base count: ' + str(target_base_count))
print('nontarget read count: ' + str(nontarget_read_count))
print('nontarget base count: ' + str(nontarget_base_count))
print('both read count: ' + str(both_read_count))
print('both base count: ' + str(both_base_count))

