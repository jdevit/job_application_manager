from interface.interface import Interface
from flask import Flask

app = Interface.getInstance()
flask_app = app.app
app.run()
