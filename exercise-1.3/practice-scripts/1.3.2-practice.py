# Exercise 1.3. Code Practice 2: FOR loops

# Define a list of test scores
test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]

# Sort the list in descending order
test_scores.sort(reverse=True)

# Print the top three scores
for i in range(0,3):
    print(test_scores[i])