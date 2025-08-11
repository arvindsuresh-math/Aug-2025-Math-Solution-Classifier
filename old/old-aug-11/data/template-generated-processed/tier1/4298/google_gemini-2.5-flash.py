def solve():
    """Index: 4298.
    Returns: Peter's remaining money after shopping.
    """
    # L1
    kilos_potatoes = 6 # 6 kilos of potatoes
    price_per_kilo_potatoes = 2 # $2 per kilo
    price_potatoes = kilos_potatoes * price_per_kilo_potatoes

    # L2
    kilos_tomatoes = 9 # 9 kilos of tomato
    price_per_kilo_tomatoes = 3 # $3 per kilo
    price_tomatoes = kilos_tomatoes * price_per_kilo_tomatoes

    # L3
    kilos_cucumbers = 5 # 5 kilos of cucumbers
    price_per_kilo_cucumbers = 4 # $4 per kilo
    price_cucumbers = kilos_cucumbers * price_per_kilo_cucumbers

    # L4
    kilos_bananas = 3 # 3 kilos of bananas
    price_per_kilo_bananas = 5 # $5 per kilo
    price_bananas = kilos_bananas * price_per_kilo_bananas

    # L5
    total_spent = price_potatoes + price_tomatoes + price_cucumbers + price_bananas

    # L6
    initial_money = 500 # carried $500 to the market
    remaining_money = initial_money - total_spent

    # FA
    answer = remaining_money
    return answer