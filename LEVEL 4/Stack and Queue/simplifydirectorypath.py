    s = A.split("/")
    res = "/"
    stk = []
    for i in range(len(s)):
        if s[i] != "" and s[i].isalpha() == True:
            stk.append(s[i])
        elif s[i] != "" and len(stk) != 0 and s[i] == "..":
            stk.pop()
        
    if len(stk) != 0:
        for i in range(len(stk)):
            res += stk[i]+"/"
    else:
        res = "/"
    
    if len(res)>1:
        res = res.rstrip("/")
        return res
    
    return res