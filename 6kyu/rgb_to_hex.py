# def check_num(x):
#     if x>255:
#         return 255
#     if x<0:
#         return 0
#     return x

# def rgb(r, g, b):
#     nums=[r,g,b]
#     n=list(map(check_num,nums ))
#     fmt = '{:02X}' * len(n)
#     return fmt.format(*n)


def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

print(rgb(0, 0, 300))

