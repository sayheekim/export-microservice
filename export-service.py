from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from flask import Flask, jsonify, send_file
import csv
from io import BytesIO
from bson import json_util
import json
import pandas as pd

# MongoDB Atlas connection details
MONGO_URI = "mongodb+srv://sayheekim:D2CbSIaKZr1fgpGV@cluster0.zkdixgx.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "nutrition_app"
COLLECTION_NAME = "users"

app = Flask(__name__)

# export to csv format
@app.route('/csv')
def export_csv():
    # Connect to MongoDB Atlas
    client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

   # Query the collection and convert the data to a pandas DataFrame
    cursor = collection.find()
    df = pd.DataFrame(list(cursor))

    # Create a BytesIO object to hold the CSV data in memory
    csv_data = BytesIO()

    # Export the DataFrame to CSV and write to BytesIO
    df.to_csv(csv_data, index=False, encoding='utf-8')

    # Reset the BytesIO object to the beginning
    csv_data.seek(0)

    # Close the MongoDB connection
    client.close()

    # Return CSV file as a response
    return send_file(csv_data, mimetype='text/csv', as_attachment=True, download_name='export.csv')

# export to json format
@app.route('/json')
def export_json():
    # Connect to MongoDB Atlas
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Retrieve data from MongoDB
    cursor = collection.find()
    data = list(parse_json(cursor))

    # Convert the list to JSON
    json_data = jsonify(data)

    # Save JSON data to a file (temporarily)
    with open('data.json', 'w') as file:
        file.write(json_data.get_data(as_text=True))

    # Send the file as an attachment and remove the temporary file
    return send_file('data.json', as_attachment=True, download_name='export.json', mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=8000)