# CS175
# Brian Mohabeer
# rainfall.py

# Declare variables to hold the total rainfall,
# monthly rainfall, average rainfall (all float), the number
# of years, and the total number of months.

# Get (input) number of years (validate input must be 1 to 3)
number_of_years = int(input("Enter the number of years (1, 2, or 3): "))

while number_of_years > 3 or number_of_years < 1:
    print ("Invalid number of years please enter again")
    number_of_years = int(input("Enter the number of years (1, 2, or 3: "))
print(number_of_years)               


# Get (input) rainfall by month (nested for loops: year then month)
total_rainfall = 0
month = 12
for x in range(1,number_of_years+1):
    print("For year",x)
    for y in range(month):
        monthly_rainfall = float(input("Enter the rainfall amount for the month: "))
        total_rainfall = total_rainfall + monthly_rainfall
average_rainfall = total_rainfall/number_of_years/12  

# Calculate and print the total rainfall and the average rainfall
print("For",x ,"months")
print ("Total Rainfall: ", total_rainfall, "inches")     
print("Average Monthly Rainfall: ", average_rainfall,"inches")
