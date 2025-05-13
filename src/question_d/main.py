# add import
from question_d import create_multiplication_table, display_multiplication_table

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        choice = input("\nWould you like to generate the table again? (y/n): ").strip().lower()
        if choice != "y":
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()
