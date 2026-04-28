# HAD TO PUT r IN FRONT OF THE STRING BECAUSE OF THE BACKSLASH IN THE PATH, 
# OTHERWISE IT WOULD HAVE THROWN AN ERROR. THE r STANDS FOR RAW STRING AND IT TREATES BACKSLASH AS A 
# NORMAL CHARACTER INSTEAD OF AN ESCAPE CHARACTER.

#also jo bhi file create ho rhi hai wo current fold
#ke bahar create ho rhi hai matlab parent file mai idk why

#opening a file
r"""
o = open(r"C:\Users\DEEP PATHAK\Desktop\Study\Python\Py\game_of_thrones.txt", "r")
print(o.read())
"""

#creating then writing and then prunting a file
r"""
a = open("walking_dead.txt", "w")
a.write("Rick Grimes is the main character of the walking dead")
a.close()
a = open("walking_dead.txt", "r")
print(a.read())
"""

#writing to a file
r"""
r = open(r"hello.txt", "w")
r.write("This is a file created by me")
print("File created successfully")
r.close()
"""

#appending to a file
r"""
a = open("game_of_thrones.txt", "a")
a.write("\nThe show is based on the book series A Song of Ice and Fire by George R. R. Martin.")
a.close()
"""

