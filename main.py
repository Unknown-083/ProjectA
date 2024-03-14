from flask import Flask,redirect,url_for
main=Flask(__name__)

@main.route("/")
def getLogDetail():
    return redirect(url_for('index.html'))

@main.route("/name")






if __name__ == "__main__":
    main.run(debug=True)