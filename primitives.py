from collections import defaultdict


def listToDefaultDict(list, default_fun = lambda: 0.0, skip_fun = lambda x: x < 1e-6):
    res_ = defaultdict(default_fun)
    if skip_fun:
        for _ in list:
            if skip_fun(_):
                pass      
            res_[list.index(_)] = _ 
    else:
        for i in range(len(list)):
            res_[i] = list[i]        
    return res_