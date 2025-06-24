# Carolyn practices the piano for 20 minutes a day and the violin for three times as long.
# If she practice six days a week, how many minutes does she spend practicing in a month with four weeks?

# Piano practice time per day
piano_practice_per_day = 20

# Violin practice time per day is three times the piano practice time
violin_practice_per_day = piano_practice_per_day * 3

# Total practice time per day
total_practice_per_day = piano_practice_per_day + violin_practice_per_day

# Number of days Carolyn practices per week
practice_days_per_week = 6

# Total practice time per week
total_practice_per_week = total_practice_per_day * practice_days_per_week

# Number of weeks in the month
weeks_in_month = 4

# Total practice time in a month
total_practice_in_month = total_practice_per_week * weeks_in_month

# Print the result
print(f"Carolyn spends {total_practice_in_month} minutes practicing in a month with four weeks.")