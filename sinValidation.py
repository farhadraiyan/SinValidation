def validateSIN(sinNum):
    #multiple the sin by 121212121
    defNum = "121212121"
    prod = 0
    #check if the length is 9 digit
    if(len(sinNum) != 9):
        return False
    else:
        for i in range(9):
            currProd = int(defNum[i])*int((sinNum[i]))
            strCurr = str(currProd)
            if(len(strCurr))>1:
                intCurr = int(strCurr[0])+int(strCurr[1])
                prod+=int(intCurr)
            else:
                prod+=int(strCurr)
    if(prod%10==0):
        return True
    return False      


print(validateSIN("130692544"))
