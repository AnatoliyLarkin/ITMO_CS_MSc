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


@app.cell
def _():
    def problem_3():
        _ = input()

    
        def merge(subarr1, subarr2):
    
    
            if True:
                merged_array = []
    
                i, i_max = 0, len(subarr1) 
                j, j_max = 0, len(subarr2) 
    
                while i < i_max and j < j_max:
    
                    if subarr1[i] <= subarr2[j]:
                        merged_array.append(subarr1[i])
                        i += 1
                    else:
                        merged_array.append(subarr2[j])
                        j += 1
    
    
                if i == i_max:
                    merged_array.extend(subarr2[j:])
    
                else:
                    merged_array.extend(subarr1[i:])
    
                return(merged_array)

            

    
            

        def solve(arr):

            if len(arr) == 1:
                return(arr)

            else:
                midpoint = len(arr) // 2
                s1,s2 = arr[:midpoint], arr[midpoint:]
                return(merge(solve(s1), solve(s2)))
        
        

        

        arr = list(map(int, input().split(' ')))

        solution = solve(arr)
        print(*solution)

    problem_3()
    return


@app.cell
def _():
    def problem_4():
        _ = input()

    
        def solve(arr):

            count_array = [0 for i in range(10)]

            for i in arr:
                count_array[int(i)] += 1

            num = ''

            for i in range(len(count_array)):
                if count_array[i] != 0:
                    num += count_array[i] * str(i)

            return(num[::-1])


        

        

        arr = list(input().split(' '))

        solution = solve(arr)
    
        print(solution)

    problem_4()
    return


if __name__ == "__main__":
    app.run()
