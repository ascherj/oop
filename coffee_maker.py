class CoffeeMaker:
    """
    A class representing a coffee maker for smart home system simulation.

    Attributes:
        brand (str): The maker's brand (e.g., Keurig, Nespresso)
        waterLevel (float): Amount of water in the reservoir (in liters)
        coffeeBeans (int): Grams of coffee beans available
        isOn (bool): Whether the machine is powered on
        cupSize (str): The selected brew size (e.g., small, medium, large)
    """

    # Cup size specifications (water in ml, beans in grams)
    CUP_SIZES = {
        "small": {"water": 120, "beans": 8},
        "medium": {"water": 180, "beans": 12},
        "large": {"water": 240, "beans": 16}
    }

    def __init__(self, brand, waterLevel=1.0, coffeeBeans=100, cupSize="medium"):
        """
        Initialize a new CoffeeMaker instance.

        Args:
            brand (str): The maker's brand
            waterLevel (float, optional): Initial water level in liters. Defaults to 1.0.
            coffeeBeans (int, optional): Initial coffee beans in grams. Defaults to 100.
            cupSize (str, optional): Default cup size. Defaults to "medium".
        """
        self.brand = brand
        self.waterLevel = max(0.0, waterLevel)  # Ensure non-negative
        self.coffeeBeans = max(0, coffeeBeans)  # Ensure non-negative
        self.isOn = False  # Coffee makers typically start off
        self.cupSize = cupSize if cupSize in self.CUP_SIZES else "medium"
        self.maxWaterCapacity = 2.0  # Maximum water reservoir capacity in liters
        self.maxBeansCapacity = 500  # Maximum bean storage in grams

    def turnOn(self):
        """
        Turn on the coffee maker.

        Returns:
            bool: True if successfully turned on, False if already on
        """
        if not self.isOn:
            self.isOn = True
            return True
        return False

    def turnOff(self):
        """
        Turn off the coffee maker.

        Returns:
            bool: True if successfully turned off, False if already off
        """
        if self.isOn:
            self.isOn = False
            return True
        return False

    def brew(self):
        """
        Make coffee if there's enough water and beans, reducing both accordingly.

        Returns:
            dict: Result of brewing attempt with status and message
        """
        if not self.isOn:
            return {"success": False, "message": "Coffee maker is turned off"}

        if self.cupSize not in self.CUP_SIZES:
            return {"success": False, "message": f"Invalid cup size: {self.cupSize}"}

        required_water = self.CUP_SIZES[self.cupSize]["water"] / 1000.0  # Convert ml to liters
        required_beans = self.CUP_SIZES[self.cupSize]["beans"]

        if self.waterLevel < required_water:
            return {
                "success": False,
                "message": f"Not enough water. Need {required_water:.2f}L, have {self.waterLevel:.2f}L"
            }

        if self.coffeeBeans < required_beans:
            return {
                "success": False,
                "message": f"Not enough coffee beans. Need {required_beans}g, have {self.coffeeBeans}g"
            }

        # Brew the coffee
        self.waterLevel -= required_water
        self.coffeeBeans -= required_beans

        return {
            "success": True,
            "message": f"Successfully brewed {self.cupSize} coffee! Water: {self.waterLevel:.2f}L, Beans: {self.coffeeBeans}g remaining"
        }

    def refillWater(self, amount):
        """
        Add water to the reservoir.

        Args:
            amount (float): Amount of water to add in liters

        Returns:
            dict: Result of refill attempt
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            return {"success": False, "message": "Water amount must be a positive number"}

        if self.waterLevel + amount > self.maxWaterCapacity:
            overflow = (self.waterLevel + amount) - self.maxWaterCapacity
            self.waterLevel = self.maxWaterCapacity
            return {
                "success": False,
                "message": f"Water tank full. Added {amount - overflow:.2f}L, {overflow:.2f}L overflow"
            }

        self.waterLevel += amount
        return {
            "success": True,
            "message": f"Added {amount:.2f}L water. Current level: {self.waterLevel:.2f}L"
        }

    def addBeans(self, amount):
        """
        Add coffee beans to the storage.

        Args:
            amount (int): Amount of coffee beans to add in grams

        Returns:
            dict: Result of adding beans
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            return {"success": False, "message": "Bean amount must be a positive number"}

        amount = int(amount)  # Convert to integer for grams

        if self.coffeeBeans + amount > self.maxBeansCapacity:
            overflow = (self.coffeeBeans + amount) - self.maxBeansCapacity
            self.coffeeBeans = self.maxBeansCapacity
            return {
                "success": False,
                "message": f"Bean storage full. Added {amount - overflow}g, {overflow}g overflow"
            }

        self.coffeeBeans += amount
        return {
            "success": True,
            "message": f"Added {amount}g coffee beans. Current amount: {self.coffeeBeans}g"
        }

    def setCupSize(self, size):
        """
        Set the cup size for brewing.

        Args:
            size (str): Cup size (small, medium, large)

        Returns:
            bool: True if valid size set, False otherwise
        """
        if size in self.CUP_SIZES:
            self.cupSize = size
            return True
        return False

    def getStatus(self):
        """
        Get the current status of the coffee maker.

        Returns:
            dict: Current status information
        """
        return {
            "brand": self.brand,
            "isOn": self.isOn,
            "waterLevel": self.waterLevel,
            "coffeeBeans": self.coffeeBeans,
            "cupSize": self.cupSize,
            "canBrew": self.canBrew()
        }

    def canBrew(self):
        """
        Check if the coffee maker can brew with current resources.

        Returns:
            bool: True if can brew, False otherwise
        """
        if not self.isOn or self.cupSize not in self.CUP_SIZES:
            return False

        required_water = self.CUP_SIZES[self.cupSize]["water"] / 1000.0
        required_beans = self.CUP_SIZES[self.cupSize]["beans"]

        return self.waterLevel >= required_water and self.coffeeBeans >= required_beans

    def __str__(self):
        """
        String representation of the coffee maker.

        Returns:
            str: A formatted string representation
        """
        status = "ON" if self.isOn else "OFF"
        can_brew = "Ready" if self.canBrew() else "Not Ready"
        return f"{self.brand} Coffee Maker - {status} - Water: {self.waterLevel:.2f}L - Beans: {self.coffeeBeans}g - Cup: {self.cupSize} - {can_brew}"

    def __repr__(self):
        """
        Official string representation of the coffee maker.

        Returns:
            str: A string that could recreate the object
        """
        return f"CoffeeMaker('{self.brand}', {self.waterLevel}, {self.coffeeBeans}, '{self.cupSize}')"


