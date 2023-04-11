import credit_outcome as co


def main():
    # Create a dictionary to store the outcomes and their counts
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Do not progress - module retriever": 0, "Exclude": 0}

    # Create a boolean variable to control the loop
    continue_loop = True

    # Start the loop
    while continue_loop:
        # Get the input for pass, defer and fail credits from the user and validate it
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

        # Ask the user if they want to continue or quit
        choice = input("Do you want to continue? (enter any key to continue or enter q to quit and view results: ")
        # If they enter n (case-insensitive), set the loop variable to False
        if choice.lower() == "q":
            continue_loop = False

    # Print the histogram of the outcomes using the co module
    co.print_histogram(outcomes)


# Call the main function
main()
