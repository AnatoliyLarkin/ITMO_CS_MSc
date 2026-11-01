import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    from math import log2
    def find_enthropy(s):
        allowed_symbols = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        s = s.upper()
        s = [i for i in s if i in allowed_symbols]
        hashmap_p = {i: s.count(i)/len(s) for i in list(allowed_symbols)}
        H = 0
        for i in hashmap_p:
            H += hashmap_p[i] * log2(hashmap_p[i]+10**-10)
        H *= -1
        return(round(H,3))
    

    return (find_enthropy,)


@app.cell
def _(find_enthropy):
    import urllib.request

    url = "https://ctlab.itmo.ru/~aivanov/bi_2026/text_en.txt"

    with urllib.request.urlopen(url) as response:
        s = response.read().decode('utf-8')

    print(find_enthropy(s))
    return


if __name__ == "__main__":
    app.run()
