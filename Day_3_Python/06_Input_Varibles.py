Partner = ('Fatima','Anam','Novelia')
Name = input("Enter you Partner\'s name: ")
if Name in Partner:
    if Name == 'Fatima':
        print("You are married to Fatima")
    elif Name == 'Anam':
        print("You are married to Anam")
    else:
        print("You are Luckiest Person Who are not married yet")
else:
    print("You are not married yet")
