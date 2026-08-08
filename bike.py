from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, reg_no, brand, daily_price, engine_cc):
        super().__init__(reg_no, brand, daily_price)
        self.engine_cc = engine_cc

    def display(self):
        super().display()
        print(f"Engine: {self.engine_cc}cc")

    # keeping same rent logic for now