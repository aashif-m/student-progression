# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1998768 20221368 
 
# Date: 2023/04/11 


import credit_outcome_functions as co


def clear_file(file_name):
    """
    Clear contents of the file.

    :param file_name: name of file
    :type file_name: str
    :return: None
    """

    with open(file_name, "w") as file:
        file.write("")


def save_progression_data_file(pass_credits, defer_credits, fail_credits, file_name):
    """
    Save the credits and outcome of a student in the file.

    :param pass_credits: The number of credits passed by the student.
    :type pass_credits: int
    :param defer_credits: The number of credits deferred by the student.
    :type defer_credits: int
    :param fail_credits: The number of credits failed by the student.
    :type fail_credits: int
    :param file_name: name of file
    :type file_name: str
    :return: None
    """

    with open(file_name, "a") as file:
        # Use co module to determine outcome based on pass and defer credits
        outcome = co.get_outcome(pass_credits, defer_credits)
        file.write(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}\n")


def print_progression_data_file(file_name):
    """Print the progression data from the file.

    :param file_name: name of file
    :return: None
    """

    print("Part 3:")
    with open(file_name, "r") as file:
        print(file.read())


def main():
    # Define the file name
    file_name = "progression_data.txt"

    # Create a dictionary to store the outcomes and their counts
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Module retriever": 0, "Exclude": 0}

    # Clear the progression data file using the defined function
    clear_file(file_name)

    # Create a boolean variable to control the loop
    continue_loop = True

    # Start the loop
    while continue_loop:
        # Get the input for pass,defer and fail credits from the user and validate it
        pass_credits = co.get_credits_input("pass")
        defer_credits = co.get_credits_input("defer")
        fail_credits = co.get_credits_input("fail")
        
        # Keeps count of total credits entered
        total_credits = sum([pass_credits, defer_credits, fail_credits])

        # Check if the total credits is equal to 120
        if total_credits != 120:
            print("Total incorrect.")
        # Continue with the program if no errors
        else:
            # If yes, get the outcome based on the pass and defer credits using the co module
            outcome = co.get_outcome(pass_credits, defer_credits)
            # Print the outcome
            print(outcome)
            # Increment the count of the outcome in the dictionary by one
            outcomes[outcome] += 1

            # Save the progression data in the file using the defined function
            save_progression_data_file(pass_credits, defer_credits, fail_credits, file_name)

        # Prompts the users if they want to continue or quit and view results
        choice = input("Do you want to continue? (enter any key to continue or enter q to quit and view results: ")
        if choice.lower() == "q":
            continue_loop = False

    # Print the histogram of the outcomes using the co module
    co.print_histogram(outcomes)

    # Print the progression data from the file using the defined function
    print_progression_data_file(file_name)


# Call the main function
main()
