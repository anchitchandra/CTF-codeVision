from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
import pytz

app = Flask(__name__)

session1 = []
session2 = []
session3 = []
session4 = []
session5 = []
BanAccounts = []
attempt_list = {}
IST = pytz.timezone('Asia/Kolkata')
timelist = []


@app.route('/', methods=['GET', 'POST'])
def login():
    pasd = ""
    uid = ""
    msg = ""
    try:
        if request.method == 'POST' or 'GET' and 'log' in request.form:
            uid = request.form.get('uid')
            pasd = request.form.get('pasd')
            msg = request.form.get('msg')

            with open('db.csv', 'r') as db_file:
                db_reader = csv.DictReader(db_file)
                for line in db_reader:
                    if uid in BanAccounts:
                        msg = "Your account has been banned"
                    else:
                        if uid == line['uid'] and pasd == line['password']:
                            try:
                                if uid not in attempt_list.keys():
                                    attempt_list[uid] = [0, 0, 0, 0, 0]
                                session1.append(uid)


                                msg = "Login success"
                                now = datetime.now(IST)
                                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                                with open('info.csv', 'a') as info_file:
                                    fieldnames = ['Time', 'Uid']
                                    csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                                    csv_writer.writeheader()
                                    csv_writer.writerow({'Time': dt_string, 'Uid': uid})
                                return redirect(url_for('getset', usr=uid))
                            except:
                                msg = "FILL the form properly"
                        elif uid == "" and pasd == "":
                            msg = "FILL the form properly"
                        else:
                            msg = "Uid & password dosen't match"
        return render_template('login.html', uid=uid, pasd=pasd, msg=msg)
    except:
        msg = "error"


globalusers = [0, 0, 0, 0]


@app.route('/S.7079code1vision-question-CTF-AKC-CODEFREAKS-WEB.html/<usr>/', methods=['GET', 'POST'])
def getset(usr):
    msg = ""
    ans = ""
    attm = ""
    one = ""
    two = ""
    three = ""
    four = ""
    attm = "Wrong! Lost attempts" + str(attempt_list[usr][0]) + "/5"
    if usr in BanAccounts or usr not in session1:
        return redirect(url_for('login'))

    else:
        if request.method == 'POST' or 'GET' and 'sign' in request.form:
            txt = request.form.get('txt')
            msg = request.form.get('msg')
            attm = request.form.get('attm')
            one = request.form.get('one')
            three = request.form.get('three')
            four = request.form.get('four')
            two = request.form.get('two')
            if txt == "Nine":
                try:
                    msg = "correct"
                    globalusers[1] += 1
                    with open('correctattempt.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'time correct attempt Q1']
                        now = datetime.now(IST)
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'time correct attempt Q1': dt_string})
                    session1.remove(usr)
                    session2.append(usr)
                    return redirect(url_for('getset2', usr=usr))
                except:
                    msg = "There might be some error please refresh the page!!"

            else:
                globalusers[2] += 1
                msg = "Wrong Answer!"
                now = datetime.now(IST)
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                with open('correctattempt.csv', 'a') as info_file:
                    fieldnames = ['Uid', 'time wrong attempt Q1', 'answer']
                    csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerow(
                        {'Uid': usr, 'time wrong attempt Q1': dt_string, 'answer': txt})
                attempt_list[usr][0] += 1

                timelist.append(dt_string)
                print(timelist)
                attm = "Wrong! Lost attempts" + str(attempt_list[usr][0]) + "/5"

                if attempt_list[usr][0] == 5:
                    globalusers[3] += 1
                    with open('attemptinfo.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'Attempts Q1', 'time of each attempt']
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'Attempts Q1': attempt_list[usr][0], 'time of each attempt': timelist})
                        BanAccounts.append(usr)
                        timelist.clear()
                    return redirect(url_for('login'), code=301)



        one = globalusers[1] + globalusers[2]
        two = globalusers[1]
        three = globalusers[2]
        four = globalusers[3]
        return render_template('S.7079code1vision-question-CTF-AKC-CODEFREAKS-WEB.html', msg=msg, ans=ans, attm=attm,
                               one=one, two=two, three=three, four=four)


