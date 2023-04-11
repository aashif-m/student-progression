import credit_outcome as co


def save_progression_data_list(pass_credits, defer_credits, fail_credits, progression_list):
    """
    Save the credits and outcome of a student in a list.

    :param pass_credits: The number of credits passed by the student.
    :param defer_credits: The number of credits deferred by the student.
    :param fail_credits: The number of credits failed by the student.
    :param progression_list: The list to store the credits and outcome of the student.
    :return: None
    """
    credits = [pass_credits, defer_credits, fail_credits]
    progression_list.append(credits)


def print_progression_data_list(progression_list):
    """
    Print the progression list with outcomes.

    :param progression_list: The list of credits and outcomes for each student.
    :return: None
    """
    print("Part 2:")
    for credits in progression_list:
        pass_credits, defer_credits, fail_credits = credits
        # Use co module to determine outcome based on pass and defer credits
        outcome = co.get_outcome(pass_credits, defer_credits)


# define the main function
def main():
    # create a dictionary to store the outcomes and their counts
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Do not progress - module retriever": 0, "Exclude": 0}
    # create an empty list to store the progression data
    progression_list = []

    # create a boolean variable to control the loop
    continue_loop = True

    # start the loop
    while continue_loop:
        # get the input for pass,defer and fail credits from the user and validate it
        pass_credits = co.get_credits_input("pass")
        defer_credits = co.get_credits_input("defer")
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

            # save the progression data in the list using the defined function
            save_progression_data_list(pass_credits, defer_credits, fail_credits, progression_list)

        # ask the user if they want to continue or quit
        choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
        # if they enter n (case-insensitive), set the loop variable to False
        if choice.lower() == "n":
            continue_loop = False

    # print the histogram of the outcomes using the co module
    co.print_histogram(outcomes)

    # print the progression data list using the defined function
    print_progression_data_list(progression_list)


# call the main function
main()
