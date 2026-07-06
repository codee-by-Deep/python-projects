import sqlite3

def create_table():
    conn = sqlite3.connect('inventory_manager.db')
    cursor = conn.cursor()

    cursor.execute("""create table if not exists inventory(
                   id integer primary key autoincrement,
                   name text,
                   quantity integer,
                   price real)""")
    
    conn.commit()
    conn.close()

def add_products():
    conn = sqlite3.connect('inventory_manager.db')
    cursor = conn.cursor()

    name = input("Enter the name of the product:")
    quantity = int(input("Enter the quantity of the product: "))
    price = float(input("Enter the price of the product:"))

    cursor.execute("insert into inventory(name,quantity,price) values (?, ?, ?)", (name,quantity,price))
    print("product added Successfully")
    conn.commit()
    conn.close()


def view_products():
    conn = sqlite3.connect('inventory_manager.db')
    cursor = conn.cursor()

    cursor.execute("select * from inventory")
    result = cursor.fetchall()
    for row in result:
        print("Id:",row[0],"| Product Name:",row[1],"| Quantity of Product:", row[2],"| Price of Product: ",row[3])
    conn.commit()
    conn.close()

def update_products():
    conn = sqlite3.connect('inventory_manager.db')
    cursor = conn.cursor()

    view_products()

    id = int(input("Enter Id: "))
    new_quantity = int(input("Enter the new Quantity: "))

    cursor.execute("update inventory set quantity = ? where id = ?",(new_quantity,id))
    print("Updated Successfully")

    conn.commit()
    conn.close()
    view_products()

def delete_products():
    conn = sqlite3.connect("inventory_manager.db")
    cursor = conn.cursor()

    view_products()

    id = int(input("Enter the Id for Deletion: "))

    cursor.execute("delete from inventory where id = ?",(id,))
    print("Product Deleted Successfully")

    conn.commit()
    conn.close()
    view_products()

def search_products():
    conn = sqlite3.connect('inventory_manager.db')
    cursor = conn.cursor()

    search = input("Enter the name of Product: ")
    cursor.execute("select * from inventory where name like ?",('%'+ search +'%',))
    result = cursor.fetchall()
    for row in result:
        print("Id:",row[0],"| Name:",row[1],"| Quantity:",row[2],"| Price:",row[3])

    conn.commit()
    conn.close()
   

def menu():
    while True:
        option = int(input("""---INVENTORY---
            1.Add Products
            2.View Products
            3.Update Products
            4.DeleteProducts
            5.Search Products
            6.Exit
            """))
        
        if option == 1:
                add_products()
        elif option == 2:
            view_products()
        elif option == 3:
            update_products()
        elif option == 4:
                delete_products()
        elif option == 5:
                search_products()
        elif option == 6:
            print("Exited")
            break
        else:
            print("Invalid option")

create_table()
menu()




