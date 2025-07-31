import re
import sys

Dict = {}
with open(sys.argv[1]) as firFILE:
	for line in firFILE:
		line = line.rstrip()
		if re.match('@', line) and re.search(' ', line):
			Line = line.split(' ')
			title = Line[0][1:]
			Dict[title] = title

Species = {}
with open(sys.argv[2]) as secFILE:
	for line in secFILE:
		line = line.rstrip()
		if not re.match('@', line):
			Line = line.split('\t')
			title = Line[0]
			ref = Line[2]
			if re.search('veillonella_rogosae', ref):
				target = 'Veillonella_rogosae'
			elif re.search('Salmonella_enterica', ref):
				target = 'Salmonella_enterica'
			elif re.search('tig0000', ref):
				target = 'Saccharomyces_cerevisiae'
			elif re.search('Roseburia_hominis', ref):
				target = 'Roseburia_hominis'
			elif re.search('Prevotella_corporis', ref):
				target = 'Prevotella_corporis'
			elif re.search('Lactobacillus_fermentum', ref):
				target = 'Lactobacillus_fermentum'
			elif re.search('Fusobacterium_nucleatum', ref):
				target = 'Fusobacterium_nucleatum'
			elif re.search('Faecalibacterium_prausnitzii', ref):
				target = 'Faecalibacterium_prausnitzii'
			elif re.search('coli', ref):
				target = 'Escherichia_coli'
			elif re.search('Clostridium_difficille', ref):
				target = 'Clostridioides_difficile'
			elif not re.search(r'[A-Za-z]', ref):
				target = 'Candida_albican'
			elif re.search('Bifidobacterium_adolescentis', ref):
				target = 'Bifidobacterium_adolescentis'
			elif re.search('Akkermansia_muciniphila', ref):
				target = 'Akkermansia_muciniphila'
			elif re.search('methanobrevibacter_smithii', ref):
				target = 'Methanobrevibacter_smithii'
			elif re.search('Enterococcus_faecalis', ref):
				target = 'Enterococcus_faecalis'
			elif re.search('Clostridium_perfringens', ref):
				target = 'Clostridium_perfringens'
			elif re.search('Bacteroides_fragilis', ref):
				target = 'Bacteroides_fragilis'
			else:
				target = ''
			Species[title] = target

with open(sys.argv[3]) as thiFILE:
	for line in thiFILE:
		line = line.rstrip()
		if not re.match('@', line):
			Line = line.split('\t')
			title = Line[0]
			ref = Line[2]
			if re.search(r'chr[0-9]', ref):
				target = 'Human'
				Species[title] = target

Time = []
Length = {}
Title = []
with open(sys.argv[4]) as fouFILE:
	for line in fouFILE:
		line = line.rstrip()
		if not re.match('filename_fastq', line):
			Line = line.split('\t')
			if Line[4] in Dict.keys():
				Time.append(float(Line[9]))
				Title.append(Line[4])
				Length[Line[4]] = int(Line[15])


mark = 0
print('min\tHuman\tVeillonella_rogosae\tSalmonella_enterica\tSaccharomyces_cerevisiae\tRoseburia_hominis\tPrevotella_corporis\tLactobacillus_fermentum\tFusobacterium_nucleatum\t' + 
	'Faecalibacterium_prausnitzii\tEscherichia_coli\tClostridioides_difficile\tCandida_albican\tBifidobacterium_adolescentis\tAkkermansia_muciniphila\tMethanobrevibacter_smithii\t' +
	'Enterococcus_faecalis\tClostridium_perfringens\tBacteroides_fragilis')
for i in range(900, 172801, 900):
	Human_length = 0
	Veillonella_rogosae_length = 0
	Salmonella_enterica_length = 0
	Saccharomyces_cerevisiae_length = 0
	Roseburia_hominis_length = 0
	Prevotella_corporis_length = 0
	Lactobacillus_fermentum_length = 0
	Fusobacterium_nucleatum_length = 0
	Faecalibacterium_prausnitzii_length = 0
	Escherichia_coli_length = 0
	Clostridioides_difficile_length = 0
	Candida_albican_length = 0
	Bifidobacterium_adolescentis_length = 0
	Akkermansia_muciniphila_length = 0
	Methanobrevibacter_smithii_length = 0
	Enterococcus_faecalis_length = 0
	Clostridium_perfringens_length = 0
	Bacteroides_fragilis_length = 0
	for j in range(mark, len(Time)):
		title = Title[j]
		if Species[title] == 'Human':
			Human_length += Length[title]
		if Species[title] == 'Veillonella_rogosae':
			Veillonella_rogosae_length += Length[title]
		elif Species[title] == 'Salmonella_enterica':
			Salmonella_enterica_length += Length[title]
		elif Species[title] == 'Saccharomyces_cerevisiae':
			Saccharomyces_cerevisiae_length += Length[title]
		elif Species[title] == 'Roseburia_hominis':
			Roseburia_hominis_length += Length[title]
		elif Species[title] == 'Prevotella_corporis':
			Prevotella_corporis_length += Length[title]
		elif Species[title] == 'Lactobacillus_fermentum':
			Lactobacillus_fermentum_length += Length[title]
		elif Species[title] == 'Fusobacterium_nucleatum':
			Fusobacterium_nucleatum_length += Length[title]
		elif Species[title] == 'Faecalibacterium_prausnitzii':
			Faecalibacterium_prausnitzii_length += Length[title]
		elif Species[title] == 'Escherichia_coli':
			Escherichia_coli_length += Length[title]
		elif Species[title] == 'Clostridioides_difficile':
			Clostridioides_difficile_length += Length[title]
		elif Species[title] == 'Candida_albican':
			Candida_albican_length += Length[title]
		elif Species[title] == 'Bifidobacterium_adolescentis':
			Bifidobacterium_adolescentis_length += Length[title]
		elif Species[title] == 'Akkermansia_muciniphila':
			Akkermansia_muciniphila_length += Length[title]
		elif Species[title] == 'Methanobrevibacter_smithii':
			Methanobrevibacter_smithii_length += Length[title]
		elif Species[title] == 'Enterococcus_faecalis':
			Enterococcus_faecalis_length += Length[title]
		elif Species[title] == 'Clostridium_perfringens':
			Clostridium_perfringens_length += Length[title]
		elif Species[title] == 'Bacteroides_fragilis':
			Bacteroides_fragilis_length += Length[title]
		if Time[j] > i:
			mark = j + 1
			break
	print(str(i/3600) + '\t' + str(Human_length/1048576) + '\t' + str(Veillonella_rogosae_length/1048576) + '\t' + str(Salmonella_enterica_length/1048576) + '\t' + str(Saccharomyces_cerevisiae_length/1048576) + '\t' 
		+ str(Roseburia_hominis_length/1048576) + '\t' + str(Prevotella_corporis_length/1048576) + '\t' + str(Lactobacillus_fermentum_length/1048576) + '\t' + str(Fusobacterium_nucleatum_length/1048576) + '\t' +
		 str(Faecalibacterium_prausnitzii_length/1048576) + '\t' + str(Escherichia_coli_length/1048576) + '\t' + str(Clostridioides_difficile_length/1048576) + '\t' + str(Candida_albican_length/1048576) + '\t' +
		 str(Bifidobacterium_adolescentis_length/1048576) + '\t' + str(Akkermansia_muciniphila_length/1048576) + '\t' + str(Methanobrevibacter_smithii_length/1048576) + '\t' + str(Enterococcus_faecalis_length/1048576) + '\t' 
		 + str(Clostridium_perfringens_length/1048576) + '\t' + str(Bacteroides_fragilis_length/1048576))
