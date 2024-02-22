import random
import string

def generate_password(length, complexity):
    # Define characters based on complexity
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        print("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")
        return None
    
    # Generate password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt user for password length
    length = int(input("Enter the desired length of the password: "))
    
    # Prompt user for complexity level
    complexity = input("Enter the complexity level ('low', 'medium', or 'high'): ").lower()
    
    # Generate password
    password = generate_password(length, complexity)
    
    # Display generated password
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
