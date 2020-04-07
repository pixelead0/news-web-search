from app import app
from app.config import Config

app.run('0.0.0.0', port=5000, debug=Config.DEBUG)
