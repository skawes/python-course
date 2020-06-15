import webbrowser
chrome=webbrowser.get('google-chrome')
chrome.open('www.google.com')
# my_file=open("E:\\awes.txt","r")
# for line in my_file:
#     print(line)
#
# my_file.close()
#
# for i in range(5):
#     print(i)

# opening file with 'with' as it has advantages
# with open("E:\\awes.txt","r") as my_file:
#     for line in my_file:
#         if "awes" in line:
#             print("Awes is there")
# with open("E:\\awes.txt", "r") as my_file:
#     lines = my_file.readlines()
# for line in lines:
#     print(line, end='')

# writing to a file
names = ["awes", "mohd", "shaikh"]
with open("E:\\pythonwrite.txt", "w") as write_file:
    for i in range(1, 11):
        print("{0:>2} times 2 is {1}".format(i, i * 2),file=write_file)
print(dir())