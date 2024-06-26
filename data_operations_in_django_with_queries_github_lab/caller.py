import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student


def add_students():
    student = Student(
        student_id="FC5204",
        first_name="John",
        last_name="Doe",
        birth_date="1995-05-15",
        email="john.doe@university.com"
    )

    student.save()

    Student.objects.create(
        student_id="FE0054",
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@university.com",
    )

    student = Student()

    student.student_id = "FH2014"

    student.first_name = "Alice"

    student.last_name = "Johnson"

    student.birth_date = "1998-02-10"

    student.email = "alice.johnson@university.com"

    student.save()

    Student.objects.create(
        student_id="FH2015",
        first_name="Bob",
        last_name="Wilson",
        birth_date="1996-11-25",
        email="bob.wilson@university.com"
    )

    return "Added 4 students!"


def get_students_info():
    all_student = Student.objects.all()
    result = []
    for student in all_student:
        result.append(f"Student №{student.student_id}: {student.first_name} {student.last_name}; "
                      f"Email: {student.email}")

    return "\n".join(map(str, result))


def update_students_emails():
    all_students = Student.objects.all()

    for students in all_students:
        students.email = students.email.replace(students.email.split("@")[1], "uni-students.com")
        students.save()


def truncate_students():
    all_students = Student.objects.all()

    for student in all_students:
        student.delete()


truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")


