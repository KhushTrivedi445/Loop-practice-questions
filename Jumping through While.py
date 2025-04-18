'''Given a positive integer x, the task is to print the numbers from 1 to x 
in the order as 12, 22, 32, 42, 52, ... (in increasing order).'''


a=int(input("Enter the number: "))
def jump(a):
    for i in range (1,a):
        b=(pow(i,2))
        if(b<a):
            print(b)
jump(a)            