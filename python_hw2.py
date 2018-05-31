from Bio import SeqIO
import pandas as pd
import argparse

class Kmer_container:

    counter = 0
    sequence = ''

    def __init__(self, kmer_name):
        self.sequence = kmer_name
        self.locus_list = []
        self.seq_id_list = []

    def increase(self):
        self.counter += 1

    def increase_n(self, n):
        self.counter += n

    def positions(self, kmer_index,seq_id):
        self.locus_list.append(kmer_index)
        self.seq_id_list.append(seq_id)
        self.increase()

    def locuses_view(self):
        view_table = pd.DataFrame(columns=['kmer', 'kmer_position', 'sequence_id'])
        for i in range(self.counter):
            view_table.loc[i] = [self.sequence,str(self.locus_list[i])+':'+ str(self.locus_list[i]+23),self.seq_id_list[i]]
        print(view_table)

def kmer_parser(input,kmer_size):
    sequences = SeqIO.parse(input, 'fasta')
    known_kmers = {}
    for sequence in sequences:
        for i in range(len(sequence.seq) - kmer_size + 1):
            kmer = str(sequence.seq[i:(i+kmer_size)])
            if kmer in known_kmers:
                known_kmers[kmer].positions(i, sequence.id)
            else:
                known_kmers[kmer] = Kmer_container(kmer)
                known_kmers[kmer].positions(i,sequence.id)

    count = 0
    max_index = None
    for i in known_kmers:
        known_kmers[i].locuses_view()
        if known_kmers[i].counter > count:
            count = known_kmers[i].counter
            max_index=i
        else:
            continue

    print('______________________MOST COUNTED KMER____________________')
    print(known_kmers[max_index].locuses_view())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Time to find some kmers in your data!')
    parser.add_argument('-i', '--input', help='input sequences in fasta format', type=str, required=True)
    parser.add_argument('-s', '--size', help='kmer size', type=int, default=23)
    args = parser.parse_args()
    input = args.input
    size = args.size

    kmer_parser(input, size)

