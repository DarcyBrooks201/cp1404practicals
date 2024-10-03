"""CP1404 Prac 3 Do-From_Scratch exercise files.py"""
# 1
name = input("name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()



