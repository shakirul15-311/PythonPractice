def printf(str, *args): #for coding as like c/c++ we use this
    print(str % args, end='')

def calculate(a,b,c):
    if(c==1):
        printf("______________________\n")
        printf("\n %d + %d = %d\n",a,b,a+b)
        printf("______________________\n")
    elif(c==2):
        printf("______________________\n")
        printf("\n %d-%d = %d\n",a,b,a-b)
        printf("______________________\n")
    elif(c==3):
        printf("______________________\n")
        printf("\n %d*%d = %d\n",a,b,a*b)
        printf("______________________\n")
    else:
        if(b==0):
            printf("______________________\n")
            printf("\n Math Error\n")
            printf("______________________\n")
        else:
            printf("______________________\n")
            printf("\n %d/%d = %d\n",a,b,a/b)
            printf("______________________\n")
while(1):
    printf("Input 2 number :\n")
    printf("_________________\n")
    a=int(input())
    b=int(input())
    
    printf("Choose:\n 1 for Addition\n 2 for Substruction\n 3 for Multiplication\n 4 for ADivision \n")
    
    
    c=int(input())
    calculate(a,b,c)
    
    printf("\n\n\n")
