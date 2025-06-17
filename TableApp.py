# Ask the user for the number (n)
n = int(input("Enter a number to generate its multiplication table: "))

# Ask for layout preference
layout = input("Choose layout (horizontal/vertical): ").strip().lower()

# Initialize the table list
table = []

# Generate multiplication table
if layout == "horizontal":
    for i in range(1, 11):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)

    # Print horizontally
    print("\n--- Horizontal Multiplication Table ---")
    for row in table:
        for val in row:
            print(f"{val:4}", end=" ")
        print()

elif layout == "vertical":
    for i in range(1, n + 1):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)

    # Print vertically
    print("\n--- Vertical Multiplication Table ---")
    for row in table:
        for val in row:
            print(f"{val:4}", end=" ")
        print()

else:
    print("Invalid layout option. Please choose 'horizontal' or 'vertical'.")
#For example , using number N=3 (vertical) output is
--- Vertical Multiplication Table ---
   1    2    3
   2    4    6
   3    6    9
   4    8   12
   5   10   15
   6   12   18
   7   14   21
   8   16   24
   9   18   27
  10   20   30
