'''Given a number x, the task is to print the numbers from x to 0 
in decreasing order in a single line.'''


a=int(input("Enter the number: "))
print(a)
def decrease(a):
    while(a>0):
        a=a-1
        print(a)
decrease(a)
    