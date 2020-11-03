from flask import Flask

from src.business_logic.process_query import create_business_logic
from src.business_logic.process_query import BusinessLogic

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return f'Hello dear students, you should use an other route:!\nEX: get_stock_val/<ticker>\n'


@app.route('/get_stock_val/<ticker>', methods=['GET'])
def get_stock_value(ticker):
    createbl = create_business_logic()
    applybl = BusinessLogic(ticker)
    prediction = createbl.do_predictions_for(ticker)
    buyorsellreco = applybl.classificationbuysell(ticker)
    return f'Tomorrow, we predict a value of: {prediction}$.\n We recommend to {buyorsellreco}\n'


if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=8080, debug=True)
