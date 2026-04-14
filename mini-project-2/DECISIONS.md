### 1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?

ODM (Object Document Mapper) is converting to the MongoDB document to the python objects. We use the Beanie because it makes the code will be more clear, reliable, readable. Also provides built-in validation and async-compatible code.


### 2. What is the role of the `Database` class — why wrap Beanie methods inside it instead of calling them directly in routes?

The Database class is used to organize and manage the database operations in one place. we want to be more clear, reliable and easy to modify, so we put these operations inside the database class.


### 3. What happens if `initialize_database()` is not called on startup? What would break and why?

If initialize_database() is not called, the connection between the application and MongoDB will not work. That's why creating, reading, updating or deleting data will fail. When the application tries to reach the database, the program can crash or give a connection error.


### 4. What is the difference between the `Event` document and the `EventUpdate` model, and why are they two separate classes?

Event Document represents the full structure of the data stored in the database. It include what it needs for creating and saving an event. EventUpdate model is used just for updating existing events, so it includes optional fields. We use these two classes for separate the creation and update logic and to make the code more flexible and safer.

## PART B 

### 1. Why does `DATABASE_URL` use `mongo` as the hostname instead of `localhost`? What would happen if you kept `localhost`?

Each container has its own network. If i wrote the localhost instead of the MongoDB the fastAPI will search inside itself and it will search, can not find it and it will give the connection error. When you wrote the mongo Docker network will know that name and it will send to the right container.


### 2. What does `depends_on` in `docker-compose.yml` do? Does it guarantee MongoDB is fully ready before FastAPI starts — and if not, what would?

depends_on only define that MongoDB container's already started , but does not mean that guarantee the MongoDB accepy the connections . So, If FastAPI start so fastly MongoDB might not be ready yet and it can give the connection error. For real guarantee we need to use healthcheck. 


### 3. What is the purpose of the volume in the `mongo` service? What happens to your data if you remove it and run `docker compose down`?

Without a volume, MongoDB will be stay inside the container. when the docker compose down container will be delete, and data will go with the container. Your data can be write on your computer's mongo-data/ folders because of Volume , even container delete the data will not gone anywhere.


### 4. Why do we copy `requirements.txt` and run `pip install` before copying the rest of the app code in the Dockerfile?

Docker get the every step to take the cache. requirements.txt if copy on its own,Docker only re-runs pip install when that file actually changes. If i change my application code, docker will be use cache layer and skips reinstalling packages, which saves a lot of time. If both were copied together, every small changes would trigger a full reinstall.

