import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Student, Group, Teacher, Subject, Grade
from database_config import url_to_db
from pprint import pprint
from colorama import init, Fore

# Initialize colorama for colored terminal output
init(autoreset=True)

# Initialize Faker for generating fake data
fake = Faker()

# Database connection setup
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)

# Constants for data generation
NUM_GROUPS = 3
NUM_TEACHERS = 5
NUM_SUBJECTS = 8
NUM_STUDENTS = 50
MAX_GRADES_PER_STUDENT = 20

def clear_existing_data(session):
    """Clear all existing data from the database."""
    for model in [Grade, Student, Subject, Teacher, Group]:
        session.query(model).delete()
    session.commit()

def create_groups(session):
    """Create groups in the database."""
    groups = [Group(name=f"Group {i + 1}") for i in range(NUM_GROUPS)]
    session.add_all(groups)
    session.commit()
    print(Fore.GREEN + f"Groups: {', '.join([group.name for group in groups])} successfully added!")
    return groups

def create_teachers(session):
    """Create teachers in the database."""
    teachers = [Teacher(name=fake.name()) for _ in range(NUM_TEACHERS)]
    session.add_all(teachers)
    session.commit()
    print(Fore.GREEN + f"Teachers: {', '.join([teacher.name for teacher in teachers])} successfully added!")
    return teachers

def create_subjects(session, teachers):
    """Create subjects and assign them to teachers."""
    subjects = [
        Subject(name=fake.word().capitalize(), teacher=random.choice(teachers))
        for _ in range(NUM_SUBJECTS)
    ]
    session.add_all(subjects)
    session.commit()
    print(Fore.GREEN + f"Subjects: {', '.join([subject.name for subject in subjects])} successfully added!")
    return subjects

def create_students(session, groups):
    """Create students and assign them to groups."""
    students = [
        Student(name=fake.name(), group=random.choice(groups))
        for _ in range(NUM_STUDENTS)
    ]
    session.add_all(students)
    session.commit()
    
    print(Fore.GREEN + "Students:")
    pprint([student.name for student in students])
    
    return students

def create_grades(session, students, subjects):
    """Create grades for students and assign them to subjects."""
    grades = []
    
    for student in students:
        for _ in range(random.randint(1, MAX_GRADES_PER_STUDENT)):
            grade = Grade(
                student=student,  # Reference to Student object
                subject=random.choice(subjects),  # Reference to Subject object
                score=random.randint(1, 100),  # Generate a random score between 1 and 100
                date_received=fake.date_between(start_date="-2y", end_date="today"),
            )
            grades.append(grade)

    session.add_all(grades)
    session.commit()
    
    print(Fore.GREEN + "Grades for students successfully added!")

def seed_data():
    """Main function to seed the database with initial data."""
    session = Session()
    
    try:
        # Clear existing data from the database
        clear_existing_data(session)
        
        # Create and add groups, teachers, subjects, students, and grades
        groups = create_groups(session)
        teachers = create_teachers(session)
        subjects = create_subjects(session, teachers)
        students = create_students(session, groups)
        create_grades(session, students, subjects)

        print(Fore.CYAN + "Data successfully added to the database!")

    except Exception as e:
        # Rollback any changes if an error occurs
        session.rollback()
        print(Fore.RED + f"Error while seeding the database: {e}")
    
    finally:
        # Close the database session
        session.close()

if __name__ == "__main__":
    seed_data()