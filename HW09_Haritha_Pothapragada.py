"""This is HW09"""
from collections import defaultdict
import os
from prettytable import PrettyTable
from HW08_Haritha_Pothapragada import file_reading_gen


class Student:
    """This is Student class with a variable to with the Pretty Table fields"""
    PT_FIELD = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives']

    def __init__(self, id, name, dept):
        """This is Student class which stores CWID,Name,Completed Course and a dictionary"""
        self._cwid = id
        self._name = name
        self._dept = dept
        self._course_dict = defaultdict(str)

    def set_grades(self, course, grade):
        """setting the _course_dict with {course: grade}"""
        self._course_dict[course] = grade

    def get_student(self):
        """returns cwid,name,_course_dict.keys (sorted)"""
        return [self._cwid, self._name, self._dept, self._course_dict]


class Instructor:
    """This is Instructor class with a variable to with the Pretty Table fields"""
    PT_FIELD = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, id, name, dept):
        """This initializes the cwid,name,dept and a default dict(int) of the instructor"""
        self._cwid = id
        self._name = name
        self._dept = dept
        self._student_dict = defaultdict(int)

    def set_students(self, course):
        """increments the count of the student associated with the grade """
        self._student_dict[course] += 1

    def get_instructor(self):
        """returns cwid,name,dept and _student_dict"""
        for key, value in self._student_dict.items():
            yield ([self._cwid, self._name, self._dept, key, value])


class Major:
    """This is Major class with a variable to with the Pretty Table fields and the passing grades"""
    PASSING_GRADES = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}
    PT_FIELD = ['Dept', 'Required', 'Electives']

    def __init__(self, major):
        """This initializes the major and two sets for required courses and elective courses """
        self._major = major
        self._required = set()
        self._elective = set()

    def add_course(self, flag, course):
        """This populates the two sets"""
        if flag.upper() == 'R':
            self._required.add(course)
        elif flag.upper() == 'E':
            self._elective.add(course)
        else:
            raise ValueError(f"unexpected flag '{flag}' encountered in major.txt")

    def major_pt(self):
        """this returns the values required of the major pretty table"""
        return [self._major, sorted(self._required), sorted(self._elective)]

    def course_details(self, course_dict):
        """this gives completed ,required and elective courses for the student pretty table"""
        completed = {course for course, grade in course_dict.items() if grade in Major.PASSING_GRADES}
        required = self._required - completed
        if self._elective.intersection(completed):
            electives = None
        else:
            electives = self._elective

        return [sorted(list(completed)), required, electives]


class Repository:
    """This the Repository class"""

    def __init__(self, dir_path, ptable=False):
        """This initializes the student dict , instructor dict and opens these three files"""
        self._students = {}
        self._instructors = {}
        self._major = {}
        self._get_students(os.path.join(dir_path, "students.txt"))
        self._get_instructors(os.path.join(dir_path, "instructors.txt"))
        self._get_grades(os.path.join(dir_path, "grades.txt"))
        self._get_major(os.path.join(dir_path, "majors.txt"))
        if ptable:
            print("Majors Summary")
            self.major_prettytable()
            print("Students Summary")
            self.student_prettytable()
            print("Instructors Summary")
            self.instructor_prettytable()

    def _get_students(self, path):
        """this function reads the students.txt file and stores it in a dict{cwid:Student}"""
        try:
            for cwid, name, major in file_reading_gen(path, 3, sep=';', header=True):
                self._students[cwid] = Student(cwid, name, major)
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

    def _get_instructors(self, path):
        """this function reads the instructors.txt file and stores it in a dict{cwid:Instructor}"""
        try:
            for cwid, name, major in file_reading_gen(path, 3, sep='|', header=True):
                self._instructors[cwid] = Instructor(cwid, name, major)
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

    def _get_grades(self, path):
        """This function reads the grade.txt and adds the items in the Student and the Instructor instance"""
        try:
            for student_cwid, course, grade, instructor_cwid in file_reading_gen(path, 4, sep='|', header=True):
                if student_cwid in self._students:
                    self._students[student_cwid].set_grades(course, grade)
                else:
                    print(f"Found grade for an unknown student {student_cwid}")
                if instructor_cwid in self._instructors:
                    self._instructors[instructor_cwid].set_students(course)
                else:
                    print(f"Found grade for unknown instructor")
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)

    def _get_major(self, path):
        """This function reads the majors.txt and adds the items in the Major instance"""
        try:
            for dept, flag, course in file_reading_gen(path, 3, sep='\t', header=False):
                if dept not in self._major:
                    self._major[dept] = Major(dept)
                self._major[dept].add_course(flag, course)
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

    def major_prettytable(self):
        """prints the major pretty table"""
        pt_major = PrettyTable(Major.PT_FIELD)
        for i in self._major.keys():
            pt_major.add_row(self._major[i].major_pt())
        print(pt_major)

    def student_prettytable(self):
        """prints the student pretty table"""
        pt_student = PrettyTable(Student.PT_FIELD)
        for key in self._students:
            cwid, name, dept, course_dict = self._students[key].get_student()
            try:
                completed, required, electives = (self._major[dept].course_details(course_dict))
            except KeyError:
                print(f"KeyError no such major found in major.txt {dept}")
                return
            pt_student.add_row([cwid, name, dept, completed, required, electives])
        print(pt_student)

    def instructor_prettytable(self):
        """prints the instructor pretty table"""
        pt_instructor = PrettyTable(Instructor.PT_FIELD)
        for key in self._instructors:
            for i in self._instructors[key].get_instructor():
                pt_instructor.add_row(i)
        print(pt_instructor)


if __name__ == '__main__':
    """main function to create instance"""
    REPO = Repository(r'C:\SSW810\Repository', ptable=True)
    # test = Repository(r'C:\SSW810\Stevens_test')
