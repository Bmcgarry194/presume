""" Tests for profile.py
"""

import unittest as unittest
from src.profile import Profile


class Test(unittest.TestCase):
    def test_init(self):
        example = Profile(name="Tester McTasty", phone_num="8087654321",
                          email="mctasty@me.com")
        self.assertEqual(example.name, "Tester McTasty")
        self.assertEqual(example.phone_num, "8087654321")
        self.assertEqual(example.email, "mctasty@me.com")

    def test_edit_address(self):
        example = Profile(name="Tester McTasty")
        example.edit_address(street="775 McNeill St.")
        self.assertEqual(example.address['street'], "775 McNeill St.")
        example.edit_address(city="Honolulu")
        self.assertEqual(example.address['city'], "Honolulu")
        example.edit_address(state="HI")
        self.assertEqual(example.address['state'], "HI")
        example.edit_address(zip="96817")
        self.assertEqual(example.address['zip'], "96817")

    def test_edit_skills(self):
        example = Profile(name="Tester McTasty")
        example.edit_skills("Python", "Numpy", "Matplotlib")
        self.assertIn("Python", example.skills)


if __name__ == '__main__':
    unittest.main()
