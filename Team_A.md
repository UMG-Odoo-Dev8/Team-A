<div align="center">
  <h1> School Management System User's Manual</h1>
 
  <sub>Group Members: Zaw Thu Htet, May Phyo Thu
  <br>
  <small> 21, July, 2021</small>
  </sub>
</div>

## Table of Contents
- [Project Overview](#project-overview)
- [Custom Module Installation](#custom-module-installation)
- [Operation](#operation)
    - [Create Courses](#create-courses)
    - [Create Data](#create-data)
    - [Add Data into Sections](#add-data-into-sections)
    - [Create Attendance](#create-attendance)
    - [Request Leave](#request-leave)
    - [View Roll call Percentage](#view-roll-call-percentage)
    - [Create Exam Questions](#create-exam-questions)
    - [Test Exam and Generate Result](#test-exam-and-generate-result)

## Projcet Overview
School management system is very convenient for checking students' roll-call percentage and also useful  for saving attendance records for each student and for testing exams.<br>
    Functions of the system:
- Manage attendance
- Test Exam


## Custom Module Installation
To run this system you need to install our custom module in odoo version 15. By clicking install button you can easily access this system.

![installation](./images/install.png)

## Operation

### Create Courses
Firstly, go to ***Course*** menu and create new course by clicking create button.
![create courses](./images/course.png)

 In this form view, you can add totoal chapters of related course and can define course start-date and end-date.
![create courses](./images/course_create.png)

### Create Data
Click ***Profile*** menu and create new data like studens' info and teachers'info.

![create data](./images/new_profile.png)

Choose role (teacher head,teacher or student), fill required informations and save by clicking save button.<br>

Create new Student
![create data](./images/new_student.png)
Create new Teacher
![create data](./images/new_teacher.png)
Create new Teacher Head
![create data](./images/new_t_head.png)

Can see same role in a collection by chosing this options
![create data](./images/searchc_panel.png)


### Add Data into Sections
After creating needed data, you can add these data into sections. A section can have one teacher head, many teachers and many students. You need to define students' roll numbers and keep in mind to define like A1(Section A's roll-1), A2, B1(Section B's roll-1),B2 

![section](./images/section.png)
![section](./images/section_A.png)


### Create Attendance
Click on ***Attendance*** menuitem and create new attendance record for each student
![attendance](./images/attendance.png)

Need to add today's month. After adding check-in,check-out time, attendance hours and roll-call point(roll-call percent) of that day will be automatically caculated.
![attendance](./images/attendance_create.png)

### Request Leave
To request leave go to ***Leave*** menuitem. 
![leave](./images/leave.png)

Add month name you want to leave. Can choose leave type,can define wanted durations by  selecting start date and end date.
![leave](./images/leave_create.png)


### View Roll call Percentage
To See roll call percentage of each student, go to ***Total Percent*** menu. 
![total percent](./images/total_percent.png)

By selecting student's name and by inserting the name of month you want to view ,can see that student's attendance record and roll call percent
![total percent](./images/total_pecent_view.png)

### Create Exam Questions
Go to ***Quizz***  menu and write questions and define correct answers. Can also define scores for each questions and can hide some questions that do not want to show in exam form view by removing check mark  in the active column .

![quizz](./images/quizz.png)
![quizz](./images/quizz_create.png)

### Test Exam and Generate Result
To answer exam questions go to ***Exam*** menu. Choose course name and student whose roll-call precentage is at least 80%.
![exam](./images/exam.jpg)

After selecting course, you can answer questions. And then, click submit button to see your result.
![exam](./images/exam_submit.jpg)