# 1. Get size of the string
def get_password_size(password):
    password_size = len(password)
    return password_size


# 2. Get digits and their locations
def get_digits_info(password):
    digits = []
    digit_positions = []

    for i, char in enumerate(password):
        if char.isdigit():
            digits.append(char)
            digit_positions.append(i)

    return digits, digit_positions


# 3. Get symbols and their locations
def get_symbols_info(password):
    symbols = []
    symbol_positions = []

    for i, char in enumerate(password):
        # Check if character is NOT alphanumeric (i.e., it's a symbol)
        if not char.isalnum():
            symbols.append(char)
            symbol_positions.append(i)

    return symbols, symbol_positions