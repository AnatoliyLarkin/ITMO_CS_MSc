import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    #Write a program that prints the Hello World! string.
    def solve_problem1():
        print('Hello World!')

    solve_problem1()
    return


@app.cell
def _():
    #Write a Python program that reads two strings from the input and concatenates them into a single string. The result should be printed as the output.
    def solve_problem2():
        a,b = input(), input()
        print(a+b)


    solve_problem2()
    return


@app.cell
def _():
    #Write a Python program that reads a string and an integer, and repeats the string a specified number of times. The program should then print the resulting repeated string.
    def solve_problem3():
        a,n = input(), int(input())

        print(a*n)

    solve_problem3()
    return


@app.cell
def _(x):
    #Create a variable y and assign it the same value as variable x. Assume that variable x was assigned previously and you can refer to it in your code.
    def solve_problem4(x):
        y = None
        y = x

    solve_problem4(x)
    return


@app.cell
def _(x, y):
    #You have two variables x and y. Write a program that swaps the values of two variables.
    def solve_problem5(x,y):
        y,x = x,y

    solve_problem5(x,y)
    return


@app.cell
def _():
    #Write a Python program that calculates the mean (average) of a list of floating-point numbers provided as input. The numbers will be given one per line, and the end of the list is indicated by the symbol *.
    def solve_problem6():

        arr = []
    
        while True:
            x = input()

            if x == '*':
                break
            arr.append(float(x))

        if arr:
            print(sum(arr)/len(arr))

    solve_problem6()
        
       
    
    return


@app.cell
def _():
    #Write a Python program that finds both the minimum and maximum values from a list of floating-point numbers provided as input. The numbers will be entered one per line, and the input will end with the symbol *.


    def solve_problem7():
        arr = []

        while True:
            x = input()
            if x == '*':
                break
            arr.append(float(x))

        min_value = float('inf')
        max_value = float('-inf')

        for i in arr:

            if i > max_value:
                max_value = i
            if i < min_value:
                min_value = i

        print(min_value, max_value)

    solve_problem7()
    return


@app.cell
def _():
    #Write a Python program that determines whether a given value has a high or low expression based on a provided threshold. The program will take two inputs: the value to be evaluated and the threshold. If the value is greater than or equal to the threshold, it is considered “High expression”, otherwise, it is considered “Low expression”.
    def solve_problem8():
        val, threshold = float(input()), float(input())

        if val >= threshold:
            print('High expression')
        else:
            print('Low expression')

    solve_problem8()
    return


@app.cell
def _():
    #Write a Python program that evaluates a list of floating-point numbers and determines whether each value has high or low expression based on a given threshold. If a value is greater than or equal to the threshold, it is considered "High expression", otherwise, it is considered "Low expression".


    def solve_problem9():
    
        threshold = float(input())
        arr = []

        while True:
            x = input()
            if x == '*':
                break
            arr.append(float(x))

        for val in arr:
            if val >= threshold:
                print('High expression')
            else:
                print('Low expression')

    solve_problem9()
        
    
    return


@app.cell
def _():
    #Write a Python program that calculates the mean (average) values for two groups of floating-point numbers. The first 5 numbers represent Group A, and the last 5 numbers represent Group B. Your task is to compute and display the mean for both groups separately.


    def solve_problem10():
        arr1 = []
        arr2 = []


        while len(arr1) < 5:
            arr1.append(float(input()))

        while len(arr2) < 5:
            arr2.append(float(input()))


        for arr in [arr1,arr2]:
            print(sum(arr)/len(arr))

    solve_problem10()
    return


@app.cell
def _():
    #Write a Python program that calculates the Fold Change between two groups of floating-point numbers. The first 5 numbers represent Group A, and the last 5 numbers represent Group B. The Fold Changes is calculated as the ratio of the mean of Group B to the mean of Group A. Your task is to compute the Fold Change and output the result.


    def solve_problem11():
        arr1 = []
        arr2 = []


        while len(arr1) < 5:
            arr1.append(float(input()))

        while len(arr2) < 5:
            arr2.append(float(input()))


        arr1_mean = sum(arr1)/len(arr1)
        arr2_mean = sum(arr2)/len(arr2)

        print(arr2_mean/arr1_mean)

    solve_problem11()
    return


@app.cell
def _():
    #Write a Python program that reads a list of integers and calculates two values:

       # The sum of all positive numbers in the list.
       # The sum of all negative numbers in the list.


    def solve_problem12():
        arr = []

        while True:
            x = input()
            if x == '*':
                break
            arr.append(float(x))


        sum_pos = 0
        sum_neg = 0

        for i in arr:
            if i >= 0:
                sum_pos += i
            else:
                sum_neg += i

        print(int(sum_pos), int(sum_neg))

    solve_problem12()

    

    return


@app.cell
def _():
    #Write a Python program that surrounds a given string with another string (prefix and suffix) using the + operator.

    def solve_problem13():
        a = input()
        b = input()

        print(b+a+b)

    solve_problem13()
    return


@app.cell
def _():
    # Consider the lactose operon. The program receives two lines as input. The first is responsible for the presence or absence of glucose in the cell. The second is responsible for the presence or absence of lactose in the cell. Your task is to give a message about whether the operon will be turned on or off. The message should be consistent with the picture.



    def solve_problem14():
        a,b = input(), input()
        res = None
        if a == '+ GLUCOSE' and b == '+ LACTOSE':
            res = 'OPERON OFF because CAP not bound'

        elif a == '+ GLUCOSE' and b == '- LACTOSE':
            res = 'OPERON OFF both because lac repressor bound and because CAP not bound'

        elif a == '- GLUCOSE' and b == '- LACTOSE':
            res = 'OPERON OFF because lac repressor bound'

        elif a == '- GLUCOSE' and b == '+ LACTOSE':
            res = 'OPERON ON'

        if res:
            print(res)

        
    solve_problem14()  
    return


if __name__ == "__main__":
    app.run()
