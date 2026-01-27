# 1.5.2 Practice Script: Implementing a Height Class
# This script defines a Height class with methods to represent and calculate heights.

# Define the Height class
class Height(object):
    # Initialize the Height object with feet and inches
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    # String representation of the Height object
    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    # Method to add two Height objects
    def __add__(self, other):
        # Converting both objects' heights into inches
        height_self_inches = self.feet * 12 + self.inches
        height_other_inches = other.feet * 12 + other.inches

        # Adding them up
        total_height_inches = height_self_inches + height_other_inches
        # Getting the output in feet
        output_feet = total_height_inches // 12
        # Getting the output in inches
        output_inches = total_height_inches % 12

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)
    
    # Method to subtract two Height objects
    def __sub__(self, other):
        # Converting both objects' heights into inches
        height_self_inches = self.feet * 12 + self.inches
        height_other_inches = other.feet * 12 + other.inches

        # Subtracting them
        diff_inches = height_self_inches - height_other_inches
        abs_diff_inches = abs(diff_inches)

        # Getting the output in feet
        output_feet = abs_diff_inches // 12
        # Getting the output in inches
        output_inches = abs_diff_inches % 12

        # Returning the final output as a new Height object
        # If the result was negative, make the feet negative to indicate "shorter"
        if diff_inches < 0:
            output_feet = -output_feet
            # Optional: if feet is 0 but inches exist, make inches negative
            if output_feet == 0:
                output_inches = -output_inches

        return Height(output_feet, output_inches)

    # Methods to compare two Height objects
    def __lt__(self, other):
        height_self_inches = self.feet * 12 + self.inches
        height_other_inches = other.feet * 12 + other.inches
        return height_self_inches < height_other_inches

    def __le__(self, other):
        height_self_inches = self.feet * 12 + self.inches
        height_other_inches = other.feet * 12 + other.inches
        return height_self_inches <= height_other_inches
    
    def __gt__(self, other):
        height_self_inches = self.feet * 12 + self.inches
        height_other_inches = other.feet * 12 + other.inches
        return height_self_inches > height_other_inches
    
    def __ge__(self, other):
        height_self_inches = self.feet * 12 + self.inches
        height_other_inches = other.feet * 12 + other.inches
        return height_self_inches >= height_other_inches

    def __eq__(self, other):
        height_self_inches = self.feet * 12 + self.inches
        height_other_inches = other.feet * 12 + other.inches
        return height_self_inches == height_other_inches
    
    def __ne__(self, other):
        height_self_inches = self.feet * 12 + self.inches
        height_other_inches = other.feet * 12 + other.inches
        return height_self_inches != height_other_inches
    
# Create two Height instances based on user input
print("\nStep 1: Create two Height instances based on user input.")
raw_a = input("Enter person A's height (feet,inches): ").split(",")
person_A_height = Height(int(raw_a[0]), int(raw_a[1]))
raw_b = input("Enter person B's height (feet,inches): ").split(",")
person_B_height = Height(int(raw_b[0]), int(raw_b[1]))

# Select a comparison operation
print("\nStep 2: Select a comparison operation.")
operator = str(input("Enter a comparison operator (>, >= or !=): "))

# Calculate the height difference
# print("\nStep 2: Calculate the height difference.")
# height_difference = person_A_height - person_B_height

# Display the heights and the difference
# print("\nStep 3: Display the heights and the difference.")
# print("Person A's height:", person_A_height)
# print("Person B's height:", person_B_height)
# print("Height difference:", height_difference)

# Compare the two heights
print("\nStep 3: Compare the two heights.")
if operator == ">":
    print(f"\n{person_A_height} > {person_B_height}: {person_A_height > person_B_height}")
elif operator == ">=":
    print(f"{person_A_height} >= {person_B_height}: {person_A_height >= person_B_height}")
elif operator == "!=":
    print(f"{person_A_height} != {person_B_height}: {person_A_height != person_B_height}")
else:
    print("Invalid operator entered.")