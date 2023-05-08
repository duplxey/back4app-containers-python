# flask-todo

A simple RESTful API for tracking TODO tasks.

## Development

1. Fork/Clone

2. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

3. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

4. Initialize the database:

    ```sh
    (venv)$ python init_db.py
    ```

5. Run the server:

    ```sh
    (venv)$ flask run
    ```
    
 6. Navigate to [http://localhost:5000/](http://localhost:5000/) in your favorite web browser.

## Deploy (Docker)

1. [Install Docker](https://docs.docker.com/engine/install/) (if you don't have it yet).

2. Build and tag the image:
    ```sh
    (venv)$ docker build -t flask-todo:1.0 .
    ```

3. Start a new container:
   ```sh
    (venv)$ docker run -it -p 5000:5000 -d flask-todo:1.0
    ```

4. Navigate to [http://localhost:5000/](http://localhost:5000/) in your favorite web browser.