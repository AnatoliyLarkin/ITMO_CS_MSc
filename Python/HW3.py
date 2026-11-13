import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    def ch_count(s : str, ch = 'CG'):

        hashmap = {i:0 for i in set(list(ch))}
        for i in list(s):
            if i in hashmap:
                hashmap[i] += 1


        return(hashmap)


    ch_count('ABCDEF', ch = 'ABC')

    return


app._unparsable_cell(
    r"""
    def dist(arr):


        def euclidean_dist()
    """,
    name="_"
)


@app.cell
def _():
    def h_dist(s1,s2):
        h_dist = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                h_dist += 1
        return(h_dist)

    h_dist("CAGCCTACTAACGGGAT","CATCGTAATGACGGCCT")
    return


@app.cell
def _():
    def get_prot(s):


        rna_codons = {
        "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
        "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
        "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
        "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
        "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
        "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
        "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
        "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
        "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
        "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
        "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
        "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
        "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
        "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }

        i = s.index('AUG') + 3
        prot = ''


        while i+2 < len(s):
            codon = s[i:i+3]

            if rna_codons[codon] == '*':
                return(prot)
        
            prot += rna_codons[codon]
            i += 3

        return(prot)

    rna_seq = "CAUGCAUGAAUUACUUUGGAGACUGGACUAGU"
    get_prot(rna_seq) # returns "HELLWRLD"
    return


@app.cell
def _():
    def calc_mass(s):
        mass = 0

        amino_acid_mass = {
        "G": 57.021464,
        "A": 71.037114,
        "S": 87.032028,
        "P": 97.052764,
        "V": 99.068414,
        "T": 101.047678,
        "C": 103.009184,
        "I": 113.084064,
        "L": 113.084064,
        "N": 114.042927,
        "D": 115.026943,
        "Q": 128.058578,
        "K": 128.094963,
        "E": 129.042593,
        "M": 131.040485,
        "H": 137.058912,
        "F": 147.068414,
        "R": 156.101111,
        "Y": 163.063329,
        "W": 186.079313,
    }
        for i in list(s):
            mass += amino_acid_mass[i]

        return(mass)

    calc_mass("GTYCWIF")
    return


@app.cell
def _():
    def get_unique_characters(arr):
        merged = ''

        for i in arr:
            merged += i

        uniques = list(set(list(merged)))
        return(uniques)

    def profile_dict(*args):

    
        unique_characters = get_unique_characters(args)

        l = len(args[0])

        matrix = {i: [0] * l for i in unique_characters}

        for s in args:

            for i in range(len(s)):

                matrix[s[i]][i] += 1

        return(matrix)
    
    

    

    profile_dict("AAAAAAAA","CCCCCTGC","ATGGATCT")
    return


@app.cell
def _():
    flat_res = []


    def flat_list(lst, flat_res):
        for elem in lst:
            if isinstance(elem, list):
                flat_list(elem, flat_res)
            else:
                flat_res.append(elem)
        return flat_res


    flat_res = []
    flat_res = flat_list([1, [2, [3, 4]]], flat_res)
    flat_res
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
