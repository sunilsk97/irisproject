from flask import Flask, jsonify,render_template, request, redirect, url_for
import config
from iris_app.utils import Iris

app = Flask(__name__)
#model = pickle.load(open("iris_app",'iris_Logistic_model.pkl', 'rb'))
@app.route("/") # HOme API

def hello_iris():
    print("Welcome to IRIS Prediction")
    return render_template("home.html")


################################################################################
################################################################################

@app.route("/predict", methods= ['POST','GET'])

def get_pred_species():

    #data=request.form
    #print("data is :", data)  # immutable dictionary
    if request.method =='POST':
        SepalLengthCm = request.form['SepalLengthCm']
        print("SepalLengthCm",SepalLengthCm)
        SepalWidthCm = request.form['SepalWidthCm']
        print("SepalWidthCm",SepalWidthCm)
        PetalLengthCm = request.form['PetalLengthCm']
        print("PetalLengthCm",PetalLengthCm)
        PetalWidthCm = request.form['PetalWidthCm'] 
        print("PetalWidthCm",PetalWidthCm)
        #return redirect (url_for('result'))
    
        iris_predict = Iris(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    #print(iris_predict)
        pred_species=iris_predict.get_predicted_species()
   # print(pred_species)
        #return jsonify({"Return": f"predicted species is :{pred_species}"})   
        return render_template("after.html", pred=pred_species)

   
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)

