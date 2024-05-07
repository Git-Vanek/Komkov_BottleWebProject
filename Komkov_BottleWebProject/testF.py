import unittest
import myform

list_mail_uncor = ["", "1", "@", "@mail", "1@mail.ru", "asd@mail.com", "@@mail.ru", "q2we@mail.ru.com", ".qwe@mail.ru", "test1.@gmail.com", "0.....@mail.ru", "11234567891234567890123456789011@mail.ru"]

class Test_test_F_mail(unittest.TestCase):
    def test_Test_test_F_mail(self):
        for check in list_mail_uncor:
            self.assertFalse(myform.mailcheck(check));

if __name__ == '__main__':
    unittest.main()

