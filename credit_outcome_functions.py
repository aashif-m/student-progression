# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1998768 20221368
 
# Date: 2023/04/11 


def get_credits_input(credit_type):
    """
    Gets and validates user’s credits.

    :param credit_type: The type of credit, pass or defer or fail.
    :type credit_type: str
    :return: The number of credits entered by the user.
    :rtype: int
    """

    while True:
        try:
            # Prompts user to input the number of credits
            credits = int(input(f"Please enter your {credit_type} credits: "))

            # Checks if the credits inputted are in the range 0, 20, 40, 60, 80, 100 and 120
            if credits not in range(0, 121, 20):
                print("Out of range")
            else:
                return credits

        # If the entered value is not an integer, print an error message to prompt the user to enter an integer value.
        except ValueError:
            print("Integer Required")


def get_outcome(pass_credits, defer_credits):
    """
    Determines the outcome of a student based on their pass and defer credits.

    :param pass_credits: The number of credits that the student passed.
    :type pass_credits: int
    :param defer_credits: The number of credits that the student deferred.
    :type defer_credits: int
    :return: The outcome of the student, which can be one of the following:
        - "Progress" if the student passed all 120 credits.
        - "Progress (module trailer)" if the student passed 100 credits and deferred 20 credits.
        - "Module retriever" if the student passed and deferred at least 60 credits in total.
        - "Exclude" if the student passed and deferred less than 60 credits in total.
    :rtype: str
    """

    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Progress (module trailer)"
    elif pass_credits + defer_credits >= 60:
        return "Module retriever"
    else:
        return "Exclude"


def print_histogram(outcomes):
    """
    Prints a histogram of the outcomes of the students.

    :param outcomes: A dictionary that maps each outcome to the number of students who achieved it.
    :type outcomes: dict
    :return: None
    """
    
    # Define the labels for the outcomes
    outcomes_labels = ('Progress', 'Trailer', 'Retriever', 'Excluded')

    # Print horizontal line
    print("-" * 63)
    print("Histogram")

    # Loop through the outcomes and print the histogram
    for outcome, count in zip(outcomes_labels, outcomes.values()):
        # Format the outcome and value with spaces and colons
        outcome_value = f"{outcome} {count}"
        # Print the outcome and value followed by asterisks
        print(f"{outcome_value:12}: {'*' * count}")

    # Print the total number of outcomes
    print(f"{sum(outcomes.values())} outcomes in total.")
    
    # Print horizontal line
    print("-" * 63)