# Example usage and testing
if __name__ == "__main__":
    # Create a coffee maker instance
    coffee_maker = CoffeeMaker("Keurig", 1.5, 150, "medium")

    print("Initial coffee maker state:")
    print(coffee_maker)
    print(f"Status: {coffee_maker.getStatus()}")

    # Try to brew while off
    print("\nTrying to brew while coffee maker is off...")
    result = coffee_maker.brew()
    print(f"Brew result: {result['message']}")

    # Turn on and brew
    print("\nTurning on coffee maker...")
    coffee_maker.turnOn()
    print(coffee_maker)

    print("\nBrewing medium coffee...")
    result = coffee_maker.brew()
    print(f"Brew result: {result['message']}")
    print(coffee_maker)

    # Change cup size and brew
    print("\nChanging to large cup size...")
    coffee_maker.setCupSize("large")
    result = coffee_maker.brew()
    print(f"Brew result: {result['message']}")
    print(coffee_maker)

    # Refill water
    print("\nRefilling water...")
    result = coffee_maker.refillWater(0.5)
    print(f"Refill result: {result['message']}")
    print(coffee_maker)

    # Add more beans
    print("\nAdding more coffee beans...")
    result = coffee_maker.addBeans(100)
    print(f"Add beans result: {result['message']}")
    print(coffee_maker)

    # Brew multiple cups
    print("\nBrewing multiple cups...")
    for i in range(3):
        result = coffee_maker.brew()
        print(f"Cup {i+1}: {result['message']}")
        if not result['success']:
            break

    print(f"\nFinal state: {coffee_maker}")
