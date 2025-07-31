import re
import sys

Title = []
with open(sys.argv[1]) as firFILE:
	for line in firFILE:
		line = line.rstrip()
		if re.match('@', line) and re.search(' ', line):
			Line = line.split(' ')
			title = Line[0][1:]
			Title.append(title)

Unblock = {}
with open(sys.argv[2]) as secFILE:
	for line in secFILE:
		line = line.rstrip()
		if not re.match('filename_fastq', line):
			Line = line.split('\t')
			if Line[-1] == 'data_service_unblock_mux_change':
				Unblock[Line[4]] = 1
			elif Line[-1] == 'signal_positive':
				Unblock[Line[4]] = 0
			else:
				Unblock[Line[4]] = 2

Match = {}
Length = {}
with open(sys.argv[3]) as thiFILE:
	for line in thiFILE:
		line = line.rstrip()
		if not re.match('@', line):
			Line = line.split('\t')
			if Line[0] not in Length.keys():
				Length[Line[0]] = len(Line[9])
			if Line[2] == '*':
				Match[Line[0]] = 0
			else:
				Match[Line[0]] = 1

unblock_match_read_number = 0
unblock_match_base_number = 0
unblock_unmatch_read_number = 0
unblock_unmatch_base_number = 0
receive_match_read_number = 0
receive_match_base_number = 0
receive_unmatch_read_number = 0
receive_unmatch_base_number = 0
Total_len = 0
Unblock_length_list = []
Receive_length_list = []
for i in Title:
	Total_len += Length[i]
	if Unblock[i] == 1 and Match[i] == 1:
		unblock_match_read_number += 1
		unblock_match_base_number += Length[i]
		Unblock_length_list.append(Length[i])
	elif Unblock[i] == 1 and Match[i] == 0:
		unblock_unmatch_read_number += 1
		unblock_unmatch_base_number += Length[i]
		Unblock_length_list.append(Length[i])
	elif Unblock[i] == 0 and Match[i] == 1:
		receive_match_read_number += 1
		receive_match_base_number += Length[i]
		Receive_length_list.append(Length[i])
	elif Unblock[i] == 0 and Match[i] == 0:
		receive_unmatch_read_number += 1
		receive_unmatch_base_number += Length[i]
		Receive_length_list.append(Length[i])

unblock_read_number = unblock_match_read_number + unblock_unmatch_read_number
receive_read_number = receive_match_read_number + receive_unmatch_read_number
if len(Unblock_length_list) != 0:
	unblock_median_length = sorted(Unblock_length_list)[int(len(Unblock_length_list)/2)]
	unblock_read_average_length = int((unblock_match_base_number + unblock_unmatch_base_number) / unblock_read_number)
if len(Receive_length_list) != 0:
	receive_median_length = sorted(Receive_length_list)[int(len(Receive_length_list)/2)]
	receive_read_average_length = int((receive_match_base_number + receive_unmatch_base_number) / receive_read_number)

print('total read number: ' + str(len(Title)))
print('total base number: ' + str(Total_len))
print('')
print('unblock read number: ' + str(unblock_read_number))
if unblock_read_number != 0:
	print('unblock reads average length: ' + str(unblock_read_average_length))
	print('unblock reads median length: ' + str(unblock_median_length))
print('receive read number: ' + str(receive_read_number))
if receive_read_number != 0:
	print('receive reads average length: ' + str(receive_read_average_length))
	print('receive reads median length: ' + str(receive_median_length))
print('')
print('unblock matched read number: ' + str(unblock_match_read_number))
if unblock_match_read_number != 0:
	print('unblock matched reads average length: ' + str(int(unblock_match_base_number/unblock_match_read_number)))
print('unblock unmatched read number: ' + str(unblock_unmatch_read_number))
if unblock_match_read_number != 0:
	print('unblock unmatched reads average length: ' + str(int(unblock_unmatch_base_number/unblock_unmatch_read_number)))
print('receive matched read number: ' + str(receive_match_read_number))
if receive_match_read_number != 0:
	print('receive matched reads average length: ' + str(int(receive_match_base_number/receive_match_read_number)))
print('receive unmatched read number: ' + str(receive_unmatch_read_number))
if receive_match_read_number != 0:
	print('receive unmatched reads average length: ' + str(int(receive_unmatch_base_number/receive_unmatch_read_number)))


