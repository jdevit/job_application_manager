from interface.interface import Interface
from flask import Flask

flask_app = Flask(__name__)
Interface.getInstance(flask_app).run()

