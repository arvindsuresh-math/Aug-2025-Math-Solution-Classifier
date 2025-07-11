from fractions import Fraction

def solve():
    """Index: 946.
    Returns: the total amount Ruby pays for 13 dance classes.
    """
    # L1
    pack_price = 75 # $75 for 10 classes in one pack
    pack_classes = 10 # 10 classes in one pack
    avg_class_price = pack_price / pack_classes

    # L2
    additional_class_increase = Fraction(1, 3) # 1/3 more than the average price
    additional_class_price = avg_class_price * (1 + additional_class_increase)

    # L3
    total_classes = 13 # 13 total classes
    extra_classes = total_classes - pack_classes

    # L4
    extra_classes_cost = extra_classes * additional_class_price

    # L5
    total_cost = pack_price + extra_classes_cost

    # FA
    answer = total_cost
    return answer