# Simple Blockchain Concept in Python

## Introduction
This project demonstrates a basic implementation of a blockchain using Python with a simple Flask application. Blockchain is a decentralized and distributed ledger that records transactions across a network of computers. Each transaction is added to a chain of blocks in a secure and transparent manner.

## Features
- **Blockchain:** The core blockchain functionality is implemented, consisting of blocks linked together.
- **Mining:** Proof-of-work concept is used for block mining.
- **Transactions:** Simple transaction structure is defined.
- **API Routes:** Basic Flask routes are provided for interacting with the blockchain.

## Getting Started
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/simple-blockchain-python.git
    ```

2. Navigate to the project directory:
    ```bash
    cd simple-blockchain-python
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python blockhain.py PORT
    ```

## API Routes
The following routes can be used to interact with the blockchain:

- **Get Blockchain:**
    - **Endpoint:** `/blockchain`
    - **Method:** `GET`
    - **Description:** Retrieve the entire blockchain.

- **Mine a Block:**
    - **Endpoint:** `/mine`
    - **Method:** `GET`
    - **Description:** Mine a new block and add it to the blockchain.

- **Add a Transaction:**
    - **Endpoint:** `/transactions/new`
    - **Method:** `POST`
    - **Description:** Add a new transaction to the pending transactions list.

## Example Usage
### Get Blockchain
```bash
curl http://localhost:PORT/blockchain
```
### Mine a Block
```bash
curl http://localhost:PORT/mine
```
### Add a Transaction
```bash
curl -X POST -H "Content-Type: application/json" -d '{"sender": "3c1dd188f3c74fb29b21889de1ee4943", "recipient": "0e6b092047a448aa83af316fd1214d51", "amount": 1.5}' http://localhost:PORT/transactions/new

```

