from flask import Flask,redirect,url_for,render_template,request,session
from doctors.fun import checkdoctor
from doctors.fun import checkname
from doctors.fun import checkpsw
from doctors.fun import getname
from patients.patient import getpatients
from patients.patient import addpatient

app = Flask(__name__)
app.secret_key="hello"
@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        id=request.form["id"]
        name=request.form["username"]
        psw=request.form["password"]
        namemes=checkname(name)
        pswmes=checkpsw(psw)
        if(namemes==pswmes=="valid"):
          if checkdoctor(id,name,psw):
            session["doctor"]=id
            return redirect(url_for("viewpatients"))
          else:
            return render_template("login.html",content="Name not registered in the site")
        else:
            return render_template("login.html",content1=namemes,content2=pswmes)

    else:
        return render_template("login.html")

@app.route('/viewpatients')
def viewpatients():
        if "doctor" in session:
         ##  addpatient(0,"hamad","abosbet","206736357","21","0","0")
           return render_template("patientslist.html",content=getname(session["doctor"]),pplist=getpatients(int(session["doctor"])))

@app.route('/addpatients',methods=["POST","GET"])
def addpatients():
        if "doctor" in session:
           if request.method=="POST":
               firstname=request.form["patFirstName"]
               lastname=request.form["patLastName"]
               idnum=request.form["patid"]
               age=request.form["patage"]
               gender=str(request.form["gender"])
               smoke=str(request.form["smoke"])
               wbc=request.form["wbc"]
               neut=request.form["neut"]
               lymph=request.form["lymph"]
               Creatinine=request.form["Creatinine"]
               hdl=request.form["hdl"]
               iron=request.form["iron"]
               urea=request.form["urea"]
               rbc=request.form["rbc"]
               akal=request.form["akal"]
               hct=request.form["hct"]
               hb=request.form["hb"]
               eth= request.form.get("eth")!=None
               wes=request.form.get("wes")!=None
               addpatient(session["doctor"],firstname,lastname,idnum,age,gender,smoke,wbc,neut,lymph,Creatinine,hdl,iron,urea,rbc,akal,hct,hb,eth,wes)
               return redirect(url_for("viewpatients"))
           else:
                  return render_template("patients.html",content=getname(session["doctor"]))





if __name__=="__main__":
    app.run(debug=True)
