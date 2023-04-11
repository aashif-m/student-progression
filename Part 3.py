import credit_outcome as co


def clear_progression_data_file():
    """Clear the progression data file.

    This function deletes all the content of the progression_data.txt file.
    It is used to reset the file before saving new data.

    Returns:
        None
    """
    with open("progression_data.txt", "w") as file:
        file.write("")


def save_progression_data_file(pass_credits, defer_credits, fail_credits):
    """Save the credits and outcome of a student in the file.

    This function appends a new line to the progression_data.txt file with
    the credits and outcome of a student.

    Args:
        pass_credits (int): The number of credits passed by the student.
        defer_credits (int): The number of credits deferred by the student.
        fail_credits (int): The number of credits failed by the student.

    Returns:
        None
    """
    with open("progression_data.txt", "a") as file:
        # Use co module to determine outcome based on pass and defer credits
        outcome = co.get_outcome(pass_credits, defer_credits)
        file.write(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}\n")


def print_progression_data_file():
    """Print the progression data from the file.

    This function reads and prints the content of the progression_data.txt file.

    Returns:
        None
    """

    print("Part 2:")
    with open("progression_data.txt", "r") as file:
        print(file.read())


# Define the main function
def main():
    # Create a dictionary to store the outcomes and their counts
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Do not progress - module retriever": 0, "Exclude": 0}

    # Clear the progression data file using the defined function
    clear_progression_data_file()

    # Create a boolean variable to control the loop
    continue_loop = True

    # Start the loop
    while continue_loop:
        # Get the input for pass,defer and fail credits from the user and validate it
        pass_credits = co.get_credits_input("pass")
        defer_credits = co.get_credits_input("defer")
        fail_credits = co.get_credits_input("fail")
        
        # Calculate the total credits by adding the three inputs
        total_credits = sum([pass_credits, defer_credits, fail_credits])

        # Check if the total credits is equal to 120
        if total_credits != 120:
            print("Total incorrect.")

        else:
            # If yes, get the outcome based on the pass and defer credits using the co module
            outcome = co.get_outcome(pass_credits, defer_credits)
            # Print the outcome
            print(outcome)
            # Increment the count of the outcome in the dictionary by one
            outcomes[outcome] += 1

            # Save the progression data in the file using the defined function
            save_progression_data_file(pass_credits, defer_credits, fail_credits)

        # Ask the user if they want to continue or quit
        choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
        # If they enter n (case-insensitive), set the loop variable to False
        if choice.lower() == "n":
            continue_loop = False

    # Print the histogram of the outcomes using the co module
    co.print_histogram(outcomes)

    # Print the progression data from the file using the defined function
    print_progression_data_file()


# Call the main function
main()
