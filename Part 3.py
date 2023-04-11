import credit_outcome as co

def main():
    outcomes = {"Progress": 0, "Progress (module trailer)": 0, "Do not progress - module retriever": 0, "Exclude": 0}

    co.clear_progression_data_file()
    
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

            co.save_progression_data_file(pass_credits, defer_credits, fail_credits)
        choice = input("Do you want to continue? (enter any key to continue or enter n to quit and view results: ")
        if choice.lower() == "n":
            continue_loop = False

    co.print_histogram(outcomes)

    co.print_progression_data_file()

if __name__ == "__main__":
    main()