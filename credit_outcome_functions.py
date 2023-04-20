# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1998768 20221368
 
# Date: 2023/04/11 


def get_credits_input(credit_type):
    """
    Asks the user to enter their credits for a given credit type, validates that it is within the valid range, and returns it as an integer.

    Args:
        credit_type (str): The type of credit, pass or defer or fail.

    Returns:
        int: The number of credits entered by the user.

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

    Args:
        pass_credits (int): The number of credits that the student passed.
        defer_credits (int): The number of credits that the student deferred.

    Returns:
        str: The outcome of the student, which can be one of the following:
            - "Progress" if the student passed all 120 credits.
            - "Progress (module trailer)" if the student passed 100 credits and deferred 20 credits.
            - "Do not progress - module retriever" if the student passed and deferred at least 60 credits in total.
            - "Exclude" if the student passed and deferred less than 60 credits in total.
    """
    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Progress (module trailer)"
    elif pass_credits + defer_credits >= 60:
        return "Do not progress - module retriever"
    else:
        return "Exclude"


def print_histogram(outcomes):
    """
    Prints a histogram of the outcomes of the students.

    Args:
        outcomes (dict): A dictionary that maps each outcome to the number of students who achieved it.

    Returns:
        None
    """
    print("---------------------------------------------------------------")
    print("Histogram")
    print(f"Progress {outcomes['Progress']}  : {'*' * outcomes['Progress']}")
    print(f"Trailer {outcomes['Progress (module trailer)']}   : {'*' * outcomes['Progress (module trailer)']}")
    print(f"Retriever {outcomes['Do not progress - module retriever']} : {'*' * outcomes['Do not progress - module retriever']}")
    print(f"Excluded {outcomes['Exclude']}  : {'*' * outcomes['Exclude']}")
    print(f"{sum(outcomes.values())} outcomes in total.")
    print("----------------------------------------------------------------")