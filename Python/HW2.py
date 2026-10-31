import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    def problem_1():
        #Write a Python program that takes a list of strings and converts all of them to uppercase to ensure consistency in the dataset.

        n = input()
        print(n.upper())

    problem_1()
    return


@app.cell
def _():
    def problem_2():
        #Write a Python program that takes a string and converts it to a list using a given separator. The program should print the resulting list to the standard output.
    
        n = input()
        s = input()
        res = n.split(s)
        print(res)

    problem_2()
    return


@app.cell
def _():
    def problem_3():
        #Write a Python program that checks if a specific word (provided by the user) is present in a list of words. The program should perform a case-insensitive search.

        string = input().upper().split(' ')
        key = input().upper()

        if key in string:
            return('Word found')

        return('Word not found')

    print(problem_3())
    return


@app.cell
def _():
    def problem_4():
        #Design a program that calculates and formats the performance metrics of an Instagram influencer. The user will input their name, follower count, and average number of likes per post (could be float). Your task is to calculate the engagement rate using the following formula:

    #engagement rate=likesfollowers⋅100engagement rate=followerslikes​⋅100

    #Your program should output the following summary for the given input:

    #"[Name], with [Followers] followers, has an average engagement rate of [Rate]% with [Likes] likes per post"

        nick = input()
        n_followers = int(input())
        likes_per_post = float(input())
        eng_rate = round(likes_per_post / n_followers * 100, 2)


        if likes_per_post.is_integer():
            formatted_likes = f"{int(likes_per_post):,}"
        else:
            formatted_likes = f"{likes_per_post:,}"

        # Build and print the formatted output summary
        res = f"{nick}, with {n_followers:,} followers, has an average engagement rate of {eng_rate:.2f}% with {formatted_likes} likes per post"

        print(res)


    problem_4()

    

    
    
    return


@app.cell
def _():
    def problem_5():

        n0 = int(input())
        epochs = int(input())

        ans = n0 * (2**epochs)

        print(f"After {epochs} divisions, the cell culture has grown to {ans:.2e} cells.")

    problem_5()
    return


@app.cell
def _():
    def problem_6():
        t = int(input())
        board = dict()

        for _ in range(t):
            name = input()
            score = int(input())
            board[name] = score


        header = 'Player                   Score'
        dashes = '------------------------------'

        print(header)
        print(dashes)

        for i in board:
            ngaps = len(dashes) - len(i) - len(str(board[i]))

            print(f"{i}{' '*ngaps}{str(board[i])}")

    problem_6()
    


    
    return


@app.cell
def _():
    def problem_7():

        arr = list(map(int, input().split(' ')))

        def _mean(arr):
            return(sum(arr)/len(arr))


        def _sd(arr):
            sd2 = 0
            mean_arr = _mean(arr)
            for i in arr:
                sd2 += ((i - mean_arr)**2) #/ len(arr) - 1
            
            sd2 /= len(arr)-1
        
            return(sd2**(0.5))

        print(round(_mean(arr),3), round(_sd(arr),3))

    problem_7()
            

    
    return


@app.cell
def _():
    return


@app.cell
def _():
    def problem_8():
        arr = list(map(float, input().split(' ')))


        def _mean(arr):
            return(sum(arr)/len(arr))


        def _sd(arr):
            sd2 = 0
            mean_arr = _mean(arr)
            for i in arr:
                sd2 += ((i - mean_arr)**2) #/ len(arr) - 1
            
            sd2 /= len(arr)-1
        
            return(sd2**(0.5))


        scaled = []

        m = _mean(arr)
        s = _sd(arr)
    
        for i in arr:

            scaled_i = (i - m) / s

            scaled.append(scaled_i)

        print(sorted(scaled))

    problem_8()

    


    return


@app.cell
def _():
    def problem_9():
        arr = list(map(str, input().split(' ')))

        hashmap = {i:0 for i in list(set(arr))}
        l = len(arr)

        for elem in arr:
            hashmap[elem] += 1

        for k in hashmap:
            val = hashmap[k] / l * 100
        
            hashmap[k] = f'{val:.2f}%'

        hashmap = dict(sorted(hashmap.items()))

        for i in hashmap:
            print(f'{i}: {hashmap[i]}')

    
    problem_9()
        

    
    return


@app.cell
def _():
    def problem_10():
        arr = list(map(str, input().split(' ')))

        hashmap = {i:[] for i in list(set(arr))}


        for i in range(len(arr)):

            hashmap[arr[i]].append(i)

        hashmap = dict(sorted(hashmap.items()))

        for i in hashmap:
            print(f"{i}: {' '.join(map(str, hashmap[i]))}")



    problem_10()
    
    
    return


