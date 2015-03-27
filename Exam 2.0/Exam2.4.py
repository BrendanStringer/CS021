# Define the main function
def main():

    # Open the output file
    outputFile = open('number_list.txt','w')

    # Use a for loop to write data to the file
    for writeNum in list(range(1,101)):

        # Write data to the file
        outputFile.write(str(writeNum) + '\n')

    # Close the outputFile
    outputFile.close()

# Run the main function
main()
