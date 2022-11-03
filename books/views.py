from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import mysql.connector
from django.urls import reverse
from django.shortcuts import redirect
users=""
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bookio"
        )
    mydb1 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bookio"
        )
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
def mysql():


    mycursor = mydb.cursor()
    #mycursor.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255),username varchar(10) primary key,email varchar(20),phone_no varchar(10),password varchar(8))")
    #mycursor.execute("CREATE TABLE book (name VARCHAR(255),book_id varchar(15) primary key,publication varchar(50),author varchar(20),conditions varchar(10),mrp int,selling_price int,year varchar(50),branch varchar(50))")
    #mycursor.execute("CREATE TABLE buyers (buyer_name VARCHAR(255),book_name varchar(255),price int)");
    #mycursor.execute("CREATE TABLE sellers (seller_name VARCHAR(255),book_name varchar(255),b_id varchar(15) primary key,publication varchar(50),author varchar(20),conditions varchar(10),mrp int,selling_price int)")
    #mycursor.execute("create procedure id_count(out i int) begin declare c int default 0; select count(*) from book into c; set i=c+1; end;")
    #mycursor.execute("insert into book (name, branch,year,book_id,publication,author,conditions,mrp,selling_price) values('CNS','CS','3',1,'Pearson','Kurose','Excellent',500,250)")
    #mycursor.execute("insert into book (name, branch,year,book_id,publication,author,conditions,mrp,selling_price) values('DBMS','CS','3',2,'Thomas','Sudarshan','Good',500,250)")
    #mycursor.execute("insert into book (name, branch,year,book_id,publication,author,conditions,mrp,selling_price) values('EXE','ENTC','3',3,'Pearson','Kurose','Excellent',500,250)")
    #mycursor.execute("insert into book (name, branch,year,book_id,publication,author,conditions,mrp,selling_price) values('ECE','ENTC','2',4,'Thomas','Sudarshan','Excellent',500,250)")
    #mycursor.execute("insert into book (name, branch,year,book_id,publication,author,conditions,mrp,selling_price) values('CG','IT','3',5,'Pearson','Kurose','Excellent',500,250)")
    #mycursor.execute("insert into book (name, branch,year,book_id,publication,author,conditions,mrp,selling_price) values('OS','IT','2',6,'Thomas','Sudarshan','Good',500,250)")
    #mycursor.execute("insert into book (name, branch,year,book_id,publication,author,conditions,mrp,selling_price) values('Chemistry','FE','1',7,'Pearson','Kurose','Excellent',500,250)")
    #mycursor.execute("insert into book (name, branch,year,book_id,publication,author,conditions,mrp,selling_price) values('Physics','FE','1',8,'Thomas','Sudarshan','Good',500,250)")
    mydb.commit()
mysql()


