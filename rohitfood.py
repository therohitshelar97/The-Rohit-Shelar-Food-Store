from flask import *
import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'rohit_veg'
    )

cursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/veg")
def veg():
    cursor.execute("select * from userveg")
    data = cursor.fetchall()
    return render_template('veg.html',userdata = data)

@app.route("/create",methods = ["POST"])
def create():
    uname=request.form.get('uname')
    dname=request.form.get('dname')
    addr=request.form.get('addr')
    contact=request.form.get('contact')
    insq="insert into usernonveg(Customer_Name,Dish_Name,Address,Contact) values('{}','{}','{}','{}')".format(uname,dname,addr,contact)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("order"))
    except:
        db.rollback()
        return "Error in query"

@app.route("/non_veg")
def non_veg():
    cursor.execute("select * from usernon")
    data1 = cursor.fetchall()
    return render_template('non_veg.html',userdata1=data1)

@app.route("/create1",methods = ["POST"])
def create1():
    uname1=request.form.get('uname1')
    dname1=request.form.get('dname1')
    addr1=request.form.get('addr1')
    contact1=request.form.get('contact1')
    insq1="insert into usernonveg1(Customer_Name,Dish_Name,Address,Contact) values('{}','{}','{}','{}')".format(uname1,dname1,addr1,contact1)
    try:
        cursor.execute(insq1)
        db.commit()
        return redirect(url_for("order"))
    except:
        db.rollback()
        return "Error in query"

@app.route("/order")
def order():
    cursor.execute("select * from usernonveg")
    data=cursor.fetchall()
    cursor.execute("select * from usernonveg1")
    data1=cursor.fetchall()
    return render_template('order.html',ordata=data,ordata1=data1)

@app.route("/delete")
def delete():
    id=request.args.get('id')
    ins="delete from usernonveg where id = {}".format(id)
    ins1="delete from usernonveg1 where id = {}".format(id)
    try:
        cursor.execute(ins)
        cursor.execute(ins1)
        db.commit()
        return redirect(url_for("order"))
    except:
        db.rollback()
        return "Error in query"




if __name__=='__main__':
    app.run(debug=True)