from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
model = pickle.load(open('finalized_model.pkl', 'rb'))


@app.route('/index')
def home():
    return render_template('index.html')
  
@app.route("/predictapi" , methods=['GET', 'POST'])
def predict_clas():
  weight=request.args.get('weight')
  length1=request.args.get('length1')
  length2=request.args.get('length2')
  length3=request.args.get('length3')
  height=request.args.get('height')
  width=request.args.get('width')
  prediction = model.predict([[weight,length1,length2,length3,height,width]])
  return render_template('index.html', prediction_text=prediction )

@app.route("/predict" , methods=['GET', 'POST'])
def predict_class():
 
  weight=request.form['weight']
  length1=request.form['length1'] 
  length2=request.form['length2'] 
  length3=request.form['length3'] 
  height=request.form['height'] 
  width=request.form['width']
  prediction = model.predict([[weight,length1,length2,length3,height,width]])
  return render_template('index.html', prediction_text='fish type  {}'.format(prediction) )


if __name__ == "__main__":
  app.run()
