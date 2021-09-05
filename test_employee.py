import unittest
from unittest import mock
from unittest.mock import patch

from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Marcin', 'Bielinski', 50000)
        self.emp_2 = Employee('Bob', 'Ross', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Marcin.Bielinski@email.com')
        self.assertEqual(self.emp_2.email, 'Bob.Ross@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Bielinski@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Ross@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Marcin Bielinski')
        self.assertEqual(self.emp_2.fullname, 'Bob Ross')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Bielinski')
        self.assertEqual(self.emp_2.fullname, 'Jane Ross')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:

            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Bielinski/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2. monthly_schedule('June')
            mocked_get. assert_called_with('http://company.com/Ross/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()