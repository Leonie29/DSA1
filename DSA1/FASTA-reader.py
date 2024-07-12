import sys

def read_fasta(filename, ids):
    print(filename)
    for id in ids:
        print(id)

if __name__ == '__main__':
    arguments = sys.argv[1:]
    filename = arguments[0]
    ids = arguments[1:]
    
    read_fasta(filename, ids)