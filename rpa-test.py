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
                    "Name": "Empresa de modelo 1",
                    "Logradouro": "Av. das americas, 2000",
                    "Cidade": "Santa Fé",
                    "Estado": "SP",
                    "debitos": []
            }
            return(jsonify(ret))
        elif cnpjin == cnpjerr:
            ret = {
                    "cnpj": cnpjin,
                    "status": "ERR",
                    "Name": "Empresa de modelo 2",
                    "Logradouro": "Av. europa, 1000",
                    "Cidade": "Santa falta de pagamento",
                    "Estado": "SP",
                    "debitos": [
                        {
                            "mes": "Abril",
                            "ano": "2020",
                            "valor": 10000
                        },
                          {
                            "mes": "Janeiro",
                            "ano": "2020",
                            "valor": 20000
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
                "status": "Ticket criado",
                "tiketTile": req_data['Problem'],
                "id": id,
                "date": d1
            }
            return(jsonify(ret))
    else:
        return('DOC')  
    
if __name__ == '__main__':
    app.run(port=8888, host='0.0.0.0')
