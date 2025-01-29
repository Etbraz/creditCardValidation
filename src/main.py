def get_credit_card_banner(card_number):
    card_number = str(card_number)
    banners = {
        "Mastercard": {"length": [16], "prefixes": ["51", "52", "53", "54", "55"]},
        "Visa": {"length": [16], "prefixes": ["4"]},
        "American Express": {"length": [15], "prefixes": ["34", "37"]},
        "Diners Club": {"length": [14, 16, 19], "prefixes": ["300", "301", "302", "303", "304", "305", "36", "38", "39"]},
        "Discover": {"length": [16], "prefixes": ["6011"] + [str(i) for i in range(622126, 622926)] + ["64", "65"]},
        "enRoute": {"length": [15], "prefixes": ["2014", "2149"]},
        "JCB": {"length": [16], "prefixes": [str(i) for i in range(3528, 3589)]},
        "Voyager": {"length": [15], "prefixes": ["8699"]},
        "HiperCard": {"length": [13, 16], "prefixes": ["637095", "637599", "606282"]},
        "Aura": {"length": [16], "prefixes": ["5078", "5079", "5080"]}
    }

    for banner, rules in banners.items():
        if len(card_number) in rules["length"]:
            if any(card_number.startswith(prefix) for prefix in rules["prefixes"]):
                return banner
    return "Unknown"

def validate_credit_card_number(card_number):
    def luhn_algorithm(card_number):
        total = 0
        reverse_digits = card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    banner = get_credit_card_banner(card_number)
    if banner == "Unknown":
        return False

    return luhn_algorithm(card_number)

def input_and_validate_credit_card():
    card_number = input("Please enter your credit card number: ")
    if validate_credit_card_number(card_number):
        banner = get_credit_card_banner(card_number)
        print(f"Credit card is valid. Banner: {banner}")
    else:
        print("Credit card is invalid.")

def main():
    while True:
        print("1. Validate a credit card number")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            input_and_validate_credit_card()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    main()
