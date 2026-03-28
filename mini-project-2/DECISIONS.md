### 1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?

ODM (Object Document Mapper) is converting to the MongoDB document to the python objects. We use the Beanie because it makes the code will be more clear, reliable, readable. Also provides built-in validation and async-compatible code.


### 2. What is the role of the `Database` class — why wrap Beanie methods inside it instead of calling them directly in routes?

The Database class is used to organize and manage the database operations in one place. we want to be more clear, reliable and easy to modify, so we put these operations inside the database class.


### 3. What happens if `initialize_database()` is not called on startup? What would break and why?

If initialize_database() is not called, the connection between the application and MongoDB will not work. That's why creating, reading, updating or deleting data will fail. When the application tries to reach the database, the program can crash or give a connection error.


### 4. What is the difference between the `Event` document and the `EventUpdate` model, and why are they two separate classes?

Event Document represents the full structure of the data stored in the database. It include what it needs for creating and saving an event. EventUpdate model is used just for updating existing events, so it includes optional fields. We use these two classes for separate the creation and update logic and to make the code more flexible and safer.