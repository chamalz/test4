from coincurve import PublicKey
from sha3 import keccak_256
import time
cnt=77777777777772560
i=0
start_time = time.time()
while i<18000:
    private_key =cnt.to_bytes(32, byteorder='big')
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    addr=addr.hex()
    private_key=private_key.hex()
    cnt=cnt+1
    i=i+1
    if addr==str("hgjhgjhghjg"):
     s=private_key+" : "+addr
print("--- %s seconds ---" % (time.time() - start_time))
print (addr)