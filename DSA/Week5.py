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
def _(bisect):
    import sys
    #import bisect

    def problem_3():
        answer = []

        def solve():
            input_data = sys.stdin.read().split()
            if not input_data:
                return
        
            arr = []
    
            for i in range(0, len(input_data), 2):
                cmd = input_data[i]
                x = int(input_data[i+1])
        
                if cmd == 'insert':
                    idx = bisect.bisect_left(arr, x)
                    if idx == len(arr) or arr[idx] != x:
                        arr.insert(idx, x)
                
                elif cmd == 'delete':
                    idx = bisect.bisect_left(arr, x)
                    if idx < len(arr) and arr[idx] == x:
                        arr.pop(idx)
                
                elif cmd == 'exists':
                    idx = bisect.bisect_left(arr, x)
                    if idx < len(arr) and arr[idx] == x:
                        answer.append('true')
                    else:
                        answer.append('false')
                
                elif cmd == 'next':
                    idx = bisect.bisect_right(arr, x)
                    if idx < len(arr):
                        answer.append(str(arr[idx]))
                    else:
                        answer.append('none')
                
                elif cmd == 'prev':
                    idx = bisect.bisect_left(arr, x)
                    if idx > 0:
                        answer.append(str(arr[idx-1]))
                    else:
                        answer.append('none')

        solve()

        for i in answer:
            print(i)


    problem_3()
    return


@app.cell
def _():
    def problem_4():
        import bisect


        answers = []
        arr = []
        n = int(input())

        for i in range(n):


            q = list(map(int, input().split()))
            cmd, x = q[0],q[1]

            if cmd == 1:
                    idx = bisect.bisect_left(arr, x)
                    if idx == len(arr) or arr[idx] != x:
                        arr.insert(idx, x)

            elif cmd == -1:
                    idx = bisect.bisect_left(arr, x)
                    if idx < len(arr) and arr[idx] == x:
                        arr.pop(idx)

            else:
                answers.append(arr[-x])


        for i in answers:
            print(i)

    problem_4()
        
        
    

    return


@app.cell
def _():
    def problem_5():
        import bisect
        answers = []

        n = int(input())
        arr = []
        last_y = 0
        prev_was_query = False

        for _ in range(n):
            cmd = input().split()

            if cmd[0] == '+':
                x = int(cmd[1])
        
                if prev_was_query:
                    x = (x + last_y) % 10**9
            
                idx = bisect.bisect_left(arr, x)
                if idx == len(arr) or arr[idx] != x:
                    arr.insert(idx, x)
            
                prev_was_query = False

            else:
                l, r = int(cmd[1]), int(cmd[2])

                idx_l = bisect.bisect_left(arr, l)
                idx_r = bisect.bisect_right(arr, r)

                last_y = sum(arr[idx_l:idx_r])
                answers.append(last_y)
        
                prev_was_query = True

        for i in answers:
            print(i)


    problem_5()
        

    return


@app.cell
def _():
    def problem_e():
        import sys
        import random

        data = sys.stdin.read().split()

    
        n = int(data[0])
        idx = 1
    
        max_nodes = n + 2
        key = [0] * max_nodes
        prio = [0] * max_nodes
        sub_sum = [0] * max_nodes
        left = [0] * max_nodes
        right = [0] * max_nodes
    
        node_cnt = 0
        root = 0
        rand = random.getrandbits

        def new_node(x):
            nonlocal node_cnt
            node_cnt += 1
            key[node_cnt] = x

        
            prio[node_cnt] = rand(30)
            sub_sum[node_cnt] = x
            return node_cnt

        def pull(t):
            if t:
                sub_sum[t] = key[t] + sub_sum[left[t]] + sub_sum[right[t]]


            

        def split(t, x):
            if not t:
                return 0, 0
            if key[t] < x:
                l_tree, r_tree = split(right[t], x)
            
                right[t] = l_tree
                pull(t)
            
                return t, r_tree
            else:
                l_tree, r_tree = split(left[t], x)
                left[t] = r_tree
                pull(t)
                return l_tree, t

        def merge(a, b):
            if not a or not b:
                return a or b
            
            if prio[a] > prio[b]:
                right[a] = merge(right[a], b)
                pull(a)
                return a
            else:
                left[b] = merge(a, left[b])
            
                pull(b)
                return b

        seen = set()
        last_y = 0
        MOD = 10**9
        out = []

        for _ in range(n):
            op = data[idx]
            if op == '+':
                val = (int(data[idx + 1]) + last_y) % MOD
                idx += 2
                last_y = 0  
            
                if val not in seen:
                    seen.add(val)
                    t1, t2 = split(root, val)
                    root = merge(merge(t1, new_node(val)), t2)
            else:
                l = int(data[idx + 1])
                r = int(data[idx + 2])
                idx += 3
            
                if l > r:
                    last_y = 0
                else:
                    t1, t2 = split(root, l)
                    t2, t3 = split(t2, r + 1)
                    last_y = sub_sum[t2]
                    root = merge(merge(t1, t2), t3)
                out.append(str(last_y))


        sys.stdout.write('\n'.join(out) + '\n')


    problem_e()
    return


if __name__ == "__main__":
    app.run()
