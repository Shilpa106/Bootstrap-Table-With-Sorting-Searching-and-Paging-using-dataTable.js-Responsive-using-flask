from flask import Flask
from flask import Flask, render_template
import requests
import pandas as pd
import random
import csv

app=Flask(__name__,template_folder='templates')

@app.route('/')
def hello_world():
    with open("sample_data.csv", mode='r') as infile:

        reader = csv.reader(infile, skipinitialspace=True)
        keys = next(reader)
        ret_list = []
        for row in reader:
            ret_list.append({})
            for key, value in zip(keys, row):
                ret_list[-1][key] = value
        
    return render_template("index.html",len = len(ret_list), data=ret_list)

   

if __name__ == "__main__":
    port = 5000 + random.randint(0, 999)
    app.run(debug=True, port=port)
    # app.run()
