# import the credit_outcome module as co
import credit_outcome as co


def main():
    # create a dictionary to store the outcomes and their counts
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Do not progress - module retriever": 0, "Exclude": 0}

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

        # ask the user if they want to continue or quit
        choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
        # if they enter n (case-insensitive), set the loop variable to False
        if choice.lower() == "n":
            continue_loop = False

    # print the histogram of the outcomes using the co module
    co.print_histogram(outcomes)


# call the main function
main()
