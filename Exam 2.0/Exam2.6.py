# Define the main function
def main():

    # Define numbers1 and numbers2
    numbers1 = ['This','is','a','list','of','undefined','length']
    numbers2 = []

    # Cylcle through numbers1 
    for value in numbers1:

        # Append value to numbers2
        numbers2.append(value)

    # Quick Test
    numbers2.append('test')

    # Print the reslts
    print(numbers1)
    print(numbers2)

# Run the main function
main()
