from app import app
from utils.db import db
import os

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("0.0.0.0:$PORT", default=5000))
