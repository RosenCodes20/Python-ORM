from datetime import date

from django.db import models

from main_app.choices import GradeChoice, CarChoices


class Lecturer(models.Model):
    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(
        max_length=100
    )

    code = models.CharField(
        max_length=10
    )

    lecturer = models.ForeignKey(
        to=Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    student_id = models.CharField(
        max_length=10,
        primary_key=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    birth_date = models.DateField()

    email = models.EmailField(
        unique=True
    )

    subjects = models.ManyToManyField(Subject, through="StudentEnrollment")


class StudentEnrollment(models.Model):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE
    )

    enrollment_date = models.DateField(
        default=date.today
    )

    grade = models.CharField(
        max_length=1,
        choices=GradeChoice,
    )


class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(
        Lecturer,
        on_delete=models.CASCADE
    )

    email = models.EmailField(
        unique=True
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    office_location = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


class Car(models.Model):
    engine = models.CharField(
        max_length=50
    )

    brand = models.CharField(
        max_length=100,
        choices=CarChoices.choices
    )

    employee = models.ManyToManyField(
        "Employee",
        through="EmployeeCar"
    )


class EmployeeCar(models.Model):
    employee = models.ForeignKey(
        to="Employee",
        on_delete=models.CASCADE
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    employee_age = models.PositiveIntegerField(null=True, blank=True)
    car_made_date = models.DateField(null=True, blank=True)


class Employee(models.Model):
    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    birth_date = models.DateField()


class Country(models.Model):

    name = models.CharField(
        max_length=100
    )

    capital = models.CharField(
        max_length=50
    )

    highest_populated_town = models.CharField(
        max_length=50
    )


class City(models.Model):

    name = models.CharField(
        max_length=100
    )

    population = models.IntegerField()

    restaurants = models.PositiveIntegerField(
        default=5
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )