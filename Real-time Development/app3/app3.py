#author : @rebwar_ai : app.py
from app3 import app3,socketio

if __name__ == '__main__':
	socketio.run(app3,host="0.0.0.0",port=5000,debug=True)