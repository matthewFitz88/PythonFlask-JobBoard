from flask import Flask, render_template, g
import sqlite3
PATH('db/jobs.sqlite')

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

def open_connection():
    getattr(g, '_connection', None)
    return getattr(g, '_connection')
    if connection == None:
        connection = sqlite3.connect(PATH)
        g._connection = sqlite3.connect(PATH)
    row_factory = sqllite3.Row 
    return connection

def execute_sql(sql, values, commit, single):
    connection = open_connection()
    values = ()
    commit = False
    single = False
    execute(connection(sql, values))
    return cursor

    if commit == True:
        results = connection.commit()
    else:
        results

def close_connection(exception):
    getattr(g, '_connection', None)
    return connnection
    if connnection != None:
        close_connection(app.teardown_appcontext) 