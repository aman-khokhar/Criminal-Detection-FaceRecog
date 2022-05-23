import numpy
from flask import Flask, request,jsonify
from flask_ngrok import run_with_ngrok
import mysql.connector
import base64
import cv2
import face_recognition
from werkzeug.utils import secure_filename
app = Flask(__name__)
run_with_ngrok(app)
conn = mysql.connector.connect(host="localhost", user="root", password="")
mycusrsor = conn.cursor(buffered=True)

global isdetectbyphoto
isdetectbyphoto=False
global detectbyphotoimg
global photoid

def decoding_FaceStr( encoding_str):
    # Convert to a list
    str = ''.join(encoding_str)
    dlist = str.strip(' ').split(',')
    # Convert str from list to float
    dfloat = list(map(float, dlist))
    face_encoding = numpy.array(dfloat)
    return face_encoding

def adminlogin(id, p):
    global isdetectbyphoto
    mycusrsor.execute("select a_id,a_pass from criminaldetection.admin")
    myresult = mycusrsor.fetchall()
    id=int(id)
    flag=0
    for i in myresult:
        if i[0] == id and i[1] == p:
            flag = 1
        else:
            pass
    if flag==1:
        isdetectbyphoto = False
        return jsonify("login successfull")
    else:
        return jsonify("incorrect id and password")

def userlogin(id1, p1):
    mycusrsor.execute("select u_id,u_pass from criminaldetection.user")
    myresult = mycusrsor.fetchall()
    id1 = int(id1)
    flag=0
    for i in myresult:
        if i[0] != id1 and i[1] != p1:
            pass
        else:
            flag = 1
    if flag == 1:
        return jsonify("login successfull")
    else:
        return jsonify("incorrect id and password")

def forgotPassword(id1, p1):
    mycusrsor.execute("select a_recovery_code from criminaldetection.admin")
    myresult=mycusrsor.fetchall()
    id1=int(id1)
    for i in myresult:
        if id1==i[0]:
            sql = ("update criminaldetection.admin set a_pass=%s where a_recovery_code=%s")
            data = (p1,id1)
            mycusrsor.execute(sql, data)
            conn.commit()
            return jsonify("recovery code is valid")
        else:
            pass
    return jsonify("recovery code is not valid")

@app.route('/ForgotPassword', methods=['POST', 'GET', 'PUT'])
def put():
    rcode = request.form['recovery_code']
    pwd= request.form['pass']
    return forgotPassword(rcode,pwd)

@app.route('/AdminLogin', methods=['POST', 'GET', 'PUT'])
def AdminLogin():
    #print(request.form['id'], request.form['password'])
    return adminlogin(request.form['id'], request.form['password'])



@app.route('/UserLogin', methods=['POST', 'GET', 'PUT'])
def UserLogin():
    uid = request.form['id']
    pwd = request.form['password']
    #print(request.form['id'], request.form['password'])
    return userlogin(uid, pwd)




@app.route('/AddUSer', methods=['POST', 'GET', 'PUT'])
def AddUSer():
    uid = request.form['id']
    uname = request.form['name']
    upwd = request.form['password']
    uemail = request.form['email']
    ucontact = request.form['contact']
    sql = ("insert into criminaldetection.user(u_id,u_name,u_pass,u_email,u_contact)""values(%s,%s,%s,%s,%s)")
    data = (uid, uname, upwd, uemail, ucontact)
    try:
        # Executing the SQL command
        mycusrsor.execute(sql, data)
        # Commit your changes in the database
        print("successfull")
        conn.commit()

    except:
        # Rolling back in case of error
        conn.rollback()
        print("unsuccessfull")
    return jsonify(uid, uname, upwd, uemail, ucontact)

