import pickle
import os
os.system("clear")

print("Hello, user")
name = input("Who are you?")
print("Nice to meet you, " + name)


cod = input("And, what's your password?")
print("Ok, your password is: " + cod)

user = [name, cod]


pickle.dump(user, open("login.dat" , "wb"))
login = pickle.load(open("login.dat", "rb"))
print("Now, your login is registered in our sistem")
print("There's your login:")
print(login)