import mysql.connector


# Connect to MySQL
def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9963200487A",
            database="product_db"
        )

        print("MySQL connected successfully!")
        return connection

    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None


# Add Product
def add_product(connection):
    try:
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        cursor = connection.cursor()

        query = """
        INSERT INTO Products (Product_Name, Category, Price, Quantity)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, category, price, quantity)

        cursor.execute(query, values)
        connection.commit()

        print("Product added successfully!")

        cursor.close()

    except ValueError:
        print("Please enter valid price and quantity.")

    except mysql.connector.Error as e:
        print("Error:", e)


# View Products
def view_products(connection):
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Products")

        products = cursor.fetchall()

        print("\nProduct List:")
        print("-" * 70)

        for product in products:
            print(product)

        cursor.close()

    except mysql.connector.Error as e:
        print("Error:", e)


# Update Product
def update_product(connection):
    try:
        product_id = int(input("Enter Product ID to update: "))
        new_price = float(input("Enter new price: "))

        cursor = connection.cursor()

        query = """
        UPDATE Products
        SET Price = %s
        WHERE Product_ID = %s
        """

        cursor.execute(query, (new_price, product_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Product updated successfully!")
        else:
            print("Product ID not found.")

        cursor.close()

    except ValueError:
        print("Please enter valid values.")

    except mysql.connector.Error as e:
        print("Error:", e)


# Delete Product
def delete_product(connection):
    try:
        product_id = int(input("Enter Product ID to delete: "))

        cursor = connection.cursor()

        query = "DELETE FROM Products WHERE Product_ID = %s"

        cursor.execute(query, (product_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Product deleted successfully!")
        else:
            print("Product ID not found.")

        cursor.close()

    except ValueError:
        print("Please enter a valid Product ID.")

    except mysql.connector.Error as e:
        print("Error:", e)


# Main Program
connection = connect_database()

if connection:
    while True:
        print("\n===== PRODUCT MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product Price")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(connection)

        elif choice == "2":
            view_products(connection)

        elif choice == "3":
            update_product(connection)

        elif choice == "4":
            delete_product(connection)

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

    connection.close()
    print("MySQL connection closed.")