@app.route('/GetCriminalImage', methods=['POST', 'GET', 'PUT'])
def GetCriminalImage():
    cid = request.form['cid']
    cid=int(cid)
    sql = ("select c_photo from criminaldetection.criminal where c_id=%s")
    data = (cid,)
    mycusrsor.execute(sql, data)
    myresult = mycusrsor.fetchone()
    #print(type(myresult))
    with open(myresult, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    #print(image_data)
    return jsonify(image_data)
    #return (myresult)


@app.route('/AddAdmin', methods=['POST', 'GET', 'PUT'])
def AddAdmin():
    aid = request.form['id']
    aname = request.form['name']
    apwd = request.form['password']
    aemail = request.form['email']
    acontact = request.form['contact']
    apost = request.form['post']
    arecovery = request.form['recoveycode']

    sql = (
        "insert into criminaldetection.admin(a_id,a_name,a_pass,a_email,a_contact,a_post,a_recovery_code)""values(%s,%s,%s,%s,%s,%s,%s)")
    data = (aid, aname, apwd, aemail, acontact, apost, arecovery)
    try:
        # Executing the SQL command
        mycusrsor.execute(sql, data)
        # Commit your changes in the database
        print("successfull")
        conn.commit()
    except:
        # Rolling back in case of error
        conn.rollback()
        print("unsuccessfull")
    return jsonify(aid, aname, apwd, aemail, acontact, apost, arecovery)


@app.route('/DetectByPhoto', methods=['POST', 'GET', 'PUT'])

def DetectByPhoto():
    global isdetectbyphoto
    global photoid
    curimg = request.form['cphoto']
    isdetectbyphoto=True
    #print(isdetectbyphoto)
    inputimge = face_recognition.load_image_file(curimg)
    inputimge = cv2.cvtColor(inputimge, cv2.COLOR_BGR2RGB)
    facesLocCurImg = g = face_recognition.face_locations(inputimge)
    inputencode = face_recognition.face_encodings(inputimge)
    detectbyphotoimg=inputencode
    mycusrsor.execute("select c_encode_photo from criminaldetection.criminal")
    myresult = mycusrsor.fetchall()
    j=0
    for i in myresult:
        j=j+1
        print(i)
        dbencode=decoding_FaceStr(i)
        matches = face_recognition.compare_faces(inputencode, dbencode)
        faceDis = face_recognition.face_distance(inputencode, dbencode)
        #print(matches,faceDis)
        if not matches:
            pass
        else:
            if matches[0]:
                sql="select c_fname,c_mname,c_lname,crime_record from criminaldetection.criminal where c_id=%s"
                d=(j,)
                photoid=j
                mycusrsor.execute(sql,d)
                myresult = mycusrsor.fetchone()
                print(myresult)
                return jsonify(myresult)
    return jsonify("match not found")

@app.route('/LiveDetection', methods=['POST', 'GET','PUT'])
def LiveDetection():
    global isdetectbyphoto
    global detectbyphotoimg
    global photoid
    if isdetectbyphoto==True :
        print("deteted by photo")
        curimg = request.form['curimg']
        inputimge = face_recognition.load_image_file(curimg)
        cv2.imshow('Webcam', inputimge)
        inputimge = cv2.cvtColor(inputimge, cv2.COLOR_BGR2RGB)
        inputencode = face_recognition.face_encodings(inputimge)
        photoid=int(photoid)
        sql="select c_encode_photo from criminaldetection.criminal where c_id=%s"
        d = (photoid,)
        mycusrsor.execute(sql, d)
        for i in mycusrsor:
            dbencode = decoding_FaceStr(i)
            matches = face_recognition.compare_faces(inputencode, dbencode)
            faceDis = face_recognition.face_distance(inputencode, dbencode)
            faceLoc = face_recognition.face_locations(inputimge)
            if not matches:
                pass
            else:
                if matches[0]:
                    sql = "select c_id,c_fname,c_mname,c_lname,crime_record from criminaldetection.criminal where c_id=%s"
                    d = (photoid,)
                    mycusrsor.execute(sql, d)
                    myresult = mycusrsor.fetchone()
                    mylist = [myresult, faceLoc]
                    return jsonify(mylist)

        return jsonify("match not found")

    else:
        print("live feed")
        curimg = request.form['curimg']
        inputimge = face_recognition.load_image_file(curimg)
        cv2.imshow('Webcam', inputimge)
        inputimge = cv2.cvtColor(inputimge, cv2.COLOR_BGR2RGB)
        inputencode = face_recognition.face_encodings(inputimge)
        mycusrsor.execute("select c_encode_photo from criminaldetection.criminal")
        #myresult = mycusrsor.fetchall()
        j=0
        for i in mycusrsor:
            j=j+1
            dbencode = decoding_FaceStr(i)
            matches = face_recognition.compare_faces(inputencode, dbencode)
            faceDis = face_recognition.face_distance(inputencode, dbencode)
            faceLoc= face_recognition.face_locations(inputimge)
            print(matches)
            if not matches:
                pass
            else:
                if matches[0]:
                    sql = "select c_id,c_fname,c_mname,c_lname,crime_record from criminaldetection.criminal where c_id=%s"
                    d = (j,)
                    mycusrsor.execute(sql, d)
                    myresult = mycusrsor.fetchone()
                    mylist=[myresult,faceLoc]
                    return jsonify(mylist)

        return jsonify("match not found")


@app.route('/RegisterCriminal',methods = ['POST', 'GET','PUT'])
def getCriminal():
   if request.method == 'POST':
       cid = request.form['cid']
       cphoto = request.files['cphoto']
       cfname = request.form['cfname']
       cmname = request.form['cmname']
       clname = request.form['clname']
       cnickname = request.form['cnickname']
       chomeaddress = request.form['chomeaddress']
       ccrimerecord = request.form['crimerecord']

       imgOne = face_recognition.load_image_file(cphoto)
       imgOne = cv2.cvtColor(imgOne, cv2.COLOR_BGR2RGB)
       faceLocMain = face_recognition.face_locations(imgOne)[0]
       img_face_encoding = face_recognition.face_encodings(imgOne)[0]

       cphoto.save(secure_filename(cphoto.filename))
       url = cphoto.filename
       with open(url,"rb") as image_file:
           encoded_string=base64.b64decode(image_file.read())
       args=encoded_string

       encoding_array_list = img_face_encoding.tolist()
       encoding_str_list = [str(i) for i in encoding_array_list]
       encoding_str = ', '.join(encoding_str_list)
       db= encoding_str
       mycusrsor = conn.cursor()
       sql = (
           "INSERT INTO criminaldetection.`criminal`(`c_id`, `c_photo`, `c_encode_photo`, `c_fname`, `c_mname`, `c_lname`, `c_nickname`, `c_home_address`, `crime_record`)""VALUES(%s,%s,%s, %s, %s,%s,%s,%s,%s)")
       data = (cid, args,db, cfname, cmname, clname, cnickname, chomeaddress, ccrimerecord)
       try:
           # Executing the SQL command
           mycusrsor.execute(sql, data)
           # Commit your changes in the database
           conn.commit()
           return jsonify("successfull")
       except:
           # Rolling back in case of error
           conn.rollback()
           return jsonify("successfull")
       print (cid, cphoto, cfname, cmname, clname, cnickname, chomeaddress, ccrimerecord)

app.run()