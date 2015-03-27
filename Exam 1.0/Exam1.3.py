#Brendan L. Stringer
#Exam 1.3.py

base = int(input("enter the base: "))

exp = int(input("enter the exponent: "))

result = 1

# use a loop to calculate base raised to the power of exp. 

# you may NOT use any built in functionality (** operator,

# pow function) for calculating the power



for i in range(1,exp+1): 

	result *= base



print(base,"raised to",exp, "is", result)