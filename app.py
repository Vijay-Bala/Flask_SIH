import os
import pandas as pd
from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api, Resource
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("cred1.json", scope)
client = gspread.authorize(creds)

sheets_id = '1IVBLRJCX7Fr79PP7_Tc_o9Ml0g9Uv2Q6JS3dqrSqeXY'
sheet = client.open_by_key(sheets_id).sheet1
df = pd.read_csv("https://docs.google.com/spreadsheets/d/1IVBLRJCX7Fr79PP7_Tc_o9Ml0g9Uv2Q6JS3dqrSqeXY/export?format=csv")
df = df[1:]

def get_records():
    df = pd.DataFrame(sheet.get_all_records())
    records = df.to_dict(orient='records')
    return records

app = Flask(__name__)
CORS(app)

api = Api(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/map.html')
def fun3():
    return render_template('map.html')

@app.route('/main.html')
def fun():
    return render_template('main.html')

@app.route('/main2.html')
def fun2():
    return render_template('main2.html')

@app.route('/leak.html')
def fun4():
    return render_template('leak.html')

class All(Resource):
    def get(self):
        return get_records()

class Flow(Resource):
    def get(self, val):
        records = get_records()
        return [i for i in records if i['type'].lower().startswith(val.lower())]

class Time(Resource):
    def get(self, val):
        records = get_records()
        return [i for i in records if i['Time'].lower().startswith(val.lower())]

api.add_resource(All, '/api/')
api.add_resource(Flow, '/api/flow/<string:val>')
api.add_resource(Time, '/api/time/<string:val>')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
