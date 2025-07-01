class Car:
    def __init__(self, make: str, model: str, year: int, color: str, fuel_level: float = 100.0, is_engine_on: bool = False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = fuel_level  # 0.0 to 100.0
        self.is_engine_on = is_engine_on

    def start_engine(self):
        """Turns the engine on if there's enough fuel."""
        if self.fuel_level > 0:
            self.is_engine_on = True
            return "Engine started successfully."
        else:
            return "Cannot start engine: insufficient fuel."

    def stop_engine(self):
        """Turns the engine off."""
        self.is_engine_on = False
        return "Engine stopped."

    def drive(self, distance: float) -> str:
        """Reduces fuel level based on distance traveled and returns a message about remaining fuel."""
        if not self.is_engine_on:
            return "Cannot drive: engine is not running. Please start the engine first."

        if distance <= 0:
            return "Invalid distance. Please enter a positive value."

        # Assuming fuel consumption of 1% per unit distance (you can adjust this rate)
        fuel_consumption = distance * 1.0  # 1% fuel per unit distance

        if self.fuel_level < fuel_consumption:
            # Drive as far as possible with remaining fuel
            actual_distance = self.fuel_level / 1.0
            self.fuel_level = 0.0
            self.is_engine_on = False  # Engine stops when fuel runs out
            return f"Ran out of fuel after driving {actual_distance:.1f} units. Engine stopped. Fuel level: {self.fuel_level:.1f}%"

        self.fuel_level -= fuel_consumption
        return f"Drove {distance} units. Remaining fuel: {self.fuel_level:.1f}%"

    def refuel(self, amount: float):
        """Increases the fuel level by the specified amount, up to 100%."""
        if amount <= 0:
            return "Invalid fuel amount. Please enter a positive value."

        self.fuel_level = min(100.0, self.fuel_level + amount)
        return f"Refueled. Current fuel level: {self.fuel_level:.1f}%"

    def get_details(self) -> str:
        """Returns a string with the car's make, model, year, and color."""
        return f"{self.year} {self.make} {self.model} ({self.color})"

    def __str__(self) -> str:
        """String representation of the car with all details."""
        engine_status = "On" if self.is_engine_on else "Off"
        return (f"{self.get_details()}\n"
                f"Fuel Level: {self.fuel_level:.1f}%\n"
                f"Engine: {engine_status}")


# Example usage
if __name__ == "__main__":
    # Create a car instance
    my_car = Car("Toyota", "Camry", 2023, "Blue")

    print("=== Car Details ===")
    print(my_car.get_details())
    print(f"Fuel Level: {my_car.fuel_level}%")
    print(f"Engine Status: {'On' if my_car.is_engine_on else 'Off'}")

    print("\n=== Starting Engine ===")
    print(my_car.start_engine())

    print("\n=== Driving ===")
    print(my_car.drive(25))
    print(my_car.drive(30))

    print("\n=== Refueling ===")
    print(my_car.refuel(20))

    print("\n=== Final Status ===")
    print(my_car)
