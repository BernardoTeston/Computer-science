#exercise 1 

#`try`/`except` and `if` statements both manage program flow, but they serve different purposes. `try`/`except` is designed for handling unexpected errors, like file issues, while `if` statements check predictable conditions, like input ranges. `try` can catch multiple exceptions and allows for error propagation, but it can slow down performance if used frequently. In contrast, `if` statements are usually faster but require explicit checks for different cases. Use `try` for managing errors and `if` for routine conditions.

#exercise 2 

grades = float(input("Hi, what is your score? "))

def get_grade(grades):
    if 90 <= grades <= 100:
        return "A"
    elif 80 <= grades < 90:
        return "B"
    elif 70 <= grades < 80:
        return "C"
    elif 60 <= grades < 70:
        return "D"
    elif 0 <= grades < 60:
        return "F"
    else:
        return "Invalid score"

# Call the function to get the grade
grade = get_grade(grades)

#output
print(f"Your grade for a score of {grades} is: {grade}")



#exercise 3

def calculate_cost(start_hour, start_minute, end_hour, end_minute):
    # Convert start and end times to total minutes
    start_time = start_hour * 60 + start_minute
    end_time = end_hour * 60 + end_minute

    total_cost = 0.0

    day_rate = 2.50
    night_rate = 1.75
    night_cutoff = 21 * 60 

    # Determine the cost
    if end_time <= night_cutoff:
        total_cost = ((end_time - start_time) / 60) * day_rate
    elif start_time < night_cutoff:
        # Split time
        daytime_minutes = night_cutoff - start_time
        nighttime_minutes = end_time - night_cutoff
        total_cost = (daytime_minutes / 60) * day_rate + (nighttime_minutes / 60) * night_rate
    else:
        #night rate
        total_cost = ((end_time - start_time) / 60) * night_rate

    return total_cost

# nput
start_hour = int(input("Enter the starting hour (0-23): "))
start_minute = int(input("Enter the starting minute (0-59): "))
end_hour = int(input("Enter the ending hour (0-23): "))
end_minute = int(input("Enter the ending minute (0-59): "))

# Calculate cost
cost = calculate_cost(start_hour, start_minute, end_hour, end_minute)

print(f"The total babysitting cost is: ${cost:.2f}")


#exercise 4


def elegible_citizen(age, citizenship):
    senator_elegible = age >=30 and citizenship >= 9
    representative_elegible = age >=25 and citizenship >= 7
    return senator_elegible, representative_elegible

#find age and citizenship
age = int(input("Enter your age:"))
citizenship = int(input("Enter how many years of citizenship you have:"))

senator_elegible_1, representative_elegible_1 = elegible_citizen(age,citizenship)

if senator_elegible_1:
    print("You are elegible to be the senator!")
else:
    print("You are not elegible to be the senator.")
if representative_elegible_1:
    print("You are elegible to be the representative!")
else:
    print("You are not elegible to be the representative.")

#exercise 5(exercise 5 of the week 5)

def get_some_strings(num_strings):
    strings = []
    for _ in range(num_strings):
        try:
            strings.append(input("Enter a string: "))
        except KeyboardInterrupt:
            print("\nInput process interrupted.")
            break
    return strings

def main():
    try:
        count = int(input("How many strings will you enter? "))
        strings = get_some_strings(count)
        print("You entered:", strings)
    except ValueError:
        print("Invalid input! Please enter an integer.")
    except KeyboardInterrupt:
        print("\nInput process interrupted.")

if __name__ == "__main__":
    main()

