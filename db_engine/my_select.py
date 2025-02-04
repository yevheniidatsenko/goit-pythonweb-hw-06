from sqlalchemy.orm import aliased, sessionmaker
from sqlalchemy import create_engine, func
from models import Student, Group, Teacher, Subject, Grade
from database_config import url_to_db
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# Set up the session
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
session = Session()

# Function to round results
def round_results(results):
    if isinstance(results, tuple):
        return tuple(
            round(value, 2) if isinstance(value, float) else value for value in results
        )
    elif isinstance(results, list):
        return [round_results(result) for result in results]
    return results

# 1. Find the top 5 students with the highest average grade across all subjects
def select_top_students():
    result = (
        session.query(Student.name, func.avg(Grade.score).label("average_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(func.avg(Grade.score).desc())
        .limit(5)
        .all()
    )
    return round_results(result)

# 2. Find the student with the highest average grade in a specific subject
def select_highest_student_in_subject(subject_name):
    query = (
        session.query(Student.name, func.avg(Grade.score).label("average_grade"))
        .join(Grade)
        .join(Subject)
        .filter(func.lower(Subject.name) == subject_name.lower())  # Case-insensitive comparison
        .group_by(Student.id)
        .order_by(func.avg(Grade.score).desc())
    )
    result = query.first()
    return round_results([result])[0] if result else ("No student found", None)

# 3. Find the average grade in groups for a specific subject
def select_average_grade_by_group(subject_name):
    SubjectAlias = aliased(Subject)
    result = (
        session.query(Group.name, func.avg(Grade.score).label("average_grade"))
        .select_from(Group)
        .join(Student)
        .join(Grade, Grade.student_id == Student.id)
        .join(SubjectAlias, SubjectAlias.id == Grade.subject_id)
        .filter(func.lower(SubjectAlias.name) == subject_name.lower())  # Case-insensitive comparison
        .group_by(Group.name)
        .all()
    )
    return round_results(result)

# 4. Find the overall average grade (across all grades)
def select_overall_average_grade():
    result = session.query(func.avg(Grade.score).label("average_grade")).scalar()
    return round(result, 2) if result is not None else "No grades available"

# 5. Find the courses taught by a specific teacher
def select_courses_by_teacher(teacher_name):
    result = (
        session.query(Subject.name)
        .join(Teacher)
        .filter(func.lower(Teacher.name) == teacher_name.lower())  # Case-insensitive comparison
    )
    return result.all() if result else [("No courses found",)]

# 6. Find the list of students in a specific group
def select_students_in_group(group_name):
    result = (
        session.query(Student.name)
        .join(Group)
        .filter(func.lower(Group.name) == group_name.lower())  # Case-insensitive comparison
    )
    return result.all() if result else [("No students found",)]

# 7. Find grades of students in a specific group for a specific subject
def select_grades_in_group_for_subject(group_name, subject_name):
    result = (
        session.query(Student.name, Grade.score)
        .join(Group)
        .join(Grade)
        .join(Subject)
        .filter(
            func.lower(Group.name) == group_name.lower(),
            func.lower(Subject.name) == subject_name.lower(),
        )  # Case-insensitive comparison
    )
    return result.all() if result else [("No grades found",)]

# Function to print query results with colors
def print_query_result(query_result, title):
    print(Fore.CYAN + Style.BRIGHT + title)
    if query_result:
        for row in query_result:
            print(Fore.GREEN + str(row))
    else:
        print(Fore.RED + "No results found.")
    print(Fore.WHITE + "-" * 50)

if __name__ == "__main__":
    
   ## Example calls to functions and printing results
   
   # Example usage of each function with potential data.
   print_query_result(select_top_students(), "1. Top 5 Students with Highest Average Grades:")
   
   print_query_result(
         [select_highest_student_in_subject("Cup")],  
         "2. Student with Highest Average Grade in 'Cup':",
     )
    
   print_query_result(
         select_average_grade_by_group("Police"),  
         "3. Average Grades by Group for 'Police':",
     )
     
   print_query_result(
         [select_overall_average_grade()],  
         "4. Overall Average Grade Across All Grades:",
     )
     
   print_query_result(
         select_courses_by_teacher("Mr. Joseph Meyer"),  
         "5. Courses Taught by 'Mr. Joseph Meyer':",
     )
     
   print_query_result(
         select_students_in_group("Group 1"),  
         "6. List of Students in 'Group 1':",
     )
     
   print_query_result(
         select_grades_in_group_for_subject("Group 2", "Consider"),  
         "7. Grades of Students in 'Group 2' for 'Consider':",
     )

   print_query_result(
         select_grades_in_group_for_subject("Group 3", "Police"),  
         "8. Grades of Students in 'Group 3' for 'Police':",
     )

   print_query_result(
         select_courses_by_teacher("Prof. Johnson"),  
         "9. Courses Taught by 'Prof. Johnson':",
     )

   print_query_result(
         select_students_in_group("Group 3"),  
         "10. List of Students in 'Group 3':",
     )