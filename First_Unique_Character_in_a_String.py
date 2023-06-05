def First_Unique_Character_in_a_String(line):
    alpha = [0]*26
    for l in line:
        alpha[ord(l)-97]+=1
    ans = -1
    i = 0
    for l in line:
        if alpha[ord(l)-97] == 1:
            ans = i
            break
        i+=1
    return ans
