import random

# Function to generate a balanced sequence of brackets
def generate_balanced_sequence():
    brackets = ["(", ")", "[", "]", "{", "}"]
    random.shuffle(brackets)
    
    # Ensure the first three brackets are opening brackets
    balanced_sequence = brackets[:3] + brackets[3:]
    
    return "".join(balanced_sequence)

# Generate a balanced sequence of six brackets
balanced_sequence = generate_balanced_sequence()
print(balanced_sequence)
