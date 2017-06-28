from add_spy_user import add_spy_user
add_user = {
            'spy_name':["JON","MANU","RAJ","TOM","DOM"],
            'spy_age':["22","23","24","43","34"],
            'spy_rating':["4","5","5"],
            'spy_status':["hloo","hiiii","I am Rjo"],
            'spy_user_name':["JON","MANU","RAJ"],
            'spy_user_password':["121","212","123","111"],
            'friend':[["MANU","RJO"],["JON","RJO"],["JON","MANU"]]
        }


status_list=["Hey! I am new on Spy Chat","I am available"]
def add_status(status):
    current_status=status
    status_list.append(current_status)

    print "Your current status :\t%s"%current_status
    spy_choice= raw_input("Did you want update your status from The Status List(Yes/No) :\t")
    spy_choice=spy_choice.upper()
    if spy_choice=='Y' or spy_choice=='YES':
        j=1
        for temp in status_list:
            print "\n\t%d.\t%s"%(j,temp)
            j=j+1
        print "\n\t%d.\tNone of these\n"%j
        spy_choice1=raw_input("Enter your Choice")
        spy_choice1=int(spy_choice1)
        if spy_choice1<j:
            current_status=status_list[spy_choice1-1]
        elif spy_choice1==len(status_list)+1:
            pass
        else:
            print "Enter a Valid option"
    elif spy_choice=='N' or spy_choice=='No':
        current_status=raw_input("Enter your new status :\t")
        #status_list.append(current_status)
    else:
        print "Sorry Dude! You have not enter a valid option"
    return current_status




def friends(index):
    if len(add_user['friend'][index])<=1:
        print "You have no friend currently"
    print "Select peoples you know :\t"
    counter=1
    i=0
    while i<len(add_user["spy_name"]):
        if add_user["spy_name"][i]==add_user['friend'][index]:
            temp=temp+1
            i=i+1
        else:
            if add_user["spy_name"][i]==add_user['spy_name'][index]:
                i=i+1
            else:
                print"\n\t%d\t%s" % (counter, add_user["spy_name"][i])
                counter = counter + 1
                i = i + 1
    select_friend=raw_input("\nSelect a friend :\t")
    select_friend=int(select_friend)
    if select_friend<=len(add_user["spy_name"]):
        add_user['friend'][index].append(add_user["spy_name"][select_friend-1])
        print "Congractulation %s and you are now Friends" %add_user["spy_name"][select_friend-1]
        for temp in add_user['friend'][index]:
            print"%s"%(temp)
    else:
        print "\n\t##Please enter a Valid option##"
    return add_user['friend'][index]


def delete(index):
    if len(add_user['friend'][index])<=1:
        print "You have no friend currently"
    for temp in add_user['friend'][index]:
        print"%s" % (temp)
    select_friend = raw_input("\nSelect a friend :\t")
    select_friend = int(select_friend)






