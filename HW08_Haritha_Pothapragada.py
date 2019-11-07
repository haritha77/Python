""" HW08 implementation file"""
import datetime
import os
from collections import defaultdict
from prettytable import PrettyTable


def date_arithmetic():
    """ this function date_arithmetic uses Python’s datetime module"""
    dt1 = datetime.datetime.strptime('Feb 27, 2000', "%b %d, %Y")
    dt2 = datetime.datetime.strptime('Feb 27, 2017', "%b %d, %Y")
    dt3 = datetime.datetime.strptime('Jan 1, 2017', "%b %d, %Y")
    dt4 = datetime.datetime.strptime('Oct 31, 2017', "%b %d, %Y")
    three_days_after_02272000 = dt1 + datetime.timedelta(days=3)  # your code goes here for calculation
    three_days_after_02272017 = dt2 + datetime.timedelta(days=3)  # your code goes here for calculation
    days_passed_01012017_10312017 = dt4 - dt3  # your code goes here for calculation
    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017


def file_reading_gen(path, fields, sep=',', header=False):
    """ Reading text files with a fixed number of fields, separated by a pre-defined character"""
    try:
        fp = open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Cant open file {path}")
    else:
        with fp:
            for line_no, line in enumerate(fp):
                lin = line.strip('\n').split(sep)
                if len(lin) == fields:
                    if header:
                        header = False
                        continue
                    yield (l for l in lin)
                else:
                    raise ValueError(f'{path} has {len(lin)} fields on line {line_no + 1} but expected {fields} ')


class FileAnalyzer:
    """ summarizing the Python files in a directory"""

    def __init__(self, directory):
        """ initialises the directory and the file summary variables """
        self.directory = directory  # NOT mandatory!
        self.files_summary = dict()

        self.analyze_files()

    def analyze_files(self):
        """ a method that populate the summarized data into self.files_summary"""
        try:
            os.chdir(self.directory)
        except FileNotFoundError:
            raise FileNotFoundError("No such Directory or cant open it ")
        files = os.listdir('.')
        for i in files:
            is_a_py = (i.endswith(".py"))
            if is_a_py:
                self.files_summary[i] = {}
                try:
                    fp = open(os.path.join(os.getcwd(), i))
                except FileNotFoundError:
                    raise FileNotFoundError(f"Cant open file {i}")
                else:
                    with fp:
                        def_count = 0
                        class_count = 0
                        line_count = 0
                        char_count = 0
                        for line in fp:
                            line_count += 1
                            char_count += len(line)
                            li = line.strip('').strip('/n').split()
                            if len(li) == 0:
                                continue
                            if li[0] == "def":
                                def_count += 1
                            elif li[0] == "class":
                                class_count += 1
                        self.files_summary[i]['class'] = class_count
                        self.files_summary[i]['function'] = def_count
                        self.files_summary[i]['line'] = line_count
                        self.files_summary[i]['char'] = char_count

    def pretty_print(self):
        """  a method that print out the pretty table from the data stored in the self.files_summary"""
        print(f"Summary of {os.getcwd()}")
        pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])
        for key, value in self.files_summary.items():
            file = os.path.join(os.getcwd(), key)
            pt.add_row([file, value['class'], value['function'], value['line'], value['char']])

        print(pt)


if __name__ == '__main__':
    file_name = r"C:\Users\Haritha\PycharmProjects\untitled\test"
    fa = FileAnalyzer(file_name)
    fa.pretty_print()
