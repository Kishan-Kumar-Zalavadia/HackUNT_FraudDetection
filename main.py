import pandas as pd
from flask import Flask, request, jsonify, render_template
import json

# Create a Flask app
app = Flask(__name__)
@app.route('/')
def transaction_form():
    return render_template('transaction.html')
with open('transactions.json', 'r') as f:
    transactions = json.load(f)

def is_fraud(transaction):
    # Rule 1: High amount (above $10,000 is suspicious)
    if transaction['amount'] > 10000:
        return True

    # Rule 2: Balance mismatch (error in balance calculation)
    if (transaction['oldBalanceOrig'] - transaction['amount']) != transaction['newBalanceOrig']:
        return True

    # Rule 3: Zero balance destination with significant amount
    if transaction['oldBalanceDest'] == 0 and transaction['amount'] > 1000:
        return True

    # Add more rules as needed
    return False

# Define the API endpoint
@app.route('/check_fraud', methods=['POST'])
def check_fraud():
    # Get the transaction_id from the POST request
    data = request.get_json(force=True)
    transaction_id = data.get('transaction_id')

    # Find the transaction with the given transaction_id
    transaction = next((tx for tx in transactions if tx["transaction_id"] == transaction_id), None)

    if transaction:
        print("coming")
        # Check if the transaction is fraudulent
        fraud_result = is_fraud(transaction)
        return jsonify({
            'transaction_id': transaction_id,
            'is_fraud': fraud_result
        })
    else:
        return jsonify({
            'error': 'Transaction not found'
        }), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)