"""This is the test file for HW09"""
import unittest
from HW09_Haritha_Pothapragada import Repository


class TestModule(unittest.TestCase):
    """This is a test class """

    def test_major_prettytable(self):
        """This is used to test the major pretty table values """
        lis = []
        repo = Repository(r'C:\SSW810\Repository')
        for i in repo._major.keys():
            lis.append(repo._major[i].major_pt())
        result = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],
                   ['CS 501', 'CS 513', 'CS 545']],
                  ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'],
                   ['SSW 540', 'SSW 565', 'SSW 810']]]
        self.assertEqual(lis, result)

    def test_correct_student(self):
        """This is used to test the student pretty table values """
        lis = []
        repo = Repository(r'C:\SSW810\Repository')
        for key in repo._students:
            cwid, name, dept, course_dict = repo._students[key].get_student()
            completed, required, electives = (repo._major[dept].course_details(course_dict))
            lis.append([cwid, name, dept, completed, required, electives])
        result = [
            ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'],
             {'SSW 540', 'SSW 555'}, None],
            ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'],
             {'SSW 540', 'SSW 555'}, None],
            ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], {'SSW 564', 'SSW 540'},
             {'CS 501', 'CS 513', 'CS 545'}],
            ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'],
             {'SSW 540', 'SSW 555'},{'CS 501', 'CS 513', 'CS 545'}],
            ['10183', 'Chapman, O', 'SFEN', ['SSW 689'],
             {'SSW 567', 'SSW 564', 'SSW 540', 'SSW 555'},
             {'CS 501', 'CS 513', 'CS 545'}],
            ['11399', 'Cordova, I', 'SYEN', ['SSW 540'],
             {'SYS 671', 'SYS 800', 'SYS 612'}, None],
            ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 671', 'SYS 612'},
             {'SSW 565', 'SSW 540', 'SSW 810'}],
            ['11658', 'Kelly, P', 'SYEN', [],
             {'SYS 671', 'SYS 800', 'SYS 612'}, {'SSW 565', 'SSW 540', 'SSW 810'}],
            ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'],
             {'SYS 671', 'SYS 800', 'SYS 612'},
             {'SSW 565', 'SSW 540', 'SSW 810'}],
            ['11788', 'Fuller, E', 'SYEN',
             ['SSW 540'],
             {'SYS 671', 'SYS 800', 'SYS 612'}, None]]
        self.assertEqual(lis, result)

    def test_correct_instructor(self):
        """this is used to test teh instructor pretty table"""
        lis_instructor = []
        repo = Repository(r'C:\SSW810\Repository')
        for key in repo._instructors:
            for i in repo._instructors[key].get_instructor():
                lis_instructor.append(i)

        res = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],
               ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
               ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
               ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
               ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
               ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
               ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
               ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
               ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
               ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
               ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
               ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        self.assertEqual(lis_instructor, res)


if __name__ == '__main__':
    unittest.main()
