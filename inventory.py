# inventory_oops.py

# --- Base Class ---
class Inventory:
    def __init__(self):
        self.products = {}   # {product_name: {"price": x, "quantity": y}}
        self.earnings = 0

    def add_product(self, name, price, quantity):
        if name in self.products:
            self.products[name]["quantity"] += quantity
            self.products[name]["price"] = price
        else:
            self.products[name] = {"price": price, "quantity": quantity}
        print(f"✅ Added/Updated product: {name} | Price: ₹{price} | Quantity: {quantity}")

    def purchase_product(self, name, quantity):
        """Original purchase method (basic version)"""
        if name not in self.products:
            print("❌ Product not found!")
            return
        product = self.products[name]
        if quantity > product["quantity"]:
            print("❌ Not enough stock available!")
            return
        total_cost = product["price"] * quantity
        product["quantity"] -= quantity
        self.earnings += total_cost
        print(f"🛒 Purchased {quantity} x {name} for ₹{total_cost}")

    def show_stock(self):
        if not self.products:
            print("❌ No products available.")
            return
        print("\n📦 Available Stock:")
        for name, info in self.products.items():
            print(f" - {name}: ₹{info['price']} | Quantity: {info['quantity']}")

    def show_earnings(self):
        print(f"\n💰 Total Earnings: ₹{self.earnings}")


# --- Child Class (Method Overriding Example) ---
class UpdatedInventory(Inventory):
    def purchase_product(self, name, quantity):
        """Overridden method: updates stock and prints a custom message"""
        if name not in self.products:
            print("❌ Product not found!")
            return

        product = self.products[name]
        if quantity > product["quantity"]:
            print("❌ Not enough stock available!")
            return

        # Perform purchase
        total_cost = product["price"] * quantity
        product["quantity"] -= quantity
        self.earnings += total_cost

        # Overridden behavior
        print(f"🛒 Purchased {quantity} x {name} for ₹{total_cost}")
        print(f"📉 Stock updated: Remaining {product['quantity']} units of {name}")

        if product["quantity"] == 0:
            print(f"⚠️ {name} is now out of stock!")


# --- Main program ---
def main():
    store = UpdatedInventory()  # <-- using subclass with overridden method
    while True:
        print("\n=== 🏬 INVENTORY MANAGEMENT SYSTEM ===")
        print("1️⃣ Add Product")
        print("2️⃣ Purchase Product")
        print("3️⃣ Show Stock")
        print("4️⃣ Show Total Earnings")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Product name: ").strip()
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            store.add_product(name, price, quantity)
        elif choice == "2":
            name = input("Product name to purchase: ").strip()
            quantity = int(input("Quantity to purchase: "))
            store.purchase_product(name, quantity)
        elif choice == "3":
            store.show_stock()
        elif choice == "4":
            store.show_earnings()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
