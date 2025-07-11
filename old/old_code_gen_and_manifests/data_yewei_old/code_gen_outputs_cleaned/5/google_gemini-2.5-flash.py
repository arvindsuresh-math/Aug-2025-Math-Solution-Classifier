def solve():
    # Number of yellow flowers
    yellow_flowers = 10

    # Percentage more purple flowers than yellow
    purple_more_percentage = 80
    # Calculate the additional number of purple flowers
    additional_purple_flowers = (purple_more_percentage / 100) * yellow_flowers

    # Total number of purple flowers
    purple_flowers = yellow_flowers + additional_purple_flowers

    # Total number of yellow and purple flowers
    total_yellow_purple_flowers = yellow_flowers + purple_flowers

    # Percentage of green flowers compared to yellow and purple flowers
    green_percentage = 25
    # Calculate the number of green flowers
    green_flowers = (green_percentage / 100) * total_yellow_purple_flowers

    # Total number of flowers in the garden
    total_flowers = total_yellow_purple_flowers + green_flowers

    return int(total_flowers)

# Execute the function to get the answer
# answer = solve()
# print(answer)