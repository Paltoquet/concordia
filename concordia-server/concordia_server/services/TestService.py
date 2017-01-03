from concordia_server import app
from concordia_server import db
from flask import jsonify

@app.route('/test')
def test():
    # Create a new sensor
    sensor = {
        'title': 'bullometreV2',
        'value': 47
    }
    
    # Insert the sensor
    db.sensors.insert(sensor)
    return jsonify(sensor)
