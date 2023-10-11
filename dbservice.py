import psycopg2

conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='12345')

def get_data(products):
    cursor = conn.cursor()
    query = f"SELECT * FROM {products}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_data1(sales):
    cursor = conn.cursor()
    query = f"SELECT * FROM {sales}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def insert_data(values):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO products (product_name, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

def insert_data1(values1):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO sales (pid, quantity, created_at) VALUES (%s, %s, %s)"
        cursor.execute(query, values1)
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()


def profit():
    cursor = conn.cursor()
    m =" SELECT SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit,\
    sales.created_at FROM sales JOIN products ON sales.product_id= products.product_id  WHERE sales.created_at >=\
    '2022-10-13 05:00:48'  AND sales.created_at <= '2023-10-05 20:33:31' GROUP BY sales.created_at\
    ORDER BY sales.created_at ASC;"

    cursor.execute(m)
    data3=cursor.fetchall()
    return data3


def check_email(email):
    cursor = conn.cursor()
   
    cursor.execute("SELECT * FROM users WHERE email= %s",(email,))
    data4=cursor.fetchone()
    if data4:
        return data4
    else:
        return False

def email_pass(email,password):
    cursor = conn.cursor()
    check_all = 'SELECT * FROM users WHERE email=%s and password=%s'

    cursor.execute(check_all,(email,password))
    
    data5=cursor.fetchone()
    

    if data5 :
        if data5[3] == password: 
            return data5
        else:
            return False  
    
   

def create_user(reg1):
    cursor = conn.cursor()
    query2 = "INSERT INTO users (full_name, email, password) VALUES (%s, %s,%s)"
    cursor.execute(query2,reg1)
    
    conn.commit()
   
# conn.close()