@app.cell
def _():
    def problem_11():
        v1 = list(map(float, input().split(' ')))
        v2 = list(map(float, input().split(' ')))

        dotproduct = 0

        for i in range(len(v1)):
            dotproduct += v1[i] * v2[i]


        print(dotproduct)


    problem_11()
    return


@app.cell
def _():
    def problem_12():

        arr1 = list(map(int, input().split(', ')))

        arr2 = list(map(int, input().split(', ')))


        def merge(arr1,arr2):
    
            i = 0
            j = 0
            merged = []
            while i < len(arr1) and j < len(arr2):
    
                if arr1[i] < arr2[j]:
                    merged.append(arr1[i])
                    i += 1
    
                elif arr1[i] > arr2[j]:
                    merged.append(arr2[j])
                    j += 1
    
                else:
                    merged.append(arr1[i])
                    merged.append(arr2[j])
                    j += 1
                    i += 1
    
    
            if i == len(arr1):
                merged.extend(arr2[j:])
    
            if j == len(arr2):
                merged.extend(arr1[i:])
    
            return(merged)
    
    
    
        def merge_sort(arr):
            if len(arr) <= 1:
                return(arr)
    
            midpoint = (0 + len(arr)) //2
            left,right = arr[:midpoint], arr[midpoint:]
            return(merge(merge_sort(left), merge_sort(right)))


        arr1 = merge_sort(arr1)
        arr2 = merge_sort(arr2)
        arr = list(map(str,merge(arr1,arr2)))

        print(', '.join(arr))

    


    problem_12()

    
    return


@app.cell
def _():
    def problem_13():

        arr1 = list(map(int, input().split(', ')))

        arr2 = list(map(int, input().split(', ')))

        arr = arr1 + arr2

      #  print(arr)



        def merge(arr1,arr2):
    
            i = 0
            j = 0
            merged = []
            while i < len(arr1) and j < len(arr2):
    
                if arr1[i] < arr2[j]:
                    merged.append(arr1[i])
                    i += 1
    
                elif arr1[i] > arr2[j]:
                    merged.append(arr2[j])
                    j += 1
    
                else:
                    merged.append(arr1[i])
                    merged.append(arr2[j])
                    j += 1
                    i += 1
    
    
            if i == len(arr1):
                merged.extend(arr2[j:])
    
            if j == len(arr2):
                merged.extend(arr1[i:])
    
            return(merged)
    
    
    
        def merge_sort(arr):
            if len(arr) <= 1:
                return(arr)
    
            midpoint = (0 + len(arr)) //2
            left,right = arr[:midpoint], arr[midpoint:]
            return(merge(merge_sort(left), merge_sort(right)))


        arr = merge_sort(arr)

        hashmap = {i:[] for i in list(set(arr))}


        def format_n(n):
            if n == int(n):
                return(int(n))
            return(n)
        

        for i in range(len(arr)):
            hashmap[arr[i]].append(i+1)

        for n in hashmap:
            s = sum(hashmap[n])
            l = len(hashmap[n])

            hashmap[n] = format_n(s/l)

            print(f'{n}: {hashmap[n]}')

    problem_13()

        
    
    
    return


@app.cell
def _():
    def problem_14():

        arr1 = list(map(int, input().split(', ')))

        arr2 = list(map(int, input().split(', ')))

        arr = arr1 + arr2

      #  print(arr)



        def merge(arr1,arr2):
    
            i = 0
            j = 0
            merged = []
            while i < len(arr1) and j < len(arr2):
    
                if arr1[i] < arr2[j]:
                    merged.append(arr1[i])
                    i += 1
    
                elif arr1[i] > arr2[j]:
                    merged.append(arr2[j])
                    j += 1
    
                else:
                    merged.append(arr1[i])
                    merged.append(arr2[j])
                    j += 1
                    i += 1
    
    
            if i == len(arr1):
                merged.extend(arr2[j:])
    
            if j == len(arr2):
                merged.extend(arr1[i:])
    
            return(merged)
    
    
    
        def merge_sort(arr):
            if len(arr) <= 1:
                return(arr)
    
            midpoint = (0 + len(arr)) //2
            left,right = arr[:midpoint], arr[midpoint:]
            return(merge(merge_sort(left), merge_sort(right)))


        arr = merge_sort(arr)

        hashmap = {i:[] for i in list(set(arr))}


        

        for i in range(len(arr)):
            hashmap[arr[i]].append(i+1)

        for n in hashmap:
            s = sum(hashmap[n])
            l = len(hashmap[n])

            hashmap[n] = s/l



        def u(hashmap, arr):
          #  print(hashmap)
            n = len(arr)

            r = sum(hashmap[x] for x in arr)


            u = r - (n * (n + 1)) / 2


            return(u)


        answer = [u(hashmap, arr1), u(hashmap,arr2)]
        print(*answer)
    


    




    problem_14()
    
    return


if __name__ == "__main__":
    app.run()
