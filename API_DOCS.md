## API Documentation

# Elevator System
1. POST  /elevator-system/ - To create new elevator system
   ```
   Request-
   
   {
    "name": "string",
    "max_floor": 0,
    "number_of_elevators": 0
    }

   Response- status code = 201
   
   {
    "id": 0,
    "name": "string",
    "max_floor": 0,
    "number_of_elevators": 0
   }
   ```
 2. GET  /elevator-system/ - To get list of all elevator systems.
    ```
    Response- status code = 200
    {
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
      {
        "id": 0,
        "name": "string",
        "max_floor": 0,
        "number_of_elevators": 0
      }
    ]
    }
    ```
  3. GET /elevator-system/id/ - To retrieve a single instance of elevator system
     ```
     Response- status code = 200
     {
      "id": 0,
      "name": "string",
      "max_floor": 0,
      "number_of_elevators": 0
     }
     ```

   4. PATCH /elevator-system/id/ - To update a single instance of elevator system
      ```
      Response- status code = 200
       {
        "id": 0,
        "name": "string",
        "max_floor": 0,
        "number_of_elevators": 0
       }
      ```

  5. GET /elevator-system/id/elevators/ - To get list of all elevators in a elevator system
     ```
     Response- status code = 200
     {
      "count": 1,
      "next": null,
      "previous": null,
      "results": [
        {
          "id": 1,
          "created_on": "2023-12-15T13:42:39.341853Z",
          "modified_on": "2023-12-15T15:25:58.243807Z",
          "current_floor": 2,
          "is_operational": true,
          "is_door_open": true,
          "running_status": 0,
          "elevator_system": 1
        }
      ]
      }
     ```

# Elevator

1. POST /elevator/ - To create a elevator in a elevator system

   ```
   Request-
   {
     "current_floor": 0,
     "is_operational": true,
     "is_door_open": true,
     "running_status": 1,
     "elevator_system": 0
   }

   Response- status code = 200
   {
     "id":0,
     "current_floor": 0,
     "is_operational": true,
     "is_door_open": true,
     "running_status": 1,
     "elevator_system": 0
   }
   ```

2. GET /elevator/id/ - To retrieve a particular elevator in a elevator system
   ```
   Response - status code = 200
   {
     "id": 0,
     "created_on": "2023-12-15T21:08:07.572Z",
     "modified_on": "2023-12-15T21:08:07.572Z",
     "current_floor": 0,
     "is_operational": true,
     "is_door_open": true,
     "running_status": 1,
     "elevator_system": 0
   }
   ```

3. PATCH /elevator/id/ - To update a particular elevator.
   ```
   Response - status code = 200
   {
     "id": 0,
     "created_on": "2023-12-15T21:08:07.572Z",
     "modified_on": "2023-12-15T21:08:07.572Z",
     "current_floor": 0,
     "is_operational": true,
     "is_door_open": true,
     "running_status": 1,
     "elevator_system": 0
   }
   ```

4. GET /elevator/id/requests/ - To get all elevator request for a particular elevator id.

   ```
   Response - status code = 200
   {
     "count": 30,
     "next": null,
     "previous": null,
     "results": [
       {
         "id": 1,
         "created_on": "2023-12-15T14:06:41.460814Z",
         "modified_on": "2023-12-15T14:06:41.827503Z",
         "requested_floor": 0,
         "destination_floor": 2,
         "request_time": "2023-12-15T14:06:41.460894Z",
         "is_active": false,
         "elevator": 1
       },
       ]
    ```

5. GET /elevator/id/fetch_destination/ - To fetch destination of an elevator.

    ```
    Response - status code = 200
    {
     "running": true,
     "details": "string",
     "destination_floor": 0,
     "current_floor": 0
   }
    ```
   
