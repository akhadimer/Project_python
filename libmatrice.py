def det2(arg):
    return (arg[0][0] * arg[1][1] - arg[0][1] * arg[1][0])


def det3(arg):
    return (arg[0][0] * det2([[arg[1][1],arg[1][2]],arg[2][1],arg[2][2]])) - (arg[0][1] * det2([[arg[1][0],arg[1][2]],arg[2][0],arg[2][2]])) + (arg[0][2] * det2([arg[1][0],arg[1][1],arg[2][0],arg[2][1]]))
