#Activity 3.2.2 Step 10
from Post import Post

all_posts_archive = []

username = input("enter your username")

print("welcome" + " " + username)

user_input = input(""" what would you like to do?
"new" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change their username associated with future posts
"print" - Display the current, up-to-date list of all posts
"quit" - End the program
""")

while user_input != "quit":
    if user_input == "new":
        message = input("what data would you like to post?")
        all_posts_archive.append(Post(username, message))
    elif user_input == "remove":
        index = input("what is the index for the message that will be removed")
        del all_posts_archive[int(index)]
    elif user_input == "change user":
        username = input("what username would you like to change to?")
    elif user_input == "print":
        for post in all_posts_archive:
            print(Post)
    else:
        user_input = input("invalid input, try again")

    user_input = input(""" what would you like to do?
    "new" - Add a post to the archive
    "remove" - Remove a post from the archive
    "change user" - Change their username associated with future posts
    "print" - Display the current, up-to-date list of all posts
    "quit" - End the program
    """)