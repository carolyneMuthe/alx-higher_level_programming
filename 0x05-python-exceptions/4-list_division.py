#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists and returns
                                       a new list with the results."""
    result = []

    for i in range(list_length):
        try:
            # Check if indices are in range for both lists
            if i >= len(my_list_1):
                print("out of range")
                result.append(0)
                continue
            if i >= len(my_list_2):
                print("out of range")
                result.append(0)
                continue

            # Attempt to perform the division
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            # Check if the elements are of the correct type
            if not isinstance(num1, (int, float)):
                print("wrong type")
                result.append(0)
                continue
            if not isinstance(num2, (int, float)):
                print("wrong type")
                result.append(0)
                continue

            # Perform the division
            result.append(num1 / num2)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except Exception as e:
            print("Error: {}".format(e))
            result.append(0)

    return result