@app.route('/S.9334code1vision-question-CTF-AKC-CODEFREAKS-WEB.html.html/<usr>/', methods=['GET', 'POST'])
def getset2(usr):
    txt = ""
    msg = ""
    attm = ""
    one = ""
    two = ""
    three = ""
    four = ""
    attm = "Wrong! Lost attempts" + str(attempt_list[usr][1]) + "/5"
    if usr in BanAccounts or usr not in session2:
        return redirect(url_for('login'))

    else:
        if request.method == 'POST' or 'GET' and 'sign' in request.form:
            txt = request.form.get('txt')
            msg = request.form.get('msg')
            attm = request.form.get('attm')
            one = request.form.get('one')
            three = request.form.get('three')
            four = request.form.get('four')
            two = request.form.get('two')
            if txt.lower() == "error":
                try:
                    globalusers[1] += 1
                    msg = "correct"
                    with open('correctattempt.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'time correct attempt Q2']
                        now = datetime.now(IST)
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'time correct attempt Q2': dt_string})
                    session2.remove(usr)
                    session3.append(usr)
                    return redirect(url_for('getset3', usr=usr))

                except:
                    msg = "There might be some error please refresh the page!!"
            else:
                globalusers[2] += 1
                msg = "Wrong Answer!"
                now = datetime.now(IST)
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                with open('correctattempt.csv', 'a') as info_file:
                    fieldnames = ['Uid', 'time wrong attempt Q2', 'answer']
                    csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerow(
                        {'Uid': usr, 'time wrong attempt Q2': dt_string, 'answer': txt})
                attempt_list[usr][1] += 1
                timelist.append(dt_string)
                attm = "Wrong! Lost attempts" + str(attempt_list[usr][1]) + "/5"

                if attempt_list[usr][1] == 5:
                    globalusers[3] += 1
                    with open('attemptinfo.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'Attempts Q2', 'time of each attempt']
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'Attempts Q2': attempt_list[usr][1], 'time of each attempt': timelist})
                        BanAccounts.append(usr)
                        timelist.clear()
                    return redirect(url_for('login'))


        one = globalusers[1] + globalusers[2]
        two = globalusers[1]
        three = globalusers[2]
        four = globalusers[3]
        return render_template('S.9334code1vision-question-CTF-AKC-CODEFREAKS-WEB.html.html', txt=txt, msg=msg,
                               attm=attm, one=one, two=two, three=three, four=four)


@app.route('/S.6203code1vision-question-CTF-AKC-CODEFREAKS-WEB.html/<usr>', methods=['GET', 'POST'])
def getset3(usr):
    txt = ""
    msg = ""
    attm = ""
    one = ""
    two = ""
    three = ""
    four = ""
    attm = "Wrong! Lost attempts" + str(attempt_list[usr][2]) + "/5"
    if usr in BanAccounts or usr not in session3:
        return redirect(url_for('login'))

    else:
        if request.method == 'POST' or 'GET' and 'sign' in request.form:
            txt = request.form.get('txt')
            msg = request.form.get('msg')
            attm = request.form.get('attm')
            one = request.form.get('one')
            three = request.form.get('three')
            four = request.form.get('four')
            two = request.form.get('two')
            if txt == "31":
                try:
                    globalusers[1] += 1
                    msg = "correct"
                    with open('correctattempt.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'time correct attempt Q3']
                        now = datetime.now(IST)
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'time correct attempt Q3': dt_string})
                    session3.remove(usr)
                    session4.append(usr)
                    return redirect(url_for('getset4', usr=usr))

                except:
                    msg = "There might be some error please refresh the page!!"
            else:
                globalusers[2] += 1
                msg = "Wrong Answer!"
                now = datetime.now(IST)
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                with open('correctattempt.csv', 'a') as info_file:
                    fieldnames = ['Uid', 'time wrong attempt Q3', 'answer']
                    csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerow(
                        {'Uid': usr, 'time wrong attempt Q3': dt_string, 'answer': txt})
                attempt_list[usr][2] += 1
                timelist.append(dt_string)
                attm = "Wrong! Lost attempts" + str(attempt_list[usr][2]) + "/5"

                if attempt_list[usr][2] == 5:
                    globalusers[3] += 1
                    with open('attemptinfo.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'Attempts Q3', 'time of each attempt']
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'Attempts Q3': attempt_list[usr][2], 'time of each attempt': timelist})
                        BanAccounts.append(usr)
                        timelist.clear()
                    return redirect(url_for('login'))

        one = globalusers[1] + globalusers[2]
        two = globalusers[1]
        three = globalusers[2]
        four = globalusers[3]
        return render_template('S.6203code1vision-question-CTF-AKC-CODEFREAKS-WEB.html', txt=txt, msg=msg, attm=attm,
                               one=one, two=two, three=three, four=four)


@app.route('/S.7034code1vision-question-CTF-AKC-CODEFREAKS-WEB.html/<usr>', methods=['GET', 'POST'])
def getset4(usr):
    txt = ""
    msg = ""
    attm = ""
    one = ""
    two = ""
    three = ""
    four = ""
    attm = "Wrong! Lost attempts" + str(attempt_list[usr][3]) + "/5"
    if usr in BanAccounts or usr not in session4:
        return redirect(url_for('login'))

    else:
        if request.method == 'POST' or 'GET' and 'sign' in request.form:
            txt = request.form.get('txt')
            msg = request.form.get('msg')
            attm = request.form.get('attm')
            one = request.form.get('one')
            three = request.form.get('three')
            four = request.form.get('four')
            two = request.form.get('two')
            if txt in ["50 49", "50, 49", "50 ,49", "50 , 49"]:
                try:
                    globalusers[1] += 1
                    msg = "correct"
                    with open('correctattempt.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'time correct attempt Q4']
                        now = datetime.now(IST)
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'time correct attempt Q4': dt_string})
                    session4.remove(usr)
                    session5.append(usr)
                    return redirect(url_for('getset5', usr=usr))

                except:
                    msg = "There might be some error please refresh the page!!"
            else:
                globalusers[2] += 1
                msg = "Wrong Answer!"
                now = datetime.now(IST)
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                with open('correctattempt.csv', 'a') as info_file:
                    fieldnames = ['Uid', 'time wrong attempt Q4', 'answer']
                    csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerow(
                        {'Uid': usr, 'time wrong attempt Q4': dt_string, 'answer': txt})
                attempt_list[usr][3] += 1
                timelist.append(dt_string)
                attm = "Wrong! Lost attempts" + str(attempt_list[usr][3]) + "/5"

                if attempt_list[usr][3] == 5:
                    globalusers[3] += 1
                    with open('attemptinfo.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'Attempts Q4', 'time of each attempt']
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'Attempts Q4': attempt_list[usr][3], 'time of each attempt': timelist})
                        BanAccounts.append(usr)
                        timelist.clear()
                    return redirect(url_for('login'))

        one = globalusers[1] + globalusers[2]
        two = globalusers[1]
        three = globalusers[2]
        four = globalusers[3]
        return render_template('S.7034code1vision-question-CTF-AKC-CODEFREAKS-WEB.html', msg=msg, txt=txt, attm=attm,
                               one=one, two=two, three=three, four=four)


