

# def decrypt(encrypted_text, n):
#     if encrypted_text=="" or n<1:
#         return encrypted_text
#     for i in range(n):
#         result=""
#         start=0
#         mid=int(len(encrypted_text)/2)
#         while(mid<len(encrypted_text)):
#             result+=encrypted_text[mid]
#             if(start<int(len(encrypted_text)/2)):
#                 result+=encrypted_text[start]
#             start+=1    
#             mid+=1
#         encrypted_text=result
#     return result


# def encrypt(text, n):
#     if text=="" or n<1:
#         return text
#     for i in range(n):
#         odd=""
#         even=""
#         index=0
#         while(index<len(text)):
#             if (index%2):
#                 odd+=text[index]
#             else:
#                 even+=text[index]
#             index+=1
#         text=odd+even
#     return(text)



def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

print(encrypt("01234", 2))
print(decrypt(encrypt("01234", 2),2))




