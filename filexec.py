# filename = input("enter file path: ")
# try:
#     f = open(filename)
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("File not found")



filename = '/etc/protocols'
f = open(filename)
try:
    f.write('test')
except:
    print("File write error")
finally:
    print("finally")
    f.close()
