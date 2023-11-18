def new_sum(*nums):
    res = 0
    for x in nums:
        try:
            res += sum(*x)
        except:
            res += x
    return res
