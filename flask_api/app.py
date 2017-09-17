from flask import Flask


app = Flask(__name__)

@app.route("/")
def api_endpoint():
    return "This is API endpoint"


@app.route("/resource")
def api_resource():
    return "This is API resource"



if __name__ == '__main__':
    app.run(debug=True)

