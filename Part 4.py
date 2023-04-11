import credit_outcome as co

def get_student_id():
    """
    Prompts the user to enter a student ID and returns it in lowercase format.
    """
    student_id = input("Please enter the student ID (w1234567): ").lower()
    return student_id

def is_valid_student_id(student_id):
    """
    Returns True if the given student ID is in the correct format (w1234567).
    """
    return student_id.startswith("w") and student_id[1:].isdigit() and len(student_id) == 8

def check_existing_student_id(student_id: str, students: dict) -> bool:
    """
    Returns True if the given student ID already exists in the given dictionary.
    """
    return student_id in students

def prompt_overwrite(student_id):
    """
    Prompts the user if they want to overwrite an existing outcome for the given student ID.
    Returns True if they answer 'y', False otherwise.
    """
    overwrite = input(f"The student ID {student_id} already has an outcome. Do you want to overwrite it? (enter y to overwrite or any other key to skip): ")
    return overwrite.lower() == "y"

def write_student_data(student_id: str, pass_credits: int, defer_credits: int, fail_credits: int, students: dict) -> None:
    """
    Writes the outcome for a student with the given ID and credits to the given dictionary.
    """
    if pass_credits == 120:
        students[student_id] = f"Progress - {pass_credits}, {defer_credits}, {fail_credits}"
    elif pass_credits == 100:
        students[student_id] = f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}"
    elif pass_credits >= 40 and defer_credits >= 20 or pass_credits >= 60 or defer_credits >= 60:
        students[student_id] = f"Module retriever - {pass_credits}, {defer_credits}, {fail_credits}"
    else:
        students[student_id] = f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}"

def print_student_outcomes(students):
    """
    Prints the student IDs and outcomes from the given dictionary.
    """
    for student_id, outcome in students.items():
        print(f"{student_id}: {outcome}")

# Intialise progression outcome counts
progress_count, trailer_count, retriever_count, exclude_count = [0]*4

students = {}

# Initialize a variable to control the loop
continue_loop = True

while continue_loop:

    student_id = co.get_student_id()

    if not co.is_valid_student_id(student_id):
        print(f"The student ID {student_id} is not in the correct format (w1234567). Please try again.")
        continue

    if co.check_existing_student_id(student_id, students):
        if not co.prompt_overwrite(student_id):
            continue

    # Get credits for pass, defer and fail
    pass_credits = co.get_credits_input("pass")
    defer_credits = co.get_credits_input("defer")
    fail_credits = co.get_credits_input("fail")

    # Keeps count of total credits entered
    total_credits = sum([pass_credits, defer_credits, fail_credits])

    #Checks if total credits is equal to 120, else print that the total is incorrect
    if total_credits != 120:
        print("Total incorrect")

    # Continue with the program if no errors
    else:
        # Counts and records the progression outcomes and credits in a dictionary
        co.write_student_data(student_id, pass_credits, defer_credits, fail_credits, students)

    # Prompts the users if they want to continue or quit and view results
    choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
    if choice.lower() == "n":
        continue_loop = False

print("\nPart 4:")

print_student_outcomes(students)