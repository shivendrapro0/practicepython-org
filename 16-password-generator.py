import random, string

def generatePass(passlen,restrcit):
    password = ""
    for r in restrcit:
        p = ''.join([random.choice(r) for _ in range(int(passlen/restrcit.__len__())) ])
        password = password + p
    password = list(password)
    random.shuffle(password)
    return ''.join(password)

restrcit=[string.digits,string.ascii_letters,string.digits,string.punctuation]
print(generatePass(15,restrcit))
