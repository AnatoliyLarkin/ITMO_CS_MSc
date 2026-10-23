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

        t = int(input())
        t_i = 0


        edgecases = {36 : [15,14,6,1], 40: [14,15,10,1], 44: [14,15,10,5]}

        def solve(n):
            if n <= 30:
                return([['NO'], []])

            elif n in edgecases:
                return([['YES'], edgecases[n]])

            else:
                x = n - 6 - 10 - 14

                return([['YES'], [6,10,14, x]])

    


        while t_i < t:

            n = int(input())

            solution = solve(n)

            for i in solution:
                if i:
                    answer.append(i)

            t_i += 1


        for i in answer:
            print(*i)


    problem_1()
    return


@app.cell
def _():
    def problem_6():

        n = int(input())
        n_i = 0
        answer = []
        stack = []
        while n_i < n:


            n_i += 1
            cmd = input()
            try:
                cmd = int(cmd)
                answer.append(stack.pop())
            except:
                k = list(map(int, cmd.split(' ')))[1]
                stack.append(k)

        for i in answer:
            print(i)


    problem_6()

    return


@app.cell
def _():
    def problem_7():
        query = list(input())
        stack = []
        lefts = set(['(', '{', '['])
        rights = set([')', '}', ']'])
        hashmap = {')': '(', '}': '{', ']': '['}

        for s in query:
            if s in lefts:
                stack.append(s)

            elif s in rights:

                if not stack:
                    return(False)

                prev = stack.pop()

                if hashmap[s] != prev:
                    return(False)


        if len(stack) == 0:
           return(True)
        return(False)

    ans = problem_7()
    if ans:
        print('YES')
    else:
        print('NO')
        
    
    
    return


@app.cell
def _():
    def problem_8():
        answers = []
        current_stack = []
        min_stack = []

        n =int(input())
        n_i = 0

        while n_i < n:

            cmd = input()

            try: 
                cmd = int(cmd)

                if cmd == 2:
                    current_stack.pop()
                    min_stack.pop()

                elif cmd == 3:
                    answers.append(min_stack[-1])


            except:

                k = list(map(int, cmd.split(' ')))[-1]
                current_stack.append(k)

                if not current_stack or not min_stack or k <= min_stack[-1]:
                    min_stack.append(k)
                else:
                    min_stack.append(min_stack[-1])


            n_i += 1

        for i in answers:
            print(i)


    problem_8()



    return


@app.cell
def _():
    def problem_2():
        t = int(input())
        t_i = 0
        answers = []

        def solve(arr,n):
            seen = set([])
            p = []
            n_i = 0


            for i in arr:
                if i not in seen:
                    seen.add(i)
                    p.append(i)
                    n_i += 1
                if n_i == n:
                    return(p)



        while t_i < t:

            t_i += 1
            n = int(input())
            arr = list(map(int, input().split(' ')))
            solution = solve(arr,n)
            answers.append(solution)

        for i in answers:
            print(*i)


    problem_2()

    return


@app.cell
def _():
    return


@app.cell
def _():
    def problem_3():
        _ = input()
        arr = list(map(int, input().split(' ')))
        k = int(input())
        k_i = 0
        answers = []


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






        def merge_sort(arr):

            if len(arr) == 1:
                return(arr)

            else:
                midpoint = len(arr) // 2
                s1,s2 = arr[:midpoint], arr[midpoint:]
                return(merge(merge_sort(s1), merge_sort(s2)))




        def binary_search(n,arr, low, up):

            if low > up:
                return(False)

            midpoint = (low+up) // 2

            if arr[midpoint] == n:
                return(midpoint)

            elif n < arr[midpoint]:
                return(binary_search(n,arr,low,midpoint-1))

            else:
                return(binary_search(n,arr, midpoint+1, up))

        arr_x = merge_sort(arr)
        while k_i < k:


            query = list(map(int, input().split(' ')))
            l,r = query[0], query[1]

            l_index = binary_search(l, arr_x, 0, len(arr_x)-1)
            r_index = binary_search(r, arr_x, 0, len(arr_x)-1)

    

    
            k_i += 1

            answers.append(r_index - l_index)

        answers = ' '.join(list(map(str, answers)))

        print(answers)



    problem_3()
    return


@app.cell
def _():
    def problem_4():

        C = float(input())

        low = 0
        up = C
    
        gap = 1e-8 
    
        while True: 
            midpoint = (low + up) / 2
            C_i = midpoint**2 + midpoint**(0.5)
            if abs(C_i - C) < gap:
                x = round(midpoint, 10)
                break        
            if C_i > C:
                up = midpoint
            else:
                low = midpoint

        print(x)




    problem_4()
    return


if __name__ == "__main__":
    app.run()
