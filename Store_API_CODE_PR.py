#Note-For Instruction please read the Description of this File.
from flask import Flask,request
import json
from datetime import datetime

app = Flask(__name__)
@app.route("/Store/<string:JSONArray>")
def store(JSONArray):
    from datetime import datetime
    # print(date_time)
    tax_rates = {"Food": 0.05, "Medicine": 0.05, "clothesL1k": 0.05, "Imported": 0.18, "Book": 0,"Music":0.03,"clothesG1k":0.12}
    date_and_time = datetime.now()

    JSON_OBJECT_LIST = json.loads(JSONArray)
    lst = []

    for JSON_OBJECT in JSON_OBJECT_LIST:
        final_dict = {}
        final_dict['item'] = JSON_OBJECT['item']
        price = JSON_OBJECT['price'] * JSON_OBJECT['quantity']
        if (JSON_OBJECT['itemCategory'] == "Clothes"):
            if (JSON_OBJECT['price'] < 1000):
                JSON_OBJECT['itemCategory'] = "clothesL1k"
            else:
                JSON_OBJECT['itemCategory'] = "clothesG1k"
        final_dict['final_price'] = price + price * (tax_rates[JSON_OBJECT['itemCategory']])
        final_dict['tax_amount'] = price * (tax_rates[JSON_OBJECT['itemCategory']])
        final_dict['tax_rate'] = (tax_rates[JSON_OBJECT['itemCategory']])
        lst.append(final_dict)
    JSON_OBJECT_LIST = json.dumps(lst)
    return JSON_OBJECT_LIST
if __name__=="__main__":
    app.run(debug=True,port=9000)
