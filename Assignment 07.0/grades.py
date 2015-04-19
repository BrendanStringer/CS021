# Brendan L. Stringer 
# CS 021 
# Grades.py 

# This will read the grades out of an output file and then make a corrosponding letter grade file while printing a histogram of ****

def main(): 

        # Prepare for graceful error exiting
        try:

                # Start Varibles
                Acount = 0 
                Bcount = 0
                Ccount = 0
                Dcount = 0
                Fcount = 0

                # Open the grades.dat file
                numGradeFile = open('grades.dat', 'r')

                # Open the letter grades file
                letGradeFile = open('letterGrades.dat', 'w')

                # Index through the numGrade File 
                for numGrade in numGradeFile: 

                        if float(numGrade) >= 90: 
                                letGrade = 'A'
                                Acount += 1
                        elif float(numGrade) >= 80: 
                                letGrade = 'B'
                                Bcount += 1
                        elif float(numGrade) >= 70:
                                letGrade = 'C'
                                Ccount += 1
                        elif float(numGrade) >= 60: 
                                letGrade = 'D'
                                Dcount += 1
                        elif float(numGrade) < 60:
                                letGrade = 'F'
                                Fcount += 1

                        letGradeFile.write(letGrade + '\n')

                # Print the histogram
                letGradeFile.write('\n\n')
                letGradeFile.write('A: ')
                for star in range(0,Acount):
                        letGradeFile.write('*')
                letGradeFile.write('\n')

                letGradeFile.write('B: ')
                for star in range(0,Bcount):
                        letGradeFile.write('*')
                letGradeFile.write('\n')

                letGradeFile.write('C: ')
                for star in range(0,Ccount):
                        letGradeFile.write('*')
                letGradeFile.write('\n')

                letGradeFile.write('D: ')
                for star in range(0,Dcount):
                        letGradeFile.write('*')
                letGradeFile.write('\n')

                letGradeFile.write('F: ')
                for star in range(0,Fcount): 
                        letGradeFile.write('*')
                letGradeFile.write('\n')


                #Close files 
                numGradeFile.close()
                letGradeFile.close()

        # Except the errors
        except FileNotFoundError as err:
                print('\n')
                print('The sepcified grades.dat file is not in the specified directory.')
                print('Please check the working directory.')
                print('The error is printed below.')
                print(err)
                print('\n')

        except IOError as err:
                print('\n')
                print('The sepcified grades.dat file is not in the specified directory.')
                print('Please check the working directory.')
                print('The error is printed below.')
                print(err)
                print('\n')

        except ValueError as err:
                print('\n')
                print('There is an invalid value in grades.dat.')
                print('Please check the data.dat file.')
                print(err)
                print('\n')

        except Exception as err: 
                print('\n')
                print('There was an unknown error.')
                print('The error message is printed below.')
                print(err)
                print('\n')

# Run the main function
main()
