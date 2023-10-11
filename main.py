
from flask import Flask, render_template, request, redirect,url_for,session,flash

from dbservice import insert_data,insert_data1,get_data,get_data1,profit,check_email,email_pass,create_user
from datetime import datetime



app = Flask(__name__)
app.secret_key="1990" 

def confirm_auth():
    return 'id' in session
 

@app.route("/")
def index():
  return render_template("index.html") 

#route for login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  
        email = request.form['email']
        password = request.form['password']
        log_in = email_pass(email, password)
        if log_in:
            session["id"] = log_in[0] 
            return redirect(url_for("dashboard"))          
        else:
            flash("Invalid Email or Password")
    return render_template("login.html")


#route for register   
@app.route("/register", methods=["GET","POST"])
def register1():
    if request.method == "POST":
        full_name = request.form.get('full_name')

        email = request.form.get('email')

        password = request.form.get('password')

        values=(full_name, email, password) 

        exists =check_email(email)
        
        if exists :
            flash("Email already exist")
           
        else:
            flash("Registered succesfully!")
            create_user(values)
            return redirect("/login")
        
    return render_template("login.html")

#route for dashboard
@app.route("/dashboard")
def dashboard():  
    if confirm_auth(): 
        p1=[float(i[0]) for i in profit()]
        p2=[str(i[1]) for i in profit()]
        return render_template("dashboard.html", myprof = p1, myprof2=p2)
    else:
        flash("Log in to access")
        return redirect(url_for("login"))

#route for adding products
@app.route("/add_products", methods=['POST'])
def add_products():
    
    prod_n=request.form['product_name']
    buy_p=request.form['buying_price']
    sell_p=request.form['selling_price']
    stock_q=request.form['stock_quantity'] 

    values=(prod_n,buy_p,sell_p,stock_q)
        
    insert_data(values)
       
    return redirect("/products")

#route for accessing products
@app.route("/products",methods=['GET', 'POST'])
def products():
    if confirm_auth():
        sp=get_data("products")
        return render_template("products.html", myprods = sp)
    else:
        flash("Log in to access")
        return redirect(url_for("login"))

#route for adding sales
@app.route("/add_sales" , methods=['POST'])
def add_sales():
    product_id= request.form['pid']
    quantity= request.form['quantity']
    created_at= datetime.now().replace(microsecond=0)

    values1=(product_id,quantity,created_at)
            
    insert_data1(values1)
    return redirect("/sales")

#route for accessing sales
@app.route("/sales", methods=['GET', 'POST'])
def sales():
    if confirm_auth():
        ss=get_data("products")
        sp1=get_data1("sales")
        return render_template("sales.html", myprods1 = sp1,prd=ss)
    else:
        flash("Log in to access")
        return redirect(url_for("login"))


#route for logging out
@app.route("/logout",methods=['GET','POST'])
def logout():
    session.pop("id", None)
    return redirect('/login')



app.run(debug=True)