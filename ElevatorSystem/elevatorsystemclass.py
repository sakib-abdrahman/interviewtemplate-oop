# Elevator System (Frequency: 4 / 5)
# Problem: Simulate an elevator system that handles multiple requests, directions, and floors.
# Concepts: State management, scheduling

from collections import deque
import heapq
import time
from enum import Enum

class State(Enum):
    IDLE = 1
    UP = 2
    DOWN = 3

class RequestOrigin(Enum):
    INSIDE = 1
    OUTSIDE = 2

class Request:
    def __init__(self, origin, origin_floor, destination_floor=None):
        self.origin = origin
        self.origin_floor = origin_floor
        self.destination_floor = destination_floor

    def __lt__(self, other):
        return self.destination_floor < other.destination_floor

class Elevator:
    def __init__(self, current_floor=1):
        self.current_floor = current_floor  # current floor
        self.state = State.IDLE  # begin state
        self.up_queue = []  # minheap
        self.down_queue = []  # minheap

    # open elevator
    def open_doors(self):
        print(f"Doors are OPEN on floor {self.current_floor}")

    # close elevator
    def close_doors(self):
        print(f"Doors are CLOSED")

    # up request to queue
    def add_up_request(self, request):
        heapq.heappush(self.up_queue, request)

    # down request to queue
    def add_down_request(self, request):
        heapq.heappush(self.down_queue, request)

    def process_up_requests(self):
        while self.up_queue:
            request = heapq.heappop(self.up_queue)
            self.move_to_floor(request.destination_floor)

    def process_down_requests(self):
        while self.down_queue:
            request = heapq.heappop(self.down_queue)
            self.move_to_floor(request.destination_floor)

    def move_to_floor(self, floor):
        if self.current_floor != floor:
            print(f"Moving from floor {self.current_floor} to floor {floor}")
            time.sleep(1)  # Simulate movement time
            self.current_floor = floor
            print(f"Arrived at floor {floor}")
        self.open_doors()
        time.sleep(1)  # Simulate door open time
        self.close_doors()

    def operate(self):
        if self.up_queue or self.state == State.UP:
            print("Processing UP requests...")
            self.process_up_requests()
        if self.down_queue or self.state == State.DOWN:
            print("Processing DOWN requests...")
            self.process_down_requests()
        self.state = State.IDLE  # done and idle
        print("Elevator is now IDLE.")

class Controller:
    def __init__(self):
        self.elevator = Elevator()

    def send_up_request(self, origin_floor, destination_floor):
        request = Request(RequestOrigin.OUTSIDE, origin_floor, destination_floor)
        self.elevator.add_up_request(request)

    def send_down_request(self, origin_floor, destination_floor):
        request = Request(RequestOrigin.OUTSIDE, origin_floor, destination_floor)
        self.elevator.add_down_request(request)

    # start processing
    def handle_requests(self):
        self.elevator.operate()

class Main:
    @staticmethod
    def main():
        controller = Controller()

        # up and down
        controller.send_up_request(1, 5)
        controller.send_down_request(4, 2)
        controller.send_up_request(3, 6)

        # process requests
        controller.handle_requests()

        print("New requests...")
        controller.send_up_request(1, 9)
        controller.send_down_request(5, 2)

        # process new requests
        controller.handle_requests()

if __name__ == "__main__":
    Main.main()