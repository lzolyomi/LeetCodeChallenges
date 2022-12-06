def int_to_roman(num: int) -> str:
    ROMAN_NUMERALS = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    # Initialize an empty string to store the Roman numeral.
    roman = ""

    # Loop through the Roman numerals in descending order of value.
    for roman_numeral, value in ROMAN_NUMERALS.items():
        # Calculate the number of times the current Roman numeral can be subtracted from the given number.
        quotient = num // value

        # Add the Roman numeral to the string for each time it can be subtracted.
        roman += roman_numeral * quotient

        # Subtract the value of the current Roman numeral from the given number.
        num -= quotient * value

    return roman


if __name__ == "__main__":
    test = 14
    print(int_to_roman(test))
