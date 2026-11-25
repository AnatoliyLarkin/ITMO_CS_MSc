import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import sys
    def problem_1():
        t = int(input())
        answers =[]
        for _ in range(t):

            q   = sys.stdin.readline().split()

            n,x = int(q[0]), int(q[1])

            if n == 1 or n == 2:
                answers.append(1)

            else:
                f = int((n-3)/x) + 2

                answers.append(f)

        for i in answers:
            print(i)

    problem_1()
        

        
    return


@app.cell
def _():
    def problem_2():
        import sys
        input_data = sys.stdin.read().split()


        idx = 0
        t = int(input_data[idx])
        idx += 1

        results = []
        for _ in range(t):
            n = int(input_data[idx])
            m = int(input_data[idx + 1])
            idx += 2
    
            has_symmetric_tile = False
    
            for _ in range(n):
                a = int(input_data[idx])
                b = int(input_data[idx + 1])
                c = int(input_data[idx + 2])
                d = int(input_data[idx + 3])
                idx += 4
        
                if b == c:
                    has_symmetric_tile = True
            
            if m % 2 == 0 and has_symmetric_tile:
                results.append("YES")
            else:
                results.append("NO")
        
        for i in results:
            print(i)


    problem_2()
    return


@app.cell
def _():

    def problem_3():
        import sys
        import random
        input_data = sys.stdin.read().split()



        n = int(input_data[0])
        m = int(input_data[1])

        val = list(range(n + 1))
        prio = [random.randint(1, 10**9) for _ in range(n + 1)]

        sz = [0] + [1] * n
        left = [0] * (n + 1)


        right = [0] * (n + 1)


        stack = []
        for i in range(1, n + 1):
            last = 0
            while stack and prio[stack[-1]] < prio[i]:
        
                last = stack.pop()
                sz[last] = 1 + sz[left[last]] + sz[right[last]]
            left[i] = last
            if stack:
        
                right[stack[-1]] = i
            stack.append(i)
    
        while stack:
            curr = stack.pop()
            sz[curr] = 1 + sz[left[curr]] + sz[right[curr]]
    
        root = stack[0] if stack else (1 if n > 0 else 0)

        root = max(range(1, n + 1), key=prio.__getitem__)




        def split(t, k):
            if not t:
        
                return 0, 0
            left_sz = sz[left[t]]
    
            if k <= left_sz:
                l, left[t] = split(left[t], k)
        
                sz[t] = 1 + sz[left[t]] + sz[right[t]]
        
                return l, t
            else:
                right[t], r = split(right[t], k - left_sz - 1)

        
                sz[t] = 1 + sz[left[t]] + sz[right[t]]
                return t, r

        def merge(l, r):
            if not l or not r:
                return l or r
            if prio[l] > prio[r]:
                right[l] = merge(right[l], r)
                sz[l] = 1 + sz[left[l]] + sz[right[l]]
                return l
            else:
                left[r] = merge(l, left[r])
                sz[r] = 1 + sz[left[r]] + sz[right[r]]
                return r

        idx = 2
        for _ in range(m):
            l = int(input_data[idx]) - 1
    
            r = int(input_data[idx + 1]) - 1
            idx += 2
    
            if l == 0:
                continue
        
            t1, t2 = split(root, l)
            t2, t3 = split(t2, r - l + 1)
            root = merge(merge(t2, t1), t3)

        ans = []
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = left[curr]
            curr = stack.pop()
            ans.append(str(val[curr]))
            curr = right[curr]

        print(" ".join(ans))


    problem_3()
    
    return


@app.cell
def _():

    def problem_4():
      from itertools import chain
      import sys

      n, m = map(int, input().split())
      queries = [tuple(map(int, input().split())) for _ in range(m)]
      answers = []

      def solve(n, queries):
        B = 500
        arr = list(range(1, n + 1))
        blocks = [arr[i : i + B] for i in range(0, n, B)]
      
        rev = [False] * len(blocks)

        def split_at(pos):
          if pos == 0:
            return 0
          cur = 0

        
          for i, b in enumerate(blocks):
            if cur == pos:
              return i
            if cur + len(b) > pos:
            
              if rev[i]:
                b.reverse()
                rev[i] = False
              k = pos - cur
            
              blocks[i : i + 1] = [b[:k], b[k:]]
              rev[i : i + 1] = [False, False]
            
              return i + 1
            cur += len(b)
          return len(blocks)

        for l, r in queries:
        
          i1 = split_at(l - 1)
          i2 = split_at(r)

          blocks[i1:i2] = blocks[i1:i2][::-1]
        
          rev[i1:i2] = [not x for x in rev[i1:i2]]
        

          if len(blocks) > 2 * B:
            flat = list(
                chain.from_iterable(
                
                    b[::-1] if is_rev else b for b, is_rev in zip(blocks, rev)
                )
            )
            blocks = [flat[i : i + B] for i in range(0, n, B)]
          
            rev = [False] * len(blocks)

        res = list(
        
            chain.from_iterable(
                b[::-1] if is_rev else b for b, is_rev in zip(blocks, rev)
            )
        )
        return " ".join(map(str, res))

      answers.append(solve(n, queries))

      for i in answers:
        print(i)


    problem_4()
    return


