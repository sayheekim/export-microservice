# Overview

This is a microservice implented by Sayhee Kim for project partner Alejandro
for the OSU CS 361 Portfolio Project.

It is a program written in Python, and uses Flask and Pymongo to retrieve documents related
to my partner's project that are stored in MongoDb, and export them to a useful .cvs or .json
format, depending on the http endpoint.

# Get started

You can recreate the environment that was used to develop this microservice
(which contains all its required dependencies) by doing the following:

1.  Open your terminal / command prompt
2.  Navigate to this project directory
3.  Create the virtual environment using the commands:

    -   On Unix or MacOS:

        python3 -m venv venv
        source venv/bin/activate

    -   On Windows:

        python3 -m venv venv
        .\venv\Scripts\activate

4.  Installl Project Dependencies using the command:
    pip install -r requirements.txt

5.  Now you can run the program via the command:
    python3 export-service.py.

    You should see a message confirming the service is running in your terminal/commad prompt, like so:

    -   Serving Flask app 'export-service'
    -   ...
    -   Running on http://127.0.0.1:8000

# How to Request Data

-   The Flask server is running on the URL provided in Step 5 above. (http://127.0.0.1:8000), and has two endpoints (/'/csv' and '/json').
-   While the service is running, you can trigger the "csv export" service with a HTTP GET request to the '/csv' path.
    (For example, you can simply visit "http://127.0.0.1:8000/csv" in your browser, or send a GET request from your own program. You can also use Postman or a similar service to test.)
-   While the service is running, you can trigger the "json export" service with a HTTP GET request to the '/json' path. (For example, you can simply visit "http://127.0.0.1:8000/json" in your browser, or send a GET request from your own program. You can also use Postman or a similar service to test.)

# How to Receive Data

-   Once the service is triggered at an endpoint, it will automatically prepare the file sin the requested format and send the export file back. No additional action is needed.
-   You should automatically be prompted to save the export, which will be in .csv or .json file, depending on which endpoint was requested.
-   You can also customize the names the files will be downloaded as, by changing the "download_name" parameter in the send\_\_file() methods inside export-service.py.

# Additional Notes

-   Once you have your own MongoDB database set up, replace the values of MONGO_URI, DB_NAME, and COLLECTION_NAME variables in export-service.py to retrieve data from your database. (Currently it is retrieving data from my personal database.)

# UML Diagram:

![UML diagram](./UML.png)
