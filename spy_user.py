import sys
from termcolor import colored, cprint                                       #used for adding color to the text
from steganography.steganography import Steganography                       #used for encrypting and decrypting the data
from add_spy_user import add_spy_user                                       #used for adding details of new user on to the dictionary
from datetime import datetime                                               #used for adding date and time functionalty
from os import listdir                                                      #used for fatching files name from the system
from os.path import isfile, join                                            #used for fatching files name from the system
add_user = {                                                                #Dictionary for storing hole of the data of the Spy_chat
            'spy_name':["Mr. JON","Mr. MANU","Mr. RAJ","Mr. TOM","Mr. DOM"],
            'spy_age':["22","23","24","43","34"],
            'spy_rating':["4","5","5","4","3"],
            'spy_status':["I am Jon","I am Khiladi","I love Tinka","",""],
            'spy_user_name':["JON","MANU","RAJ","TOM","DOM"],
            'spy_user_password':["121","212","123","111","222"],
            'friend':[["MANU","RJO"],["JON","RJO"],["JON","MANU"],[],[]],
            'spy_chat':[[],[],[],[],[]]
        }


status_list=["Hey! I am new on Spy Chat","I am available"]                   #List of default status



#--------------------------------------------------------------defination of search_friend function-----------------------------------------------------------------------------


def search_friend(index):
    temp1 = 1
    print "\nSelect a friend to whom you want to send message \n"
    for temp in add_user['friend'][index]:
        print"\n\t%d.\t%s" % (temp1, temp)
        temp1 = temp1 + 1
    print "\n"
    friend_choice = raw_input("Select a Friend :\t")
    friend_choice = int(friend_choice)
    return friend_choice

#---------------------------------------------------------- function for setting up the status of different users------------------------------------------------------------------


def add_status(status):
    current_status=status
    status_list.append(current_status)

    print "Your current status :\t%s"%current_status
    spy_choice= raw_input("Did you want update your status from The Status List(Yes/No) :\t")
    spy_choice=spy_choice.upper()
    if spy_choice=='Y' or spy_choice=='YES':
        j=1                                                                  #temp variable used as a counter
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
        print "\n\tSorry Dude! You have not enter a valid option"
    return current_status                                                   #



#--------------------------------------------------------------------- function for adding friends to the friend list of different users---------------------------------------




def friends(index):
    if len(add_user['friend'][index])<=0:
        print "You have no friend currently"
    print "Select peoples you know :\t"
    temp=1                                                                       #temp variable used as a counter
    counter=1
    list=[]
    i=0                                                                          #temp variable used as a counter
    print "\n\tS.No.\tUser's\t\t\tStatus"
    while i<len(add_user["spy_name"]):
        if add_user["spy_name"][i]==add_user['friend'][index] or add_user['friend'][index]== add_user["spy_name"][i] :
            i=i+1
        else:
            if add_user["spy_name"][i]==add_user['spy_name'][index]:
                i=i+1
            else:
                print"\n\t %d\t  %s\t\t%s" % (counter, add_user["spy_name"][i], add_user["spy_status"][i])
                counter = counter + 1
                list.append(add_user["spy_name"][i])
                i = i + 1
    select_friend=raw_input("\nSelect a friend :\t")
    select_friend=int(select_friend)-1
    i = len(add_user['friend'][index])                                          #used for storing tepmary the length of frind list of perticular index
    key=0                                                                       #key variable used for identify wether the element in the list is same or diffrent
    if i>0:
        while i>0:
            if list[select_friend] == add_user['friend'][index][i-1]:
                key=1
            i=i-1
        if key==0:
            add_user['friend'][index].append(list[select_friend])
            print "\n\tCongractulation %s and you are now Friends" %add_user["spy_name"][select_friend-1]
        else:
            print "\n\tThis friend is already in your friend list "
        temp1=1                                                                #temp variable used as a counter
        for temp in add_user['friend'][index]:
            print"\n\t%d.\t%s"%(temp1,temp)
            temp1=temp1+1
        print "\n"
    else:
        print "\n\t##Please enter a Valid option##"
    return add_user['friend'][index]





