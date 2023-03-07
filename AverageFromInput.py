#CS 175L
#Brian Mohabeer
#AverageFromInput

def main():
    # Open the numbers.txt file for reading.
    numbers_file = open('numbers.txt', 'r')
    # Assign variables for loop
    total = 0
    x = 0
    # Read all the lines from the file.
    for line in numbers_file:
        # Assign variables
        number = float(line)
        total = total + number
        x = x + 1
        # Format and display the amount.
        print(f'I read in {x} numbers(s) Current number is: {number:.2f}    Total is: {total:.2f}')

    # Calculate average
    average = total/x
    print(f'Average: {average:.2f}')

        
    # Close the file.
    numbers_file.close()

# Call the main function.
if __name__ == '__main__':
    main()

