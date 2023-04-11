import credit_outcome as co


def clear_progression_data_file():
    """
    Clear the progression data file.

    This function deletes all the content of the progression_data.txt file.
    It is used to reset the file before saving new data.
    :return: None
    """
    with open("progression_data.txt", "w") as file:
        file.write("")


def save_progression_data_file(pass_credits, defer_credits, fail_credits):
    """
    Save the credits and outcome of a student in the file.

    This function appends a new line to the progression_data.txt file with
    the credits and outcome of a student.
    :param pass_credits: The number of credits passed by the student.
    :param defer_credits: The number of credits deferred by the student.
    :param fail_credits: The number of credits failed by the student.
    :return: None
    """
    with open("progression_data.txt", "a") as file:
        # Use co module to determine outcome based on pass and defer credits
        outcome = co.get_outcome(pass_credits, defer_credits)
        file.write(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}\n")


def print_progression_data_file():
    """
    Print the progression data from the file.

    This function reads and prints the content of the progression_data.txt file.
    It assumes that each line of the file has the format:
    outcome - pass_credits, defer_credits, fail_credits
    :return: None
    """
    print("Part 2:")
    with open("progression_data.txt", "r") as file:
        print(file.read())


# define the main function
def main():
    # create a dictionary to store the outcomes and their counts
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Do not progress - module retriever": 0, "Exclude": 0}

    # clear the progression data file using the defined function
    clear_progression_data_file()

    # create a boolean variable to control the loop
    continue_loop = True

    # start the loop
    while continue_loop:
        # get the input for pass credits from the user and validate it
        pass_credits = co.get_credits_input("pass")
        # get the input for defer credits from the user and validate it
        defer_credits = co.get_credits_input("defer")
        # get the input for fail credits from the user and validate it
        fail_credits = co.get_credits_input("fail")
        # calculate the total credits by adding the three inputs
        total_credits = sum([pass_credits, defer_credits, fail_credits])

        # check if the total credits is equal to 120
        if total_credits != 120:
            # if not, print an error message
            print("Total incorrect.")

        else:
            # if yes, get the outcome based on the pass and defer credits using the co module
            outcome = co.get_outcome(pass_credits, defer_credits)
            # print the outcome
            print(outcome)
            # increment the count of the outcome in the dictionary by one
            outcomes[outcome] += 1

            # save the progression data in the file using the defined function
            save_progression_data_file(pass_credits, defer_credits, fail_credits)

        # ask the user if they want to continue or quit
        choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
        # if they enter n (case-insensitive), set the loop variable to False
        if choice.lower() == "n":
            continue_loop = False

    # print the histogram of the outcomes using the co module
    co.print_histogram(outcomes)

    # print the progression data from the file using the defined function
    print_progression_data_file()


# call the main function
main()
