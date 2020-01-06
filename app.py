from flask import Flask, render_template, json, flash, jsonify, request, url_for, Response, redirect
from flask import flash
from flask_sqlalchemy import SQLAlchemy
import os, csv

app = Flask(__name__, static_folder = "static", template_folder='templates')
app.config['SECRET_KEY']= 'sdfvbukjfn738uif78g2ne8ivb78er'

baseFile = 'data/valid-db.csv'
cacheFile = 'data/cache-db.csv'
dataFile = 'data/data-cache.csv'

#CSV-FUNCTIONS
def csvWriter(data, filename):
    with open(filename, 'a') as csvfileW:
        writerObject=csv.writer(csvfileW)
        writerObject.writerow(data)

def csvWriterSTRING(data, filename):
    with open(filename, 'a') as csvfileWSTR:
        csvfileWSTR.write(data)

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

# db= SQLAlchemy(app)

# class Identity(db.Model):
#     #id = db.Column(db.Integer)
#     usn = db.Column(db.Integer,unique = True, nullable = False, primary_key = True)
#     name = db.Column(db.String(),nullable = False)
#     person = db.relationship("Vote", backref='name', lazy = True)

#     def __repr__(self):
#         return f"USN('{self.name}')"

# class Vote(db.Model):
#     user_id = db.column(db.Integer,db.ForeignKey('identity.usn'))
#     acsg = db.Column(db.Integer(),nullable = False)
#     acsb = db.Column(db.Integer(),nullable = False)
#     asplb = db.Column(db.Integer(),nullable = False)
#     asplg = db.Column(db.Integer(),nullable = False)
#     assb = db.Column(db.Integer(),nullable = False)
#     ass = db.Column(db.Integer(),nullable = False)
#     acs = db.Column(db.Integer(),nullable = False)
#     acs = db.Column(db.Integer(),nullable = False)


    
@app.route("/", methods = ["POST","GET"])
def form():         
    return render_template("login.html")

@app.route("/splb", methods = ["POST","GET"])
def splb():
    if request.form["vote_check"] == "voting":
        return flash("Start Voting!")
    return render_template("splb.html",title = "splb")

@app.route("/splg", methods = ["POST","GET"])
def splg():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("splg.html", title = "splg")

@app.route('/csb',methods=["POST","GET"])
def csb():
    if request.method == "POST":
        if "name4" in request.form: getPollVal="1"
        if "name5" in request.form: getPollVal="2"
        if "name6" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("csb.html", title = "csb")

@app.route('/csg',methods=["POST","GET"])
def csg():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("csg.html", title = "csg")

@app.route('/ssb',methods=["POST","GET"])
def ssb():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("ssb.html", title = "ssb")

@app.route('/ssg',methods=["POST","GET"])
def ssg():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("ssg.html", title = "ssg")

@app.route('/asplb',methods=["POST","GET"])
def asplb():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("asplb.html", title = "asplb")

@app.route('/asplg',methods=["POST","GET"])
def asplg():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("asplg.html", title = "asplg")

@app.route('/acsb',methods=["POST","GET"])
def acsb():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("acsb.html", title = "acsb")

@app.route('/acsg',methods=["POST","GET"])
def acsg():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("acsg.html", title = "acsg")

@app.route('/assb',methods=["POST","GET"])
def assb():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("assb.html", title = "assb")

@app.route('/assg',methods=["POST","GET"])
def assg():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("assg.html", title = "assg")

@app.route('/login',methods = ["POST"])
def login():
    if request.method == "POST":
        getKey= request.form['pwd']
        f=open('data/usn_cache.txt','w')
        f.write(getKey)
        f.close()
        with open(cacheFile) as csvfileR:
            readCSV = csv.reader(csvfileR, delimiter=',')
            cacheUSN = []
            for row in readCSV:
                if row==[]: continue
                cacheUSN.append(row[0])
        if getKey in cacheUSN:
            flash("Wrong USN!!!",category="error")
            return redirect(url_for('form'))
        else:
            f = open(dataFile, "w")
            f.truncate()
            f.close()
            with open(baseFile) as csvfileBase:
                baseUSN=[]
                readBaseCSV = csv.reader(csvfileBase, delimiter=',')
                for baseRow in readBaseCSV:
                    baseUSN.append(baseRow[0])
            if getKey in baseUSN:
                csvWriterSTRING(getKey, dataFile)
                csvWriter('', dataFile)
                flash("LOGGED IN")
                return redirect(url_for('forfeit'))
            else: 
                flash("Wrong USN!!!",category="error")
                return redirect(url_for('form'))
            
@app.route('/forfeit', methods=["POST","GET"])
def forfeit():
    return render_template("forfeit.html")

# def forfeit_data(usnEntered):
#     if "critical_act" in request.form:
#         return redirect(url_for('thank')) 



@app.route('/thank',methods=["POST","GET"]) # need to modify
def thank():
    if request.method == "POST":
        if request.form["critical_act"]=="forfeit":
            f=open('data/usn_cache.txt','r')
            usnEntered=None
            for line in f:
                line=line.strip('\n')
                usnEntered=line
            csvWriterSTRING(usnEntered, 'data/forfeit-db.csv')
            csvWriterSTRING('', 'data/forfeit-db.csv')
            return render_template("thank.html")
        with open(dataFile) as datafileR:
            readdataCSV = csv.reader(datafileR, delimiter=',')
            cacheData = []
            for row in readdataCSV:
                if row==[]: continue
                cacheData.append(row[0])
        csvWriter(cacheData, cacheFile)
        if(request.form == True):
            return render_template("thank.html", title = "Thank You")
    return render_template("thank.html", title = "Thank You")
    
if __name__ == '__main__':
    app.run(host="0.0.0.0" , port = 4000)
