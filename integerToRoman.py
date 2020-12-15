class Solution:
    def intToRoman(self, num: int) -> str:
        
        rez = ""
        rez = self.itr(num, rez)
        return rez
        
        
    def itr(self, num, rez) -> str:
        
        if(num <= 0):
            return rez
        
        if(num - 1000 >= 0):
            rez += "M"
            rez = self.itr(num - 1000, rez)
        elif(num - 900 >= 0):
            rez += "CM"
            rez = self.itr(num - 900, rez)
        elif(num - 500 >= 0):
            rez += "D"
            rez = self.itr(num - 500, rez)
        elif(num - 400 >= 0):
            rez += "CD"
            rez = self.itr(num - 400, rez)
        elif(num - 100 >= 0):
            rez += "C"
            rez = self.itr(num - 100, rez)
        elif(num - 90 >= 0):
            rez += "XC"
            rez = self.itr(num - 90, rez)
        elif(num - 50 >= 0):
            rez += "L"
            rez = self.itr(num - 50, rez)
        elif(num - 40 >= 0):
            rez += "XL"
            rez = self.itr(num - 40, rez)
        elif(num - 10 >= 0):
            rez += "X"
            rez = self.itr(num - 10, rez)
        elif(num - 9 >= 0):
            rez += "IX"
            rez = self.itr(num - 9, rez)
        elif(num - 5 >= 0):
            rez += "V"
            rez = self.itr(num - 5, rez)
        elif(num - 4 >= 0):
            rez += "IV"
            rez = self.itr(num - 4, rez)
        elif(num - 1 >= 0):
            rez += "I"
            rez = self.itr(num - 1, rez)
        
        
        return rez
    
    
    
    
    
    
