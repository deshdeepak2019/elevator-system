## Models

**1. CreatedModifiedModel** - An abstract base model providing automatic tracking of creation and modification timestamps.

    Attributes:
        created_on (DateTimeField): A timestamp indicating when this object was initially created.
            This field is automatically set to the current datetime when the object is first saved.

        modified_on (DateTimeField): A timestamp indicating when this object was last modified.
            This field is automatically updated to the current datetime on every save.
            
    Usage:
        Your models can inherit from this base model to benefit from automatic timestamp tracking.

**2. ElevatorSystem** - Represents an elevator system in a building, utilizing Django's default ID as the primary key.
```
    Attributes:
        name (CharField): Name of the elevator system.
        
        max_floor (IntegerField): Maximum floor in the elevator system.
            The system assumes a minimum floor of 0, and this field enforces a minimum value of 1.

        number_of_elevators (PositiveIntegerField): Maximum number of elevators in the elevator system.

    Constraints:
        - `max_floor` must be greater than or equal to 1

    Usage:
        This model can be used to represent a building with multiple elevators.
        Inherit from `CreatedModifiedBaseModel` for automatic timestamp tracking.
```

**3. Elevator** - Represents a singular movable unit within an elevator system.
```

    Attributes:
        elevator_system (ForeignKey): Reference to the ElevatorSystem to which this elevator belongs.
        
        current_floor (PositiveSmallIntegerField): Current floor of the elevator. Default is 0.

        is_operational (BooleanField): Indicates whether the elevator is operational or not. Default is True.

        is_door_open (BooleanField): Indicates whether the elevator door is open or closed. Default is True.

        running_status (IntegerField): Running status of the elevator, such as UP, DOWN, etc.
            Choices are defined by the `RunningStatus` enumeration.

    Usage:
        This model is used to represent a singular unit within an elevator system.
        Inherit from `CreatedModifiedBaseModel` for automatic timestamp tracking.
```

**4. ElevatorRequest** - Represents an elevator request made by a user.
```
    Attributes:
        elevator (ForeignKey): Reference to the Elevator for which the request is made.
        
        requested_floor (PositiveSmallIntegerField): Floor requested by the user.

        destination_floor (PositiveSmallIntegerField): Destination floor to which the user wants to go.

        request_time (DateTimeField): Time at which the user requested the elevator. Automatically set to the current datetime on creation.

        is_active (BooleanField): Indicates whether the request is still active or has been fulfilled. Default is True.

    Constraints:
        - The requested floor and destination floor cannot be the same.

    Usage:
        This model is used to represent elevator requests made by users.
        Inherit from `CreatedModifiedBaseModel` for automatic timestamp tracking.

```
