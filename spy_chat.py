from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('Raja', 'Mr.', 4.9, 27)
friend_two = Spy('Mata Hari', 'Ms.', 4.39, 21)
friend_three = Spy('No', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]



j=0
    key=0
    while i<len(add_user['spy_name'][index]):
        while j<len(add_user['friend'][index]):
            if add_user['friend'][index][j]==add_user['spy_name'][i]:
                key=0
                break
            else:
                key=1
            j = j + 1
        if key==0:
            list.append(add_user['spy_name'][i])
        i=i+1
    print list



key=0
        print add_user['friend'][index][select_friend]==add_user['friend'][index][i-1]
        print "passsssssssssssssssssssss"
        while i>0:
            if add_user['friend'][index][select_friend]==add_user['friend'][index][i-1]:
                key=1
            print add_user['friend'][index][select_friend] == add_user['friend'][index][i - 1]
            i=i-1
        if key==0: