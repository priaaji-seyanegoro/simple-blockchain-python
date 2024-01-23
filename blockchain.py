import sys
import hashlib
import json
import blockchain
from uuid import uuid4
from flask.json import jsonify

from flask import Flask, request
from time import time


class Blockchain(object):
  difficulty_target = "0000"

  def hash_block(self, block):
    block_endcoded = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_endcoded).hexdigest()

  def __init__(self):
    self.chain = []
    self.current_transactions = []
    genesis_hash = self.hash_block("genesis_block")
    self.append_block(
        hash_of_previous_block=genesis_hash,
        nonce=self.proof_of_work(0, genesis_hash, []),
    )

  def proof_of_work(self, index, hash_of_previous_block, transactions):
    nonce = 0
    while self.valid_proof(index, hash_of_previous_block, transactions,
                           nonce) is False:
      nonce += 1
    return nonce

  def valid_proof(self, index, hash_of_previous_block, transactions, nonce):
    content = f"{index}{hash_of_previous_block}{transactions}{nonce}"
    content_hash = hashlib.sha256(content.encode()).hexdigest()
    return content_hash[:len(self.difficulty_target)] == self.difficulty_target

  def append_block(self, hash_of_previous_block, nonce):
    block = {
        "index": len(self.chain),
        "timestamp": time(),
        "transactions": self.current_transactions,
        "nonce": nonce,
        "hash_of_previous_block": hash_of_previous_block
    }
    self.current_transactions = []
    self.chain.append(block)
    return block

  def add_transcation(self, sender, recipient, amount):
    self.current_transactions.append({
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    })
    return self.last_block["index"] + 1

  @property
  def last_block(self):
    return self.chain[-1]
  
app = Flask(__name__)
node_identifier = str(uuid4()).replace("-", "")
blockchain = blockchain.Blockchain()

@app.route('/blockchain', methods=['GET'])
def full_chain():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return jsonify(response), 200
  
@app.route('/mine', methods=['GET'])
def mine_block():
  blockchain.add_transcation(sender="0", recipient=node_identifier, amount=1)
  last_block_hash = blockchain.hash_block(blockchain.last_block)
  index = len(blockchain.chain)
  nonce = blockchain.proof_of_work(index, last_block_hash, blockchain.current_transactions)
  block = blockchain.append_block(last_block_hash, nonce)
  response = {
      'message': "New Block Forged",
      'index': block['index'],
      'hash_of_previous_block': block['hash_of_previous_block'],
      'nonce': block['nonce'],
      'transactions': block['transactions']
  }
  return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
  values = request.get_json()
  required = ['sender', 'recipient', 'amount']
  if not all(k in values for k in required):
    return 'Missing values', 400
  index = blockchain.add_transcation(values['sender'], values['recipient'], values['amount'])
  response = {'message': f'Transaction will be added to Block {index}'}
  return jsonify(response), 201

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=int(sys.argv[1]))