# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1998768 20221368
 
# Date: 2023/04/11 


import credit_outcome_functions as co


def validate_student_id(student_id):
    """
    Validate the student ID and return True if it is in the correct format.

    The correct format is a lowercase letter 'w' followed by seven digits.
    For example: w1234567
    If the student ID is not in the correct format, print an error message and return False.

    Args:
        student_id (str): The student ID to be validated.

    Returns:
        bool: True if the student ID is valid, False otherwise.
    """
    if not student_id.startswith("w") or not student_id[1:].isdigit() or len(student_id) != 8:
        print(f"The student ID {student_id} is not in the correct format (w1234567). Please try again.")
        return False
    else:
        return True


def display_results(students):
    """
    Display the results stored in a dictionary.

    This function prints the student ID and outcome for each student in the dictionary.
    The outcome is based on the credits passed, deferred, and failed by the student.

    Args:
        students (dict): A dictionary of student ID and outcome pairs.

    Returns:
        None
    """
    print("Part 4:")
    for student_id, outcome in students.items():
        print(f"{student_id}: {outcome}")


# Main function that controls the program flow
def main():
    # Create an empty dictionary to store student IDs and outcomes
    students = {}

    # Initialize a variable to control the loop
    continue_loop = True

    while continue_loop:

        # Input student ID and convert it to lowercase
        student_id = input("Please enter the student ID (w1234567) : ").lower()

        # Validate the student ID
        if not validate_student_id(student_id):
            continue

        # Check if the student ID already exists in the dictionary
        if student_id in students:
            # Prompts the user if they want to overwrite the existing outcome
            overwrite = input(
                f"The student ID {student_id} already has an outcome. Do you want to overwrite it? (enter y to "
                f"overwrite or any other key to skip): ")

            # If input is not 'y' then skip this student ID
            if overwrite.lower() != "y":
                continue

        # Get the input for pass,defer and fail credits from the user and validate it
        pass_credits = co.get_credits_input("pass")
        defer_credits = co.get_credits_input("defer")
        fail_credits = co.get_credits_input("fail")

        # Keeps count of total credits entered
        total_credits = sum([pass_credits, defer_credits, fail_credits])

        # Check if the total credits is equal to 120
        if total_credits != 120:
            print("Total incorrect")

        # Continue with the program if no errors
        else:
            # Calculate and store the progression outcome and credits in a dictionary
            outcome = co.get_outcome(pass_credits, defer_credits)
            print(outcome)
            students[student_id] = f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}"

        # Prompts the users if they want to continue or quit and view results
        choice = input("Do you want to continue? (enter any key to continue or enter q to quit and view results: ")
        if choice.lower() == "q":
            continue_loop = False

    # Display the results
    display_results(students)


# Call the main function
main()
