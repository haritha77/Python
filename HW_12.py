import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/instructors")
def instructor():
    dbpath = r"C:\SSW810\Repository\repo.db"
    try:
        db = sqlite3.connect(dbpath)
    except sqlite3.OperationalError:
        return f"Unable to connect to the db {dbpath}"
    else:
        query = """select instr.CWID,instr.Name,instr.Dept,grade.Course,count(grade.StudentCWID) as no_of_stud
                         from HW11_instructors instr
                         join HW11_grades grade on instr.CWID=grade.InstructorCWID
                         group by grade.Course,grade.InstructorCWID;"""
        data = [{'cwid': CWID, 'name': Name, 'dept': Department, 'course': Course, 'student_cnt': stu_cnt}
                for CWID, Name, Department, Course, stu_cnt in db.execute(query)]
        db.close()
        return render_template(
            'instructors.html',
            title='Stevens Repository',
            table_title="Courses and student counts",
            instructors=data
        )


app.run(debug=False)
