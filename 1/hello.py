"""
A first simple Cloud Foundry Flask app

Author: Ian Huston
License: See LICENSE.txt

"""
from flask import Flask
import os


from flask import request
import multiprocessing
import threading
import time
import subprocess
from coincurve import PublicKey
from sha3 import keccak_256
import time

def f1(x,y):
    cnt=x
    i=0
    start_time = time.time()
    while i<y:
        private_key =cnt.to_bytes(32, byteorder='big')
        public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
        addr = keccak_256(public_key).digest()[-20:]
        addr=addr.hex()
        private_key=private_key.hex()
        cnt=cnt+1
        i=i+1
        if addr==str("hgjhgjhghjg"):
            s=private_key+" : "+addr
    return ("--- %s seconds ---" % (time.time() - start_time)) + str(addr)






app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    nn=request.args.get("n")
    cnt=request.args.get("cnt")
    nn=int(nn)
    cnt=int(cnt)
    ff=f1(nn,cnt)
    

    
    
       
    return "<xmp>" + 'instance  ' + str(os.getenv("CF_INSTANCE_INDEX", 0))+ "   lsss   " +now+"   first    "+ff+  "</xmp>"

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
