import unittest
from src.main import get_credit_card_banner, validate_credit_card_number

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

    is_valid = luhn_algorithm(card_number)
    print(f"Card Number: {card_number}, Banner: {banner}, Luhn Valid: {is_valid}")
    return is_valid

class TestCreditCardFunctions(unittest.TestCase):

    def test_get_credit_card_banner(self):
        self.assertEqual(get_credit_card_banner("4111111111111111"), "Visa")
        self.assertEqual(get_credit_card_banner("5105105105105100"), "Mastercard")
        self.assertEqual(get_credit_card_banner("371449635398431"), "American Express")
        self.assertEqual(get_credit_card_banner("30569309025904"), "Diners Club")
        self.assertEqual(get_credit_card_banner("6011111111111117"), "Discover")
        self.assertEqual(get_credit_card_banner("201400000000009"), "enRoute")
        self.assertEqual(get_credit_card_banner("3530111333300000"), "JCB")
        self.assertEqual(get_credit_card_banner("869941234567890"), "Voyager")
        self.assertEqual(get_credit_card_banner("6370950000000000"), "HiperCard")
        self.assertEqual(get_credit_card_banner("5078000000000000"), "Aura")
        self.assertEqual(get_credit_card_banner("0000000000000000"), "Unknown")

    def test_validate_credit_card_number(self):
        self.assertTrue(validate_credit_card_number("4111111111111111"))  # Valid Visa
        self.assertTrue(validate_credit_card_number("5105105105105100"))  # Valid Mastercard
        self.assertTrue(validate_credit_card_number("371449635398431"))  # Valid American Express
        self.assertTrue(validate_credit_card_number("30569309025904"))  # Valid Diners Club
        self.assertTrue(validate_credit_card_number("6011111111111117"))  # Valid Discover
        self.assertTrue(validate_credit_card_number("201400000000009"))  # Valid enRoute
        self.assertTrue(validate_credit_card_number("3530111333300000"))  # Valid JCB
        self.assertTrue(validate_credit_card_number("869941234567890"))  # Valid Voyager
        self.assertTrue(validate_credit_card_number("6370950000000000"))  # Valid HiperCard
        self.assertTrue(validate_credit_card_number("5019783781775035"))  # Valid Aura
        print(validate_credit_card_number("1234567812345670"))  # Debug print statement
        self.assertFalse(validate_credit_card_number("1234567812345670"))  # Invalid number

if __name__ == "__main__":
    unittest.main()