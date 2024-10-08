#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    # Compute the weighted sum and sum of weights
    weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)

    # Return the weighted average
    return weighted_sum / total_weight if total_weight != 0 else 0
