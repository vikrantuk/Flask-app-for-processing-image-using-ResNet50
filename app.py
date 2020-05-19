from flask import Flask

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def create_pred():
    pass

app.run(port=5000)
