import os

a = open("file_list.js", "w")
content = "FILE_LIST = ["
for path, subdirs, files in os.walk(r'../data'):
   for filename in files:
     f = os.path.join(path, filename)
     if str(f)[-3:] == "csv":
     	content += "\"" + str(f)[3:] + '\", ' + os.linesep
     #a.write(str(f) + ', ' + os.linesep)
content = content[:-3]
content += "]"
a.write("// A way get a value from another .js file is saving the variable in the browser\n")
a.write(content+'\n')
#a.write("localStorage.setItem(\"fileList\",fileList);")
