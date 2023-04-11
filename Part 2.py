import credit_outcome as co

def save_progression_data_list(pass_credits, defer_credits, fail_credits, progression_list):
    credits = [pass_credits, defer_credits, fail_credits]
    progression_list.append(credits)

def print_progression_data_list(progression_list):
    print("Part 2:")
    for credits in progression_list:
        pass_credits, defer_credits, fail_credits = credits
        outcome = co.get_outcome(pass_credits, defer_credits)
        print(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}")


def main():
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Do not progress - module retriever": 0, "Exclude": 0}
    progression_list = []
    
    continue_loop = True

    while continue_loop:
        pass_credits = co.get_credits_input("pass")
        defer_credits = co.get_credits_input("defer")
        fail_credits = co.get_credits_input("fail")
        total_credits = sum([pass_credits, defer_credits, fail_credits])

        if total_credits != 120:
            print("Total incorrect.")

        else:
            outcome = co.get_outcome(pass_credits, defer_credits)
            print(outcome)
            outcomes[outcome] += 1

            save_progression_data_list(pass_credits, defer_credits, fail_credits, progression_list)
        choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
        if choice.lower() == "n":
            continue_loop = False

    co.print_histogram(outcomes)

    print_progression_data_list(progression_list)

if __name__ == "__main__":
    main()