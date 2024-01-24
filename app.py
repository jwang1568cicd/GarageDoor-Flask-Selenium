from flask import Flask, flash, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    #name = request.args.get("name")
    print('render_template call index.html')
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
