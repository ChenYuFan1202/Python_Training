#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys,string,argparse

#數字與英文的對應字典
_1to9dict = {"0":"","1":"one","2":"two","3":"three",
             "4":"four","5":"five","6":"six","7":"seven",
             "8":"eight","9":"nine"}
_10to19dict = {"0":"ten","1":"eleven","2":"twelve",
               "3":"thirteen","4":"fourteen","5":"fifteen",
               "6":"sixteen","7":"seventeen","8":"eighteen",
               "9": "nineteen"}
_20to99dict = {"2":"twenty","3":"thirty","4":"forty",
               "5":"fifty","6":"sixty","7":"seventy",
               "8":"eighty","9":"ninety"}

#數字位數與數字英文單位的對應串列（list）
#magnitude: the large size or importance of something
_magnitude_list = [(0,""),(3," thousand "),(6," million "),
                   (9," billion "),(12," trillion "),(15,"")]

#數字轉英文的函式
def num2words(num_string):
    if num_string == "0":
        return "zero"
    num_string = num_string.replace(",","")
    num_length = len(num_string)
    max_digits = _magnitude_list[-1][0]
    if num_length > max_digits:
        return "Sorry, can't handle numbers with more than "               "{0} digits".format(max_digits)
    num_string = "00" + num_string
    word_string = ""
    
    for mag,name in _magnitude_list:
        if mag >= num_length:
            return word_string
        else:
            hundreds, tens, ones = num_string[-mag-3],            num_string[-2],num_string[-1]
            if not (hundreds == tens == ones == "0"):
                word_string = _handle1to999(hundreds,tens,ones) +                 name + word_string
                
#處理1~999的函式
def _handle1to999(hundreds,tens,ones):
    if hundreds == "0":
        return _handle1to99(tens,ones)#_10to19dict[tens] + _1to9dict[ones]
    else:
        return _1to9dict[hundreds] +         " hundred " + _handle1to99(tens,ones)
    
#處理1~99的函式
def _handle1to99(tens,ones):
    if tens == "0":
        return _1to9dict[ones]
    elif tens == "1":
        return _10to19dict[ones]
    else:
        return _20to99dict[tens] + " " +  _1to9dict[ones]
    
#負責處理測試模式的函式
def test():
    values = sys.stdin.read().split()
    for val in values:
        print("{0} = {1}".format(val,num2words(val)))
        
#定義主控函式
def main():
    parser = argparse.ArgumentParser(usage = __doc__)#usage:字串，主要是會顯示來告知使用者說應該怎麼使用你寫的 program
    #__doc__為docstring文件字串
    parser.add_argument("num",nargs="*")
    
    parser.add_argument("-t","--test",dest="test",
                       action = "store_true",default=False,
                       help = "Test mode: reads from stdin")
    args = parser.parse_args()
    if args.test:
        test()
    else:
        try:
            result = num2words(args.num[0])
        except KeyError:
            parser.error("argument contains non-digits")
        else:
            print("{0}的英文唸法是:{1}".format(args.num[0],result))

if __name__ == "__main__":
    main()
else:
    print("n2w已被匯入為模組")

