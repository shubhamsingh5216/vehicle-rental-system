from car import Car
from bike import Bike

car1 = Car("KA01AB1234", "Toyota", 1000, 5)
car2 = Car("KA03CD5678", "Honda", 1200, 7)
bike1 = Bike("KA02XY1111", "Yamaha", 500, 150)

vehicles = [car1, car2, bike1]

while True:
    print("\n===== Vehicle Rental System =====")
    print("1. Show all vehicles")
    print("2. Calculate rent")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for i, v in enumerate(vehicles):
            print(f"\nVehicle {i+1}:")
            v.display()

    elif choice == "2":
        try:
            index = int(input("Select vehicle number: ")) - 1

            if index < 0 or index >= len(vehicles):
                print("Invalid selection")
                continue

            days = int(input("Enter number of days: "))

            rent = vehicles[index].calculate_rent(days)
            print(f"Total Rent: ₹{rent}")

        except ValueError:
            print("Please enter valid numbers")

    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Wrong choice, try again")