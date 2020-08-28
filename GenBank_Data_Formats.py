from Bio import Entrez
from Bio import SeqIO

def genbank(ids):
    Entrez.email = "aia5618@psu.edu"
    ids = ids.replace(" ", ", ")

    # Fetch data from GenBank server
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))

    # Find shortest string
    min = 9999999999
    id = 0
    for i in range(len(records)):
            print (">" + records[id].description)
            print (records[id].seq)
        #if len(records[i].seq) < min:  
            #min = len(records[i].seq)
            #id = i
            

# Tests
genbank("NM_001009148 JF927157")


#The Smallest GenBank Entry ID will be displayed in the output
#This was an answer to a ROSALIND Armory question, but it can be altered to display multiple GenBank ID's

