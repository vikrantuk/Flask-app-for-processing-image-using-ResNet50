from flask import Flask,request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def create_pred():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return("done")

app.run(port=5000)
