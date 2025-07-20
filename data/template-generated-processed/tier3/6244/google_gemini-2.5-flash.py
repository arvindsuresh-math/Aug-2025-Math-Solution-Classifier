def solve():
    """Index: 6244.
    Returns: the amount of money Tony is spending per square foot of house.
    """
    # L1
    num_guest_bedrooms = 2 # The 2 guest bedrooms
    sq_ft_per_guest_bedroom = 200 # 200 sq ft each
    total_guest_bedrooms_sq_ft = num_guest_bedrooms * sq_ft_per_guest_bedroom

    # L2
    master_suite_sq_ft = 500 # The master bedroom and bath totaled 500 sq ft
    other_areas_sq_ft = 600 # kitchen, guest bath and living area totaled 600 sq ft
    total_house_sq_ft = master_suite_sq_ft + total_guest_bedrooms_sq_ft + other_areas_sq_ft

    # L3
    monthly_rent = 3000 # Tony spends $3,000 a month on rent
    cost_per_sq_ft = monthly_rent / total_house_sq_ft

    # FA
    answer = cost_per_sq_ft
    return answer