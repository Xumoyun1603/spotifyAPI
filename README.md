# spotifyAPI
Simple Spotify API

## How to start

Clone repository and create **.env** file in **BASE_DIR**
```
export SECRET_KEY=Your secret_key in settings.py
export DEBUG=True
export POSTGRES_DB=postgres
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=Your postgres password
export POSTGRES_HOST=127.0.0.1
```

You need executable permission on the **entrypoint.sh** file.(Terminal)
```
$ chmod +x entrypoint.sh
```

Run the **docker-compose up** command from the top level directory for project.
```
$ docker-compose up
```

Spotify API should be running at port **8000** on your Docker host. Go to **http://localhost:8000** on a web browser

## The documentation of the API

Go to **http://localhost:8000/docs/** on a web browser to see the swagger docs.

Go to **http://localhost:8000/redoc/** on a web browser to see the redoc docs.

Shut down services and clean up by using either of these methods: Stop the application by typing **Ctrl-C** in the same shell in where you started it.

Or, for a more elegant shutdown, switch to a different shell, and run **docker-compose down** from the top level of your Django sample project directory.
```
$ docker-compose down
```
