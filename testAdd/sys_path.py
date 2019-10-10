import  os
filedir ="E:"+os.sep
for abs_path,dirs,files in os.walk(filedir):
    for name in files:
        print(os.path.join(abs_path, name))
    for name in dirs:
        print(os.path.join(abs_path, name))