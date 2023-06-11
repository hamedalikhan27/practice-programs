# Here goes my first self python program. Hope this goes well
town_name = input("Give a mystical town name = ")
boy_name = input("Your name = ")
verb1 = input("Enter a verb = ")
house_hold_object = input("Enter a house hold item = ")
insect = input("Which insect do you hate the most = ")

madlib = f"Once upon a time, in a small town called {town_name}, there was a boy named\
 {boy_name} who embarked on a wild {verb1} adventure. Armed with determination and a\
 {house_hold_object}, he delved into the world of coding. His first program was\
 supposed to print 'hello world' but alas, his fingers slipped, and it hilariously\
 outputted 'hello {insect}' "

print(madlib)