class Solution:
    def intToRoman(self, num: int) -> str:
        d = {'I': 1,'V' : 5,'X' : 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000, 'IV': 4,
             'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900}
        d = dict(sorted(d.items(), key = operator.itemgetter(1),reverse=True))
        res = ""
        for key, val in d.items():
            if num//val:
                count= num//val
                res+= key*count
                num = num % val
        return res        