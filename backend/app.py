from flask import Flask , request

app = Flask(__name__)

@app.route('/analyze',methods=['GET','POST'])
def hello_world():
    data = request.get_json()
    
    print(data)

    return {"status": "success"}

if __name__ == '__main__':
    app.run(debug=True)