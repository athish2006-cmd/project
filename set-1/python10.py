def convert_base(number_str, from_base, to_base):
    """
    Converts a number from one base to another.

    Args:
        number_str (str): The number as a string in the original base.
        from_base (int): The original base of the number.
        to_base (int): The target base for the conversion.

    Returns:
        str: The number as a string in the new base.
    """
    try:
        decimal_value = int(number_str, from_base)

        # Step 2: Convert from base 10 to the target base
        if to_base == 10:
            return str(decimal_value)
        elif to_base < 2 or to_base > 36:
            return "Target base must be between 2 and 36."

        new_base_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = []
        
        if decimal_value == 0:
            return "0"

        while decimal_value > 0:
            remainder = decimal_value % to_base
            result.append(new_base_chars[remainder])
            decimal_value //= to_base
        
        return ''.join(result[::-1])

    except ValueError as e:
        return f"Error: {e}. Ensure input number is valid for the given 'from_base'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


binary_num = "101010"
decimal_result = convert_base(binary_num, 2, 10)
print(f"'{binary_num}' in base 2 is '{decimal_result}' in base 10")


hex_num = "2A"
octal_result = convert_base(hex_num, 16, 8)
print(f"'{hex_num}' in base 16 is '{octal_result}' in base 8")


decimal_num = "255"
hex_result = convert_base(decimal_num, 10, 16)
print(f"'{decimal_num}' in base 10 is '{hex_result}' in base 16")

base3_num = "210"
base5_result = convert_base(base3_num, 3, 5)
print(f"'{base3_num}' in base 3 is '{base5_result}' in base 5")
