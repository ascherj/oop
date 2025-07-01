class Smartphone:
    """
    A class representing a smartphone for mobile app or device simulation.

    Attributes:
        brand (str): The manufacturer (e.g., Apple, Samsung)
        model (str): The specific model (e.g., iPhone 14, Galaxy S23)
        batteryLevel (int): Battery percentage (0 to 100)
        storageCapacity (int): Storage in GB (e.g., 128, 256)
        isLocked (bool): Whether the phone is currently locked
    """

    def __init__(self, brand, model, storageCapacity, batteryLevel=100):
        """
        Initialize a new Smartphone instance.

        Args:
            brand (str): The manufacturer
            model (str): The specific model
            storageCapacity (int): Storage in GB
            batteryLevel (int, optional): Initial battery level (0-100). Defaults to 100.
        """
        self.brand = brand
        self.model = model
        self.storageCapacity = storageCapacity
        self.batteryLevel = max(0, min(100, batteryLevel))  # Ensure valid range
        self.isLocked = True  # Phones typically start locked
        self._correctPin = "1234"  # Default PIN for demo purposes

    def unlock(self, pin=None):
        """
        Unlock the phone if the correct PIN is provided.

        Args:
            pin (str, optional): The PIN to unlock the phone. Defaults to "1234" for demo.

        Returns:
            bool: True if successfully unlocked, False if incorrect PIN
        """
        if pin is None:
            pin = "1234"  # Default for demo purposes

        if pin == self._correctPin:
            self.isLocked = False
            return True
        return False

    def lock(self):
        """
        Lock the phone.

        Returns:
            bool: True (always successful)
        """
        self.isLocked = True
        return True

    def charge(self, amount):
        """
        Increase battery level by the specified amount, up to 100%.

        Args:
            amount (int): Amount to charge (percentage points)

        Returns:
            int: New battery level after charging
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Charge amount must be a non-negative number")

        self.batteryLevel = min(100, self.batteryLevel + amount)
        return self.batteryLevel

    def useBattery(self, amount):
        """
        Decrease battery level based on usage.

        Args:
            amount (int): Amount of battery to use (percentage points)

        Returns:
            int: New battery level after usage
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Battery usage amount must be a non-negative number")

        self.batteryLevel = max(0, self.batteryLevel - amount)
        return self.batteryLevel

    def getSpecs(self):
        """
        Get specifications of the smartphone.

        Returns:
            str: A formatted string with brand, model, and storage capacity
        """
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storageCapacity}GB"

    def getBatteryStatus(self):
        """
        Get the current battery status.

        Returns:
            str: Battery status description
        """
        if self.batteryLevel > 80:
            return "Excellent"
        elif self.batteryLevel > 50:
            return "Good"
        elif self.batteryLevel > 20:
            return "Low"
        elif self.batteryLevel > 10:
            return "Critical"
        else:
            return "Very Low"

    def __str__(self):
        """
        String representation of the smartphone.

        Returns:
            str: A formatted string representation
        """
        lock_status = "Locked" if self.isLocked else "Unlocked"
        battery_status = self.getBatteryStatus()
        return f"{self.brand} {self.model} ({self.storageCapacity}GB) - Battery: {self.batteryLevel}% ({battery_status}) - {lock_status}"

    def __repr__(self):
        """
        Official string representation of the smartphone.

        Returns:
            str: A string that could recreate the object
        """
        return f"Smartphone('{self.brand}', '{self.model}', {self.storageCapacity}, {self.batteryLevel})"


# Example usage and testing
if __name__ == "__main__":
    # Create a smartphone instance
    phone = Smartphone("Apple", "iPhone 14", 256, 85)

    print("Initial phone state:")
    print(phone)
    print(f"Specs: {phone.getSpecs()}")

    # Try to use the phone while locked
    print(f"\nPhone locked: {phone.isLocked}")

    # Unlock with wrong PIN
    print("\nTrying to unlock with wrong PIN...")
    success = phone.unlock("0000")
    print(f"Unlock successful: {success}")

    # Unlock with correct PIN
    print("\nUnlocking with correct PIN...")
    success = phone.unlock("1234")
    print(f"Unlock successful: {success}")
    print(phone)

    # Use some battery
    print("\nUsing phone (battery drain)...")
    phone.useBattery(25)
    print(f"Battery after usage: {phone.batteryLevel}%")
    print(phone)

    # Charge the phone
    print("\nCharging phone...")
    phone.charge(40)
    print(f"Battery after charging: {phone.batteryLevel}%")
    print(phone)

    # Lock the phone
    print("\nLocking phone...")
    phone.lock()
    print(phone)
