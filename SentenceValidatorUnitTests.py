import unittest
from SentenceValidator import *

class Test_check_first_letter(unittest.TestCase):
    def test_first_letter_uppercase(self):
        self.assertTrue(check_first_letter('Hi there dan'))
    def test_first_letter_lowercase(self):
        self.assertFalse(check_first_letter('hi there dan'))
    def test_first_letter_integer(self):
        self.assertFalse(check_first_letter('1 Hi there dan'))

class Test_check_quotations(unittest.TestCase):
    def test_even_number_quotes(self):
        self.assertTrue(check_quotations('There are 2 quotation marks in this sentence " " '))
    def test_odd_number_quotes(self):
        self.assertFalse(check_quotations('There are 3 quotation marks in this sentence " " "'))
    def test_no_quotes(self):
        self.assertTrue(check_quotations('There are no quotation marks in this sentence'))

class Test_check_last_letter(unittest.TestCase):
    def test_ending_in_period(self):
        self.assertTrue(check_last_letter('This sentence ends in a period.'))
    def test_ending_in_question_mark(self):
        self.assertTrue(check_last_letter('This sentence ends in a question mark?'))
    def test_ending_in_exclamation_mark(self):
        self.assertTrue(check_last_letter('This sentence ends in a exclamation mark?'))
    def test_ending_in_invalid_character(self):
        self.assertFalse(check_last_letter('This sentence ends in a hashtag #'))

class Test_check_for_non_trailing_period(unittest.TestCase):
    def test_no_non_trailing_period(self):
        self.assertTrue(check_for_period('Periods can only be found at the end of the sentence.'))
    def test_non_trailing_period(self):
        self.assertFalse(check_for_period('Wow there is a period in the . middle of the sentence.'))


class Test_check_numbers(unittest.TestCase):
    def test_number_one(self):
        self.assertTrue(check_numbers('Jimmy one .'))
    def test_number_13(self):
        self.assertTrue(check_numbers('13 is the number James Harden wears.'))
    def test_number_1(self):
        self.assertFalse(check_numbers('Jimmy 1 .'))

class Test_is_sentence_valid(unittest.TestCase):
    def test_valid_case_1(self):
        self.assertTrue(is_sentence_valid('The quick brown fox said “hello Mr lazy dog”.'))
    def test_valid_case_2(self):
        self.assertTrue(is_sentence_valid('The quick brown fox said hello Mr lazy dog.'))
    def test_valid_case_3(self):
        self.assertTrue(is_sentence_valid('One lazy dog is too few, 13 is too many.'))
    def test_valid_case_4(self):
        self.assertTrue(is_sentence_valid('One lazy dog is too few, thirteen is too many.'))
    def test_valid_case_5(self):
        self.assertTrue(is_sentence_valid('How many "lazy dogs" are there?'))
    def test_invalid_case_1(self):
        self.assertFalse(is_sentence_valid('The quick brown fox said "hello Mr. lazy dog".'))
    def test_invalid_case_2(self):
        self.assertFalse(is_sentence_valid('the quick brown fox said “hello Mr lazy dog".'))
    def test_invalid_case_3(self):
        self.assertFalse(is_sentence_valid('"The quick brown fox said “hello Mr lazy dog."'))
    def test_invalid_case_4(self):
        self.assertFalse(is_sentence_valid('One lazy dog is too few, 12 is too many.'))
    def test_invalid_case_5(self):
        self.assertFalse(is_sentence_valid('Are there 11, 12, or 13 lazy dogs?'))
    def test_invalid_case_6(self):
        self.assertFalse(is_sentence_valid('There is no punctuation in this sentence'))
if __name__ == '__main__':
    unittest.main()