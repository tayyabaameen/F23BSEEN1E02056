# Number of rows in the pattern
num_rows = 5

# Iterate through each row
for i in range(1, num_rows + 1):
    # Print the numbers in each row
    for j in range(i):
        print(i, end=" ")
    
    # Move to the next line after printing each row
    print()
