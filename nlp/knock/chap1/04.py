s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
s = s.split(' ')
s = [n.replace('.', '') for n in s]

indexs = [1,5,6,7,8,9,15,16,19]
indexs = [i - 1 for i in indexs]

dic = {}
for i in range(len(s)):
    if i in indexs:
        n = s[i][0]
    else:
        n = s[i][0:2]

    dic[n] = i + 1

print(dic)