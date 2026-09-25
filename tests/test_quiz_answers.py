import unittest

from application.routes import calculate_test_score


class QuizAnswerTestCase(unittest.TestCase):
    def test_step1_has_a_false_answer(self):
        form_data = {
            'q1': 'true',
            'q2': 'true',
            'q3': 'false',
            'q4': 'true',
        }

        score = calculate_test_score(form_data, 'step1')

        self.assertEqual(score, 100)


if __name__ == '__main__':
    unittest.main()
