#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide elements of two lists element by element."""
    result = []

    for i in range(list_length):
        try:
            # Check if we have enough elements in both lists
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]

            # Perform division
            result.append(value_1 / value_2)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except TypeError:
            print("wrong type")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            continue  # This line is optional; it can be omitted.

    return result
