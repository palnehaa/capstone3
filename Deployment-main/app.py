from flask import Flask,render_template
from flask import request
import numpy as np
import pickle

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 12)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        list1 = []
        list1.append(to_predict_list['doj'])
        list1.append(to_predict_list['duration'])
        list1.append(to_predict_list['np'])
        list1.append(to_predict_list['ob'])
        list1.append(to_predict_list['pct_diff'])
        list1.append(to_predict_list['c_relocate'])
        list1.append(to_predict_list['gender'])
        list1.append(to_predict_list['c_source'])
        list1.append(to_predict_list['exp'])
        list1.append(to_predict_list['loc'])
        list1.append(to_predict_list['age'])
        list1.append(to_predict_list['lob'])
        to_predict_list = list(map(int, list1))
        result = ValuePredictor(to_predict_list)       
        if result== 'Joined':
            prediction ='Result: The candidate will be joining the company.'
        else:
            prediction ='Result: The candidate will not be joining the company.'  
	    
        	         
        return render_template("home.html",prediction = prediction)
	#redirect(url_for('index') + '#myModal')

if __name__ == '__main__':
    app.run(debug=True)

