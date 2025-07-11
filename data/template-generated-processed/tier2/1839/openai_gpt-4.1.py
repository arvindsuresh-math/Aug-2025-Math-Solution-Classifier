def solve():
    """Index: 1839.
    Returns: the combined weight of the donkey and elephant in pounds.
    """
    # L1
    elephant_weight_tons = 3 # elephant weighs 3 tons
    ton_in_pounds = 2000 # a ton is 2000 pounds
    elephant_weight_pounds = elephant_weight_tons * ton_in_pounds

    # L2
    donkey_weight_loss_percent = 0.9 # donkey weighs 90% less
    donkey_weight_loss = elephant_weight_pounds * donkey_weight_loss_percent

    # L3
    donkey_weight_pounds = elephant_weight_pounds - donkey_weight_loss

    # L4
    combined_weight = donkey_weight_pounds + elephant_weight_pounds

    # FA
    answer = combined_weight
    return answer