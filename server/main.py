from flask import Flask
from flask_cors import CORS
from ROUTERS.movies_route import movies_route
from ROUTERS.persons_route import persons_route

app = Flask(__name__)
CORS(app)
app.register_blueprint(movies_route)
app.register_blueprint(persons_route)

if __name__ == "__main__":
    app.run()