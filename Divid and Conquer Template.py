#DIVID AND CONQUER TEMPLATE

def function_name(n):

    #If input is a list, recursion will depend on size
    L = len(n)

    if #Base case for list input (L < 0, 1, 2, etc):

        return #solution for smallest case

    #can have multple base case if statements

    else:

        #Divid problem, this is if a list
        m = L//#b, divid problem by what


        #Handle sub problems
        x = function_name(#if list function_name(n[0:m])
        y = function_name(#if list function_name(n[m:L])


        return x + y #combine subproblems
