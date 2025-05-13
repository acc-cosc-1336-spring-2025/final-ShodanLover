# main.py

# add import
from question_b import get_most_likely_ancestor_consensus

def main():
    while True:
        print("Menu:")
        print("1 - Find substring positions in DNA sequence")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                dna_string1 = input("Enter a DNA string (9 to 16 characters): ").strip().upper()
                if 8 < len(dna_string1) <= 16:
                    break
                else:
                    print("DNA string must be greater than 8 and at most 16 characters.")

            while True:
                dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").strip().upper()
                if len(dna_string2) == 4:
                    break
                else:
                    print("DNA substring must be exactly 4 characters.")

            result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

            if result:
                print("Positions found:", *result)
            else:
                print("Substring not found.")
            print()

        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
