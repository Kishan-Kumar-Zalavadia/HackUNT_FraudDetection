# Fraudulent Transaction Detection API

This is a Flask-based web application that allows users to check whether a transaction is potentially fraudulent based on transaction data. The application includes a basic logic for fraud detection and serves a simple HTML page where users can input a transaction ID to check its status.

## Features
- **Fraud Detection Logic**: Determines if a transaction is fraudulent based on basic rules (e.g., amount threshold).
- **REST API**: Exposes an API endpoint (`/check_fraud`) that accepts transaction IDs via JSON and returns whether the transaction is fraudulent.
- **HTML Form**: A simple web form to input transaction IDs and display results dynamically.
- **JSON Data**: Uses a `transactions.json` file to simulate a database of transactions.

## Technologies Used
- **Flask**: For building the web server and API.
- **HTML/CSS**: For the user interface.
- **JavaScript (Fetch API)**: For sending requests to the Flask API and updating the web page dynamically.

## Setup and Installation

### Prerequisites
- Python 3.x
- Flask
- JSON data file (`transactions.json`) with transaction data

### 1. Clone the repository

### 2. Install dependencies
Create a virtual environment (optional but recommended) and install the required packages:
```bash
python3 -m venv venv
source venv/bin/activate 
pip install Flask
```

### 3. Prepare/include `transactions.json`

### 4. Run the Flask app
```bash
python main.py
```

### 5. Access the Application
Open your browser and go to:
```
http://127.0.0.1:5000/
```
Enter a transaction ID (e.g., "tx_001") and check if the transaction is valid or fraudulent.

## API Endpoints

### 1. `/check_fraud` (POST)
This endpoint accepts a transaction ID as input and returns a fraud status.
- **Request Body** (JSON):
  ```json
  {
      "transaction_id": "tx_001"
  }
  ```
- **Response** (JSON):
  ```json
  {
      "transaction_id": "tx_001",
      "is_fraud": false,
      "amount": 500.0,
      "old_balance": 1000.0,
      "new_balance": 500.0
  }
  ```


## Contributing
Feel free to open issues or submit pull requests if you have any improvements to suggest or find bugs in the application.

## License
This project is licensed under the MIT License.