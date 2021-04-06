print("Program to output compressed version of string\n");

def compress(string):
    cmap = []
    idx = -1
    
    for x in string:
        if idx < 0:
            cmap.append([x, 1])
            idx = 0
        else:
            if cmap[idx][0] == x:
                cmap[idx][1] += 1
            else:
                cmap.append([x, 1])
                idx += 1
    s = ""
    for cc in cmap:
        s += str(cc[0]) + str(cc[1])  
    if len(s) < len(string):
        return s
    else:
        return string


print(compress("aabcccccaaaddddfffssssaaaasd"))