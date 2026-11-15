import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo


    return


@app.cell
def _():
    def problem_2():
        t = int(input())
        answers = []


        def solve(arr):
            first_book_idx = -1
            last_book_idx = -1
        
            for i in range(len(arr)):

                if arr[i] == 1:

                    if first_book_idx == -1:
                        first_book_idx = i
                    last_book_idx = i

            if first_book_idx == last_book_idx:
                return(0)

            else:
                return(arr[first_book_idx:last_book_idx+1].count(0))
            

        for _ in range(t):
            foo = input()
            arr = list(map(int,input().split(' ')))
            n = solve(arr)
            answers.append(n)

        for i in answers:
            print(i)

    problem_2()
    return


@app.cell
def _():
    def problem_3():
        n = int(input())
        numbers = [0] + list(map(int, input().split()))

        dp = [0] * (n + 1)
        dp[1] = numbers[1]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2], dp[i - 1]) + numbers[i]

        return dp[n]

    print(problem_3())
    return


@app.cell
def _():
    def problem_4():

        q = list(map(int, input().split()))
        n,k_max = q[0], q[1]

        dp = [0 for i in range(n)]
        dp[0] = 1



        for cell_idx in range(1, len(dp)):


            for k in range(1,k_max+1):
                if cell_idx-k < 0:
                    break
            
                dp[cell_idx] += (dp[cell_idx-k])


        print(dp[-1])

            


    problem_4()
    
    return


@app.cell
def _():
    def problem_1():
        ans = []
        t = int(input())

        for _ in range(t):
            m = list(map(int, input().split()))[1]
            arr = list(map(int, input().split()))

            if sum(arr) == m:
                ans.append('YES')
            else:
                ans.append('NO')


        for i in ans:
            print(i)

    problem_1()
    return


@app.cell
def _():
    def problem_6():
        mat = []
        x = list(map(int, input().split()))
        nrows, ncols = x[0],x[1]
        for _ in range(nrows):
            row = list(map(int, input().split()))
        
            mat.append(row)
    


        dp = [[float('inf')] * ncols+1 for _ in range(nrows+1)]


        dp[1][1] = mat[0][0]


        for i in range(1,len(dp-1)):
            for j in range(1,len(dp[i]-1)):
                dp[i][j]

        for i in mat:
            print(i)


        for i in dp:
            print(i)
    
    problem_6()
    return


if __name__ == "__main__":
    app.run()
