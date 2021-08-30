def dot():

    n = int(input("Enter number of elements : "))
    print("----------------------------------------------------------\n\n")
    print("put spaces between each index")
    print("----------------------------------------------------------\n\n")
    u = list(map(int,input("\nEnter the numbers for vector u: ").strip().split()))[:n]
    print("----------------------------------------------------------\n\n")
    v = list(map(int,input("\nEnter the numbers for vector v: ").strip().split()))[:n]
    product=0.0

    for x in range(n):
        product+=(u[x]*v[x])

    print("Dot product of the vectors {} and {} is {}".format(u,v,product))

def cross():
    print("put spaces between each index")
    print("----------------------------------------------------------\n\n")
    u = list(map(int,input("\nEnter the numbers for vector u: ").strip().split()))[:3]
    print("----------------------------------------------------------\n\n")
    v = list(map(int,input("\nEnter the numbers for vector v: ").strip().split()))[:3]

    cross=[]
    cross.append((u[1]*v[2])-(u[2]*v[1]))
    cross.append(0-((u[0]*v[2])-(u[2]*v[0])))
    cross.append((u[0]*v[1])-(u[1]*v[0]))

    print("Cross product of the vectors {} and {} is {}".format(u,v,cross))

ans=input("1)Dot product \n2)Cross product\nPick a number: ")
print("----------------------------------------------------------\n\n")
if(ans==1):
    dot()
else:
    cross()
