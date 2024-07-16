import random

from sqlalchemy.orm import sessionmaker

from models import engine, Employee, City

Session = sessionmaker(bind=engine)

with Session() as session:
    employee = session.query(Employee).filter_by(first_name="Koko").first()

    if employee:
        employee.city_id = 3

        session.commit()
        print(f"Successfully upgraded {employee.first_name}'s city to {employee.city.city}!")

    else:
        print("Can't find that employee! Sorry :(")