#----------------------------------------------------------------function for deleating the frinends from there friend list of different users---------------------------------




def delete(index):
    if len(add_user['friend'][index])==0:
        print "\nYou have no friend currently"
    counter=1                                                                 #temp variable used as a counter
    for temp in add_user['friend'][index]:
        print"\n\t%d\t%s" % (counter,temp)
        counter=counter+1
    select_friend = raw_input("\nSelect a friend :\t")
    select_friend = int(select_friend)
    i=len(add_user['friend'][index])                                           #used for storing tepmary the length of frind list of perticular index
    if i==0:
        print "You have No friend to Delete\n"
    else:
        temp1 = select_friend                                                   #temp variable used for storing the input enter by user
        temp=0                                                                  #temp variable used as a counter
        lis=[]
        while temp1<len(add_user['friend'][index]):
            add_user['friend'][index][temp1-1] = add_user['friend'][index][temp1]
            temp1=temp1+1
        temp1=1
        while temp < len(add_user['friend'][index])-1:
            lis.append(add_user['friend'][index][temp])                         #Append the list with new friend name
            print "\n\t%d\t%s"%(temp1,add_user['friend'][index][temp])
            temp=temp+1
            temp1=temp1+1
        add_user['friend'][index]=lis
    return    add_user['friend'][index]

#------------------------------------------------------------------------function for sending the date and time details--------------------------------------------------------


def ChatMessage(message,index):
        message = colored(message, 'red')
        t=datetime.now()
        date = t.strftime("%b %d %Y")
        time = t.strftime("%H %M %S")
        #date=datetime.date("%b %d,%Y")
        #date=str(date)
        #date=colored(date, 'green')
        #time = datetime.time("%H:%M:%S")
        #time=str(time)
        date = colored(date, 'blue')
        time = colored(time, 'green')
        friend = colored(add_user['spy_name'][index], 'blue')
        msg=message+"  ("+date+"  "+time+")  by  "+friend                                  #concatinating message ,time and booliab value by type caasting
        return msg



#------------------------------------------------------------------------function for sending the encrypted message to the selected friend--------------------------------------



def send_message(index):
    friend_choice = search_friend(index)                                        #calling search friend function
    img_path = "original_images\\"
    img_name = ".jpg"
    select_file = [f for f in listdir("original_images\\") if isfile(join("original_images\\", f))]
    print select_file
    print ("Select from Above Images Name : ")
    X = raw_input("What is the name of the Image : ")
    original_image = img_path + X + img_name                                    #variable used for storing the path of the image
    try:
        counter = 1
        output_path = "encrypted_images\%d.jpg" %(counter)
        i=3
        while i>0:
            text = raw_input("What do you want to Say : ")
            if len(text)<=100:
                if text.upper()=="SOS":
                    text="Save our Souls"
                if text.upper()=="SAVE ME":
                    text="Please save me, I am in danger"
                if text.upper()=="HELP ME":
                    text="Please save me, I am in danger"
                if text.upper()=="HURRY UP":
                    text = "Please come fast, There is an Emergency"
                if text.upper()=="LOL":
                    text="Lot's of LOVE "
                if text.upper()=="ILU":
                    text="I Love You"
                Steganography.encode(original_image, output_path, text)   #encription process is used here
                i=0
            elif len(text)==0:
                print "\n\tPlease don't make message field empty"
            else:
                print "Message should be maximum 100 words"
                i=i-1
        counter = counter + 1

    except:
        print "Wrong Image Name"

    new_chat = ChatMessage(text,index)                                              #chat is updated with new chat by appending

    #add_user['spy_chat'][index].append(new_chat)

    print "\n\tSecret Message is sent inside the Image.\n"
    return add_user['spy_chat'][index]


#-------------------------------------------------------function for decripte the message of the selected friend--------------------------------------------------------------------


