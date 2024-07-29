# Progetto_ATAC
Progetto di simulazione del sistema di gestione database di ATAC.

Progetto creato da Giovanni di Giuseppe e Oussama Hliwa.



## Setup:

1. Type in your terminal:
    ```cmd
    source ATAC_venv/bin/activate
    ```
2. Download what's specified in the 'requirements.txt' file;
3. Type in your terminal (without quotes):
    "python -m pip install django-extensions"
4. To start the server type in your terminal:
    ```cmd
    python manage.py runserver
    ```



## Views
### Basic Pages

Views used for basic features, like the homepage.

### List Pages

Views used to list every instance of a specific class.*
> *The "Line" list is in the homepage.

### Detail Pages

Views used to show more details about a specific instance.

### Creation Tool Forms

Views used to create new instances of a specific class.

### Assignment Tool Forms

Views used to assign instances to other instances.

### Search

View used for the search bar.

### Deletion Tool Forms

Views used to delete specific instances.

### Unassignment Tool Forms

Views used to unassign instances from instances.



## Scripts
### clean_db.py

Script used to erase everything from the database.

### csv_load.py

Script used to load onto the database every CSV file located in:\
    ```Progetto_ATAC/scripts/data```

The CSV file HAS to start with the correct header for its specific class to be imported:
- `Passenger:` passenger_id,name,surname
- `Line:` line_number,name
- `Stop:` stop_id,name,latitude,longitude
- `Bus:` bus_id,capacity
- `Driver:` driver_id,name,surname\
In the specified folders there are valid CSV samples for each class.
