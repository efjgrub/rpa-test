#!/usr/bin/env python

import uuid
import json
from flask import Flask, jsonify, request
import random

from datetime import date

today = date.today()


app = Flask(__name__)

token = "tokendeexemplo"
cnpjok = '99.999.999/0001-99'
cnpjerr = '99.999.999/0002-99'

@app.route('/sample/crm/consulta', methods=["POST","GET"])
def crm():

    if request.method == 'POST':
        req_data = request.get_json()
        try:
            tokenin = request.headers['token']
            cnpjin = req_data['cnpj']
        except:
            ret = {
                "status": "denied",
                "message": "Invalid parameters"
            }
            return(jsonify(ret))
        
        if tokenin != token:
            ret = {
                "status": "denied",
                "message": "Invalid token"
            }
            return(jsonify(ret))
   
        if cnpjin == cnpjok:
            ret = {
                    "cnpj": cnpjin,
                    "status": "OK",
                    "Name": "Company sample 1",
                    "Address": " 767 5th Ave",
                    "City": "New York",
                    "Estate": "NY",
                    "d": []
            }
            return(jsonify(ret))
        elif cnpjin == cnpjerr:
            ret = {
                    "cnpj": cnpjin,
                    "status": "debt",
                    "Name": "Company sample 2",
                    "Address": " 242 W 41st St",
                    "City": "New York",
                    "Estate": "NY",
                    "d": [
                        {
                            "mouth": "April",
                            "year": "2020",
                            "value": 10000
                        },
                          {
                            "mouth": "January",
                            "year": "2020",
                            "value": 20000
                        }
                    ]
            }
            return(jsonify(ret))
        else:
            ret = {
                "status": "error",
                "message": "Invalid request"
            }
            return(jsonify(ret))
    else:
        return('DOC')

@app.route('/sample/servicedesk/ticket', methods=["POST","GET"])
def servicedesk():
    if request.method == 'POST':
        req_data = request.get_json()
        print(req_data)
        try:
            tokenin = request.headers['token']
            cnpjin = req_data['cnpj']
        except Exception as e:
            err = f'"{e}"' 
            ret = {
                "status": "denied",
                "message": "Invalid parameters",
                "Error": err
            }
            return(jsonify(ret))
        
        if tokenin != token:
            ret = {
                "status": "denied",
                "message": "Invalid token"
            }
            return(jsonify(ret))
        if not req_data['Problem']:
            ret = {
                "status": "Error",
                "message": "Problem field is necessary"
            }
            return(jsonify(ret))
        if cnpjin == cnpjok or cnpjin == cnpjerr:
            id = random.randrange(0, 999999, 4)
            d1 = today.strftime("%d/%m/%Y")
            
            ret = {
                "status": "New ticket created ",
                "ticketTitle": req_data['Problem'],
                "id": id,
                "date": d1
            }
            return(jsonify(ret))
    else:
        return('DOC')  
    
if __name__ == '__main__':
    app.run(port=8888, host='0.0.0.0')
