## this is simple JWT signer taken from https://www.jsonwebtoken.io/

var uuid = require('uuid');
var nJwt = require('njwt');

var claims = {
"role":"admin"
}

var jwt = nJwt.create(claims,"lol","HS512");
var token = jwt.compact();
console.log(token);
