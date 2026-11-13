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
        answer = []



        def solve(arr,l):

            i = 0
            while i + 2 < l:
                window = arr[i:i+3]

                if window[0] < window[1] and window[1] > window[2]:
                    return([i+1, i+2, i+3])
                
                else:
                    i += 1
            
    
            return(False)
        T = int(input())
        for _ in range(T):
            l = int(input())
            arr = list(map(int, input().split(' ')))
    
            solution = solve(arr,l)

            if not solution:
                answer.append('NO')
            else:
                answer.append('YES')
                answer.append(solution)


        for i in answer:
            if type(i) == str:
                print(i)
            else:
                print(*i)


    problem_1()
        
    return


@app.cell
def _():
    def problem_2():
        t = int(input())
        answers = []

        for _ in range(t):

            n = int(input())

            answers.append((n+1)//2)


        for i in answers:
            print(i)

    problem_2()
    return


if __name__ == "__main__":
    app.run()
