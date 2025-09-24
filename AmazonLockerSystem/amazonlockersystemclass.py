# Amazon Locker System (Frequency: 4 / 5)
# Problem: Simulate a locker storage system with size-based allocation and expiration.
# Concepts: Object mapping, inventory

from enum import Enum
from collections import defaultdict
import random
import string

class LockerSize(Enum):
    SMALL = 1
    MEDIUM = 2  # 20x20x20
    LARGE = 3  # 30x30x30

class LockerStatus(Enum):
    AVAILABLE = 1
    OCCUPIED = 2
    EXPIRED = 3

class Locker:
    def __init__(self, locker_id, size):
        self.locker_id = locker_id
        self.size = size
        self.status = LockerStatus.AVAILABLE
        self.package = None  # Stores package object when occupied
        self.code = None  # Unique code for retrieving package

    def assign_package(self, package, code):
        self.status = LockerStatus.OCCUPIED
        self.package = package
        self.code = code

    def release_package(self):
        self.status = LockerStatus.AVAILABLE
        self.package = None
        self.code = None

class Package:
    def __init__(self, package_id, size):
        self.package_id = package_id
        self.size = size

class CodeGenerator:
    @staticmethod
    def generate_code():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class LockerManager:
    def __init__(self):
        self.lockers = defaultdict(list)  # Lockers grouped by size
        self.code_to_locker = {}  # Map retrieval code to Locker

    def add_locker(self, locker):
        self.lockers[locker.size].append(locker)

    def find_available_locker(self, package_size):
        for locker in self.lockers[package_size]:
            if locker.status == LockerStatus.AVAILABLE:
                return locker
        return None

    def assign_package_to_locker(self, package):
        locker = self.find_available_locker(package.size)
        if not locker:
            raise Exception("No available locker for the package size.")
        code = CodeGenerator.generate_code()
        locker.assign_package(package, code)
        self.code_to_locker[code] = locker
        return code

    def retrieve_package(self, code):
        if code not in self.code_to_locker:
            raise Exception("Invalid code or package already retrieved.")
        locker = self.code_to_locker[code]
        if locker.status != LockerStatus.OCCUPIED:
            raise Exception("Locker is not occupied.")
        package = locker.package
        locker.release_package()
        del self.code_to_locker[code]
        return package

# Example usage:
if __name__ == "__main__":
    # Initialize lockers
    manager = LockerManager()
    manager.add_locker(Locker("L1", LockerSize.SMALL))
    manager.add_locker(Locker("L2", LockerSize.MEDIUM))
    manager.add_locker(Locker("L3", LockerSize.LARGE))

    # Assign package to locker
    package1 = Package("P1", LockerSize.SMALL)
    code = manager.assign_package_to_locker(package1)
    print(f"Package assigned to locker with code: {code}")

    # Retrieve package
    retrieved_package = manager.retrieve_package(code)
    print(f"Retrieved package ID: {retrieved_package.package_id}")