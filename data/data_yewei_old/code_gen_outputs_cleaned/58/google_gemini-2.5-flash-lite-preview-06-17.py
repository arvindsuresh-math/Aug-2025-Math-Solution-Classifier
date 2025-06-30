# Calculate the number of students who receive a $6 allowance
students_6_dollar_allowance = 60 * (2/3)

# Calculate the number of students who receive a $4 allowance
students_4_dollar_allowance = 60 - students_6_dollar_allowance

# Calculate the total allowance for students receiving $6
total_allowance_6_dollar = students_6_dollar_allowance * 6

# Calculate the total allowance for students receiving $4
total_allowance_4_dollar = students_4_dollar_allowance * 4

# Calculate the total daily allowance for all students
total_daily_allowance = total_allowance_6_dollar + total_allowance_4_dollar

print(total_daily_allowance)