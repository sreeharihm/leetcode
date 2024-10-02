class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        num =columnNumber
        op=""
        while num>0:
            op = alphabet[(num%26)-1]+op
            num-=1
            num=num//26
        return op
    
a =Solution()
print(a.convertToTitle(701))