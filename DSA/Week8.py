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
        answers = []

        def solve(a,b,x):
            b = b[::-1]

            for i in range(len(b)):
                if not b[i] + a[i] <= x:
                    return('No')
            return('Yes')

        for n in range(t):
            x = list(map(int,input().split()))[1]
            a = list(map(int,input().split()))
            b = list(map(int,input().split()))

            if n != (t-1):
                _ = input()


            answers.append(solve(a,b,x))


        for i in answers:
            print(i)


    problem_1()
    return


@app.cell
def _():
    from collections import deque


    def problem_3():
        n1 = int(input())
        arr1 = list(map(int,input().split()))
        n2 = int(input())
        arr2 = list(map(int,input().split()))

        dp = [[0 for i in range(n1+1)] for j in range(n2+1)]





    



        for j in range(1,n1+1):
            for i in range(1, n2+1):
                if arr2[i-1] == arr1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    if dp[i-1][j] > dp[i][j-1]:
                        dp[i][j] = dp[i-1][j]

                    else:
                        dp[i][j] = dp[i][j-1]




    #    for i in dp:
    #        print(i)

    
        dist = dp[-1][-1]
        lcs = deque()

        j = n1 
        i = n2 

        while i > 0 and j > 0:

            if arr1[j-1] == arr2[i-1]:
                lcs.appendleft(str(arr1[j-1]))
                i -= 1
                j -= 1

            else:

                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1

                else:
                    j -= 1
            
        print(dist)
        print(' '.join(list(lcs)))

    problem_3()
    return


@app.cell
def _():
    def problem_2():
        answers = []

        t = int(input())

        def solve(n):
            seats = list()

            for i in range(1,n+1):
                seat = 2* (n+i)
                seats.append(str(seat))

            return(' '.join(seats))
    

        for _ in range(t):
            n = int(input())
            answers.append(solve(n))

        for i in answers:
            print(i)


    



    problem_2()

    return


@app.cell
def _():
    def problem_4():
        s1 = input()
        s2 = input()

        dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
        dp[0] = [i for i in range(len(s1)+1)]


        for i in range(len(dp)):
            dp[i][0] = i


        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                cost = 0 if s2[i - 1] == s1[j - 1] else 1

                dp[i][j] = min(
                    dp[i - 1][j] + 1,     
                    dp[i][j - 1] + 1,     
                    dp[i - 1][j - 1] + cost)
        
       # for i in dp:
       #     print(i)
        dist = dp[-1][-1]
        print(dist)
    problem_4()
    return


@app.cell
def _():
    def problem_5():
    
        def solve(s):
            n = len(s)
            if n < 2:
                return 0

            pairs = {"(": ")", "[": "]", "{": "}"}
            dp = [[0] * n for _ in range(n)]

            for length in range(2, n + 1):
                for i in range(n - length + 1):
                    j = i + length - 1

                    if s[i] in pairs and pairs[s[i]] == s[j]:
                        dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)

                    for k in range(i, j):
                        dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])

            return dp[0][n - 1]

        s = input().strip()        
        print(solve(s))


    problem_5()
    return


if __name__ == "__main__":
    app.run()
