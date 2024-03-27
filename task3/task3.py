from enrollee import Enrollee

def read_enrollees(name):
    list=[]
    try:
        file = open(name, 'r',encoding='utf-8')
        for line in file:
            row = line.split()
            list.append(Enrollee(row[0], int(row[1]), int(row[2]), int(row[3])))
        file.close()
    except FileNotFoundError:
        print("File doesn't exist")
        return
    return list
list=read_enrollees('task3_input')
def write_enrollees(list,name):
    file = open(name, 'w',encoding='utf-8')
    if len(list)!=0:
        for student in list:
            file.write(student.full_name+' '+str(student.russian)+' '+str(student.math)+' '+str(student.physics)+'\n')
    file.close()
def solve(list, N):
    new_list=sorted(list,key=lambda x:(-(x.math + x.russian + x.physics),-x.math,-x.physics))
    result=[]
    for i in range(N):
        result.append(new_list[i])
    return result

print('Список абитуриентов')
list=read_enrollees('task3_input')
for student in list:
    student.print_info()
print()
print('Отобранные студенты')
result=solve(list,5)
for student in result:
    student.print_info()
write_enrollees(result,'task3_output')
