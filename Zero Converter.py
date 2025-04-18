'''You are given a number n. The number n can be negative or positive. 
If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. 
If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.

Note:- You don't have to return anything, you just have to print the array.'''


a=int(input("Enter the number: "))
print(a)
def decrease(a):
    if(a>0):
        while(a>0):
            a=a-1
            print(a)
    elif(a==0):
        print("Already Zero")
    else:
        while(a<0):
            a=a+1
            print(a)
        
decrease(a)
