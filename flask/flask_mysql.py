from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'  #server location
app.config['MYSQL_USER'] = 'mysql_username'
app.config['MYSQL_PASSWORD'] = 'mysql_password'
app.config['MYSQL_DB'] = 'myfarm'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MySQL
mysql = MySQL(app)

@app.route('/sensor_dht', methods=['POST'])
def add_dht():
    try:
        data = request.json
        temperature = data['temp']
        humidity = data['humi']
        current_time = datetime.now()
        date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sensor_dht (update_time, temperature, humidity) VALUES (%s, %s, %s)", 
                 (date_time, temperature, humidity))
        mysql.connection.commit()
        cur.close()
        
        resp = jsonify(message="Data added successfully!")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return jsonify(message="adding data error"), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", ssl_context='adhoc')
