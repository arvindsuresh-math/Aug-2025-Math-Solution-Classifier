def solve():
    # Number of roses in the garden
    num_roses = 25
    # Number of tulips in the garden
    num_tulips = 40
    # Number of daisies in the garden
    num_daisies = 35

    # L1: Calculate the total number of flowers
    total_flowers = num_roses + num_tulips + num_daisies
    # L2: Calculate the number of flowers that are not roses (tulips + daisies)
    flowers_not_roses = num_tulips + num_daisies
    # L3: Calculate the percentage of flowers that are not roses
    percentage_not_roses = (flowers_not_roses / total_flowers) * 100

    return total_flowers, flowers_not_roses, percentage_not_roses

# Get the results from the function
total_flowers, flowers_not_roses, percentage_not_roses = solve()