def solve():
    """Index: 7128.
    Returns: the total amount Blake will spend on paint and primer.
    """
    # L1
    primer_original_price = 30.00 # primer is $30.00 a gallon
    primer_discount_rate = 0.20 # 20% off
    primer_discount_amount = primer_original_price * primer_discount_rate

    # L2
    primer_sale_price_per_gallon = primer_original_price - primer_discount_amount

    # L3
    num_gallons_primer = 5 # 5 rooms; Each room will require a gallon of primer
    total_primer_cost = num_gallons_primer * primer_sale_price_per_gallon

    # L4
    num_gallons_paint = 5 # 5 rooms; Each room will require a gallon of paint
    paint_gallon_price = 25.00 # The paint costs $25.00 a gallon
    total_paint_cost = num_gallons_paint * paint_gallon_price

    # L5
    total_cost = total_primer_cost + total_paint_cost

    # FA
    answer = total_cost
    return answer