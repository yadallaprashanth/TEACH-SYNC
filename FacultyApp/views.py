from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
import os
import pickle
import pymysql
import os
from django.core.files.storage import FileSystemStorage
from datetime import datetime


global uname

def DownloadAction(request):
    if request.method == 'GET':
        filename = request.GET.get('name', False)
        with open("FacultyApp/static/files/"+filename, "rb") as file:
            content = file.read()
        file.close()
        response = HttpResponse(content,content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename='+filename
        return response

def DownloadMarks(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Faculty Name</th><th><font size="" color="black">Course Name</th>'
        output+='<th><font size="" color="black">Course Year</th><th><font size="" color="black">Result Description</th>'
        output+='<th><font size="" color="black">Marksheet Filename</th><th><font size="" color="black">Upload Date</th><th><font size="" color="black">Download Marksheet</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from marks")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                output+='<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td>'
                output+='<td><font size="" color="black">'+row[4]+'</td><td><font size="" color="black">'+row[5]+'</td>'
                output+='<td><a href=\'DownloadAction?name='+str(row[4])+'\'><font size=3 color=black>Click Here to Download</font></a></td></tr>'
        output+= "</table></br></br></br></br>"        
        context= {'data':output,'view_marks_data': True}
        return render(request, 'StudentScreen.html', context)

def ViewEngagement(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Faculty Name</th><th><font size="" color="black">Engagement Description</th>'
        output+='<th><font size="" color="black">From Date</th><th><font size="" color="black">To Date</th>'
        output+='<th><font size="" color="black">Venue</th><th><font size="" color="black">Place</th>'
        output+='<th><font size="" color="black">State</th><th><font size="" color="black">Engagement Type</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from engagement")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                output+='<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td>'
                output+='<td><font size="" color="black">'+row[4]+'</td><td><font size="" color="black">'+row[5]+'</td>'
                output+='<td><font size="" color="black">'+row[6]+'</td><td><font size="" color="black">'+row[7]+'</td></tr>'
        output+= "</table></br></br></br></br>"        
        context= {'data':output,'view_engagement_data': True,}
        return render(request, 'StudentScreen.html', context)

def ViewPublications(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Faculty Name</th><th><font size="" color="black">Publish Paper Title</th>'
        output+='<th><font size="" color="black">Author List</th><th><font size="" color="black">Journal Name</th>'
        output+='<th><font size="" color="black">Issue No</th><th><font size="" color="black">Total Pages</th>'
        output+='<th><font size="" color="black">Publisher Name</th><th><font size="" color="black">Publisher Date</th><th><font size="" color="black">Indexing</th>'
        output+='<th><font size="" color="black">Doi No</th><th><font size="" color="black">Publisher</th><th><font size="" color="black">Upload Date</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from publication")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                output+='<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td>'
                output+='<td><font size="" color="black">'+row[4]+'</td><td><font size="" color="black">'+row[5]+'</td>'
                output+='<td><font size="" color="black">'+row[6]+'</td><td><font size="" color="black">'+row[7]+'</td>'
                output+='<td><font size="" color="black">'+row[8]+'</td><td><font size="" color="black">'+row[9]+'</td>'
                output+='<td><font size="" color="black">'+row[10]+'</td><td><font size="" color="black">'+row[12]+'</td></tr>'
        output+= "</table></br></br></br></br>"        
        context= {'data':output,'view_publication_data': True,}
        return render(request, 'StudentScreen.html', context)    

def ViewSchedules(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Faculty Name</th><th><font size="" color="black">Subject Name</th>'
        output+='<th><font size="" color="black">Course Name</th><th><font size="" color="black">Year</th>'
        output+='<th><font size="" color="black">Lecture Room</th><th><font size="" color="black">Covering Topic</th>'
        output+='<th><font size="" color="black">Lecture Date</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from schedule")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                output+='<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td>'
                output+='<td><font size="" color="black">'+row[4]+'</td><td><font size="" color="black">'+row[5]+'</td>'
                output+='<td><font size="" color="black">'+row[6]+'</td></tr>'
        output+= "</table></br></br></br></br>"        
        context= {'data':output,'view_lecture_schedules': True}
        return render(request, 'StudentScreen.html', context)  

def Engagement(request):
    if request.method == 'GET':
       return render(request, 'Engagement.html', {})

def EngagementAction(request):
    if request.method == 'POST':
        global uname
        desc = request.POST.get('t1', False)
        from_date = request.POST.get('t2', False)
        to_date = request.POST.get('t3', False)
        venue = request.POST.get('t4', False)
        place = request.POST.get('t5', False)
        state = request.POST.get('t6', False)
        etype = request.POST.get('t7', False)
        status = "Error in adding engagement details"
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO engagement(faculty_name,engagement_desc,from_date,to_date,venue,place,state,engagement_type) VALUES('"+uname+"','"+desc+"','"+from_date+"','"+to_date+"','"+venue+"','"+place+"','"+state+"','"+etype+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        if db_cursor.rowcount == 1:
            status = "Engagement details added to database"
        context= {'data': status,'make_engagement_data':True}
        return render(request, 'Engagement.html', context)    

def UploadMarks(request):
    if request.method == 'GET':
       return render(request, 'UploadMarks.html', {})

def UploadMarksAction(request):
    if request.method == 'POST':
        global uname
        today = str(datetime.now())
        course = request.POST.get('t1', False)
        year = request.POST.get('t2', False)
        desc = request.POST.get('t3', False)
        filename = request.FILES['t4'].name
        myfile = request.FILES['t4'].read()
        status = "Error in adding marksheet details"
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO marks(faculty_name,course,course_year,result_description,sheet_name,upload_date) VALUES('"+uname+"','"+course+"','"+year+"','"+desc+"','"+filename+"','"+today+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        if db_cursor.rowcount == 1:
            status = "Marksheet details added to database"
            if os.path.exists("FacultyApp/static/files/"+filename):
                os.remove("FacultyApp/static/files/"+filename)
            with open("FacultyApp/static/files/"+filename, "wb") as file:
                file.write(myfile)
            file.close()             
        context= {'data': status, 'upload_marks_data':True}
        return render(request, 'UploadMarks.html', context)

def ManagePublications(request):
    if request.method == 'GET':
       return render(request, 'ManagePublications.html', {})

def ManagePublicationsAction(request):
    if request.method == 'POST':
        global uname
        today = str(datetime.now())
        paper_title = request.POST.get('t1', False)
        author_name = request.POST.get('t2', False)
        journal_name = request.POST.get('t3', False)
        issue_no = request.POST.get('t4', False)
        pages = request.POST.get('t5', False)
        publisher_name = request.POST.get('t6', False)
        publish_date = request.POST.get('t7', False)
        indexing = request.POST.get('t8', False)
        doi = request.POST.get('t9', False)
        url = request.POST.get('t10', False)
        filename = request.FILES['t11'].name
        myfile = request.FILES['t11'].read()
        status = "Error in adding publication details"
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO publication(username,paper_title,aurhor_list,journal_name,issue_no,total_pages,publisher_name,publish_date,indexing,doi_no,publish_url,filename,upload_date) VALUES('"+uname+"','"+paper_title+"','"+author_name+"','"+journal_name+"','"+issue_no+"','"+pages+"','"+publisher_name+"','"+publish_date+"','"+indexing+"','"+doi+"','"+url+"','"+filename+"','"+str(today)+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        if db_cursor.rowcount == 1:
            status = "Publication details added to database"
            if os.path.exists("FacultyApp/static/files/"+filename):
                os.remove("FacultyApp/static/files/"+filename)
            with open("FacultyApp/static/files/"+filename, "wb") as file:
                file.write(myfile)
            file.close()             
        context= {'data': status,'manage_publication_data':True}
        return render(request, 'ManagePublications.html', context)

def SubjectsSchedulesAction(request):
    if request.method == 'POST':
        global uname
        subject = request.POST.get('t1', False)
        course = request.POST.get('t2', False)
        year = request.POST.get('t3', False)
        room = request.POST.get('t4', False)
        topic = request.POST.get('t5', False)
        lecture_date = request.POST.get('t6', False)
        status = "Error in adding schedules"
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO schedule(faculty_name,subject,course,course_year,lecture_room,covering_topic,lecture_date) VALUES('"+uname+"','"+subject+"','"+course+"','"+year+"','"+room+"','"+topic+"','"+lecture_date+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            status = "Lecture Schedule saved in database"
        context= {'data': status,'manage_subjects_schedules':True}
        return render(request, 'SubjectsSchedules.html', context)

def SubjectsSchedules(request):
    if request.method == 'GET':
       return render(request, 'SubjectsSchedules.html', {})
    
def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})    

def StudentLogin(request):
    if request.method == 'GET':
       return render(request, 'StudentLogin.html', {})

def AddFaculty(request):
    if request.method == 'GET':
       return render(request, 'AddFaculty.html', {})

def AddStudent(request):
    if request.method == 'GET':
       return render(request, 'AddStudent.html', {})    

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def FacultyLogin(request):
    if request.method == 'GET':
       return render(request, 'FacultyLogin.html', {})

def AdminLoginAction(request):
    if request.method == 'POST':
        global uname
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        if username == 'admin' and password == 'admin':
            context= {'data':'welcome '+username}
            return render(request, 'AdminScreen.html', context)
        else:
            context = {'data': 'Invalid username or password. Please try again.'}
            return render(request, 'AdminLogin.html', context)
        
def FacultyLoginAction(request):
    if request.method == 'POST':
        global uname
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        index = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:    
            cur = con.cursor()
            cur.execute("select username, password FROM faculty")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and password == row[1]:
                    uname = username
                    index = 1
                    break		
        if index == 1:
            context= {'data':'welcome '+username}
            return render(request, 'FacultyScreen.html', context)
        else:
            context= {'data':'Invalid username or password. Please try again.'}
            return render(request, 'FacultyLogin.html', context)        
    
def StudentLoginAction(request):
    if request.method == 'POST':
        global uname
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        index = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:    
            cur = con.cursor()
            cur.execute("select username, password FROM student")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and password == row[1]:
                    uname = username
                    index = 1
                    break		
        if index == 1:
            context= {'data':'welcome '+username}
            return render(request, 'StudentScreen.html', context)
        else:
            context= {'data':'Invalid username or password. Please try again.'}
            return render(request, 'StudentLogin.html', context)



def ViewFaculty(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Faculty Name</th><th><font size="" color="black">Gender</th>'
        output+='<th><font size="" color="black">Contact No</th><th><font size="" color="black">Email ID</th>'
        output+='<th><font size="" color="black">Qualification</th><th><font size="" color="black">Experience</th>'
        output+='<th><font size="" color="black">Teaching Subjects</th>'
        output+='<th><font size="" color="black">Username</th><th><font size="" color="black">Password</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from faculty")
            rows = cur.fetchall()
            faculty_count = len(rows)  # get the count of faculty members
            output+='<tr>'
            for row in rows:
                output+='<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td>'
                output+='<td><font size="" color="black">'+row[4]+'</td><td><font size="" color="black">'+row[5]+'</td>'
                output+='<td><font size="" color="black">'+row[6]+'</td>'
                output+='<td><font size="" color="black">'+row[7]+'</td>'
                output+='<td><font size="" color="black">'+row[8]+'</td></tr>'
            output+= "</table></br></br></br></br>"
            context = {'data': output, 'view_faculty': True}
            return render(request, 'AdminScreen.html', context)

def AddFacultyAction(request):
    if request.method == 'POST':
        faculty = request.POST.get('t1', False)
        gender = request.POST.get('t2', False)
        contact = request.POST.get('t3', False)
        email = request.POST.get('t4', False)
        qualification = request.POST.get('t5', False)
        experience = request.POST.get('t6', False)
        teaching = request.POST.get('t7', False)
        username = request.POST.get('t8', False)
        password = request.POST.get('t9', False)
        status = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:    
            cur = con.cursor()
            cur.execute("select username FROM faculty")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username:
                    status = "Username already exists"
                    break
        if status == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO faculty(faculty_name,gender,contact_no,email,qualification,experience,teaching_subjects,username,password) VALUES('"+faculty+"','"+gender+"','"+contact+"','"+email+"','"+qualification+"','"+experience+"','"+teaching+"','"+username+"','"+password+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                status = "Faculty details added"
        context= {'data': status}
        return render(request, 'AddFaculty.html', context)


def ViewStudent(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th><font size="" color="black">Student Name</th><th><font size="" color="black">Gender</th>'
        output+='<th><font size="" color="black">Contact No</th><th><font size="" color="black">Email ID</th>'
        output+='<th><font size="" color="black">Course Name</th><th><font size="" color="black">Year</th>'
        output+='<th><font size="" color="black">Username</th><th><font size="" color="black">Password</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * from student")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                output+='<td><font size="" color="black">'+row[0]+'</td><td><font size="" color="black">'+str(row[1])+'</td>'
                output+='<td><font size="" color="black">'+row[2]+'</td><td><font size="" color="black">'+row[3]+'</td>'
                output+='<td><font size="" color="black">'+row[4]+'</td><td><font size="" color="black">'+row[5]+'</td>'
                output+='<td><font size="" color="black">'+row[6]+'</td>'
                output+='<td><font size="" color="black">'+row[7]+'</td></tr>'
            output+= "</table></br></br></br></br>"
        context = {'data': output, 'view_student': True}
        return render(request, 'AdminScreen.html', context)

def AddStudentAction(request):
    if request.method == 'POST':
        student = request.POST.get('t1', False)
        gender = request.POST.get('t2', False)
        contact = request.POST.get('t3', False)
        email = request.POST.get('t4', False)
        course = request.POST.get('t5', False)
        year = request.POST.get('t6', False)
        username = request.POST.get('t7', False)
        password = request.POST.get('t8', False)
        status = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
        with con:    
            cur = con.cursor()
            cur.execute("select username FROM student")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username:
                    status = "Username already exists"
                    break
        if status == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'facultyapp',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO student(student_name,gender,contact_no,email,course,course_year,username,password) VALUES('"+student+"','"+gender+"','"+contact+"','"+email+"','"+course+"','"+year+"','"+username+"','"+password+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                status = "Student details added"
        context= {'data': status}
        return render(request, 'AddStudent.html', context)
    


    
