a = "abcdefghigklmnopqrstuvwxyz"
a2 = "!@#$%^&*()-_+=[]{};:'"
a3 = "\",<.>?|\/"
l = len(a)
def encrypt(text , scale) -> str:
    chars = list(text)
    result = ""
    for char in chars:
        try:
            index = a.index(char) # get index
            index = index + scale # add scale
            index = index % l # solve overflow
            result = result + a[index]
        except ValueError:
            if char in a2:
                index = a2.index(char) # get index
                index = index + scale # add scale
                index = index % l # solve overflow
                result = result + a[index]

            elif char in a3:
                index = a3.index(char) # get index
                index = index + scale # add scale
                index = index % l # solve overflow
                result = result + a[index]


            
            
        