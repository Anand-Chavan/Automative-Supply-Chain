import datetime
import hashlib
import time
from uuid import uuid4  
from flask import Flask, jsonify

class Block(object):  
      
    def __init__(self, index, proof, previous_hash):#, transactions):  
        self.index = index  
        self.proof = proof  
        self.previous_hash = previous_hash  
        # self.transactions = transactions  
        self.timestamp = time.time()  
  
    @property  
    def get_block_hash(self):  
        block_string = "{}{}{}{}".format(self.index, self.proof, self.previous_hash, self.timestamp)  #, self.transactions,
        return hashlib.sha256(block_string.encode()).hexdigest()


class BlockChain(object):  
      
    def __init__(self):  
        self.chain = []  
        self.current_node_transactions = []  
        self.create_genesis_block()  

    def create_genesis_block(self):  
    	self.create_new_block(proof=0, previous_hash=0)

    def create_new_block(self, proof, previous_hash):  
	    block = Block(  
	        index=len(self.chain),  
	        proof=proof,  
	        previous_hash=previous_hash,  
	    )  
	  
	    self.chain.append(block)  
	    return block
 
  
# app = Flask(__name__)  
  
# blockchain = BlockChain()  

  
  
# @app.route('/show_block_data', methods=['GET'])  
# def show_block_data():  
    
#     block = blockchain.create_new_block(1,2).get_block_hash
      
#     response = {  
#         'message': 'Successfully Create  New Block',  
#         'Hash': block  
#     }  
#     return jsonify(response)
  
  
  
# app.run(debug=True)