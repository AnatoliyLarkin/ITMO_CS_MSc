import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    def problem1():

        def solve(a,b):
            # a > b
    
            n = ((a-b) // 10) 
            r = ((a-b) % 10) 
    
            if r != 0:
                n += 1
            return(n)
    
        t = int(input())
        t_i = 0
        answers = []
    
        while t_i < t:
            a,b = map(int, input().split(' '))
    
            if a == b:
                n = 0
            elif a > b:
                n = solve(a,b)
            else:
                n = solve(b,a)

            answers.append(n)
            t_i += 1

        for i in answers:
            print(i)
        

    problem1()
    return


@app.cell
def _():
    return


@app.cell
def _():
    def problem3():

        solution = []

        t = int(input())
        t_i = 0


        def solve(arr):
            n_strings = len(arr)
           # print(n_strings)
            arr = ''.join(arr)
    
            uniques = list(set(list(arr)))
            #print(arr, uniques)

            for i in uniques:
                #print(i, arr.count(i)//n_strings )
                if arr.count(i)%n_strings != 0:
                    return('NO')

            return('YES')

        

        while t_i < t:

            n = int(input())
            n_i = 0
            arr = []

            while n_i < n:

                n_i += 1
                arr.append(str(input()))

            res = solve(arr)
            solution.append(res)
            t_i += 1

        for i in solution:
            print(i)

    problem3()
        
    
    return


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    def problem_5():
        solution = []
        t = int(input())
        t_i = 0

        def solve(arr,k):
            k_i = 0

            while k_i < k:

                d = max(arr)
                for i in range(len(arr)):
                    arr[i] = d - arr[i]
                k_i += 1

            return(arr)
            

        while t_i < t:
            _, k = list(map(int, input().split(' ')))
            arr = list(map(int, input().split(' ')))
            solution.append(solve(arr,k))

            t_i += 1

        for i in solution:
            if len(i) == 1:
                print(str(i[0]))
            else:
                print(' '.join(list(map(str, i))))


    problem_5()
    return


if __name__ == "__main__":
    app.run()