@app.route('/S.9303code1vision-question-CTF-AKC-CODEFREAKS-WEB.html/<usr>', methods=['GET', 'POST'])
def getset5(usr):
    txt = ""
    msg = ""
    attm = ""
    one = ""
    two = ""
    three = ""
    four = ""
    attm = "Wrong! Lost attempts" + str(attempt_list[usr][4]) + "/5"
    if usr in BanAccounts or usr not in session5:
        return redirect(url_for('login'))

    else:
        if request.method == 'POST' or 'GET' and 'sign' in request.form:
            txt = request.form.get('txt')
            msg = request.form.get('msg')
            attm = request.form.get('attm')
            one = request.form.get('one')
            three = request.form.get('three')
            four = request.form.get('four')
            two = request.form.get('two')
            if txt == "31":
                try:
                    globalusers[1] += 1
                    msg = "correct"
                    with open('correctattempt.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'time correct attempt Q5']
                        now = datetime.now(IST)
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'time correct attempt Q5': dt_string})
                    session5.remove(usr)
                    return redirect("https://github.com/pratyushkr11/CTF_CONSOLE")

                except:
                    msg = "There might be some error please refresh the page!!"
            else:
                globalusers[2] += 1
                msg = "Wrong Answer!"
                now = datetime.now(IST)
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                with open('correctattempt.csv', 'a') as info_file:
                    fieldnames = ['Uid', 'time wrong attempt Q5', 'answer']
                    csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerow(
                        {'Uid': usr, 'time wrong attempt Q5': dt_string, 'answer': txt})
                attempt_list[usr][4] += 1
                timelist.append(dt_string)
                attm = "Wrong! Lost attempts" + str(attempt_list[usr][4]) + "/5"

                if attempt_list[usr][4] == 5:
                    globalusers[3] += 1
                    with open('attemptinfo.csv', 'a') as info_file:
                        fieldnames = ['Uid', 'Attempts Q5', 'time of each attempt']
                        csv_writer = csv.DictWriter(info_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {'Uid': usr, 'Attempts Q5': attempt_list[usr][4], 'time of each attempt': timelist})
                        BanAccounts.append(usr)

                    return redirect(url_for('login'))
                timelist.clear()
        one = globalusers[1] + globalusers[2]
        two = globalusers[1]
        three = globalusers[2]
        four = globalusers[3]
        return render_template('S.9303code1vision-question-CTF-AKC-CODEFREAKS-WEB.html', msg=msg, txt=txt, attm=attm,
                               one=one, two=two, three=three, four=four)


@app.route('/adminpannel.html', methods=['GET', 'POST'])
def log():
    banname = ""
    banbtn = ""
    adduseruid = ""
    adduserpasd = ""
    adduser = ""
    msg = ""
    banaccounts = ""
    if request.method == 'POST' or 'GET' and 'adduser' or 'banbtn' in request.form:
        adduser = request.form.get('adduser')
        adduseruid = request.form.get('adduseruid')
        adduserpasd = request.form.get('adduserpasd')
        banname = request.form.get('banname')
        banbtn = request.form.get('banbtn')
        banaccounts = request.form.get('banaccounts')
        msg = request.form.get('msg')
        try:
            banaccounts = BanAccounts
            if adduseruid != "" and adduserpasd != "":
                with open('db.csv', 'a') as info_file:
                    fieldnames = ['uid', 'password', '\n']
                    csv_writer = csv.DictWriter(info_file, fieldnames)
                    csv_writer.writerow(
                        {'uid': adduseruid, 'password': adduserpasd})
                msg = "user added"
            elif banname != "":
                BanAccounts.remove(banname)
                msg = "removed from ban list"
            else:
                msg = "error"
        except:
            msg = "error"
    return render_template('adminpannel.html', msg=msg, adduserpasd=adduserpasd, adduser=adduser, adduseruid=adduseruid,
                           banbtn=banbtn, banname=banname, banaccounts=banaccounts)


if __name__ == '__main__':
    app.run()
