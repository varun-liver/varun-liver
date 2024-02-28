a = "abcdefghigklmnopqrstuvwxyz"
l = len(a)
def encrypt(text , scale) -> str:
    chars = list(text)
    result = ""
    for char in chars:
        index = a.index(char) # get index
        index = index + scale # add scale
        index = index % l # solve overflow
        result = result + a[index]
        return result