def read_message(index):
    friend_choice = search_friend(index)
    sender = int(friend_choice)
    img_path = "original_images\\"

    img_path = "encrypted_images\\"
    img_name = ".jpg"
    select_file = [f for f in listdir("encrypted_images\\") if isfile(join("encrypted_images\\", f))]
    print select_file
    X = raw_input("What is the name of the Image that you want to decode: ")
    output_path = img_path + X + img_name                                           #variable used for storing the path of the image
    secret_text = Steganography.decode(output_path)                                 #decription process is used here
    print ChatMessage(secret_text, False)
    new_chat = ChatMessage(secret_text, False)                                      #chat is updated with new chat by appending
    add_user['spy_chat'][index].append(new_chat)
    print "Secret Message has been decoded!"
    print "\n\t\t****decoded Message Is : %s****\n" % secret_text
    return add_user['spy_chat'][index]


#-----------------------------------------------------------function for seeing the chat history of the friend-------------------------------------------------------------------

def chat_history(index):
    friend_choice = search_friend(index)
    temp1 = 1                                                                       #temp variable used as a counter
    print "Select a friend to whom chat history you want to see \n"
    #print len(add_user['spy_chat'][index])
    if len(add_user['spy_chat'][index])>0:
        for temp in add_user['spy_chat'][index]:
            print"\n\t%d.\t%s" % (temp1, temp)
            temp1 = temp1 + 1
    else:
        print "Sorry, You have no Chat History currentlly"
    print "\n"


#----------------------------------------------------------------------------------Berning of the main program---------------------------------------------------------------

