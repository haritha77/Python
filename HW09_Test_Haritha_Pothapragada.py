"""This is the test file for HW09"""
import sqlite3
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
        result = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']],
                  ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]
        self.assertEqual(lis, result)

    def test_correct_student(self):
        """This is used to test the student pretty table values """
        lis = []
        repo = Repository(r'C:\SSW810\Repository')
        for key in repo._students:
            cwid, name, dept, course_dict = repo._students[key].get_student()
            completed, required, electives = (repo._major[dept].course_details(course_dict))
            lis.append([cwid, name, dept, completed, required, electives])
        result = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], {'SSW 555', 'SSW 540'}, None],
                  ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], {'SSW 555', 'SSW 540'}, {'CS 501', 'CS 546'}],
                  ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 501', 'CS 546'}],
                  ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], None, None],
                  ['11717', 'Kernighan, B', 'CS', [], {'CS 570', 'CS 546'}, {'SSW 810', 'SSW 565'}]]
        self.assertEqual(lis, result)

    def test_correct_instructor(self):
        """this is used to test teh instructor pretty table"""
        lis_instructor = []
        repo = Repository(r'C:\SSW810\Repository')
        for key in repo._instructors:
            for i in repo._instructors[key].get_instructor():
                lis_instructor.append(i)
        res = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1],
               ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4],
               ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1],
               ['98762', 'Hawking, S', 'CS', 'CS 501', 1],
               ['98762', 'Hawking, S', 'CS', 'CS 546', 1],
               ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]
        self.assertEqual(lis_instructor, res)

    def test_instructor_table_db(self):
        lis = list()
        db = sqlite3.connect(r"C:\SSW810\Repository\repo.db")
        query = """select instr.CWID,instr.Name,instr.Dept,grade.Course,count(grade.StudentCWID) as no_of_stud
                         from HW11_instructors instr
                         join HW11_grades grade on instr.CWID=grade.InstructorCWID
                         group by grade.Course,grade.InstructorCWID;"""
        for row in db.execute(query):
            lis.append(row)
        res = [('98762', 'Hawking, S', 'CS', 'CS 501', 1), ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
               ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1), ('98762', 'Hawking, S', 'CS', 'CS 570', 1),
               ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1), ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4)]
        db.close()
        self.assertEqual(res, lis)


if __name__ == '__main__':
    unittest.main()
