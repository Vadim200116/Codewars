# https://www.codewars.com/kata/59de1e2fe50813a046000124/train/python

import re

def change(data, new_program, new_version):
    try:
        curr_phone = re.search(r'^Phone\: (\+1-\d{3}-\d{3}-\d{4})$', data, re.M).group(1)
        curr_version = re.search(r'^Version\: (\d+\.\d+)$', data, re.M).group(1)
    except:
        return 'ERROR: VERSION or PHONE'

    return 'Program: {} Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: {}'.format(new_program, new_version if curr_version != '2.0' else curr_version)




q=[[10,2]]
b=list(q)
b[0][1]+=1
print(q)