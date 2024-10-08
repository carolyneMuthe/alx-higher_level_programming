def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):  # This loops for i = 1 and i = 2
        try:
            if i > a:  # Check if i is greater than a
                raise Exception('Too far')
            result += (a ** b) / i  # Calculate a^b / i and add to result
        except Exception:
            break  # Exit the loop if an exception occurs

    result += a + b  # Final addition of a and b
    return result  # Return the final result#!/usr/bin/python3
def magic_calculation(a, b):
        result = 0
            
                for i in range(1, 3):  # This loops for i = 1 and i = 2
                            try:
                                            if i > a:  # Check if i is greater than a
                                                                raise Exception('Too far')
                                                                        result += (a ** b) / i  # Calculate a^b / i and add to result
                                                                                except Exception:
                                                                                                break  # Exit the loop if an exception occurs

                                                                                                result += a + b  # Final addition of a and b
                                                                                                    return result  # Return the final result
                                                                                            #!/usr/bin/python3
                                                                                            def magic_calculation(a, b):
                                                                                                    result = 0
                                                                                                        
                                                                                                            for i in range(1, 3):  # This loops for i = 1 and i = 2
                                                                                                                        try:
                                                                                                                                        if i > a:  # Check if i is greater than a
                                                                                                                                                            raise Exception('Too far')
                                                                                                                                                                    result += (a ** b) / i  # Calculate a^b / i and add to result
                                                                                                                                                                            except Exception:
                                                                                                                                                                                            break  # Exit the loop if an exception occurs

                                                                                                                                                                                            result += a + b  # Final addition of a and b
                                                                                                                                                                                                return result  # Return the final result

