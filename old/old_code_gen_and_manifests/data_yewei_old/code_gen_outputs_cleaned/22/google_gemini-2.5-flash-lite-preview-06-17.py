# Calculate the number of letters in Jamie's last name
jamie_last_name_letters = len("Grey")

# Calculate the number of letters in Bobbie's last name
# If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's.
# Let B be the number of letters in Bobbie's last name.
# B - 2 = 2 * jamie_last_name_letters
bobbie_last_name_letters = (2 * jamie_last_name_letters) + 2

# Calculate the number of letters in Samantha's last name
# Samantha’s last name has three fewer letters than Bobbie’s last name.
samantha_last_name_letters = bobbie_last_name_letters - 3

# Print the result
print(f"The number of letters in Samantha's last name is: {samantha_last_name_letters}")