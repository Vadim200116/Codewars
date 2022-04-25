# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python


def valid_parentheses(string):
    lst=list(string)
    for l in lst:
        if l=='(':
            if ')' not in lst:
                return False
            lst[lst.index(')')]=0
        elif l==')':
            return False
    return True

# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False


print(valid_parentheses("(t(est))"))







