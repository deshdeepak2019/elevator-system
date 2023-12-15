import time
from threading import Thread

from .models import Elevator, ElevatorRequest, ElevatorSystem


class RunThread(Thread):
    """
    A different thread running in an infinite loop
    to process all the requests made to an elevator
    """

    def run(self):
        while True:
            final_run()


def run_elevator(elevator: Elevator, elevator_system: ElevatorSystem):
    """
    Filter all the requests for a given elevator
    move it according to the requests.
    """
    requests_pending = ElevatorRequest.objects.filter(
        elevator=elevator,
        is_active=True,
    ).order_by("request_time")

    for request in requests_pending:
        requested_floor = request.requested_floor
        request_destination = request.destination_floor
        current_floor = elevator.current_floor

        # Invalid Cases
        # 1
        if (
            request_destination < 0
            or request_destination > elevator_system.max_floor
            or requested_floor < 0
            or requested_floor > elevator_system.max_floor
        ):
            request.is_active = False
            request.save()
            continue
        # 2
        if request_destination == requested_floor:
            request.is_active = False
            request.save()
            continue

        # Close the door
        elevator.is_door_open = False

        # Go to user starting point
        # If user is at 3rd floor and elevator current floor is at 1st floor, in this case elevator goes up
        # and vice versa
        if requested_floor > current_floor:
            # Start going up
            elevator.running_status = 1
        elif requested_floor < current_floor:
            # Start going down
            elevator.running_status = -1
        elevator.save()
        time.sleep(4)
        # user starting point reached, stop running
        # Open the door
        elevator.current_floor = requested_floor
        elevator.running_status = 0
        # Let people moving in, Open the door
        elevator.is_door_open = True
        elevator.save()

        time.sleep(4)

        # Let people get in, Close the door
        elevator.is_door_open = False
        if request_destination > elevator.current_floor:
            # Start going up
            elevator.running_status = 1
        elif request_destination < current_floor:
            # Start going down
            elevator.running_status = -1
        elevator.save()
        time.sleep(3)

        # Destination reached, stop running
        # Open the door
        elevator.current_floor = request_destination
        elevator.running_status = 0
        elevator.is_door_open = True
        elevator.save()

        request.is_active = False
        request.save()


def check_elevator_system(elevator_system: ElevatorSystem):
    """
    Filter all the elevators running in an elevator system
    and process their requests one by one.
    """
    elevators_running = Elevator.objects.filter(
        elevator_system=elevator_system,
        is_operational=True,
    )

    for elevator in elevators_running:
        run_elevator(elevator=elevator, elevator_system=elevator_system)


def final_run():
    """
    Run the process for all elevator systems
    """
    elevator_systems = ElevatorSystem.objects.all().order_by("id")

    for elevator_system in elevator_systems:
        check_elevator_system(elevator_system=elevator_system)
