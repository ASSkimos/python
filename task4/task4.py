import re
def get_text(name):
    try:
        file = open(name, 'r', encoding='utf-8')
        line = file.readlines()
        file.close()
    except:
        print("File doesn't exist")
        return
    return line
def solve(text):
    new_text=[];
    for i in range(len(text)):
        elem=re.sub(r'([a-zA-Z_]\w*)\+\+', r'\1=\1+1', text[i])
        new_text.append(elem)
    return new_text;

def write_text(name,text):
    file = open(name, 'w',encoding='utf-8')
    file.write(text)
    return
def to_string(text):
    str='';
    for i in range(len(text)):
        str+=text[i]
    return str

text=get_text('task4_input')
print(to_string(text))
print()
new_text=solve(text)
print(to_string(new_text))
write_text('task4_output',to_string(new_text))

