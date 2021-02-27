
def create_userList():
    list=[]
    while True:
        print("Create a user! End by typing 'e'! ")
        username = input("username: ")
        if username == "e":
            break
        password = input("password: ")
        if password == "e":
            break
        user = {"user": username, "key": password}
        list.append(user)
    print(list)
create_userList()
