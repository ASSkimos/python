# переменная++ -->переменная=переменная+1
def get_text(name):
    try:
        file = open(name, 'r', encoding='utf-8')
        line = file.readlines()
        file.close()
    except:
        print("File doesn't exist")
        return
    return line


def write_text(name, text):
    file = open(name, 'w', encoding='utf-8')
    file.write(text)
    return


def to_string(text):
    str = ''
    for i in range(len(text)):
        str += text[i]
    return str


# опреление некорректного символа:
# param=0 для начала переменной
# param=1 для конца переменной
def incorrect_symbol(symbol, param):
    if param == 0:
        return symbol in '(){}[]%@&*$^#<>?№-+=' or symbol.isdigit() or symbol == ' '
    else:
        return symbol in '(){}[]%@&$*^#<№>?_-+=' or symbol == ' '


def get_var(row):
    list = []
    for i in range(len(row) - 2):
        if not incorrect_symbol(row[i], 1) and row[i + 1] == '+' and row[i + 2] == '+':
            var = '++'
            end_digits = True
            j = i
            while not incorrect_symbol(row[j], 0) or end_digits:
                if not row[j].isdigit():
                    end_digits = False
                var = row[j] + var
                j = j - 1
            list.append(var)
    return list


def solve(text):
    new_list = []
    for i in range(len(text)):
        row = to_string(text[i])
        vars = get_var(row)
        for j in range(len(vars)):
            row = row.replace(vars[j], vars[j][:len(vars[j]) - 2] + '=' + vars[j][:len(vars[j]) - 2] + '+1')
        new_list.append(row)
    return new_list


text = get_text('task4_input')
print(to_string(text))
print()
for i in range(len(text)):
    print(get_var(to_string(text[i])))
print()
new_text = solve(text)
print(to_string(new_text))
write_text('task4_output', to_string(new_text))
