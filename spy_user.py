from steganography.steganography import Steganography                       #used for encrypting and decrypting the data
from add_spy_user import add_spy_user                                       #used for adding details of new user on to the dictionary
from datetime import datetime                                               #used for adding date and time functionalty
from os import listdir                                                      #used for fatching files name from the system
from os.path import isfile, join                                            #used for fatching files name from the system
add_user = {                                                                #Dictionary for storing hole of the data of the Spy_chat
            'spy_name':["JON","MANU","RAJ","TOM","DOM"],
            'spy_age':["22","23","24","43","34"],
            'spy_rating':["4","5","5"],
            'spy_status':["hloo","hiiii","I am Rjo"],
            'spy_user_name':["JON","MANU","RAJ","TOM","DOM"],
            'spy_user_password':["121","212","123","111","222"],
            'friend':[["MANU","RJO"],["JON","RJO"],["JON","MANU"],[],[]],
            'spy_chat':[[],[],[],[],[]]
        }


status_list=["Hey! I am new on Spy Chat","I am available"]                   #List of default status


def add_status(status):                                                      #function for setting up the status of different users
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
    return current_status                                                   #





def friends(index):                                                              #function for adding friends to the friend list of different users
    if len(add_user['friend'][index])<=0:
        print "You have no friend currently"
    print "Select peoples you know :\t"
    temp=1
    counter=1
    list=[]
    i=0
    while i<len(add_user["spy_name"]):
        if add_user["spy_name"][i]==add_user['friend'][index] or add_user['friend'][index]== add_user["spy_name"][i] :
            i=i+1
        else:
            if add_user["spy_name"][i]==add_user['spy_name'][index]:
                i=i+1
            else:
                print"\n\t%d\t%s" % (counter, add_user["spy_name"][i])
                counter = counter + 1
                list.append(add_user["spy_name"][i])
                i = i + 1
    select_friend=raw_input("\nSelect a friend :\t")
    select_friend=int(select_friend)-1
    i = len(add_user['friend'][index])
    key=0
    if i>0:
        while i>0:
            if list[select_friend] == add_user['friend'][index][i-1]:
                key=1
            i=i-1
        if key==0:
            add_user['friend'][index].append(list[select_friend])
            print "Congractulation %s and you are now Friends" %add_user["spy_name"][select_friend-1]
        else:
            print "This friend is already in your friend list "
        temp1=1
        for temp in add_user['friend'][index]:
            print"\n\t%d.\t%s"%(temp1,temp)
            temp1=temp1+1
        print "\n"
    else:
        print "\n\t##Please enter a Valid option##"
    return add_user['friend'][index]




def delete(index):                               #function for deleating the frinends from there friend list of different users
    if len(add_user['friend'][index])==0:
        print "You have no friend currently"
    counter=1
    for temp in add_user['friend'][index]:
        print"\n\t%d\t%s" % (counter,temp)
        counter=counter+1
    select_friend = raw_input("\nSelect a friend :\t")
    select_friend = int(select_friend)
    i=len(add_user['friend'][index])
    if i==0:
        print "You have No friend to Delete\n"
    else:
        temp1 = select_friend
        temp=0
        lis=[]
        while temp1<len(add_user['friend'][index]):
            add_user['friend'][index][temp1-1] = add_user['friend'][index][temp1]
            temp1=temp1+1
        temp1=1
        while temp < len(add_user['friend'][index])-1:
            lis.append(add_user['friend'][index][temp])
            print "\n\t%d\t%s"%(temp1,add_user['friend'][index][temp])
            temp=temp+1
            temp1=temp1+1
        add_user['friend'][index]=lis
    return    add_user['friend'][index]




def ChatMessage(message,sent_by_me):        #function for sending the date and time details
        message = message
        time = datetime.now()
        time=str(time)
        sent_by_me = sent_by_me
        sent_by_me=str(sent_by_me)
        msg=message+" ("+time+") "+sent_by_me           #concatinating message ,time and booliab value by type caasting
        return msg



