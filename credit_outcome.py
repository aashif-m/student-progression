def get_credits_input(credit_type):
    while True:
        credits = input(f"Please enter your {credit_type} credits: ")
        if is_valid_credits(credits):
            return int(credits)

def is_valid_credits(credits):
    if not credits.isdigit():
        print("Integer required")
        return False
    elif int(credits) not in range(0, 121, 20):
        print("‘Out of range.")
        return False
    else:
        return True

def get_outcome(pass_credits, defer_credits):
    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Progress (module trailer)"
    elif pass_credits + defer_credits >= 60:
        return "Do not progress - module retriever"
    else:
        return "Exclude"


def print_histogram(outcomes):
    print("---------------------------------------------------------------")
    print("Histogram")
    for outcome, count in outcomes.items():
        print(f"{outcome} {count} : {'*' * count}")
    print(f"{sum(outcomes.values())} outcomes in total.")
    print("----------------------------------------------------------------")
