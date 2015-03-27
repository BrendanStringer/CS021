import math

def main():
    num1 = int(input("enter first value: "))
    num2 = int(input("enter second value: "))
    
    #calculate and display the result of calculation (see equation)
    result = math.sqrt(square_it(num1) * square_it(num2))

    # Print the results
    print('The result is :', format(result, '0.2f'))
       
           
#function square_it takes a number and returns
#the number squared (x*x)
def square_it(x):
    return x*x

main()
