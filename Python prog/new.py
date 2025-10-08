''''import mymodule as b

a = b.person1["name"],b.person2['age']

print(a)


import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%C"))'''


def stud_det(mark):
    
    avg_mark={}
    for names,scores in mark.items():
        avg=round(sum(scores)/len(scores))
        avg_mark[names]=avg
    return avg_mark

        





