import unittest
import myform
              
list_mail_cor = ["1abcd1@mail.ru", "Test.test@gmail.com", "Newtest.1@gmail.com", "Newtest_2@gmail.com", "Newtest%3@gmail.com", "Newtest+4@gmail.com", "Newtest-5@gmail.com", "123456@gmail.com", "123456@mail.ru", "123456@yandex.ru", "TestTestTestTestTestTestTest@mail.ru", "1234567890@gmail.com"]

class Test_test_T_mail(unittest.TestCase):
    def test_list_mail_cor(self):
        for check in list_mail_cor:
            self.assertTrue(myform.mailcheck(check));

if __name__ == '__main__':
    unittest.main()

