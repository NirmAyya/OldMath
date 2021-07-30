

def iterations():
    print("\n**************************************************************************************\n")
    print("This program takes a number and if the number is even it divides it by 2, and \nif it is odd it multiplies by 3 and adds 1, see if you notice something wierd!")
    print("\n**************************************************************************************\n")
    x=int(input("What number do you want to apply the pattern to: "))
    max=x
    print(x)
    iterations=0
    print("+-----------------------------------------------------+")
    while x!=1:
        iterations=iterations+1
        if(max<x):
            max=x

        if(x%2!=0):
            x=(x*3)+1
        else:
            x=x/2
        print("|Iteration: {} | {}                              ".format(iterations,x))
        print("|------------------------------------------------------|")

    print("It took {} iterations to reach 1, the maximum value it reached was {}".format(iterations,max))

iterations()


