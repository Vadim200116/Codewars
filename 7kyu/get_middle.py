# def get_middle(s):

#     return s[int((len(s)-1)/2)] if len(s)%2   else s[int((len(s)/2)-1):(int(len(s)/2)+1)]

def get_middle(s):
   print((len(s))/2)
   return s[int((len(s)-1)/2):int(len(s)/2+1)]

print(get_middle('testt'))