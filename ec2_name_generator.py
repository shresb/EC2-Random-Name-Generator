import random
import string

# Ask the user how many names they want
num_names = int(input("How many EC2 names do you want? "))

# Ask the user for their department
department = input("Enter your department name: ")

# Make a list to hold the names
generated_names = []

# Repeat for the number of names requested
for i in range(num_names):
    # Create a random 4-digit number
    random_number = random.randint(1000, 9999)
    
    # Create 2 random letters
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=2))
    
    # Combine to make the EC2 name
    ec2_name = f"{department}-{random_letters}-{random_number}"
    
    # Save the name to the list
    generated_names.append(ec2_name)

# Show the names
print("\nHere are your EC2 names:")
for name in generated_names:
    print(name)
