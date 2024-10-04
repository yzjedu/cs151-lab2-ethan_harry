# Programmers:  [Ethan, Harry]
# Course:  CS151, [Dr. Zee]
# Due Date: 9/25/2024
# Lab Assignment: 02
# Program Purpose: [This program calculates population loss or growth, over time.]

# Print a Welcome Message
print("This program will help you evaluate population growth or loss, over time.")

# Inputs
current_population = int(input("Enter the current population: "))
seconds_per_death = float(input("Enter the number of seconds between each death: "))
seconds_per_birth = float(input("Enter the number of seconds between each birth: "))
seconds_per_immigrant = float(input("Enter the number of seconds between each new immigrant: "))
num_years = int(input("Enter the number of years projected out: "))

# Total Seconds in a Year Calculation
seconds_per_year = 365 * 24 * 60 * 60  # 1 year in seconds

# Events Per Year Calculation
deaths_per_year = seconds_per_year / seconds_per_death
births_per_year = seconds_per_year / seconds_per_birth
immigrants_per_year = seconds_per_year / seconds_per_immigrant

# Population Change Calculation
future_population = current_population + ((births_per_year - deaths_per_year + immigrants_per_year) * num_years)

# Output the Future Population
print("The future population is", int(future_population))

# Check if the Population increased, decreased, or stayed the same
if future_population > current_population:
    print("There has been an increase in population.")
elif future_population < current_population:
    print("There has been a decrease in population.")
else:
    print("The population has remained the same.")