def send_message(index):                     #function for sending the encrypted message to the selected friend
    temp1=1
    print "Select a friend to whom you want to send message \n"
    for temp in add_user['friend'][index]:
        print"\n\t%d.\t%s" % (temp1, temp)
        temp1 = temp1 + 1
    print "\n"
    friend_choice=raw_input("Select a Friend :\t")
    friend_choice = int(friend_choice)
    img_path = "original_images\\"
    img_name = ".jpg"
    select_file = [f for f in listdir("original_images\\") if isfile(join("original_images\\", f))]
    print select_file
    print ("Select from Above Images Name : ")
    X = raw_input("What is the name of the Image : ")
    original_image = img_path + X + img_name
    print original_image
    try:
        counter = 1
        output_path = "encrypted_images\%d.jpg" % counter
        i=3
        while i>0:
            text = raw_input("What do you want to Say : ")
            if len(text)<=100:
                Steganography.encode(original_image, output_path, text)
                i=0
            else:
                print "Message should be maximum 100 words"
                i=i-1
        counter = counter + 1

    except:
        print "Wrong Image Name"

    new_chat = ChatMessage(text, True)

    add_user['spy_chat'][index].append(new_chat)

    print "Secret Message is sent inside the Image."
    return add_user['spy_chat'][index]



def read_message(index):                     #function for decripte the message of the selected friend
    temp1 = 1
    print "Select a friend to whom you want to send message \n"
    for temp in add_user['friend'][index]:
        print"\n\t%d.\t%s" % (temp1, temp)
        temp1 = temp1 + 1
    print "\n"
    friend_choice = raw_input("Select a Friend :\t")
    sender = int(friend_choice)
    img_path = "original_images\\"

    img_path = "encrypted_images\\"
    img_name = ".jpg"
    select_file = [f for f in listdir("encrypted_images\\") if isfile(join("encrypted_images\\", f))]
    print select_file
    X = raw_input("What is the name of the Image that you want to decode: ")
    output_path = img_path + X + img_name
    secret_text = Steganography.decode(output_path)
    print ChatMessage(secret_text, False)
    new_chat = ChatMessage(secret_text, False)
    add_user['spy_chat'][index].append(new_chat)
    print "Secret Message has been decoded!"
    print "\n\t\t****decoded Message Is : %s****" % secret_text
    return add_user['spy_chat'][index]


def chat_history(index):             #function for seeing the chat history of the friend
    temp1 = 1
    print "Select a friend to whom chat history you want to see \n"
    for temp in add_user['friend'][index]:
        print"\n\t%d.\t%s" % (temp1, temp)
        temp1 = temp1 + 1
    print "\n"
    friend_choice = raw_input("Select a Friend :\t")
    temp1 = 1
    print "Select a friend to whom chat history you want to see \n"
    print len(add_user['spy_chat'][index])
    if len(add_user['spy_chat'][index])>0:
        for temp in add_user['spy_chat'][index]:
            print"\n\t%d.\t%s" % (temp1, temp)
            temp1 = temp1 + 1
    else:
        print "Sorry, You have no Chat History currentlly"
    print "\n"




