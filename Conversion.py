import flask
from flask.json import jsonify
import requests
from datetime import datetime
from flask import request



app = flask.Flask(__name__)
app.config["DEBUG"] = True

API_KEY = 'CBBYZVB4IR3RN85E'
@app.route('/<string:firstcurrenct>/<string:secondcurrency>/<int:amount>', methods = ['GET','POST'])
def root(firstcurrenct,secondcurrency,amount):
     if request.method == 'GET':
            try:
                amount = float(amount)
                url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(
                    firstcurrenct, secondcurrency, API_KEY)
                response = requests.get(url=url).json()
                rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
                rate = float(rate)
                result = rate * amount
                ip_address = request.remote_addr
                print(ip_address)
                reqUrl = request.url  
                print(reqUrl)
                reqTime = datetime.now()
                print(reqTime)
                # response.headers.add("Access-Control-Allow-Origin", "*")
                # params = {"firstcurrenct": firstcurrenct,
                # "secondcurrency": secondcurrency,
                # "amount": amount,
                # "ip_address": ip_address,
                # "reqTime": reqTime,
                # "rate": rate,
                # "result": result
                # }

                jsonResp = {'status':'OK','result':str(result)}
                URL="http://localhost/{}/{}/{}/{}/{}/{}/{}/{}".format(firstcurrenct,secondcurrency,str(amount),str(ip_address)
                ,str(result),rate,reqTime,reqUrl)
                response = requests.get(URL)
                return jsonify(jsonResp)
          
            except Exception as e:
                return '<h1>Bad Request : {}</h1>'.format(e)
     else:
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug = True)
