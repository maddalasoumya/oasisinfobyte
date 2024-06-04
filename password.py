import random
import string

def generate_password(length=12, include_upper=True, include_lower=True, include_digits=True, include_symbols=True):
  """
  Generates a random password based on user-defined criteria.

  Args:
      length (int, optional): Desired password length. Defaults to 12.
      include_upper (bool, optional): Include uppercase letters. Defaults to True.
      include_lower (bool, optional): Include lowercase letters. Defaults to True.
      include_digits (bool, optional): Include digits. Defaults to True.
      include_symbols (bool, optional): Include symbols. Defaults to True.

  Returns:
      str: The generated random password.
  """

  char_sets = []
  if include_upper:
    char_sets.append(string.ascii_uppercase)
  if include_lower:
    char_sets.append(string.ascii_lowercase)
  if include_digits:
    char_sets.append(string.digits)
  if include_symbols:
    char_sets.append(string.punctuation)

  all_chars = ''.join(char_sets)
  password = ''.join(random.choice(all_chars) for _ in range(length))
  return password

# Get user input with validation
while True:
  try:
    length = int(input("Enter desired password length (minimum 8): "))
    if length < 8:
      raise ValueError("Password length must be at least 8 characters.")
    break
  except ValueError:
    print("Invalid input. Please enter a number greater than or equal to 8.")

char_types = {
  'uppercase': input("Include uppercase letters (y/n)? ").lower() == 'y',
  'lowercase': input("Include lowercase letters (y/n)? ").lower() == 'y',
  'digits': input("Include digits (y/n)? ").lower() == 'y',
  'symbols': input("Include symbols (y/n)? ").lower() == 'y',
}

# Generate password based on user preferences
password = generate_password(length,char_types)

# Print the generated password
print("Your generated password:", password)
