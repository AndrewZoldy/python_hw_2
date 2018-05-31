# python_hw_2

*Kmer_info*

Script parses your .fasta file and looks for k-mers.
It will show you an table of each k-mer info (sequence, indexes and id of record)

Given script requires path to input file, you have to define it with **-i** (**--input**) argument:

*-i /path/to/your/fasta_file.fasta*

*--input /path/to/your/fasta_file.fasta*

You can switch k-mer size as you wish, for this task use **-s** (**--size**) argument:

*-s 15*

*--size 15*

!By default -s argument has value = 23.

At the end of obtained table you can find sub-table for k-mer, which has maximum occurrence (indexes of each exemplar and id of record where it was founded).
