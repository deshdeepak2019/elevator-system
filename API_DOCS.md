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
     {
      "id": 0,
      "name": "string",
      "max_floor": 0,
      "number_of_elevators": 0
     }
     ```

   4. PATCH /elevator-system/id/ - To update a single instance of elevator system
      ```
       {
        "id": 0,
        "name": "string",
        "max_floor": 0,
        "number_of_elevators": 0
       }
      ```

  5. GET /elevator-system/id/elevators/ - To get list of all elevators in a elevator system
     ```
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
     
