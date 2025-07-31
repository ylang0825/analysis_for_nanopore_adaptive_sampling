# analysis_for_nanopore_adaptive_sampling
This repository contains ​​1 shell script​​ and ​​6 Python scripts​​ designed to extract statistics from raw nanopore adaptive sampling data.

**Script Usage**  

`python target_nontarget_statistics.py [all_adaptive.fastq] [adaptive-target.sam] [adaptive-nontarget.sam]`  
​​Input​​:  
Raw sequence file, SAM alignment files for target/non-target sequences.  
​​Output​​:  
Total sequences/bases, uniquely matched sequences/bases to target/non-target, and dual-matched sequences/bases.

`python match_read_number_with_time.py [sequencing_summary.txt] [adaptive-target.sam] [control-target.sam]`  
Input:  
Nanopore sequencing summary file, SAM alignment files for adaptive/control groups.  
Output:  
A 5-column table with sequencing duration, sequence counts, and base counts for both groups.

`python unblock_reads_matched_number.py [all_adaptive.fastq] [sequencing_summary.txt] [adaptive-target.sam]`   
Input:  
Raw sequence file, nanopore sequencing summary file, SAM alignment file.  
Output:  
Statistics (counts/average/median read lengths) for accepted/rejected sequences matching/non-matching targets.  

`python read_category_statistics.py [all_adaptive.fastq] [sequencing_summary.txt]`   
Input:  
Raw sequence file, nanopore sequencing summary file.  
Output:  
Table categorizing sequences (columns: counts/bases, average/median/N50 lengths).  

`python zymogut_species_read_with_time.py [all_adaptive.fastq] [adaptive-target.sam] [adaptive-nontarget.sam] [sequencing_summary.txt]`   
Input:  
Raw sequence file, SAM alignment files for target/non-target sequences, nanopore sequencing summary file.  
Output:  
Time-series table of species-specific sequence counts.

`python zymogut_species_base_with_time.py [all_adaptive.fastq] [adaptive-target.sam] [adaptive-nontarget.sam] [sequencing_summary.txt]`   
Input:  
Raw sequence file, SAM alignment files for target/non-target sequences, nanopore sequencing summary file.  
Output:  
Time-series table of species-specific base counts.  

`sh ReadBouncer_running.sh`  
Monitors and auto-restarts ReadBouncer every 30 seconds if inactive.
