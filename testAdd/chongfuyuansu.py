#一组字母统计每个字符的数量，并排序后把最大的输出来
def sort_elements(str):
    str1 = list(str)
    set_str =set(str)
    dict1={}
    for i in set_str:
        dict1.update({i:str1.count(i)})
    list1= sorted(dict1.items(),key=lambda x:x[1],reverse=True)
    print(list1)
    print(list1[0][0])



def sort_elements2(str):
    exceptLen = 0
    temLen = 0
    exceptLetter =''
    for letter in str:
        temLen =len(str)
        str = str.replace(letter,'')
        temLen =temLen-len(str)
        if temLen >= exceptLen:
            exceptLen =temLen
            exceptLetter =letter
    print(exceptLetter)

str ="DJFDNFDNADFLAJDODTAaaaaa"
sort_elements2(str)

def format_num(s):
    s=int(s)
    num1='%0.6d'%s
    print(num1)

if __name__ == '__main__':
    s='3'
    format_num(s)

