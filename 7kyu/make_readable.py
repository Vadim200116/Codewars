# def make_readable(seconds):
    # min_del=60
    # hour_del=min_del*60

    # h=int(seconds/hour_del)
    # m=int((seconds-(h*hour_del))/min_del)
    # s=seconds-(m*min_del+h*hour_del)

    # return "%02d:%02d:%02d" % (h, m, s)

def make_readable(s):
    print(s%60)
    return '{:02}:{:02}:{:02}'.format(int(s / 3600),int( s / 60 % 60), int(s % 60))

print(make_readable(362))