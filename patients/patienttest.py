c={"Anemia":"Two 10mg pills of B12 a day for a month",
"diet":"Arrange an appointment with a nutritionist",
"bleeding":"Urgently evacuate to the hospital",
"Hyperlipidemia (blood lipids)":"Arrange an appointment with a nutritionist a 5 pill of Simvastatin a day for a week.",
"Interference in the formation of blood / blood cells":"10 mg pill of B12 per day for a month 5 mg pill of folic acid per day for 1 month",
"Hematological disorder":"Injection of a hormone to encourage red blood cell production",
"Iron poisoning":"Evacuate to the hospital",
"dehydration":"Complete rest lying down returning fluids in drinking",
"infection":"dedicated antibiotics",
"Vitamin deficiency":"Referral for a blood test to identify the missing vitamins",
"Viral disease":"Rest at home",
"Biliary diseases":"Referral for surgical treatment",
"Heart disease":"Arrange an appointment with a nutritionist",
"Blood disease":"A combiantion of cyclophosphamide and coritcosteroids",
"Liver disease":"Referral to a specific diagnosis for the purpose of determining treatment",
"Kidney disease":"Balancing blood sugar levels",
"Iron deficiency":"Two 10 mg pills of B12 a day for a month",
"Muscle diseases":"Two 5 mg pills of Altman c3 turmeric a day for a month",
"Smoker":"Quit smoking",
"Lung disease":"Quit smoking / referral for an X-ray of the lungs",
"Hyperthyroidism":"Propylthiouracil to decrease thyroid activity",
"Adult diabetes":"Insulin adjustment for the patient",
"Cancer":"Entrectinib",
"Increased consumption of meat":"Arrange an appointment with a nutritionist",
"Use of various medications":"Referral to the family doctor for a match test between the drugs",
"Malnutrition":"Arrange an appointment with a nutritionist"}



def percentage(a, b):
    return round(a / b * 100, 2)
