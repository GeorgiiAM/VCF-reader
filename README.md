# VCF-reader
Test task

- Please provide valid Python code for the following problems:
VCF file format is a standard format for SNP data. Example of such file and its
detailed specification could be found here . Assume that VCF file is correct and
corresponds to the properties of organisms.
- You need to calculate the ploidy of presented individuals (suppose it is equal
for all of them).

INPUT: filename.
	python vcf_reader.py example.vcf
	
OUTPUT: the number of ploidy (1 for haploidy, 2 for diploidy and so on).


- Calculate the histogram for distribution of lengths of intervals between
heterozygotes. The i-th element of histogram will be equal to the number of
neighbouring heterozygotes that have distance between them equal to i.

INPUT: filename, individual name (one of VCF columns).
	python vcf_reader.py example.vcf NA00001
	
OUTPUT: array H - histogram of lengths distribution.
