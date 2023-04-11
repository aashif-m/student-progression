def get_credits_input(credit_type):
    """
    Asks the user to enter their credits for a given credit type and returns it as an integer.

    Parameters:
    credit_type (str): The type of credit, pass or defer or fail.

    Returns:
    int: The number of credits entered by the user.

    Raises:
    ValueError: If the user enters an invalid credit value.
    """
    while True:
        try:
            credits = int(input(f"Please enter your {credit_type} credits: "))
            if credits not in range(0, 121, 20):
                print("Out of range")
            else:
                return credits
        except ValueError:
            print("Integer Required")


def validate_student_id(student_id):
    """Validates the student ID and returns True if it is in the correct format.

    Args:
        student_id (str): The student ID to be validated.

    Returns:
        bool: True if the student ID is in the format w1234567, False otherwise.
    """
    # Check if the input is in the correct format like w1234567
    if not student_id.startswith("w") or not student_id[1:].isdigit() or len(student_id) != 8:
        print(f"The student ID {student_id} is not in the correct format (w1234567). Please try again.")
        return False
    else:
        return True


def get_outcome(pass_credits, defer_credits):
    """
    Determines the outcome of a student based on their pass and defer credits.

    Parameters:
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


def display_results(students):
    """
    Display the results stored in a dictionary.

    This function prints the student ID and outcome for each student in the dictionary.
    The outcome is based on the credits passed, deferred, and failed by the student.
    :param students: A dictionary of student ID and outcome pairs.
    :return: None
    """
    print("Part 4:")
    for student_id, outcome in students.items():
        print(f"{student_id}: {outcome}")


def main():
    # Create an empty dictionary to store student IDs and outcomes
    students = {}

    # Initialize a variable to control the loop
    continue_loop = True

    while continue_loop:

        # Input student ID and convert it to lowercase
        student_id = input("Please enter the student ID (w1234567) : ").lower()

        # Validate the student ID using a function
        if not validate_student_id(student_id):
            continue

        # Check if the student ID already exists in the dictionary
        if student_id in students:
            # Ask the user if they want to overwrite the existing outcome
            overwrite = input(
                f"The student ID {student_id} already has an outcome. Do you want to overwrite it? (enter y to "
                f"overwrite or any other key to skip): ")

            # If input is not 'y' then skip this student ID
            if overwrite.lower() != "y":
                continue

        # Get credits for pass, defer and fail
        pass_credits = get_credits_input("pass")
        defer_credits = get_credits_input("defer")
        fail_credits = get_credits_input("fail")

        total_credits = sum([pass_credits, defer_credits, fail_credits])

        # Checks if total credits is equal to 120, else print that the total is incorrect
        if total_credits != 120:
            print("Total incorrect")

        # Continue with the program if no errors
        else:
            # Calculate and store the progression outcome and credits in a dictionary
            outcome = get_outcome(pass_credits, defer_credits)
            print(outcome)
            students[student_id] = f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}"

        # Prompts the users if they want to continue or quit and view results
        choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
        if choice.lower() == "n":
            continue_loop = False

    display_results(students)


main()