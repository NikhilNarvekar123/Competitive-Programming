class Solution:
    def myAtoi(self, s: str) -> int:
        
        # step 1
        s = s.strip()
        
        if len(s) == 0:
            return 0
        
        # step 2
        sign = 1
        start = 0
        if s[start] == '-' or s[start] == '+':
            sign = 1 if s[start] == '+' else -1
            start += 1
        
        # step 3
        num = 0
        int_min = -pow(2, 31)
        int_max = pow(2, 31) - 1
        
        for i in range(start, len(s)):
            if s[i].isnumeric():
                digit = int(s[i])
                if sign == 1 and (num > int_max // 10 or (num == int_max // 10 and digit > int_max % 10)):
                    return int_max
                elif sign == -1 and (-num < ceil(int_min / 10) or (-num == ceil(int_min / 10) and digit > abs(int_min) % 10)):
                    return int_min
                num *= 10
                num += digit
            else:
                break
        
        return sign * num
