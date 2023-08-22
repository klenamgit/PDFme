import random
import numpy
import cv2
from flask import Flask,request,current_app
from flask import send_file
from flask import render_template
import io
from multiprocessing import Process
import first
from os import remove
app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("real.html")

# @app.route("/downloads",methods=["GET"])
# def download():
#       keep='C:\\Users\\User\\Documents\\receipts\\'+name+'.pdf' 
#       return send_file(keep)

@app.route("/",methods=["POST"])
def index_upload():
      pic = cv2.imdecode(numpy.fromstring(request.files['file'].read(),numpy.uint8), cv2.IMREAD_UNCHANGED)
       
      name=random.randint(100000000,999999999)
      ratio1 = pic.shape[0] / 500.0
      print(ratio1)
      first.forshow(pic,name)
      # work='python first.py --image pic -n '+str(name)
      # Popen(work)
      keep='C:\\Users\\User\\Documents\\receipts\\'+str(name)+'.pdf'
      
      return_data = io.BytesIO()
      with open(keep,'rb') as fo:
           return_data.write(fo.read())
           return_data.seek(0)
      
      background_remove(keep)
     
      return  send_file(return_data, mimetype='application/pdf')

def background_remove(path):
     task = Process(target=rm(path))
     task.start()

def rm(path):
     remove(path)

if __name__ == "__main__":
      app.run(host="127.0.0.1", port=80,debug=True)
      