from app import app
from utils.db import db
import os

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)
    # app.run(port=os.getenv('PORT', default=5000), debug=True,)
