from flask import Flask,request
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

fpayload = ""

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def create_pred():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    fpayload = f.filename
    model = ResNet50(weights='imagenet')
    img = image.load_img(str(fpayload), target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    result = ""
    for _,res,_ in decode_predictions(preds, top=3)[0]:
        result +=  (res+" ")
    return(result)

app.run(port=5000)
