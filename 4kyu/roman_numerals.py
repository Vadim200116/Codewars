# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/pytho
class RomanNumerals:
    switch_to_roman={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",11:"IX",10:"X",5:"V",4:"IV",1:"I"}

    switch_from_roman={"I":1,"IV":4,"V":5,"IX":11,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}

    def to_roman(val):
        res=""
        for k,v in RomanNumerals.switch_to_roman.items():
            if val>=k:
                for _ in range(val//k):
                    res+=v
                val-=((val//k)*k)
        return res

    def from_roman(roman_num):
        res=0
        l=0
        while l < (len(roman_num)):
            if roman_num[l]=="I" and l==len(roman_num)-1:
                res+=1
                l+=1
            elif roman_num[l]=="I" and roman_num[l+1]=="V":
                res+=4
                l+=2
            elif roman_num[l] in RomanNumerals.switch_from_roman.keys():
                res+=RomanNumerals.switch_from_roman[roman_num[l]]
                l+=1
        return res

print(RomanNumerals.to_roman(3456))
