import jwt

public=open('public.pem','r').read()

print(public)

toto=jwt.encode({"username":"admin","admin":True,"iat": 1567179785, "exp": 1567266185}, key=public, algorithm='HS256') #pip install pyjwt==0.4.3
print(toto)
