import json

player={
    "jersey":4,
    "name":"virgil van dyjk",
    "gender":"male",
    "age":29,
    "country":"netherlands",
    "club":"liverpool",
    "position":"defender"
}

file=open("playerdetails.json","w")
json.dump(player,file)
print('data written to json successfully')
file.close()