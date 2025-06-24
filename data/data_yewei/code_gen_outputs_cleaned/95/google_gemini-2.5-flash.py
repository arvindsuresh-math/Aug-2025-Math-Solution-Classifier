def solve():
    # Define the value of a quarter and a nickel
    quarter_value = 0.25
    nickel_value = 0.05

    # L1: Calculate how many nickels are in one quarter
    nickels_per_quarter = quarter_value / nickel_value

    # Alice has 20 quarters
    num_quarters = 20

    # L2: Calculate the total number of nickels Alice receives from the bank
    total_nickels = num_quarters * nickels_per_quarter

    # L3: Calculate the number of iron nickels (20% of total nickels)
    iron_nickel_percentage = 0.20
    num_iron_nickels = total_nickels * iron_nickel_percentage

    # L4: Calculate the number of regular nickels
    num_regular_nickels = total_nickels - num_iron_nickels

    # Define the worth of an iron nickel
    iron_nickel_worth = 3.00

    # L5: Calculate the total value of the iron nickels
    value_iron_nickels = num_iron_nickels * iron_nickel_worth

    # L6: Calculate the total value of the regular nickels
    value_regular_nickels = num_regular_nickels * nickel_value

    # L7: Calculate the total value of her money
    total_value = value_iron_nickels + value_regular_nickels

    return {
        "L1": f"A quarter is worth five nickels because .25 / .05 = [[{nickels_per_quarter:.0f}]]",
        "L2": f"She gets {int(total_nickels)} nickels from the bank because {int(num_quarters)} x {int(nickels_per_quarter)} = [[{int(total_nickels)}]]",
        "L3": f"{int(num_iron_nickels)} of the nickels are iron nickels because {int(total_nickels)} x {iron_nickel_percentage:.2f} = [[{int(num_iron_nickels)}]]",
        "L4": f"{int(num_regular_nickels)} of the nickels are regular because {int(total_nickels)} - {int(num_iron_nickels)} = [[{int(num_regular_nickels)}]]",
        "L5": f"The iron nickels are worth ${value_iron_nickels:.0f} because {int(num_iron_nickels)} x {int(iron_nickel_worth)} = [[{value_iron_nickels:.0f}]]",
        "L6": f"The regular nickels are worth ${value_regular_nickels:.0f} because {int(num_regular_nickels)} x {nickel_value:.2f} = [[{value_regular_nickels:.0f}]]",
        "L7": f"Her money is now worth ${total_value:.0f} because {value_iron_nickels:.0f} + {value_regular_nickels:.0f} = [[{total_value:.0f}]]"
    }