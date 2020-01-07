from flask import Flask, render_template, json, flash, jsonify, request, url_for, Response, redirect
from flask import flash
import os, csv

app = Flask(__name__, static_folder = "static", template_folder='templates')
app.config['SECRET_KEY']= 'sdfvbukjfn738uif78g2ne8ivb78er'

baseFile = 'data/valid-db.csv'
cacheFile = 'data/cache-db.csv'
dataFile = 'data/data-cache.csv'
#############################################################################
#CSV-FUNCTIONS
def csvWriter(data, filename):
    with open(filename, 'a') as csvfileW:
        writerObject=csv.writer(csvfileW)
        writerObject.writerow(data)

def csvWriterSTRING(data, filename):
    with open(filename, 'a') as csvfileWSTR:
        csvfileWSTR.write(data)

@app.route("/", methods = ["POST","GET"])
def form():        
    return render_template("login.html")

@app.route("/splb", methods = ["POST","GET"])
def splb():
    flash("Start Voting!")
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

@app.route('/in_pres',methods=["POST","GET"])
def in_pres():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("in_pres.html", title = "President")

@app.route('/in_vpres',methods=["POST","GET"])
def in_vpres():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("in_vpres.html", title = "Vice President")

@app.route('/in_sec',methods=["POST","GET"])
def in_sec():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("in_sec.html", title = "Secretary")

@app.route('/in_tres',methods=["POST","GET"])
def in_tres():
    if request.method == "POST":
        if "name1" in request.form: getPollVal="1"
        if "name2" in request.form: getPollVal="2"
        if "name3" in request.form: getPollVal="3"
        csvWriter(getPollVal, dataFile)
    return render_template("in_tres.html", title = "Treasurer")

@app.route('/login',methods = ["POST"])
def login():
    if request.method == "POST":
        getKey= request.form['pwd']
        #print (getKey)
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
            flash("You have already voted!!!",category="error")
            return redirect(url_for('form'))
        else:
            with open('data/forfeit-db.csv') as csvfileR:
                readCSV = csv.reader(csvfileR, delimiter=',')
                forfeitUSN = []
                for row in readCSV:
                    if row==[]: continue
                    forfeitUSN.append(row[0])
            if getKey in forfeitUSN:
                flash("You have forfeited!!",category="error")
                return redirect(url_for('form'))
            f = open(dataFile, "w")
            f.truncate()
            f.close()
            with open(baseFile) as csvfileBase:
                baseUSN=[]
                baseName=[]
                readBaseCSV = csv.reader(csvfileBase, delimiter=',')
                for baseRow in readBaseCSV:
                    baseUSN.append(str(baseRow[0]))
                    baseName.append(str(baseRow[1]))
            for i in range(len(baseUSN)):
                if getKey==baseUSN[i]:
                    csvWriterSTRING(getKey, dataFile)
                    csvWriter('', dataFile)
                    flash(baseName[i]+" IS LOGGED IN")
                    return redirect(url_for('forfeit'))
            else: 
                flash("Wrong USN!!!",category="error")
                return redirect(url_for('form'))
            
@app.route('/forfeit', methods=["POST","GET"])
def forfeit():
    return render_template("forfeit.html")

@app.route('/thank',methods=["POST","GET"]) # need to modify
def thank():
    if request.method == "POST":
        try: 
            req=request.form["critical_act"]    
            if req=="forfeit":
                f=open('data/usn_cache.txt','r')
                usnEntered=None
                for line in f:
                    line=line.strip('\n')
                    usnEntered=line
                csvWriterSTRING(usnEntered, 'data/forfeit-db.csv')
                csvWriterSTRING('\n', 'data/forfeit-db.csv')
                return render_template("thank.html")
        except:
            if "name1" in request.form: getPollVal="1"
            if "name2" in request.form: getPollVal="2"
            if "name3" in request.form: getPollVal="3"
            csvWriter(getPollVal, dataFile)
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
    app.run(host="0.0.0.0" , port = 4000, debug = True) 