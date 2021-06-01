import io
import os
from patients.patienttest import getillnesses
def getsize(id):
    dic= os.listdir('patients/patientlist')
    count=0
    for x in dic:
           c=(x.split('.')[0]).split('_')
           if (int(c[0])==id):
               count=count+1
    return count
def getpatient(id):
    c={}
    file=open('patients/patientlist/'+id,'r')
    f=file.readlines()
    c["name"]=f[0].strip()
    c["lastname"]=f[1].strip()
    c["id"]=f[2].strip()
    c["gender"]=f[3].strip()
    c["smoke"]=f[4].strip()
    c["illness"]=f[5].strip()
    c["perspiction"]=f[6].strip()
    c["age"]=f[7].strip()
    file.close()
    return c

def getpatients(id):
    l=[]
    dic= os.listdir('patients/patientlist')
    for x in dic:
        if (int(((x.split('.')[0]).split('_'))[0])==id):
            l.append(getpatient(x))
    return l


def addpatient(id,name,lastname,idnum,age,gender,smoke,wbc,neut,lymph,Creatinine,hdl,iron,urea,rbc,akal,hct,hb,eth,wes):
    num=getsize(int(id))
    li=getillnesses(int(age),int(gender),int(smoke),int(wbc),int(neut),int(lymph),int(rbc),int(hct),int(urea),int(hb),float(Creatinine),int(iron),int(hdl),eth,int(akal),wes)
    file=open('patients/patientlist/'+str(id)+'_'+str(num)+'.txt','w+')
    file.write(name+"\n")
    file.write(lastname+"\n")
    file.write(idnum+"\n")
    file.write(gender+"\n")
    file.write(smoke+"\n")
    file.write(li[0]+li[1]+"\n")
    file.write(li[2]+li[3]+"\n")
    file.write(age+"\n")
    file.close()







#print(os.listdir('patientlist'))
#print(getpatient('0_0.txt')
