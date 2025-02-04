# Student Management System

This project implements a Student Management System using PostgreSQL as the database backend. The system is designed to manage data related to students, groups, teachers, subjects, and grades. It includes functionality for seeding the database with initial data and querying it to retrieve useful information.

## Homework Description

The task involves creating a database schema that includes:

- A table for **Students**
- A table for **Groups**
- A table for **Teachers**
- A table for **Subjects** (with an indication of the teacher who teaches each subject)
- A table for **Grades** (where each student has grades for subjects along with the date when the grade was received)

### Steps to Complete the Task

1. **Implement SQLAlchemy Models**: Create models for each of the tables mentioned above.
2. **Use Alembic**: Set up database migrations to apply changes to the database schema.
3. **Data Seeding**: Write a `seed.py` script to populate the database with random data using Faker, including approximately 30-50 students, 3 groups, 5-8 subjects, 3-5 teachers, and up to 20 grades per student.
4. **Querying Data**: Implement a `my_select.py` script with functions to perform various queries on the database.

### Query Examples

- Find the top 5 students with the highest average grades.
- Retrieve the average grade in groups for specific subjects.
- List courses taught by a specific teacher.

## Results

### Docker

![Docker Running](/screenshots/SCR_1.png)

### Alembic

![Alembic Migration](/screenshots/SCR_2.png)

### Database in pgAdmin

![Database Structure in pgAdmin](/screenshots/SCR_3.png)

### Seeding Data with seed.py

![Seed Data Output](/screenshots/SCR_4.png)

### Query Results from my_select.py

![Query Results](/screenshots/SCR_5.png)
![Query Results](/screenshots/SCR_6.png)
