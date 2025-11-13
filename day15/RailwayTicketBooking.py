class BookingFullError(Exception):
    """Raised when requested seat type is sold out."""
    pass


class RailwaySystem:
    """Simple railway booking system with seat-types and basic booking/cancel/view features."""
    def __init__(self):
        # seat inventory per route/seat-type (you can extend to multiple trains/routes)
        # keys are seat-type names; values are available seat counts
        self.seats = {
            "sleeper": 5,
            "ac": 3,
            "general": 10
        }
        # bookings stored as {pnr: {"name":..., "destination":..., "seat_type":..., "seats":..., "fare":...}}
        self.bookings = {}
        self._next_pnr = 1001
        # fare per seat-type
        self.fares = {"sleeper": 450.0, "ac": 1200.0, "general": 200.0}

    def list_seat_types(self):
        """Return list of available seat types and counts."""
        return [(st, self.seats[st], self.fares.get(st, 0.0)) for st in self.seats]

    def validate_name(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Invalid passenger name. Name must be non-empty text.")
        # optional: disallow digits-only names
        if any(char.isdigit() for char in name):
            raise ValueError("Invalid passenger name. Name should not contain digits.")
        return name.strip()

    def validate_seat_type(self, seat_type: str):
        seat_type = seat_type.lower().strip()
        if seat_type not in self.seats:
            # using IndexError to indicate invalid selection (as requested)
            raise IndexError(f"Invalid seat selection: '{seat_type}'.")
        return seat_type

    def book_ticket(self, name: str, destination: str, seat_type: str, seats: int = 1):
        """Book `seats` seats of `seat_type` for passenger `name` to `destination`."""
        # validate inputs
        name = self.validate_name(name)
        if not isinstance(destination, str) or not destination.strip():
            raise ValueError("Invalid destination. Destination must be non-empty text.")
        seat_type = self.validate_seat_type(seat_type)
        try:
            seats = int(seats)
        except (TypeError, ValueError):
            raise ValueError("Seats must be a whole number.")
        if seats <= 0:
            raise ValueError("Number of seats must be positive.")

        # check availability
        available = self.seats[seat_type]
        if seats > available:
            raise BookingFullError(f"Only {available} seat(s) available in {seat_type} class.")

        # reserve
        self.seats[seat_type] -= seats
        pnr = self._next_pnr
        self._next_pnr += 1
        fare = self.fares.get(seat_type, 0.0) * seats
        self.bookings[pnr] = {
            "name": name,
            "destination": destination.strip(),
            "seat_type": seat_type,
            "seats": seats,
            "fare": fare
        }
        return pnr

    def cancel_ticket(self, pnr: int):
        """Cancel booking and restore seats. Raises KeyError if PNR not found."""
        if pnr not in self.bookings:
            raise KeyError("PNR not found.")
        rec = self.bookings.pop(pnr)
        self.seats[rec["seat_type"]] += rec["seats"]
        return rec

    def view_ticket(self, pnr: int):
        if pnr not in self.bookings:
            raise KeyError("PNR not found.")
        return self.bookings[pnr]

    def availability(self):
        """Return a copy of seats availability."""
        return dict(self.seats)


def run_cli():
    system = RailwaySystem()
    menu = """
=== RAILWAY RESERVATION ===
1. List seat types & availability
2. Book ticket
3. Cancel ticket
4. View ticket details
5. View availability
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
                print("Seat types (type : available : fare per seat):")
                for st, count, fare in system.list_seat_types():
                    print(f" - {st} : {count} : ₹{fare:.2f}")

            elif choice == 2:
                name = input("Enter passenger name: ")
                destination = input("Enter destination: ")
                seat_type = input("Enter seat type (sleeper/ac/general): ")
                seats_in = input("Enter number of seats (default 1): ").strip() or "1"
                try:
                    pnr = system.book_ticket(name, destination, seat_type, seats_in)
                    rec = system.view_ticket(pnr)
                    print(f"Booking successful. PNR: {pnr}")
                    print(f"Name: {rec['name']}, Destination: {rec['destination']}, "
                          f"Seat type: {rec['seat_type']}, Seats: {rec['seats']}, Fare: ₹{rec['fare']:.2f}")
                except (ValueError, IndexError, BookingFullError) as e:
                    print("Error:", e)

            elif choice == 3:
                try:
                    pnr = int(input("Enter PNR to cancel: ").strip())
                except ValueError:
                    print("PNR must be a number.")
                    continue
                try:
                    rec = system.cancel_ticket(pnr)
                    refund = rec["fare"]
                    print(f"Cancelled PNR {pnr}. Refund: ₹{refund:.2f}")
                except KeyError as e:
                    print("Error:", e)

            elif choice == 4:
                try:
                    pnr = int(input("Enter PNR to view: ").strip())
                except ValueError:
                    print("PNR must be a number.")
                    continue
                try:
                    rec = system.view_ticket(pnr)
                    print(f"PNR {pnr}: Name: {rec['name']}, Destination: {rec['destination']}, "
                          f"Seat type: {rec['seat_type']}, Seats: {rec['seats']}, Fare: ₹{rec['fare']:.2f}")
                except KeyError as e:
                    print("Error:", e)

            elif choice == 5:
                avail = system.availability()
                print("Current availability:")
                for st, cnt in avail.items():
                    print(f" - {st} : {cnt} seat(s)")

            elif choice == 6:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Enter 1-6.")

        except Exception as e:
            # unexpected errors
            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    run_cli()
