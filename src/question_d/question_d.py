# question_d.py

# write functions here, don't add input('') statements here!
def test_config():
    return True


def create_multiplication_table():
    table = []
    for i in range(1, 6):  # Rows from 1 to 5
        row = []
        for j in range(1, 11):  # Columns from 1 to 10
            row.append(i * j)
        table.append(row)
    return table


def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(f"{value:<4}", end="")  # Left-align with spacing
        print()  # Newline after each row
