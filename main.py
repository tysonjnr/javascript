
from flask import Flask, render_template, request, redirect,session
from dbservice import get_data,insert_products,insert_sale,calc_profit
from dbservice import check_email,check_pass_match,create_user
from flask import flash,url_for

app = Flask(__name__)
app.secret_key = '1998'

#def login_check():
    #if session['email'] != None:
      # return redirect(url_for("dashboard"))
   # return redirect(url_for("login"))
# Route for the homepage
@app.route("/")
def sales_system():
    return render_template("index.html")

# Route for the dashboard
@app.route("/dashboard")
def dashboard():
    dates = []
    profits = []
    for i in calc_profit():
         dates.append(str(i[0]))
         profits.append(float(i[1]))
    return render_template("dashboard.html",dates=dates,profits=profits)

# Route for displaying and handling product data
@app.route("/add-products", methods=["POST"])
def add_products():
        productname = request.form['productname']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        stock_quantity = request.form['stock_quantity']
        columns=(productname, buying_price, selling_price, stock_quantity)
        insert_products(columns)
        return redirect('/products')
@app.route("/products")
def products():
    
    products_data = get_data("products")
    return render_template("products.html", myproducts=products_data)

#route for login
@app.route("/login", methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form['email']
        password  = request.form['password']
        submit = (email,password)
        check_pass_match(email,password)
        if submit:
         flash ("correct")
         return redirect(url_for("dashboard"))
        else:
         error = "incorrect password or email"
    return render_template("login.html", error=error)
 #route for register
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
     full_name = request.form["full_name"]
     email = request.form["email"]
     password = request.form["password"]
     values = (full_name,email,password)
     e_exist = check_email(email)
     if  e_exist:
        flash ("Email already exists.")
           
     else:
        create_user(values) 
        flash("registerd succesfully")
        return redirect('/dashboard')

    
    return render_template("register.html")
# Route for displaying sales 
@app.route("/sales", methods=["GET", "POST"])
def sales():
   
    sales_data = get_data('sales')
    products=get_data("products")
    return render_template("sales.html", mysales=sales_data,products=products)

@app.route("/add-sales" ,methods=["POST"])
def add_sales():
    product_id=request.form["product_id"]
    quantity = request.form['quantity']  
    msale=(product_id,quantity)
    insert_sale(msale)

    return redirect('/sales')



if __name__ == "__main__":
    app.run(debug=True)
