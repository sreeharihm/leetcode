class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1
        index=0
        n= len(s)
        result=0
        INT_MAX= pow(2,31)-1
        INT_MIN =-pow(2,31)
        while index < n and s[index] == ' ':
            index+=1
        if index <n and s[index] == '+':
            sign=1
            index+=1
        elif index<n and s[index] == '-':
            sign=-1
            index+=1
        while index<n and s[index].isdigit():
            digit = int(s[index])
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return INT_MAX if sign == 1 else INT_MIN
            result =result*10+digit
            index+=1
        return result * sign
    
a =Solution()
print(a.myAtoi("   -42"))