class Vehicle:
    def __init__(self, reg_no, brand, daily_price):
        self.reg_no = reg_no
        self.brand = brand
        self.daily_price = daily_price

    def display(self):
        print(f"\nReg No: {self.reg_no}")
        print(f"Brand: {self.brand}")
        print(f"Price per day: ₹{self.daily_price}")

    def calculate_rent(self, days):
        # basic rent calculation
        if days <= 0:
            print("Days should be more than 0")
            return 0

        total = self.daily_price * days

        # small discount if rented longer
        if days > 5:
            total *= 0.9  # 10% off

        return int(total)