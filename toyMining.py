import hashlib

# your target
target = ''

#timestanp and nonce values
ts = 0
n = 1

# find digest
while True:
    if n > 1048576:
        ts += 1
        n = 1
    #hash strings that look like:
    s = f":target={target}:timestamp={ts}:nonce={n}:DATA:"
    digest = hashlib.sha256(hashlib.sha256(bytes(s, encoding="utf8")).digest()).hexdigest()
    iterations = ts * 1048576 + n
    if digest.startswith(target):
        break
    n += 1

print("ID = 101272537")
print("iterations = {:,}".format(iterations))
print("timestamp =", ts)
print("nonce = {:,}".format(n))
print("s =", s)
print("digest =", digest)
