# Function prompts the user to enter the credits for a given credit type and returns the credits entered by the user 
def input_credits(credit_type):
    # Initialize a variable to control the loop
    valid = True

    # Use the variable as the loop condition
    while valid:
        try:
            # Prompts user to input the number of credits
            credits = int(input(f"Please enter your {credit_type} credits: "))

            # Checks if the credits inputted are in the range 0, 20, 40, 60, 80, 100 and 120
            if credits not in range (0,121, 20):
                print("Out of range")
            else:
                return credits
        
        # If the entered value is not an integer, print an error message to prompt the user to enter an integer value.
        except ValueError:
            print("Integer Required")

# Intialise progression outcome counts
progress_count, trailer_count, retriever_count, exclude_count = [0]*4

# Initialize a variable to control the loop
continue_loop = True

while continue_loop:
    #Get credits for pass, defer and fail
    pass_credits = input_credits("pass")
    defer_credits = input_credits("defer")
    fail_credits = input_credits("fail")

    #Keeps count of total credits entered
    total_credits = sum([pass_credits, defer_credits, fail_credits])

    #Checks if total credits is equal to 120, else print that the total is incorrect
    if total_credits != 120:
        print("Total incorrect")

    #Continue with the program if no errors
    else:
        #Checks the relavent progression outcome based on credits entered and keeps count of number of different outcomes
        if pass_credits == 120:
            print("Progress")
            progress_count += 1
        elif pass_credits == 100:
            print("Progress (module trailer)")
            trailer_count += 1
        elif pass_credits + defer_credits >= 60:
            print("Do not progress - module retriever")
            retriever_count += 1
        else:
            print("Exclude")
            exclude_count += 1

    #Prompts the users if they want to continue or quit and view results
    choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
    if choice.lower() == "n":
        continue_loop = False

#Prints a histogram of the progression outcomes
print("---------------------------------------------------------------")
print("Histogram")
print(f"Progress {progress_count} : {'*' * progress_count}")
print(f"Trailer {trailer_count} : {'*' * trailer_count}")
print(f"Retriever {retriever_count} : {'*' * retriever_count}")
print(f"Excluded {exclude_count} : {'*' * exclude_count}")
print(f"{progress_count + trailer_count + retriever_count + exclude_count} outcomes in total.")
print("----------------------------------------------------------------")