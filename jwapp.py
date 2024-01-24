from flask import Flask, flash, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    #name = request.args.get("name")
    #return render_template(index.html, name=name)
    print ('Render template g2.html')
    #return 'hello jw ret'
    return render_template('g2.html')

if __name__ == '__main__':
    app.run()
