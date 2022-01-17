import mysql.connector as con
obj=con.connect(host='localhost',user='root',password='itisroot')
if obj.is_connected():
        cur=obj.cursor()
        cur.execute("create database if not exists grocery_store")
        obj.commit()

obj2 = con.connect(host='localhost',user='root',password='itisroot',database='grocery_store')
if obj2.is_connected():
      cur1=obj2.cursor()
      cur1.execute("""CREATE TABLE if not exists products (
product_id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(45) NOT NULL,
uom_id INT NOT NULL,
price_per_unit DOUBLE NOT NULL,PRIMARY KEY (product_id));""")
      cur1.execute("""CREATE TABLE if not exists uom (
uom_id INT NOT NULL AUTO_INCREMENT,
uom_name VARCHAR(45) NOT NULL,PRIMARY KEY (uom_id));""")
      cur1.execute("""ALTER TABLE products ADD CONSTRAINT
FOREIGN KEY (uom_id)
REFERENCES uom (uom_id)
ON DELETE NO ACTION
ON UPDATE RESTRICT;""")
      cur1.execute("""CREATE TABLE if not exists orders (
order_id INT NOT NULL AUTO_INCREMENT,
customer_name VARCHAR(100) NOT NULL,
total DOUBLE NOT NULL,
datetime DATETIME NOT NULL,
PRIMARY KEY (order_id));""")
      cur1.execute("""CREATE TABLE if not exists order_details (
order_id INT NOT NULL,
product_id INT NOT NULL,
quantity DOUBLE NOT NULL,
total_price DOUBLE NOT NULL,
PRIMARY KEY (order_id),
FOREIGN KEY (order_id)
REFERENCES orders (order_id)
ON DELETE NO ACTION
ON UPDATE RESTRICT,
FOREIGN KEY (product_id)
REFERENCES products(product_id)
ON DELETE NO ACTION
ON UPDATE RESTRICT);""")
      cur1.execute("""CREATE TABLE if not exists owner (
userid varchar(25),
password varchar(15));""")
      cur1.execute("""INSERT INTO owner VALUES ('adminowner', 'admin123');""")
      obj2.commit()