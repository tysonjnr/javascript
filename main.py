
from flask import Flask, render_template, request, redirect
from dbservice import get_data,insert_products,insert_sale

app = Flask(__name__)


# Route for the homepage
@app.route("/")
def sales_system():
    return render_template("index.html")

# Route for the dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

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

# Route for displaying and handling sales data
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