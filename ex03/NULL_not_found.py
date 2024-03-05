import math


def NULL_not_found(obj: any) -> int:
    if obj is None:
        print("Nothing : ", obj, type(obj))
    elif isinstance(obj, float) and math.isnan(obj):
        print("Cheese : ", obj, type(obj))
    elif obj == 0:
        print("Zero : ", obj, type(obj))
    elif isinstance(obj, str) and obj == '':
        print("Empty : ", type(obj))
    elif isinstance(obj, bool) and not obj:
        print("Fake : ", obj, type(obj))
    else:
        print("Type not Found")
        return 1
    return 0
