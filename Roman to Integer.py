class Solution:
    # @return a int
    def romanToInt(self, s):
        dct = {}
        dct['I'] = 1; dct['i'] = 1;
        dct['V'] = 5; dct['v'] = 5;
        dct['X'] = 10; dct['x'] = 10;
        dct['L'] = 50; dct['l'] = 50;
        dct['C'] = 100; dct['c'] = 100;
        dct['D'] = 500; dct['d'] = 500;
        dct['M'] = 1000; dct['m'] = 1000;

        sum = 0;i=0
        while i < len(s):
            j = i+1;
            if(j < len(s)  and dct[s[j]] > dct[s[i]]):
                sum += dct[s[j]] - dct[s[i]];
                i = j+1;
            else:
                sum += dct[s[i]];
                i += 1
        return sum;