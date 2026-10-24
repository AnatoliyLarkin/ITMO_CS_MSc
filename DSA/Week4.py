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
        for _ in range(t):
            n = int(input())
            answers.append([1]*n)

        for i in answers:
            print(*i)
    problem_1()

        
    return


@app.cell
def _():
    def problem_2():

        def count_n(s):

            zeros, ones = 0,0

            for i in list(s):
                if i == '0':
                    zeros += 1
                else:
                    ones += 1
            return(zeros,ones)
    
        def solve(s):

            zeros,ones = count_n(s)

            if min(zeros,ones) % 2 == 1:
                return('DA')
            else:
                return('NET')

        

    
        solutions = []
        t = int(input())

        for _ in range(t):

            string = input()
            solutions.append(solve(string))

        for i in solutions:
            print(i)


    problem_2()
    return


@app.cell
def _():
    def problem_3():
        from collections import deque

        answers = []
        q = deque()

        n_ops = int(input())

        for _ in range(n_ops):

            query = input()

            if query.startswith('+'):
                n = int(query.split(' ')[1])
                q.append(n)
            else:
                answers.append(q.popleft())


        for i in answers:
            print(i)


    problem_3()
    
            
        
    return


@app.cell
def _():
    def problem_4():
        from collections import deque

        answers = []
        hashmap = dict()

        n_ops = int(input())

        def check_if_idx_exist(hashmap, idx):
            if idx not in hashmap:
                hashmap[idx] = deque()
            return(hashmap)

    
        for _ in range(n_ops):

            query = input().split(' ')

            if query[0] == 'pushfront':
                idx = int(query[1])
                n = int(query[2])
                hashmap = check_if_idx_exist(hashmap,idx)
                hashmap[idx].appendleft(n)

            elif query[0] == 'pushback':
                idx = int(query[1])
                n = int(query[2])
                hashmap = check_if_idx_exist(hashmap,idx)
                hashmap[idx].append(n)

            elif query[0] == 'popfront':
                idx = int(query[1])
                answers.append(hashmap[idx].popleft())

            elif query[0] == 'popback':
                idx = int(query[1])
                answers.append(hashmap[idx].pop())


        for i in answers:
            print(i)


    problem_4()


            
        

    
    return


@app.cell
def _():
    def problem_6():
        from collections import deque
        q = deque()
        answers = []

        n_ops = int(input())

        for i in range(n_ops):

            query = input()

            if query.startswith('+'):
                idx = int(query.split(' ')[1])
                q.append(idx)

            elif query == '-':
                answers.append(q.popleft())

            else:
                idx = idx = int(query.split(' ')[1])
                q = list(q)
                midpoint = (len(q) + 1) // 2
                q = q[:midpoint] + [idx] + q[midpoint:]
                q = deque(q)

        for i in answers:
            print(i)

    problem_6()
            
    return


if __name__ == "__main__":
    app.run()
