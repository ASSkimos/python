def get_list(name):
    file=open(name,'r')
    line=file.read()
    list=line.split(" ")
    for i in range(len(list)):
        list[i]=int(list[i])
    file.close()
    return list
def write_list(name, list):
    file = open(name, 'w')
    list=str(list)
    for i in range(len(list)):
        file.write(list[i])
    file.close()
def solve(list_of_nums):
    new_list = []
    new_list.append(list_of_nums[0])
    for i in range(1, len(list_of_nums)):
        if list_of_nums[i-1] != list_of_nums[i]:
            new_list.append(list_of_nums[i])
    return new_list


list_of_nums =get_list('task1_input')
new_list = solve(list_of_nums)
print(list_of_nums)
print(new_list)
write_list('task1_output',new_list)