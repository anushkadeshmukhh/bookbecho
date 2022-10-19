from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import mysql.connector
from django.urls import reverse
from django.shortcuts import redirect
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="bookio"
    )
def mysql():


    mycursor = mydb.cursor()
    #mycursor.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255),username varchar(10) primary key,email varchar(20),phone_no varchar(10),password varchar(8))")
    #mycursor.execute("CREATE TABLE book (name VARCHAR(255),book_id varchar(15) primary key,publication varchar(50),author varchar(20),conditions varchar(10),mrp int,selling_price int)")
    #mycursor.execute("CREATE TABLE users ()")
mysql()


def index1(request):
    #return HttpResponse("Hello world!")
    context = {
        'greeting': 0   
    }
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def check_user(request):
    template = loader.get_template('myfirst.html')
    a = request.POST['username']
    e = request.POST['psw']
    aa=tp(a,e)
    #print(aa)
    context = {
        'greeting' : aa,
        'name':a
    }
    #return render(request, 'myfirst.html', context)
    return HttpResponse(template.render(context,request))


def add_user(request):
    template = loader.get_template('myfirst.html')
    a = request.POST['username']
    b = request.POST['name']
    c = request.POST['email']
    d = request.POST['phone']
    e = request.POST['psw']
    f = request.POST['address']
    insert_user=mydb.cursor()
    sql = "INSERT INTO users (name, address,username,email,phone_no,password) VALUES (%s,%s,%s,%s,%s,%s)"
    val=(b,f,a,c,d,e)
    insert_user.execute(sql,val)
    mydb.commit()
    context = {
        'greeting': 1,
        'name' :a   
    }
    #return HttpResponseRedirect(reverse('books/index'))
    return HttpResponse(template.render(context,request))



def tp(a,e):
    tp=mydb.cursor()
    tp1="SELECT username FROM users WHERE username = %s"
    us_nm=(a,)
    tp.execute(tp1,us_nm)
    myresult = tp.fetchall()
    #print(myresult)
    if len(myresult)==0:
        return 0
    else:
        tp1="SELECT password FROM users WHERE username = %s"
        us_nm=(a,)
        tp.execute(tp1,us_nm)
        myresult = tp.fetchall()
        #print(myresult,e)
        if myresult[0][0]==e:
            return 1
        else:
            return 0

