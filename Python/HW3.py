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


@app.function
def dist(*args):
    arr = [tuple(p) for p in args]

    if len(arr) < 2:
        return 0.0

    def euclidean_dist(p1, p2):
        d = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        return d ** (1 / 2)

    def solve_naively(sub_arr):
        min_dist = float('inf')
        for i in range(len(sub_arr)):
            for j in range(i + 1, len(sub_arr)):
                d = euclidean_dist(sub_arr[i], sub_arr[j])
                if d < min_dist:
                    min_dist = d
        return min_dist

    def find_min_dist(px, py):
        n = len(px)
        if n <= 3:
            return solve_naively(px)

        mid = n // 2
        mid_point = px[mid]

        left_x = px[:mid]
        right_x = px[mid:]

        left_set = set(left_x)
        left_y = []
        right_y = []
        for p in py:
            if p in left_set:
                left_y.append(p)
            else:
                right_y.append(p)

        d_left = find_min_dist(left_x, left_y)
        d_right = find_min_dist(right_x, right_y)
        d = min(d_left, d_right)

        strip = [p for p in py if abs(p[0] - mid_point[0]) < d]

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 8, len(strip))):
                if (strip[j][1] - strip[i][1]) >= d:
                    break
                d = min(d, euclidean_dist(strip[i], strip[j]))

        return d

    arr_sorted_x = sorted(arr, key=lambda x: (x[0], x[1]))
    arr_sorted_y = sorted(arr, key=lambda x: (x[1], x[0]))

    return find_min_dist(arr_sorted_x, arr_sorted_y)


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


@app.function
def apply_f(matrix, f, axis=0):

    
    if axis == 0:
        return [f(row) for row in matrix]
    elif axis == 1:
        return [f(list(col)) for col in zip(*matrix)]


@app.function
def cbind(l_1, l_2):

    for i in range(len(l_2)):
        for j in range(len(l_2[i])):
            l_1[i].append(l_2[i][j])

    return(l_1)


if __name__ == "__main__":
    app.run()
