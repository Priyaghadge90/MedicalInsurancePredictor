from flask import Flask ,request,jsonify,render_template

from project_app.utils import MedicalInsurance
import project_config

Intobj=MedicalInsurance()

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gender_option")
def gender_option():
    col_data=Intobj.load_json_data()
    gender_values=list(col_data["gender"].keys())
    return jsonify(gender_values) 

@app.route("/smoker_option")
def smoker_option():
    col_data=Intobj.load_json_data()
    smoker_values=list(col_data["smoker"].keys())
    return jsonify(smoker_values)

@app.route("/region_option")
def region_option():
    col_names=Intobj.load_model()
    print("Column Names from model:", col_names)
    region_values= [ col_name.replace ("region_", "") for col_name in col_names if col_name.startswith("region_")]
    print("Extracted region values:", region_values)
    return jsonify(region_values)
    

@app.route("/prediction",methods=["POST"])
def prediction():
    data=request.form

    predict_charges=Intobj.predict_charges(data)
    print(f"Predicted insurance charges:{predict_charges}")

    return jsonify({"Message":"Sucessfull","result":f"Predicted insurance charges:{predict_charges}"})



if __name__=="__main__":
    app.run(host="0.0.0.0",port=project_config.FLASK_PORT_NUMBER,debug=True)
    