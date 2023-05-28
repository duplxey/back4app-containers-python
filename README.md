# back4app-containers-python

This repository demonstrates how to dockerize and deploy a [Flask]([https://react.dev/](https://flask.palletsprojects.com/en/2.3.x/)) application to [Back4app Containers](https://www.back4app.com/container-as-a-service-caas).

> To learn more check out the [article](https://blog.back4app.com/how-to-build-and-deploy-a-python-application/).

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
