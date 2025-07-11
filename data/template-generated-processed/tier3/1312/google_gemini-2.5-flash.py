def solve():
    """Index: 1312.
    Returns: the cost of one printer.
    """
    # L1
    num_keyboards = 15 # 15 keyboards
    cost_per_keyboard = 20 # keyboard costs $20
    total_keyboard_cost = num_keyboards * cost_per_keyboard

    # L2
    total_cost_all_items = 2050 # total of $2050
    num_printers = 25 # 25 printers
    total_printer_cost = total_cost_all_items - total_keyboard_cost

    # L3
    cost_per_printer = total_printer_cost / num_printers

    # FA
    answer = cost_per_printer
    return answer