# Elevator-system

The elevator system is meticulously designed with a user-centric approach. Within this system, there are elevator units akin to buildings, each housing a number of elevators. When a user initiates a request, the elevator system autonomously responds by moving either upwards or downwards based on the user's input. The algorithm governing the elevator's response to requests can undergo further optimization for enhanced efficiency. Additionally, the operational status of an elevator, whether it is currently in service or not, can be seamlessly updated through API calls. For detailed information, please refer to the documentation provided in the DOCS.md file.

## Installation :

- If pip is not in your system
  ```
  $ sudo apt-get install python-pip
  ```
- Then install virtualenv
  ```
  $ pip install virtualenv
  ```
- Create Virtual Environment
  ```
  python3 -m venv .venv
  ```
- Activate venv
  ```
    source .venv/bin/activate
  ```

1. Clone the repository and proceed to the directory containing the manage.py file.

```
git clone https://github.com/deshdeepak2019/elevator-system
```

```
cd elevator-system
```

2. Install the requirements

```
pip install -r requirements.txt
```

3. Run the development server

```
python manage.py runserver
```

## NOTE:-

1. I am using SWAGGER UI for visualize and interact with the API's resources

  <img width="959" alt="Screenshot 2023-12-16 012715" src="https://github.com/deshdeepak2019/elevator-system/assets/97728256/2a813d7c-2a99-4d6a-a4fa-26709d95dd92">

2. Using Django Jazzmin for admin Dashboard

  <img width="960" alt="Screenshot 2023-12-16 012734" src="https://github.com/deshdeepak2019/elevator-system/assets/97728256/cb8c0ff1-f1cd-495e-8a5a-230df677a26a">

3. Using DRF for viewsets and REST API.
4. Using thread to run multiple elevators simultaneously.
5. Default SQLite DB is used.
6. Models representation at [MODEL_DOCS.md](https://github.com/deshdeepak2019/elevator-system/blob/main/MODEL_DOCS.md)
7. API representation at [API_DOCS.md](https://github.com/deshdeepak2019/elevator-system/blob/main/API_DOCS.md)
