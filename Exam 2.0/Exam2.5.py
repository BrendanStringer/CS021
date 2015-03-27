
# Start the main function
def main():

    # Start exception handling
    try: 
    
        # Open the file that contains the data
        infile = open('myfile.txt','r')

        # Start the total variable
        total = 0

        # Prime the line variable 
        line = infile.readline()

        # Index through the file
        while line != '':

            # Convert the line to an integer
            num = int(line.rstrip('\n'))

            # Sum the contents
            total = total + num

            # Read the next value of the infile
            line = infile.readline()

        # Close the infile
        infile.close()

        # print the total
        print(total)

    # Except IOError
    except IOError as err:
        print('Error Opening File')
        print(err)

    # Except ValueError
    except ValueError as err:
        print('Invalid Data')
        print(err)

# Run the main function
main()
