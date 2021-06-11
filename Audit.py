import flask
from pymongo import MongoClient

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/<firstcurrenct>/<secondcurrency>/<amount>/<ip_address>/<result>/<rate>/<reqTime>/<path:reqUrl>', methods = ['GET','POST'])
def root(firstcurrenct,secondcurrency,amount,ip_address,result,rate,reqTime,reqUrl):

    client = MongoClient("mongodb+srv://devops:pNbC9lsRLyQ63HmL@cluster0.eua4t.mongodb.net/devops_project?retryWrites=true&w=majority")
    db = client.get_database('devops_project')   
    records = db.requests
    new_object = {
        'ip_Address': ip_address,
        'Time': reqTime,
        'Browser': reqUrl,
        'Amount': amount,
        'Currency': firstcurrenct,
        'Target_Currency': secondcurrency,
        'Rate': rate,
        'Conversion': result
    }
    records.insert_one(new_object)
    return flask.jsonify(message="success")


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=80 ,debug = True)
