# 🚗 Vehicle Rental System (OOP in Python)

## 📌 Overview

This project is a simple implementation of a **Vehicle Rental System** using Python and Object-Oriented Programming (OOP) concepts.

The system allows users to manage different types of vehicles (Cars and Bikes), view their details, and calculate rental costs based on the number of days.

The main goal of this project is to demonstrate how OOP concepts like **inheritance, polymorphism, and encapsulation** can be applied to solve real-world problems.

---

## 🧠 OOP Concepts Used

### 🔹 1. Classes & Objects

* Created a base class `Vehicle`
* Created objects for Car and Bike

### 🔹 2. Inheritance

* `Car` and `Bike` inherit from the `Vehicle` class
* This helps reuse common attributes like:

  * Registration number
  * Brand
  * Price per day

### 🔹 3. Polymorphism (Method Overriding)

* The method `calculate_rent()` behaves differently for different vehicles
* Example:

  * Car → extra charge added
  * Bike → normal pricing

### 🔹 4. Encapsulation

* Data and methods are kept inside classes
* Improves structure and maintainability

---

## ⚙️ Features

* Add and manage multiple vehicles
* Supports different vehicle types:

  * 🚗 Car (with number of seats)
  * 🏍️ Bike (with engine capacity)
* Display vehicle details
* Calculate rental cost based on number of days
* Menu-driven interface (CLI based)
* Basic validation for user input
* Discount for longer rental periods

---

## 🏗️ Project Structure

```
vehicle-rental-system/
│
├── vehicle.py     # Base class (Vehicle)
├── car.py         # Car class (inherits Vehicle)
├── bike.py        # Bike class (inherits Vehicle)
├── main.py        # Entry point (menu-driven system)
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shubhamsingh5216/vehicle-rental-system.git
cd vehicle-rental-system
```

### 2. Run the program

```bash
python main.py
```

---

## 🧪 Sample Flow

1. User selects an option from menu
2. System displays available vehicles
3. User selects a vehicle
4. User enters number of rental days
5. System calculates and displays total rent

---

## 💡 Example

```
===== Vehicle Rental System =====
1. Show all vehicles
2. Calculate rent
3. Exit
```

---

## 🔧 Additional Logic Implemented

* ✔ Input validation (invalid index / wrong input)
* ✔ Discount applied for rentals longer than 5 days
* ✔ Extra charge applied for cars
* ✔ Error handling using try-except

---

## 🚀 Future Improvements

This is a basic version and can be extended further:

* Add database (MySQL / PostgreSQL)
* Convert into web application using Django/Flask
* Add booking system
* Add vehicle availability tracking
* Add user authentication
* Build REST APIs

---

## 🎯 Conclusion

This project demonstrates how OOP concepts can be used to design a clean and scalable system. The structure makes it easy to extend the application with more vehicle types or additional features in the future.

---

## 👨‍💻 Author

Shubham Kumar
Final Year – Information Science & Engineering
JSS Academy of Technical Education, Bengaluru

---
