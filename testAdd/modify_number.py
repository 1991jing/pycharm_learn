import datetime

with open('C:/Users/Administrator/Desktop/change_line.txt','r',encoding='utf-8') as f :
    lines =[]
    for line in f:
        if line!='\n':
            lines.append(line)
    f.close()

with open('C:/Users/Administrator/Desktop/change_line.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if "2019.10.7" in line:
            line = line.replace('2019.10.7', str(datetime.date.today()))
        f.write(line)


