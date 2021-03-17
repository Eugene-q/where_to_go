# where-to-go
Training project on Django "Interesting places in Moscow" course [dvmn.org](https://dvmn.org).
Locations are displayed on the map. By clicking on them, you can view related information. 
In the administrative panel it is possible to add and edit the locations and associated photos. 
Photos can be sorted by dragging and dropping. 
Test data taken from [KudaGo](https://kudago.com/)

[DEMO](http://wheretogo.pythonanywhere.com/)
# installing
* Download the code.
* Go to the project folder
* Create a new virtual environment
```bash
    $ python3 -m venv env
```
* Activate the virtual environment
```bash
    $ source env/bin/activate
```
* Install the required packages from the file requirements.txt
```bash
    $ pip install -r requirements.txt
```
* Create superuser to edit database
```bash
    $ python3 manage.py createsuperuser
````
* Add test data to the database
```bash
	$ python3 load_places.py
````
* Run the server
```bash
    $ python3 manage.py runserver
````
# using
* In the browser, open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Administrative panel [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
* Also you can add new places to the database directly from json files like [this](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%92%D0%BE%D1%80%D0%BE%D0%B1%D1%8C%D1%91%D0%B2%D1%8B%20%D0%B3%D0%BE%D1%80%D1%8B.json) using special management command.
```bash
    $ python3 manage.py load_place <json url>
````