spy = 1
while (spy == 1):
    print("\n\t***Welcome to my SpyChat***\n")
    print("You wana Login or Sign-up")
    spy_user = raw_input("Enter your Choice\n\t1.\tLogin\n\t2.\tSign-Up\t")
    #spy_user=int(spy_user)
    if spy_user == "1":
        spy_login = raw_input("\nUser Name\t:\t")
        spy_password = raw_input("Password\t:\t")
        spy_login=spy_login.upper()
        i=0
        print spy_login
        print spy_password
        while i <len(add_user['spy_name']):
            print add_user['spy_user_name'][i]
            print add_user['spy_user_password'][i]
            if add_user['spy_user_name'][i] ==spy_login  and add_user['spy_user_password'][i] == spy_password:
                print ("\n\tWelocome %s\n" %(add_user['spy_name'][i]) )#login details have to assign
                while 1:
                    print "What do you want to do?\n\t1.\tStatus Change.\n\t2.\tAdd Friend.\n\t3.\tDelete Friend.\n\t4.\tSend Message.\n\t5.\tClose."
                    spy_choice=int(raw_input("Enter your choice"))
                    if int(spy_choice)>0:

                        if spy_choice == 1:
                            add_user['spy_status'][i]= add_status(add_user['spy_status'][i])
                        elif spy_choice == 2:
                            friends(i)
                        elif spy_choice == 3:
                            delete(i)
                        #elif spy_choice == 4:
                        elif spy_choice == 5:
                            print "Come back Soon"
                            exit(0)
                        else:
                            print "lora"


                spy = raw_input("Did you wana Continue...\nIf yes, Then Press 1\t")
                spy = int(spy)
            i = i + 1
        else:
            print "\n\t##WRONG! User name and Password##\n"
    elif spy_user == "2":
        print ("\n\t***Spy Chat Welcome's you***\n")
        i = 3
        while (i > 0):
            spy_name = raw_input("Enter your name :\t")
            if len(spy_name)==0:
                print ("Please enter your name First :\t")
                i=i-1
            else:
                i=0
            if i == 1:
                print("\n\tBetter luck next time...")
                exit(0)
        spy_name = spy_name.upper()
        i=3
        while(i>0):
            spy_age = raw_input("Enter your age :\t")
            #age=spy_age
            #spy_age=int(spy_age)
            if len(spy_age)!=0:
                #print ("Please enter your age First")
                i=i-1
                spy_age=int(spy_age)
                if spy_age>=0 and spy_age<100:
                    if spy_age >= 12 and spy_age <= 50:
                        print ("\tYou are VALID User")
                        i=0
                    else:
                        print("\tYou are not VALID user. Your age should be in between 12yr to 50yr.\n")
                        i=i-1
                    if i==1:
                        print("\tBetter luck next time...")
                        exit(0)
                else:
                        print ("\tPlease Enter a Valid option\n")
                        i = i - 1
                        if i == 1:
                            print("\tBetter luck next time...")
                            exit(0)
        i = 3
        while (i > 0):
            spy_Sex = raw_input("Enter your Sex \n\t1.\tMale\n\t2.\tFemale\t")
            spy_Sex = spy_Sex.upper()
            if spy_Sex == "M" or spy_Sex == "MALE" or spy_Sex == "1":
                spy_name = "Mr. " + spy_name
                print ("\n\tThank You %s" % spy_name)
                i=0
            elif spy_Sex == "F" or spy_Sex == "FEMALE" or spy_Sex == "2":
                spy_name = "Miss. " + spy_name
                print ("\n\tThank You %s" % spy_name)
                i = 0
            else:
                print ("\n\tYou have enter a wrong Choice")
                i=i-1
        i = 3
        while (i > 0):
            print ("Enter rating for our SPY-CHAT\n")
            print ("\t1.\t*\n\t2.\t**\n\t3.\t***\n\t4.\t****\n\t5.\t*****\n")
            spy_rating = raw_input ("Enter your choice.\t\t\tIf not intrested to rate us then press(N).\t")
            if spy_rating=="N" or spy_rating=="n":
                print ("Thank you, You can rate us any time")
                spy_rating=0
                i=0
            else:
                spy_rating = int(spy_rating)
                if spy_rating > 0 and spy_rating < 6:
                     print ("\n\tThank you, For your contribution.")
                     i = 0
                else:
                    print ("\tYou have enter a wrong choice")
                    i=i-1
        i = 3
        while (i > 0):
            spy_status=raw_input("Enter your Status\t")
            if len(spy_status)>0:
                i=0
            else:
                i=i-1
        spy_user_name = raw_input("Enter User name for your Spy :\t")
        spy_user_name =  spy_user_name.upper()
        j=4
        spy_user_password1 = "a"
        spy_user_password = "a1"
        while j>0:
            if spy_user_password!=spy_user_password1:
                spy_user_password=raw_input("Enter a new password :\t")
                spy_user_password1=raw_input("Re-enter your new password :\t")
                j=j-1
            else:
                j=0

        add_user=add_spy_user(spy_name,spy_age,spy_rating,spy_status,spy_user_password,spy_user_name,add_user)
        print "\n\t!i!!New user created Sucessfully!i!\n"
        spy = raw_input("Did you wana Continue...\nIf yes, Then Press 1\t")
        spy = int(spy)
    else:
        print ("You have enter a wrong Choice")
        spy = raw_input("Did you wana Continue...\nIf yes, Then Press 1\t")
        spy=int(spy)