spy = 1                                                         #Berning of the main program
while (spy == 1):
    print("\n\t***Welcome to my SpyChat***\n")
    print("You wana Login or Sign-up")                          #sign-up manu
    spy_user = raw_input("Enter your Choice\n\t1.\tLogin\n\t2.\tSign-Up\t")
    #spy_user=int(spy_user)
    if spy_user == "1":                                         #login process
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
                    spy_choice=int(raw_input("Enter your choice :\t"))
                    if int(spy_choice)>0:

                        if spy_choice == 1:
                            add_user['spy_status'][i]= add_status(add_user['spy_status'][i])#calling of the function add_status
                        elif spy_choice == 2:
                            friends(i)  #calling of the function friends
                        elif spy_choice == 3:
                            delete(i)   #calling of the function delete
                        elif spy_choice == 4:
                            print "What do you want to do\n\t1.\tSend Encrypted Message.\n\t2.\tShow Decrypted Message.\n\t3.\tSee Chat History.\n"
                            choice=raw_input("Enter your choice :\t")
                            choice=int(choice)
                            if choice==1:
                                send_message(i) #calling of the function send_message
                            elif choice==2:
                                read_message(i) #calling of the function read_message
                            elif choice==3:
                                chat_history(i) #calling of the function chat_history
                            else:
                                print "\tYou have entered a INVALID choice"
                        elif spy_choice == 5:
                            print "Come back Soon"
                            exit(0)
                        else:
                            print "\n\t##You have Enter a Wrong Choice##\n"


                spy = raw_input("Did you wana Continue...\nIf yes, Then Press 1\t")
                spy = int(spy)
            i = i + 1
        else:
            print "\n\t##WRONG! User name and Password##\n"
    elif spy_user == "2":                       #adding a new user
        print ("\n\t***Spy Chat Welcome's you***\n")
        i = 3
        while (i > 0):                              #Enter name of the user
            spy_name = raw_input("Enter your name :\t")
            if len(spy_name)==0:                    #if user strike enter without striking any input gives warning
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
            if len(spy_age)!=0:                     #if user strike enter without striking any input gives warning
                #print ("Please enter your age First")
                i=i-1
                spy_age=int(spy_age)
                if spy_age>=0 and spy_age<100:      #validation process for checking age criteria
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
            if spy_Sex == "M" or spy_Sex == "MALE" or spy_Sex == "1":   #user can enter M,m,male,MALE or 1 in input... everything will be accepted
                spy_name = "Mr. " + spy_name
                print ("\n\tThank You %s" % spy_name)
                i=0
            elif spy_Sex == "F" or spy_Sex == "FEMALE" or spy_Sex == "2":#user can enter F,f,female,FEMALE or 2 in input... everything will be accepted
                spy_name = "Miss. " + spy_name
                print ("\n\tThank You %s" % spy_name)
                i = 0
            else:
                print ("\n\tYou have enter a wrong Choice")
                i=i-1
        i = 3
        while (i > 0):
            print ("Enter rating for our SPY-CHAT\n")           #ratting is provided here
            print ("\t1.\t*\n\t2.\t**\n\t3.\t***\n\t4.\t****\n\t5.\t*****\n")
            spy_rating = raw_input ("Enter your choice(1-5).\t\t\tIf not intrested to rate us then press(N).\t")
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
        while (i > 0):                                  #first time status is update here frq new user's
            spy_status=raw_input("Enter your Status\t")
            if len(spy_status)>0:
                i=0
            else:
                i=i-1
        spy_user_name = raw_input("Enter User name for your Spy :\t")#user's name is created here
        spy_user_name =  spy_user_name.upper()
        j=4
        spy_user_password1 = "a"
        spy_user_password = "a1"
        while j>0:                                          #password validation is done here
            if spy_user_password!=spy_user_password1:
                spy_user_password=raw_input("Enter a new password :\t")
                spy_user_password1=raw_input("Re-enter your new password :\t")
                j=j-1
            else:
                j=0

        add_user=add_spy_user(spy_name,spy_age,spy_rating,spy_status,spy_user_password,spy_user_name,add_user)
        #new user is created throw this by adding up hole of the record on to the dictionary
        print "\n\t!i!!New user created Sucessfully!i!\n"
        spy = raw_input("Did you wana Continue...\nIf yes, Then Press 1\t")
        spy = int(spy)
    else:
        print ("You have enter a wrong Choice")
        spy = raw_input("Did you wana Continue...\nIf yes, Then Press 1\t")
        spy=int(spy)
        #END POINT of the program