def getillnesses(age,g,s,wbc,neut,lymph,rbc,hct,urea,hb,Creatinine,iron,hdl,e,alka,w):
    prop={}
    proptimes={}
    rare={}
    raretimes={}
    global c
    def addprop(pr):
      nonlocal proptimes
      if pr in proptimes:
          proptimes[pr]=proptimes[pr]+1
      else:
          proptimes[pr]=1
    def addrare(pr):
      nonlocal raretimes
      if pr in raretimes:
          raretimes[pr]=raretimes[pr]+1
      else:
          raretimes[pr]=1

    def wbcc():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if age>=18:
            low=4500
            high=11000
        elif age in range(3,18):
            low=5500
            high=15500
        elif age in range(-1,4):
            low=6000
            high=17500
        else:
            return "invalid"
        if wbc<low:
            prop["Viral disease"]=c["Viral disease"]
            addprop("Viral disease")
            rare["Cancer"]=c["Cancer"]
            addrare("Cancer")

        if wbc>high:
            prop["infection"]=c["infection"]
            addprop("infection")
            rare["Cancer"]=c["Cancer"]
            addrare("Cancer")
            rare["Blood disease"]=c["Blood disease"]
            addrare("Blood disease")

    def neutt():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if percentage(neut,wbc) < 28:
            prop["Interference in the formation of blood / blood cells"]=c["Interference in the formation of blood / blood cells"]
            addprop("Interference in the formation of blood / blood cells")
            prop["infection"]=c["infection"]
            addprop("infection")
            rare["Cancer"]=c["Cancer"]
            addrare("Cancer")
        elif percentage(neut,wbc) >54:
            prop["infection"]=c["infection"]
            addprop("infection")

    def lymphh():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if percentage(lymph,wbc)<36:
            prop["Interference in the formation of blood / blood cells"]=c["Interference in the formation of blood / blood cells"]
            addprop("Interference in the formation of blood / blood cells")
        elif percentage(lymph,wbc) >54:
            prop["infection"]=c["infection"]
            addprop("infection")
            prop["Cancer"]=c["Cancer"]
            addprop("Cancer")

        else:
            return "invalid"
    def ureaa():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if urea<17:
            prop["Malnutrition"]=c["Malnutrition"]
            addprop("Malnutrition")
            prop["diet"]=c["diet"]
            addprop("diet")
            prop["Liver disease"]=c["Liver disease"]
            addprop("Liver disease")

        elif urea>43:
            prop["Kidney disease"]=c["Kidney disease"]
            addprop("Kidney disease")
            prop["dehydration"]=c["dehydration"]
            addprop("dehydration")
            prop["diet"]=c["diet"]
            addprop("diet")

    def hbb():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if age>=18:
            if g==0:
                low=12
                high=18
            else:
                low=12
                high=16
        elif age in range(-1,18):
            low=11.5
            high=15.5
        else:
            return "invalid"
        if(hb<low):
           prop["Anemia"]=c["Anemia"]
           addprop("Anemia")
           prop["bleeding"]=c["bleeding"]
           addprop("bleeding")
           prop["Hematological disorder"]=c["Hematological disorder"]
           addprop("Hematological disorder")
           prop["Iron deficiency"]=c["Iron deficiency"]
           addprop("Iron deficiency")
    def hdll():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if g==0:
            if e==True:
               low=34.8
               high=74.4
            else:
               low=29
               high=62
        else:
            if e==True:
               low=40.8
               high=98.4
            else:
              low=34
              high=82

        if(hdl<low):
            prop["Heart disease"]=c["Heart disease"]
            addprop("Heart disease")
            prop["Hyperlipidemia (blood lipids)"]=c["Hyperlipidemia (blood lipids)"]
            addprop("Hyperlipidemia (blood lipids)")
            prop["Adult diabetes"]=c["Adult diabetes"]
            addprop("Adult diabetes")

    def alkaa():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if w==True:
            low=60
            high=120
        else:
            low=30
            high=90
        if alka<low:
            prop["diet"]=c["diet"]
            addprop("diet")
            prop["Vitamin deficiency"]=c["Vitamin deficiency"]
            addprop("Vitamin deficiency")
        if alka>high:
            prop["Liver disease"]=c["Liver disease"]
            addprop("Liver disease")
            prop["Biliary diseases"]=c["Biliary diseases"]
            addprop("Biliary diseases")
            prop["Hyperthyroidism"]=c["Hyperthyroidism"]
            addprop("Hyperthyroidism")
    def rbcc():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if rbc>6:
            prop["Interference in the formation of blood / blood cells"]=(c["Interference in the formation of blood / blood cells"])
            if s==1:
                prop["Smoker"]=c["Smoker"]
                addprop("Smoker")
            if rbc<4.5:
                prop["Anemia"]=c["Anemia"]
                addprop("Anemia")
                prop["bleeding"]=c["bleeding"]
                addprop("bleeding")


    def hctt():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if g==1:
            if percentage(hct,rbc)>54:
                prop["Smoker"]=c["Smoker"]
                addprop("Smoker")
            elif percentage(hct,rbc)<37:
                prop["bleeding"]=c["bleeding"]
                addprop("bleeding")
                prop["Anemia"]=c["Anemia"]
                addprop("Anemia")
        else:
            if percentage(hct,rbc)<33:
                prop["bleeding"]=c["bleeding"]
                addprop("bleeding")
                prop["Anemia"]=c["Anemia"]
                addprop("Anemia")
            if percentage(hct,rbc)<47:
                prop["Smoker"]=c["Smoker"]
                addprop("Smoker")
    def Creatininee():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if age>=17:
            low=0.6
            high=1
        elif age in range(3,17):
            low=0.5
            high=1
        elif age in range(-1,3):
            low=0.2
            high=0.5
        else:
            return "invalid"
        if Creatinine<low:
            prop["Muscle diseases"]=c["Muscle diseases"]
            addprop("Muscle diseases")
        if Creatinine>high:
            prop["Kidney disease"]=c["Kidney disease"]
            addprop("Kidney disease")
    def Ironn():
        nonlocal prop
        nonlocal rare
        nonlocal proptimes
        nonlocal raretimes
        if g==1:
            if iron>160:
                prop["Iron poisoning"]=c["Iron poisoning"]
                addprop("Iron poisoning")
            elif iron<60:
                prop["Malnutrition"]=c["Malnutrition"]
                addprop("Malnutrition")
        else:
            if iron<48:
                prop["Malnutrition"]=c["Malnutrition"]
                addprop("Malnutrition")
            elif iron>136:
                prop["Iron poisoning"]=c["Iron poisoning"]
                addprop("Iron poisoning")

    wbcc()
    neutt()
    lymphh()
    rbcc()
    hctt()
    ureaa()
    hbb()
    Creatininee()
    Ironn()
    hdll()
    alkaa()
    l=[]
    r="#The probable ilnesses,"
    for i in prop.keys():
        r+=i+"-"+str(proptimes[i])+","
    l.append(r)
    r="#The improbable illnesses,"
    for i in rare.keys():
        r+=i+"-"+str(raretimes[i])+","
    l.append(r)
    r="#The probable ilnesses perspiction,"
    for i in prop.values():
        r+=i+","
    l.append(r)
    r="#The improbable illnesses perspiction,"
    for i in rare.values():
        r+=i+","
    l.append(r)


    return l

#print(getillnesses(18,1,0,12000,100,100,5,2,40,15,0.7,80,40,0,70,0))

#(age,g,s,wbc,neut,lymph,rbc,hct,urea,hb,Creatinine,iron,hdl,e,alka,w)
#print(c["diet"])
