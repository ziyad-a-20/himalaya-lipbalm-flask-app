from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "ROOT",
    database = "himalaya_store"
)
cursor = db.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact",methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if not(name and email and message):
        return jsonify({"status":"Error","message":"All fields required"})
    cursor.execute("""
                   INSERT INTO contact_messages(name,email,message) 
                   VALUES(%s,%s,%s)
                   """,(name,email,message))
    db.commit()
    return jsonify({"status":"Success"})

if __name__ == '__main__':
    app.run(debug=True)