@app.cell
def _():
    def problem_5():
        import random
        answers = []
        n, m = map(int, input().split())

        val = list(range(n + 1))
        prio = [random.randint(1, 10**9) for _ in range(n + 1)]
    
        left = [0] * (n + 1)

    
        right = [0] * (n + 1)
        sz = [1] * (n + 1)
    
        sz[0] = 0
    
        rev = [0] * (n + 1)

        def push(u):
        
            if rev[u]:
            
                left[u], right[u] = right[u], left[u]
                if left[u]:

                
                    rev[left[u]] ^= 1
                
                if right[u]:

                
                    rev[right[u]] ^= 1
                
                rev[u] = 0

        def pull(u):
            sz[u] = sz[left[u]] + sz[right[u]] + 1

        def split(u, k):
            if not u:
                return 0, 0
            
            push(u)
            left_sz = sz[left[u]]
        
            if k <= left_sz:
                l, r = split(left[u], k)
            
                left[u] = r
            
                pull(u)
                return l, u
            else:
                l, r = split(right[u], k - left_sz - 1)
                right[u] = l
                pull(u)
                return u, r

        def merge(l, r):
            if not l or not r:
                return l or r

            
            push(l)
            push(r)
            if prio[l] > prio[r]:
                right[l] = merge(right[l], r)
            
                pull(l)
                return l

            
            else:
                left[r] = merge(l, left[r])
            
                pull(r)
                return r
            

        root = 0
        for i in range(1, n + 1):
            root = merge(root, i)

        for _ in range(m):
        
            l, r = map(int, input().split())
            t1, t2 = split(root, l - 1)
            t2, t3 = split(t2, r - l + 1)
        
            rev[t2] ^= 1
            root = merge(merge(t1, t2), t3)
        

        stack = []
        curr = root
    
        while stack or curr:
            while curr:
            
                push(curr)
                stack.append(curr)
                curr = left[curr]

            
            curr = stack.pop()
            answers.append(val[curr])

        
            curr = right[curr]

        o = list(map(str, answers))
        print(' '.join(o))

    problem_5()
            
    return


@app.cell
def _():
    return


@app.cell
def _():
    def problem_6():
        answers = []
        n = int(input())
    
        bit = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    
        def add(x, y, z, delta):

        
            i = x + 1
            while i <= n:
                j = y + 1
                while j <= n:
                
                    k = z + 1
                
                    while k <= n:
                        bit[i][j][k] += delta
                    
                        k += k & -k
                    j += j & -j
                i += i & -i

        def prefix_sum(x, y, z):
            total = 0
            i = x + 1
            while i > 0:
            
                j = y + 1
            
                while j > 0:
                
                    k = z + 1
                
                    while k > 0:
                    
                        total += bit[i][j][k]
                    
                        k -= k & -k
                    j -= j & -j
                i -= i & -i
            return total

        while True:
        
            query = list(map(int, input().split()))
            m = query[0]
        
            if m == 3:
                break
            
            elif m == 1:
                x, y, z, k = query[1], query[2], query[3], query[4]
            
                add(x, y, z, k)
            elif m == 2:
                x1, y1, z1, x2, y2, z2 = query[1], query[2], query[3], query[4], query[5], query[6]
                s = (
                    prefix_sum(x2, y2, z2)
                
                    - prefix_sum(x1 - 1, y2, z2)
                
                    - prefix_sum(x2, y1 - 1, z2)
                
                    - prefix_sum(x2, y2, z1 - 1)
                
                    + prefix_sum(x1 - 1, y1 - 1, z2)
                
                    + prefix_sum(x1 - 1, y2, z1 - 1)
                
                    + prefix_sum(x2, y1 - 1, z1 - 1)
                    - prefix_sum(x1 - 1, y1 - 1, z1 - 1)
                )
                answers.append(s)

        for i in answers:
            print(i)

    problem_6()

    return


if __name__ == "__main__":
    app.run()
