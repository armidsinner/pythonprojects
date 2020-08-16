from math import fabs

def getkoof(p1, p2):
    k = (p1[1]-p2[1])/(p1[0]-p2[0])
    b = p2[1] - k*(p2[0])
    return k, b


def checkline(k, b, p):
    return fabs(p[1]-k*p[0]-b) < 1e-5


def get_max_line(a):
    max_set = []
    for j in range(len(a)-1): 
        for i in range(j+1, len(a)):
            tmp_set = []
            if a[i][0] != a[j][0]:
                koefs = getkoof(a[j], a[i])
                print(f'Coefs for points {a[j]} and {a[i]} : {koefs}')
                for point in a:
                    if checkline(koefs[0], koefs[1], point):
                        tmp_set.append(point)
            else:
                print(f'Line through {a[j]} and {a[i]} is a vertical line')
                for point in a:
                    if a[i][0] == point[0]:
                        tmp_set.append(point)
            if len(tmp_set) > len(max_set):
                max_set = tmp_set
            print(tmp_set)
    return max_set, len(max_set)

line = get_max_line([(7.0, 3.0), (2.0, 8.0), (3.0, 8.0), (3.0, 13.0), (7.0, 4.0)])

print('\nMax points on one line:', line[1], '\nMax line includes points:', line[0])


line = get_max_line([(8.0, 3.0)])
print('\nMax points on one line:', line[1], '\nMax line includes points:', line[0])