def index1(request):
    #return HttpResponse("Hello world!")
    context = {
        'greeting': 0   
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def check_user(request):
    template = loader.get_template('main.html')
    a = request.POST['username']
    get_user(a)
    e = request.POST['psw']
    aa=tp(a,e)
    #print(aa)
    fe=mydb.cursor()
    fe1=mydb1.cursor()
    fe.execute("select name from book")
    rs=fe.fetchall()
    q=only_names(rs)
    fe1.execute("select * from book")
    
    rs1=fe1.fetchall()
    qq=name_price(rs1)
    context = {
        'greeting' : aa,
        'name':a,
        'greetings1':1,
        'rs': qq,
    }
    #return HttpResponseRedirect(reverse('index1'),context)
    return render(request, 'main.html',context)

def get_user(q):
    global users
    users=q

def add_user(request):
    template = loader.get_template('main.html')
    a = request.POST['username']
    get_user(a)
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
    fe1=mydb1.cursor()
    fe1.execute("select * from book")
    
    rs1=fe1.fetchall()
    qq=name_price(rs1)
    context = {
        'greeting': 1,
        'name' :a,
        'rs':qq

    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'main.html',context)



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

def buyer(request):
    template = loader.get_template('buyer.html')
    return render(request, 'buyer.html')


def fe(request):
    template = loader.get_template('fe.html')
    fe=mydb.cursor()
    fe1=mydb1.cursor()
    
    my1="select * from book where branch=%s"
    t1=['FE']
    #fe.execute(my1,t1)
    fe1.execute(my1,t1)
    
    rs1=fe1.fetchall()
    qq=name_price(rs1)
    
    context={
        'greetings':0,
        'rs': qq,
        'rs1': rs1
        #'rs2': rs2
    }
    return render(request, 'fe.html',context)

def comp(request):
    template = loader.get_template('comp.html')
    fe=mydb.cursor()
    fe1=mydb1.cursor()
    my1="select * from book where branch=%s"
    t1=['CS']
    fe.execute(my1,t1)
    rs=fe.fetchall()
    q=only_names(rs)
    fe1.execute(my1,t1)
    
    rs1=fe1.fetchall()
    qq=name_price(rs1)
    context={
        'rs':qq
    }
    return render(request, 'comp.html',context)

def it(request):
    template = loader.get_template('it.html')
    fe=mydb.cursor()
    fe1=mydb1.cursor()
    my1="select * from book where branch=%s"
    t1=['IT']
    fe.execute(my1,t1)
    rs=fe.fetchall()
    q=only_names(rs)
    fe1.execute(my1,t1)
    q=only_names(rs)
    rs1=fe1.fetchall()
    qq=name_price(rs1)
    context={
        'rs':qq
    }
    return render(request, 'it.html',context)

def entc(request):
    template = loader.get_template('entc.html')
    fe=mydb.cursor()
    fe1=mydb1.cursor()
    my1="select * from book where branch=%s"
    t1=['ENTC']
    fe.execute(my1,t1)
    rs=fe.fetchall()
    q=only_names(rs)
    fe1.execute(my1,t1)
    q=only_names(rs)
    rs1=fe1.fetchall()
    qq=name_price(rs1)
    context={
        'rs':qq
    }
    return render(request, 'entc.html',context)

def main(request):
    template = loader.get_template('main.html')
    fe=mydb.cursor()
    fe.execute("select * from book")
    rs=fe.fetchall()
    q=only_names(rs)
    qq=name_price(rs)
    print(qq)
    context={
        'greetings':1,
        'rs': qq,
        #'rs1': rs1
        #'rs2': rs2
    }
    return render(request, 'main.html',context)

def seller(request):
    template = loader.get_template('seller.html')
    return HttpResponse(template.render())


def add_book(request):
    template = loader.get_template('main.html')
    a = request.POST['b_name']
    b = request.POST['branch']
    c = request.POST['year']
    d = request.POST['mrp']
    h=request.POST['sp']
    e = request.POST['author']
    f = request.POST['pub']
    g= request.POST['coding']
    
    add_book=mydb.cursor()
    args=[0]
    r_args=add_book.callproc("id_count",args)
    sql = "INSERT INTO book (name, branch,year,mrp,selling_price,author,publication,conditions,book_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql1 = "INSERT INTO sellers  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(a,b,c,d,h,e,f,g,r_args[0])
    val1=(users,a,r_args[0],e,f,g,d,h)
    add_book.execute(sql,val)
    add_book.execute(sql1,val1)
    mydb.commit()
    fe=mydb.cursor()
    fe1=mydb1.cursor()
    fe.execute("select name from book")
    
    rs=fe.fetchall()
    fe1.execute("select * from book")
    q=only_names(rs)
    rs1=fe1.fetchall()
    qq=name_price(rs1)
    print(qq)
    context={
        'rs':qq
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'main.html',context)

def only_names(s):
    q=[]
    for i in range(len(s)):
        a=s[i][0]
        q.append(a)
    return q

def name_price(s):
    q=[]
    for i in range(len(s)):
        qq=[]
        qq.append(s[i][0])
        qq.append(s[i][5])
        q.append(qq)
    return q

def buy_book(request):
    template = loader.get_template('buyer.html')
    buyer=mydb.cursor()
    buyer1=mydb1.cursor()
    
    b=request.POST['book_name']
    #print(b)
    c_s="select seller_name from sellers where book_name=%s"
    d_s=[b]
    
    buyer.execute(c_s,d_s)
    rs=buyer.fetchall()
    rs=only_names(rs)
    print(rs)
    cc_s="select phone_no from users where username=%s"
    #print(rs[0])
    dd_s=[rs[0]]
    buyer1.execute(cc_s,dd_s)
    rs1=buyer1.fetchall()
    rs1=only_names(rs1)
    #print(rs1)
    #rs1=2345
    context={
        'a':users,
        'rs1':rs1,
        'rs':rs,
        'b':b,
        'greetings':0
    }
    return render(request, 'buyer.html',context)

