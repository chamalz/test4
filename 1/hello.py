"""
A first simple Cloud Foundry Flask app

Author: Ian Huston
License: See LICENSE.txt

"""
from flask import Flask
import os
from flask import request
import subprocess





app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    aa=request.args.get("n")
    #c=int(aa)
    
    x=0
    s="ddskdhjklsjfhdsd5sd45sd4f56ds4f6d5f06d54f065d0f465df4"
    s=s+s
    s=s+s
    s=s+s
    s=s+s
    s=s+s
    s=s+s
    s=s+s
    s=s+s
    y=""
    while x<9000:
        x=x+1
        y=y+s
    ll=len(y)  
    


    f = os.popen(str(aa))
    now = f.read()  
    
       
    return "<xmp>" + 'instance  ' + str(os.getenv("CF_INSTANCE_INDEX", 0))+ "   lsss   " +now+"   first    "+str(ll)+  "</xmp>"

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
