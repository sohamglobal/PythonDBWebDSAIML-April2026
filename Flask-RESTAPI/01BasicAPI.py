from flask import Flask

app=Flask(__name__)

@app.route('/profile',methods=['GET'])
def get_profile():
    p={
        "name":"praffull",
        "company":"sohamglobal",
        "post":"co-founder",
        "city":"london",
        "qualification":"mba",
        "email":"praffull@outlook.com",
        "mobile":"7391966656"
    }
    return p

@app.route('/player/<country>',methods=['GET'])
def get_player(country):
    player={
        "name":"jos buttler",
        "country":country,
        "club":["titans","manchester"],
        "age":35,
        "gender":"male"

    }
    return player

if __name__=='__main__':
    app.run(debug=True)
