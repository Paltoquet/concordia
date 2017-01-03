from concordia_server import app
from datetime import datetime
from flask_mongokit import MongoKit, Document

# Database configuration
app.config['MONGODB_HOST']     = 'localhost'
app.config['MONGODB_PORT']     =       27017
app.config['MONGODB_DATABASE'] = 'concordia'

# Database
db = MongoKit(app)

# Register all models
class Sensor(Document):
    __collection__ = 'sensors'
    structure = {
        'title'     : unicode,
        'value'     : float,
        'created_at': datetime,
    }
    required_fields = ['title', 'value']
    default_values  = {'created_at': datetime.utcnow}
    use_dot_notation = True

db.register([Sensor])