spy = 1
while (spy == 1):
    print("\n\t***Welcome to my SpyChat***\n")
    print("You wana Login or Sign-up")                                             #sign-up manu
    spy_user = raw_input("Enter your Choice\n\t1.\tLogin\n\t2.\tSign-Up\t")
    #spy_user=int(spy_user)
    if spy_user == "1":                          #login process
        print "\nIf you want to use Default user then\n\tUser Name :\tJON\n\tPassword  :\t121"
        spy_login = raw_input("\nUser Name\t:\t")
        spy_password = raw_input("Password\t:\t")
        spy_login=spy_login.upper()
        i=0
        while i <len(add_user['spy_name']):
            if add_user['spy_user_name'][i] ==spy_login  and add_user['spy_user_password'][i] == spy_password:
                print ("\n\tWelocome %s\n" %(add_user['spy_name'][i]) )             #login details have to assign
                while 1:
                    print "What do you want to do?\n\t1.\tStatus Change.\n\t2.\tAdd Friend.\n\t3.\tDelete Friend.\n\t4.\tSend Message.\n\t5.\tClose."
                    spy_choice=int(raw_input("Enter your choice :\t"))
                    if int(spy_choice)>0:

                        if spy_choice == 1:
                            add_user['spy_status'][i]= add_status(add_user['spy_status'][i])#calling of the function add_status
                        elif spy_choice == 2:
                            friends(i)                                          #calling of the function friends
                        elif spy_choice == 3:
                            delete(i)                                           #calling of the function delete
                        elif spy_choice == 4:
                            print "\nWhat do you want to do\n\t1.\tSend Encrypted Message.\n\t2.\tShow Decrypted Message.\n\t3.\tSee Chat History.\n"
                            choice=raw_input("Enter your choice :\t")
                            choice=int(choice)
                            if choice==1:
                                send_message(i)                                 #calling of the function send_message
                            elif choice==2:
                                read_message(i)                                 #calling of the function read_message
                            elif choice==3:
                                chat_history(i)                                 #calling of the function chat_history
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
    elif spy_user == "2":                                                       #adding a new user
        print ("\n\t***Spy Chat Welcome's you***\n")
        i = 3
        while (i > 0):                                                          #Enter name of the user
            spy_name = raw_input("Enter your name :\t")
            if len(spy_name)==0:                                                #if user strike enter without striking any input gives warning
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
            if len(spy_age)!=0:                                                  #if user strike enter without striking any input gives warning
                i=i-1
                spy_age=int(spy_age)
                if spy_age>=0 and spy_age<100:                                   #validation process for checking age criteria
                    if spy_age >= 12 and spy_age <= 50:
                        print ("\n\tYou are VALID User\n")
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
            if spy_Sex == "M" or spy_Sex == "MALE" or spy_Sex == "1":               #user can enter M,m,male,MALE or 1 in input... everything will be accepted
                spy_name = "Mr. " + spy_name
                print ("\n\tThank You %s" % spy_name)
                i=0
            elif spy_Sex == "F" or spy_Sex == "FEMALE" or spy_Sex == "2":           #user can enter F,f,female,FEMALE or 2 in input... everything will be accepted
                spy_name = "Miss. " + spy_name
                print ("\n\tThank You %n" % spy_name)
                i = 0
            else:
                print ("\n\tYou have enter a wrong Choice")
                i=i-1
        i = 3
        while (i > 0):
            print ("\nEnter rating for our SPY-CHAT\n")                                #ratting is provided here
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
                     if spy_rating>4:
                         print "\tYou Rated us Exicelent"
                     elif spy_rating > 3 and spy_rating<=4:
                         print "\tYou Rated us VERY GOOD"
                     elif spy_rating > 2 and spy_rating <= 3:
                         print "\tYou Rated us GOOD"
                     elif spy_rating > 1 and spy_rating <= 2:
                         print "\tYou Rated us NOT GOOD"
                     else:
                         print "\tYou Rated us POOR"
                     i = 0
                else:
                    print ("\tYou have enter a wrong choice")
                    i=i-1
        i = 3
        while (i > 0):                                                                #first time status is update here frq new user's
            spy_status=raw_input("\nEnter your Status\t")
            if len(spy_status)>0:
                i=0
            else:
                i=i-1
        i = 3
        while (i > 0):
            spy_user_name = raw_input("\nEnter User name for your Spy :\t")                 #user's name is created here
            spy_user_name =  spy_user_name.upper()
            if len(spy_user_name)>0:
                for temp in add_user['spy_name']:
                    if spy_user_name==temp:
                        print "\n\tThis user name is taken by another user. Try somthing diffrent."         #user name is
                        i=i-1
                        break
                    else :
                        print "\n\tValid user"
                        i=0
                        break
            else:
                i=i-1
            if i == -1:
                print "\n\t##You have not Enter any USER NAME##\n"
                exit(0)

        j=4
        spy_user_password1 = "a"
        spy_user_password = "a1"
        while j>0:                                                                   #password validation is done here
            if spy_user_password!=spy_user_password1:
                spy_user_password=raw_input("\nEnter a new password :\t")
                spy_user_password1=raw_input("Re-enter your new password :\t")
                j=j-1
            else:
                j=0
            if len(spy_user_password)==0:
                print "\n\tPlease Enter Password first"
                spy_user_password = raw_input("\nEnter a new password :\t")
                spy_user_password1 = raw_input("Re-enter your new password :\t")
                j=j-1

        add_user=add_spy_user(spy_name,spy_age,spy_rating,spy_status,spy_user_password,spy_user_name,add_user)
                                                                                        #new user is created throw this by adding up hole of the record on to the dictionary
        print "\n\t!i!!New user created Sucessfully!i!\n"
        print "\tSpy-Name :\t%s\t\tSpy-Age :\t%s\t\tSpy-Rating :%.2f"%(spy_name,spy_age,spy_rating)
        print "\n\tSpy-Status :\t%s\n"%spy_status
        spy = raw_input("Did you wana Continue...\nIf yes, Then Press 1\t")
        spy = int(spy)
    else:
        print ("You have enter a wrong Choice")
        spy = raw_input("Did you wana Continue...\nIf yes, Then Press 1\t")
        spy=int(spy)




        #-----------------------------------------------------------#END POINT of the program#-----------------------------------------------------------------------