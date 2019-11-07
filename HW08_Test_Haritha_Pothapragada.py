""" HW08 test file """
import datetime
import unittest
from HW08_Haritha_Pothapragada import date_arithmetic, file_reading_gen, FileAnalyzer


class TestModuleGeneratorFile(unittest.TestCase):
    """This is a test class """

    def test_date_arithmetic(self):
        """This function tests the date_arithmetic function"""
        self.assertEqual(date_arithmetic(), (
            datetime.datetime(2000, 3, 1, 0, 0), datetime.datetime(2017, 3, 2, 0, 0), datetime.timedelta(days=303)))

    def test_file_reading_gen(self):
        """This function tests the file_reading_gen function"""
        file_name = r"C:\Users\Haritha\PycharmProjects\untitled\1.py.txt"
        lis = []
        for i, j, k in file_reading_gen(file_name, fields=3, sep='|',
                                        header=True):
            lis.append((i, j, k))

        lis1 = [('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka', 'Software Engineering'),
                ('345', 'Benji Cai', 'Software Engineering')]
        self.assertTrue(lis == lis1)

    def test_file_analyzer(self):
        """This function tests the  file_analyzer"""
        file_name = r"C:\Users\Haritha\PycharmProjects\untitled\test"
        fa = FileAnalyzer(file_name)
        self.assertEqual(fa.files_summary['0_defs_in_this_file.py'], {'class': 0, 'function': 0, 'line': 3, 'char': 57})
        self.assertEqual(fa.files_summary['file1.py'], {'class': 2, 'function': 4, 'line': 25, 'char': 270})


if __name__ == '__main__':
    unittest.main()
