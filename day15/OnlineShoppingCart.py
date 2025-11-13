class OutOfStockError(Exception):
    """Raised when desired quantity exceeds product stock."""
    pass


class Store:
    """Simple store holding products as {product_id: {"name":..., "price":..., "stock":...}}"""
    def __init__(self):
        self.products = {
            1: {"name": "T-Shirt", "price": 499.0, "stock": 10},
            2: {"name": "Jeans", "price": 1299.0, "stock": 5},
            3: {"name": "Sneakers", "price": 2499.0, "stock": 3},
            4: {"name": "Cap", "price": 299.0, "stock": 20},
        }

    def get_product(self, pid):
        if pid not in self.products:
            raise KeyError("Product not found in the store.")
        return self.products[pid]

    def reduce_stock(self, pid, qty):
        prod = self.get_product(pid)
        if qty > prod["stock"]:
            raise OutOfStockError(f"Only {prod['stock']} item(s) available for {prod['name']}.")
        prod["stock"] -= qty


class Cart:
    """Cart holds items as {product_id: quantity}"""
    def __init__(self):
        self.items = {}

    def add_item(self, store: Store, pid: int, qty: int):
        if qty <= 0:
            raise ValueError("Quantity must be positive.")
        product = store.get_product(pid)  # may raise KeyError
        if qty > product["stock"]:
            raise OutOfStockError(f"Only {product['stock']} item(s) available for {product['name']}.")
        self.items[pid] = self.items.get(pid, 0) + qty
        print(f"Added {qty} x {product['name']} to cart.")

    def remove_item(self, pid: int):
        if pid not in self.items:
            raise KeyError("Product not in cart.")
        del self.items[pid]
        print("Item removed from cart.")

    def total_amount(self, store: Store):
        total = 0.0
        for pid, qty in self.items.items():
            prod = store.get_product(pid)
            total += prod["price"] * qty
        return total

    def clear(self):
        self.items = {}


def run_shopping():
    store = Store()
    cart = Cart()

    menu = """
=== ONLINE SHOP ===
1. Show products
2. Add to cart
3. Remove from cart
4. View cart & total
5. Checkout (make payment)
6. Exit
"""

    while True:
        print(menu)
        try:
            choice = int(input("Enter choice (1-6): ").strip())
        except ValueError:
            print("Invalid input! Please enter a number (1-6).")
            continue

        try:
            if choice == 1:
                print("Available Products:")
                for pid, p in store.products.items():
                    print(f"{pid}. {p['name']} - ₹{p['price']} (Stock: {p['stock']})")

            elif choice == 2:
                try:
                    pid = int(input("Enter product id to add: ").strip())
                    qty = int(input("Enter quantity: ").strip())
                except ValueError:
                    print("Invalid input! Product id and quantity must be numbers.")
                    continue
                cart.add_item(store, pid, qty)

            elif choice == 3:
                try:
                    pid = int(input("Enter product id to remove from cart: ").strip())
                except ValueError:
                    print("Invalid input! Product id must be a number.")
                    continue
                cart.remove_item(pid)

            elif choice == 4:
                if not cart.items:
                    print("Cart is empty.")
                else:
                    print("Cart contents:")
                    for pid, qty in cart.items.items():
                        p = store.get_product(pid)
                        print(f"{p['name']} x {qty} = ₹{p['price'] * qty}")
                    print(f"Total: ₹{cart.total_amount(store)}")

            elif choice == 5:
                if not cart.items:
                    print("Cart is empty. Add items before checkout.")
                    continue
                total = cart.total_amount(store)
                print(f"Total payable: ₹{total}")
                try:
                    payment = float(input("Enter payment amount: ₹").strip())
                except ValueError:
                    print("Invalid payment! Enter a numeric amount.")
                    continue
                if payment < total:
                    raise ValueError("Insufficient payment amount.")
                # finalize: reduce stock
                for pid, qty in cart.items.items():
                    store.reduce_stock(pid, qty)  # may raise OutOfStockError if concurrent change
                change = payment - total
                print(f"Payment successful. Change: ₹{change:.2f}. Thank you for shopping!")
                cart.clear()

            elif choice == 6:
                print("Exiting. Goodbye!")
                break

            else:
                print("Invalid choice. Enter 1-6.")

        except KeyError as e:
            print("Error:", e)
        except OutOfStockError as e:
            print("Error:", e)
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    run_shopping()
