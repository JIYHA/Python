import re
import string

def TestReg(lst,reg):
    for i in range(len(lst)):
        parser = re.search(reg,lst[i])
        count =0
        while parser!=None:
            yield i+1,parser.regs[0][0]+count+1,parser.group()
            count+=parser.regs[0][1]
            lst[i] = lst[i][parser.regs[0][1]:]
            parser = re.search(reg,lst[i])

reg = "[A-ZА-ЯЁ][A-ZА-ЯЁa-zа-яё]+([0-9]{4}$|[0-9]{2}$)"
[print(res) for i, j, res in TestReg(input().split(),reg)]