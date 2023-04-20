# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1998768 20221368 
 
# Date: 2023/04/11 

import credit_outcome_functions as co


def save_progression_data_list(pass_credits, defer_credits, fail_credits, progression_list):
    """
    Save the credits and outcome of a student in a list.

    Args:
        pass_credits (int): The number of credits passed by the student.
        defer_credits (int): The number of credits deferred by the student.
        fail_credits (int): The number of credits failed by the student.
        progression_list (list): The list to store the credits and outcome of the student.
    
    Returns:
        None
    """
    credits = [pass_credits, defer_credits, fail_credits]
    progression_list.append(credits)


def print_progression_data_list(progression_list):
    """
    Print the progression list with outcomes.

    Args:
        progression_list (list): The list of credits and outcomes for each student.

    Returns:
        None
    """
    print("Part 2:")
    for credits in progression_list:
        pass_credits, defer_credits, fail_credits = credits
        # Use co module to determine outcome based on pass and defer credits
        outcome = co.get_outcome(pass_credits, defer_credits)
        print(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}")


# Define the main function
def main():
    # Create a dictionary to store the outcomes and their counts
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Do not progress - module retriever": 0, "Exclude": 0}
    # Create an empty list to store the progression data
    progression_list = []

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

            # save the progression data in the list using the defined function
            save_progression_data_list(pass_credits, defer_credits, fail_credits, progression_list)

        # Prompts the users if they want to continue or quit and view results
        choice = input("Do you want to continue? (enter any key to continue or enter q to quit and view results: ")
        if choice.lower() == "q":
            continue_loop = False

    # Print the histogram of the outcomes using the co module
    co.print_histogram(outcomes)

    # Print the progression data list using the defined function
    print_progression_data_list(progression_list)


# Call the main function
main()
