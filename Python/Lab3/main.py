from idlelib.debugobj_r import remote_object_tree_item


def func(*args, **kwargs):
    count = 0
    for x,val in kwargs.items():
        for i in args:
            if i == val:
                count+=1
    print(count)

func(1, 2, 3, x=1,y=2,z=3)


def compara(d1, d2):
    if type(d1) is not type(d2):
        return False

    t = type(d1)

    if type(d1) in (dict,list,tuple,set) and (len(d1) < len(d2) or len(d2) < len(d1)):
        return False

    if t is dict:
        return all(k in d2 and compara(d1[k], d2[k]) for k in d1)
    if t in (list, tuple):
        return all(compara(d1[i], d2[i]) for i in range(len(d1)))
    if t is set:
        return all(any(compara(x, y) for y in d2) for x in d1)

    return not (d1 < d2) and not (d2 < d1)

print(compara({1,2,3,4,5,6},{1,2,3,4,5,6}))