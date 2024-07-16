# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")


print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.
vowels = ["a", "e", "i", "o", "u"]


def check_letter():
    # logic here
    user_letter = input("Add a letter: ").lower()
    for letter in vowels:
        if letter == user_letter:
            return print(f" the letter {user_letter} is a vowel")
        else:
            return print(f" the letter {user_letter} is a consonant")


check_letter()
# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.


def check_voting_eligibility():
    # Your control flow logic goes here
    valid = False
    while not valid:
        user_age = input("What is your age?: ")
        try:
            user_age = int(user_age)
            if user_age < 1:
                print("Please enter an age higher than 0")
            elif user_age > 0 and user_age < 19:
                print(f"You cannot vote, you are only {user_age} years old")
                valid = True
            else:
                print(
                    f"Congratiulations, you can vote since you are {user_age} years old!"
                )
                valid = True
        except:
            print("please enter a number")


# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.


def calculate_dog_years(age):
    dog_years = 0
    # Your control flow logic goes here
    human_years = list(range(age))
    for year in human_years:
        if year == 0 or year == 1:
            dog_years += 10
        else:
            dog_years += 7
    return print(f" your dog is {dog_years} old in doggo time")


# Call the function
calculate_dog_years(6)


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.


def weather_advice():
    # Your control flow logic goes here
    cold = False
    raining = False

    isColdUserResponse = input("Is it cold outside?: ").lower()
    isRainingUserResponse = input("Is it raining outside?: ").lower()

    if isColdUserResponse == "yes":
        cold = True
    if isRainingUserResponse == "yes":
        raining = True

    if cold and raining:
        return print(f"Wear a waterproof coat.")
    elif cold and not raining:
        return print(f"Wear a warm jacket")
    elif not cold and raining:
        return print(f"Carry an umbrella")
    else:
        return print(f"Wear light clothing")


# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.


# helper function to get the season
def get_season(month, day):
    season_month = ""
    # declare what the season month is
    if month == 11 or month <= 2:
        season_month = "winter"
    elif month >= 2 and month <= 5:
        season_month = "spring"
    elif month >= 5 and month <= 8:
        season_month = "summer"
    else:
        season_month = "fall"

        # winter starting point
    if season_month == "winter":
        if month == 11 and day > 20:
            # stay
            return "winter"
        # next snz
        elif month == 2 and day > 19:
            return "spring"
        else:
            # stay
            return "winter"
        # spring starting point
    if season_month == "spring":
        if month == 2 and day > 19:
            # stay
            return "spring"
        elif month == 5 and day > 20:
            # next szn
            return "summer"
        else:
            # stay
            return "spring"
        # summer starting point
    if season_month == "summer":
        if month == 5 and day > 20:
            # stay
            return "summer"
        elif month == 8 and day > 21:
            # next szn
            return "fall"
        else:
            # stay
            return "summer"
        # fall starting point
    if season_month == "fall":
        if month == 8 and day > 21:
            # stay
            return "fall"
        elif month == 11 and day > 20:
            # next szn
            return "winter"
        else:
            # stay
            return "fall"


# main function to determine full date and season
def determine_season():
    months_of_the_year = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    ]
    valid_month_entered = ""
    valid_day_entered = None

    #    func to get month
    def get_month():
        month_entered = input("Enter the month of the year (Jan - Dec): ").lower()
        if month_entered not in months_of_the_year:
            print("Please select a valid month")
            return get_month()
        else:
            return month_entered

    valid_month_entered = get_month()

    # func to get day
    def get_day():
        day_entered = input("Enter the day of the month: ")
        try:
            day_entered = int(day_entered)
        except:
            print("Please enter a number for the day")
            return get_day()
        if day_entered < 1 or day_entered > 31:
            print("Please select a valid day (between 1 and 31)")
            return get_day()
        return day_entered

    valid_day_entered = get_day()

    # get season function

    season = get_season(
        months_of_the_year.index(valid_month_entered), valid_day_entered
    )
    print(f"{valid_month_entered}, {valid_day_entered} is in {season}")


# Call the function
determine_season()
