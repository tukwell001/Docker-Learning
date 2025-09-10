from flask import Flask
import MYSQLdb

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    db = MYSQLdb.connect(
        host="mydb",
        user="root",
        passwd="my-secret-pw",
        db="mysql"
    )
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Hello, World! MYSQL version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)