import pandas as pd
from flask import Flask, request, jsonify, render_template
import json
import os 
import clickhouse_connect
from constants import *

app = Flask(__name__)

# Connect to SQLite database (or any other database you want to use)
def get_db_connection():
    client = clickhouse_connect.get_client(host=CLICKHOUSE_SERVER, 
                                           username=CLICKHOUSE_USER, 
                                           password=CLICKHOUSE_PASSWORD,
                                           port = CLICKHOUSE_PORT)
    return client



# Execute the query and return the result as a DataFrame
def execute_sql_query(query):
    client = get_db_connection()
    try:
        df = client.query_df(query)
    except Exception as e:
        return str(e)
    return df.to_json(orient="split") 
    

# Home route to serve the frontend HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to receive SQL queries from frontend and return results
@app.route('/execute_query', methods=['POST'])
def execute_query():
    query = request.json.get('query')
    if not query:
        return jsonify({'error': 'No SQL query provided'}), 400
    result = execute_sql_query(query)
    try:
        ret = jsonify(result)
    except Exception as e:
        ret = jsonify({'error': str(e)})
    return ret

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)



"""
curl --user 'default:5xLXcbwv2r' --data-binary 'select 1' http://35.200.164.13:80
"""