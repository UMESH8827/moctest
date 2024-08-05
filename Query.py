CREATE DATABASE STUDENT
USE STUDENT
#student first table
#create first table
create table studentdetails
(
    student_id int unsigned,
    name varchar(100),
    Age varchar(100),
    major varchar(100)
)
#insert into date in table
insert into studentdetails
(student_id,name,Age,major)
values
(1,"Umesh","22",1)

#create second table
CREATE DATABASE Courses
USE Courses
create table coursesdetail
(
    course_id int unsinged,
    course_name varchar(100),
    credits int(100)
)

insert into coursesdetail
(course_id,course_name,credits)
values
(1,"Mearnstack",2),
(2,"Python",1)

# create third table Enrollments 
create database Enrollments
use Enrollments
CREATE TABLE enrollmentsdeatails
(
    EnrollmentID int unsigned,
    StudentID int unique,
    CourseID int unique,
    Grade varchar(100)
    
)

INSERT INTO enrollmentsdeatails
(EnrollmentID,StudentID,CourseID,Grade)
Values
(1,12,4,"A"),
(2,15,2,"B"),
(3,13,5,"A+")















