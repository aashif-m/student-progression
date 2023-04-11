#Function prompts the user to enter the credits for a given credit type and returns the credits entered by the user 
def input_credits(credit_type):
    # Initialize a variable to control the loop
    valid = True

    # Use the variable as the loop condition
    while valid:
        try:
            #Prompts user to input the number of credits
            credits = int(input(f"Please enter your {credit_type} credits: "))

            #Checks if the credits inputted are in the range 0, 20, 40, 60, 80, 100 and 120
            if credits not in range (0,121, 20):
                print("Out of range")
            else:
                return credits

        #If the entered value is not an integer, print an error message to prompt the user to enter an integer value.
        except ValueError:
            print("Integer Required")

# Intialise progression outcome counts
progress_count, trailer_count, retriever_count, exclude_count = [0]*4

students = {}

# Initialize a variable to control the loop
continue_loop = True

while continue_loop:

    # Input student ID and credits and lowercases the w in the beginning if it's uppercase
    student_id = input("Please enter the student ID (w1234567) : ").lower()


    # Check if the input is in the correct format like w1234567
    if not student_id.startswith("w") or not student_id[1:].isdigit() or len(student_id) != 8:
        print(f"The student ID {student_id} is not in the correct format (w1234567). Please try again.")
        continue

    # Check if the student ID already exists in the dictionary
    if student_id in students:
         # Prompts the user if they want to overwrite the existing outcome
        overwrite = input(f"The student ID {student_id} already has an outcome. Do you want to overwrite it? (enter y to overwrite or any other key to skip): ")

        # If input is not 'y' then continue to next iteration of the loop
        if overwrite.lower() != "y":
            continue

    # Get credits for pass, defer and fail
    pass_credits = input_credits("pass")
    defer_credits = input_credits("defer")
    fail_credits = input_credits("fail")

    # Keeps count of total credits entered
    total_credits = sum([pass_credits, defer_credits, fail_credits])

    #Checks if total credits is equal to 120, else print that the total is incorrect
    if total_credits != 120:
        print("Total incorrect")

    # Continue with the program if no errors
    else:
        # Counts and records the progression outcomes and credits in a dictionary
        if pass_credits == 120:
            students[student_id] = f"Progress - {pass_credits}, {defer_credits}, {fail_credits}"
            progress_count += 1
        elif pass_credits == 100:
            students[student_id] = f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}"
            trailer_count += 1
        elif pass_credits >= 40 and defer_credits >= 20 or pass_credits >= 60 or defer_credits >= 60:
            students[student_id] = f"Module retriever - {pass_credits}, {defer_credits}, {fail_credits}"
            retriever_count += 1
        else:
            students[student_id] = f"Exclude – {pass_credits}, {defer_credits}, {fail_credits}"
            exclude_count += 1

    # Prompts the users if they want to continue or quit and view results
    choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
    if choice.lower() == "n":
        continue_loop = False

print("Part 4:")

#Loops through each key-value pair
for student_id, outcome in students.items():
    # Print the student ID and outcome
    print(f"{student_id}: {outcome}")