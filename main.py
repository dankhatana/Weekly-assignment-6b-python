def calculate_pi(iterations):
    pi = 0
    sign = 1

    for i in range(1, iterations*2, 2):
        pi += sign * (4 / i)
        sign *= -1

    return pi


def main():
    iterations = 1
    while True:
        print(f"Current value of PI: {calculate_pi(iterations)}")
        choice = input("Enter 'S' to select a new number of iterations or 'Q' to quit: ")

        if choice.lower() == 's':
            new_iterations = int(input("Enter the number of iterations: "))
            if new_iterations > 0:
                iterations = new_iterations
            else:
                print("Invalid input. Please enter a positive integer.")
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()