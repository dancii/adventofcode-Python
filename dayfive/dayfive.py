#/usr/bin/python
import hashlib

def main():
    puzzle_input = "ffykfhsq"
    var = 0
    count = 0
    password = ""
    while var != 8:
        md5hash = hashlib.md5(puzzle_input+str(count)).hexdigest()
        first_five_char = md5hash[:5]
        if first_five_char == "00000":
            password += md5hash[5]
            var+=1
        count+=1
    print(password)

def part2main():
    puzzle_input = "ffykfhsq"
    password = ['-'] * 8
    var = 0
    count = 0
    while var == 0:
        md5hash = hashlib.md5(puzzle_input+str(count)).hexdigest()
        first_five_char = md5hash[:5]
        if first_five_char == "00000":
            try:
                pos = int(md5hash[5])
                char = md5hash[6]
                password = password_creater(pos,char,password)
            except ValueError:
                pass
        count+=1
        if check_if_done(password) == True:
            break
    print("".join(password))

def password_creater(pos,char,password_list):
    if pos >= 0 and pos <= 7:
        if password_list[pos] == '-':
            password_list[pos] = char
            print(password_list)
    return password_list

def check_if_done(password_list):
    is_done = True
    for x in xrange(0, len(password_list)-1):
        if password_list[x] == '-':
            is_done = False
        if is_done == False:
            return is_done
    return is_done

#main()
part2main()
