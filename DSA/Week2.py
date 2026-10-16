import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    def problem_1():
        t = int(input())
        t_i = 0
        solutions = []


        def solve(arr):

            if len(set(arr)) == 1:
                return(len(arr))
            else:
                return(1)

        while t_i < t:
            _ = input()
            arr = list(map(int, input().split(' ')))
            solutions.append(solve(arr))
        
            t_i += 1

        for i in solutions:
            print(i)


    problem_1()
    return


@app.cell
def _():
    def problem_2():
        t = int(input())
        t_i = 0
        solutions = []


        def solve(belt):

            answer = 0
        
            last_row = belt[-1][:-1]
            last_column = [row[-1] for row in belt][:-1]

            answer += last_row.count('D')
            answer += last_column.count('R')

            return(answer)
                    
        


        while t_i < t:

            nrows = list(map(int, input().split(' ')))[0]
            belt = []
            nrows_i = 0

            while nrows_i < nrows:
                belt.append(input())
                nrows_i += 1

            t_i += 1

            solutions.append(solve(belt))


        for i in solutions:
            print(i)


        
    problem_2()
    return


if __name__ == "__main__":
    app.run()
