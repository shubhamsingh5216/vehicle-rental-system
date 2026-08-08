from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, reg_no, brand, daily_price, seats):
        super().__init__(reg_no, brand, daily_price)
        self.seats = seats

    def display(self):
        super().display()
        print(f"Seats: {self.seats}")

    def calculate_rent(self, days):
        # cars have slight extra charge
        base = super().calculate_rent(days)
        return base + 200