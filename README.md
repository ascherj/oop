# Object-Oriented Programming (OOP) Examples in Python

This repository contains a collection of Python classes that demonstrate fundamental Object-Oriented Programming concepts. Each class represents a real-world object with attributes and methods, making it perfect for learning OOP principles.

## 📚 What's Included

### 1. **BankAccount** (`bank_account.py`)
A comprehensive banking system simulation with:
- Account management (account number, holder, balance)
- Transaction operations (deposit, withdraw)
- Interest calculation
- Account status management (active/closed)

**Key Features:**
- Input validation for transactions
- Interest rate calculations
- Account closure functionality
- Detailed transaction feedback

### 2. **Book** (`book.py`)
A library management system representation featuring:
- Book metadata (title, author, ISBN, page count)
- Checkout/return functionality
- Availability tracking
- Book information management

**Key Features:**
- Check-out and return operations
- Availability status checking
- Page count updates
- Comprehensive book summaries

### 3. **Car** (`car.py`)
An automotive simulation with:
- Vehicle specifications (make, model, year, color)
- Engine control (start/stop)
- Fuel management system
- Driving simulation with fuel consumption

**Key Features:**
- Realistic fuel consumption modeling
- Engine state management
- Distance-based fuel calculation
- Refueling capabilities

### 4. **CoffeeMaker** (`coffee_maker.py`)
A smart coffee maker simulation including:
- Multiple brew sizes (small, medium, large)
- Resource management (water, coffee beans)
- Power control
- Brewing operations with validation

**Key Features:**
- Three cup size options with different requirements
- Resource capacity limits
- Smart brewing validation
- Status monitoring

### 5. **Smartphone** (`smartphone.py`)
A mobile device simulation featuring:
- Device specifications (brand, model, storage)
- Security (PIN-based locking/unlocking)
- Battery management
- Usage tracking

**Key Features:**
- PIN-based security system
- Battery level monitoring with status descriptions
- Charging and usage simulation
- Device specification reporting

## 🎯 Learning Objectives

This repository demonstrates key OOP concepts:

- **Encapsulation**: Data and methods bundled together in classes
- **Abstraction**: Complex operations simplified through method interfaces
- **Data Validation**: Input checking and error handling
- **State Management**: Object state changes through method calls
- **String Representation**: Custom `__str__` and `__repr__` methods
- **Type Hints**: Modern Python typing for better code documentation

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

### Running the Examples

Each file can be run independently to see the class in action:

```bash
# Run individual examples
python bank_account.py
python book.py
python car.py
python coffee_maker.py
python smartphone.py
```

### Using the Classes in Your Code

```python
# Example: Using the BankAccount class
from bank_account import BankAccount

# Create a new account
account = BankAccount("ACC001", "John Doe", 1000.0, 0.02)

# Perform operations
account.deposit(500)
account.withdraw(200)
account.calculateInterest()
print(account.getBalance())
```

## 📖 Class Overview

| Class | Primary Purpose | Key Methods |
|-------|----------------|-------------|
| `BankAccount` | Banking operations | `deposit()`, `withdraw()`, `calculateInterest()` |
| `Book` | Library management | `checkOut()`, `returnBook()`, `isAvailable()` |
| `Car` | Vehicle simulation | `start_engine()`, `drive()`, `refuel()` |
| `CoffeeMaker` | Appliance control | `brew()`, `refillWater()`, `addBeans()` |
| `Smartphone` | Device management | `unlock()`, `charge()`, `useBattery()` |

## 🔧 Code Features

- **Comprehensive Documentation**: All classes include detailed docstrings
- **Error Handling**: Robust input validation and error messages
- **Real-world Logic**: Realistic constraints and behaviors
- **Example Usage**: Each file includes demonstration code
- **Type Hints**: Modern Python typing for better IDE support

## 🎓 Educational Use

This repository is ideal for:
- Learning Python OOP fundamentals
- Understanding class design principles
- Practicing method implementation
- Exploring real-world programming scenarios
- Teaching programming concepts

## 🤝 Contributing

Feel free to contribute by:
- Adding new classes with different real-world objects
- Improving existing class functionality
- Adding more comprehensive examples
- Enhancing documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you have questions about the code or OOP concepts demonstrated here, feel free to open an issue for discussion.

---

**Happy Learning! 🐍✨**
