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
        nrows, ncols = map(int, input().split())
        for _ in range(nrows):
            row = list(map(int, input().split()))
            mat.append(row)

        dp = [[float('inf')] * (ncols + 1) for _ in range(nrows + 1)]
        dp[1][1] = mat[0][0]

        for i in range(1, nrows + 1):
            for j in range(1, ncols + 1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + mat[i-1][j-1]

        print(dp[-1][-1])


    problem_6()
    return


@app.cell
def _():
    from collections import deque
    def problem_5():
        q = list(map(int, input().split()))
        n,k_max = q[0], q[1]
        coins = [0] + list(map(int, input().split(' '))) + [0]

        dp_coins = [0] + [float('-inf')]*(len(coins)-2) + [float('-inf')]
       # print(coins, dp_coins)

        parents = [0] * len(dp_coins)
       # print(parents)

        for cell_idx in range(1, len(dp_coins)):
            for k in range(1,k_max+1):
                if cell_idx-k < 0:
                    break



                if dp_coins[cell_idx-k] + coins[cell_idx] > dp_coins[cell_idx]:
                    dp_coins[cell_idx] = dp_coins[cell_idx-k] + coins[cell_idx]
                    parents[cell_idx] = cell_idx-k


        path = deque()

        current_cell = len(parents) - 1
        while True:
            if current_cell == 0:
                path.appendleft(str(current_cell+1))
                break

            else:
                path.appendleft(str(current_cell+1))
                current_cell = parents[current_cell]




        print(dp_coins[-1])
        print(len(path)-1)
        print(' '.join(path))
  





    problem_5()
    return


@app.cell
def _():
    def problem_7():
        MOD = 10**9 + 7

        def mat_mul(A, B):
            size = len(A)
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                row_a = A[i]
            
                row_c = C[i]
                for k in range(size):
                    if row_a[k] == 0:
                    
                        continue
                    val = row_a[k]
                    row_b = B[k]
                
                    for j in range(size):
                        row_c[j] = (row_c[j] + val * row_b[j]) % MOD
            return C

        def mat_pow(M, power):
            size = len(M)
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            while power > 0:
                if power & 1:
                    res = mat_mul(res, M)
                M = mat_mul(M, M)
                power >>= 1
            return res

        k, n = map(int, input().split())
        f = [int(x) % MOD for x in input().split()]
        a = [int(x) % MOD for x in input().split()]

        if n < k:
            fn = f[n]
            s = sum(f[: n + 1]) % MOD
            print(fn, s)
            return

        size = k + 1
        T = [[0] * size for _ in range(size)]

        T[0][0] = 1
        for j in range(k):
            T[0][j + 1] = a[j]

        
            T[1][j + 1] = a[j]

        for i in range(2, size):
        
            T[i][i - 1] = 1

        T_pow = mat_pow(T, n - k + 1)

        V = [sum(f) % MOD] + f[::-1]

        s_n = sum(T_pow[0][j] * V[j] for j in range(size)) % MOD
    
        f_n = sum(T_pow[1][j] * V[j] for j in range(size)) % MOD

        print(f_n, s_n)

    problem_7()

    return


@app.cell
def _():
    from collections import deque as dq


    def problem_8():
      n = int(input())

      arr = list(map(int, input().split()))

      dp = [1] * n
      parents = [-1] * n

      for i in range(n):
        for j in range(i):
          if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            parents[i] = j

      max_length = max(dp)
      current_cell = dp.index(max_length)

      path = dq()

      while current_cell != -1:
        path.appendleft(str(arr[current_cell]))
        current_cell = parents[current_cell]

      print(max_length)
      print(' '.join(path))


    problem_8()
    return


if __name__ == "__main__":
    app.run()
