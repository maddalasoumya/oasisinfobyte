def calculate_bmi(weight, height):
      """Calculates BMI based on weight (kg) and height (m)."""
      bmi = weight / (height**2)
      return bmi

def bmi_category(bmi):
  """Classifies BMI into categories based on predefined ranges."""
  if bmi <= 18.5:
    return "Underweight"
  elif bmi <= 24.9:
    return "Normal weight"
  elif bmi <= 29.9:
    return "Overweight"
  else:
    return "Obese"

def main():
  """Prompts user for input, calculates BMI, and displays results."""
  try:
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))
    if weight <= 0 or height <= 0:
      raise ValueError("Weight and height must be positive values.")
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")
  except ValueError as e:
    print(f"Error: {e}")

if _name_ == "_main_":
   main()
