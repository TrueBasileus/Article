import numpy as np
import matplotlib.pyplot as plt
import math
import decimal as d
c1 = 0
c2 = 1/3
c3 = 2/3
T_c2 = 1

c2_7 = 0.3395515826
c3_7 = 0.86

a = 1
b = 1/100
omega = 1
t0 = 1
tn = 2
c11 = 0
c22 = 1
c33 = 1/2
c44 = 1
c55 = 1/2
c66 = 1
h = 1/2
alp = 1.1

d.getcontext().prec = 32

def decision(t):
    return np.log(t)


# def delay(t):
#     return np.exp(1 - 1/t)

def f(t, func_Y):
    return 1 - func_Y(np.exp(1 - 1/t))

def init_f(t):
    return np.log(t)

class Polynom:
    def __init__(self, koef):
        self.koef = koef
        self.size = len(koef)
    def of(self, alpha):
        result = 0
        for i in range(self.size):
            result += self.koef[i]*alpha**(self.size - i - 1)
        return result


T_B2 = Polynom([1, 0, 0, 0, 0])
T_v = Polynom([1, 0, -2, 0, 1])
T_B1 = Polynom([-5/12, 1/6, 7/12, 0, 0])
T_b2 = Polynom([1/12, 1/6, 1/12, 0, 0])
T_b1 = Polynom(list(map(lambda x, y: x+y, [-2/3, -1/3, 4/3, 1, 0],[-i for i in T_B2.koef])))

T_A22 = Polynom([0,0,1,0])
T_u2 = Polynom([-2.0,-3.0,0,1])
T_A21=Polynom([1, 1, 0, 0])
T_a21=Polynom(list(map(lambda x, y: x+y, [1, 2,1,0], [-i for i in T_A22.koef])))

b3 = Polynom([3/10, 67/80, 0,0,0,-7/160,0])
v = Polynom(list(map(lambda x, y: x+y, [54.0, 108.0, 45.0, -20.0, -12.0, 0.0, 1.0], [-160*i for i in b3.koef])))
b1 = Polynom(list(map(lambda x, y: x+y, [-189/20, -108/5, -27/2, 1.0, 67/20, 1.0, 0.0], [38*i for i in b3.koef])))
b2 = Polynom(list(map(lambda x, y: x+y, [27/40, 81/40, 9/4, 9/8, 9/40, 0.0, 0.0], [-7*i for i in b3.koef])))
B1 = Polynom(list(map(lambda x, y: x+y, [-243/40, -459/40, -9/2, 17/8, 49/40, 0.0, 0.0], [17*i for i in b3.koef])))
B2 = Polynom(list(map(lambda x, y: x+y, [-459/20, -243/5, -45/2, 9, 117/20, 0.0, 0.0], [73*i for i in b3.koef])))
B3 = Polynom(list(map(lambda x, y: x+y, [-81/5, -567/20, -27/4, 27/4, 27/20, 0.0, 0.0], [38*i for i in b3.koef])))

u2 = Polynom([-54.0, -135.0, -110.0, -30.0, 0.0, 1.0])
A21 = Polynom([27/4, 63/4, 49/4, 13/4, 0.0, 0.0])
A22 = Polynom([81/4, 54, 189/4, 27/2, 0.0, 0.0])
A23 = Polynom([81/4, 189/4, 135/4, 27/4, 0.0, 0.0])
a21 = Polynom([27/4, 18.0, 67/4, 13/2, 1.0, 0.0])

A31 = Polynom([81/80, 0.0, 0.0, 0.0, 0.0, 0.0])
u3 = Polynom(list(map(lambda x, y: x+y, [6.0, 5.0, -10/9, -10/9, 0.0, 1.0], [-80*i/9 for i in A31.koef])))
A32 = Polynom(list(map(lambda x, y: x+y, [-21/4, -11/2, 35/36, 11/9, 0.0, 0.0], [34*i/9 for i in A31.koef])))
A33 = Polynom(list(map(lambda x, y: x+y, [9/4, 21/4, 13/12, -23/12, 0.0, 0.0], [8*i/3 for i in A31.koef])))
a31 = Polynom(list(map(lambda x, y: x+y, [-15/4, -13/2, -83/36, 13/9, 1.0, 0.0], [14*i/9 for i in A31.koef])))
a32 = Polynom(list(map(lambda x, y: x+y, [3/4, 7/4, 49/36, 13/36, 0.0, 0.0], [-1*i/9 for i in A31.koef])))

b11 = Polynom([2/3, -3/2, 1, 0])
b55 = Polynom([-4/3, 2, 0, 0])
b66 = Polynom([2/3, -1/2, 0, 0])

a211 = Polynom([1, 0])
a311 = Polynom([-1/2, 1, 0])
a322 = Polynom([1/2, 0, 0])
a411 = Polynom([-1/2, 1, 0])
a422 = Polynom([1/2, 0, 0])
a511 = Polynom([2/3, -3/2, 1, 0])
a533 = Polynom([-4/3, 2, 0, 0])
a544 = Polynom([2/3, -1/2, 0, 0])
a611 = Polynom([2/3, -3/2, 1, 0])
a633 = Polynom([-4/3, 2, 0, 0])
a644 = Polynom([2/3, -1/2, 0, 0])

# b3_5 = Polynom([81/160,0,0,0,0,0,])
# B1_5 = Polynom([81/160, 0, 0, 0, 0, 0])

b3_5 = Polynom([9/16,0,0,0,0,0,])
B1_5 = Polynom([0, 9/20, 0, 0, 0, 0])

v_5 = Polynom(list(map(lambda x, y, z: x+y+z, [6.0, 5.0, -10/9, -10/9, 0.0, 1.0], [-80*i/9 for i in b3_5.koef], [-80*i/9 for i in B1_5.koef])))
b1_5 = Polynom(list(map(lambda x, y,z: x+y+z, [-15/4, -13/2, -83/36, 13/9, 1.0, 0.0], [104*i/9 for i in b3_5.koef], [14*i/9 for i in B1_5.koef])))
b2_5 = Polynom(list(map(lambda x, y, z: x+y+z, [3/4, 7/4, 49/36, 13/36, 0, 0.0], [-46*i/9 for i in b3_5.koef], [-i/9 for i in B1_5.koef])))
B2_5 = Polynom(list(map(lambda x, y,z: x+y+z, [-21/4, -11/2, 35/36, 11/9, 0, 0.0], [79*i/9 for i in b3_5.koef], [34*i/9 for i in B1_5.koef])))
B3_5 = Polynom(list(map(lambda x, y,z: x+y+z, [9/4, 21/4, 13/12, -23/12, 0, 0.0], [-22*i/3 for i in b3_5.koef], [8*i/3 for i in B1_5.koef])))

A21_5 = Polynom([0, -3, 0, 0.0, 0.0])
u2_5 = Polynom(list(map(lambda x, y: x+y, [-9, -12, -4, 0.0, 1], [-8*i for i in A21_5.koef])))
A22_5 = Polynom(list(map(lambda x, y: x+y, [27/4, 21/2, 15/4, 0.0, 0], [3*i for i in A21_5.koef])))
A23_5 = Polynom(list(map(lambda x, y: x+y, [0, -3, -3, 0.0, 0], [3*i for i in A21_5.koef])))
a21_5 = Polynom(list(map(lambda x, y: x+y, [9/4, 9/2, 13/4, 1, 0], [i for i in A21_5.koef])))

A31_5 = Polynom([-9/32, 0, 0.0, 0.0, 0.0])
A33_5 = Polynom([27/16, 0,0,0, 0.0])
u3_5 = Polynom(list(map(lambda x, y, z: x+y+z, [-9, -4, 4, 0, 1], [-16*i for i in A31_5.koef], [8*i/3 for i in A33_5.koef])))
a32_5 = Polynom(list(map(lambda x, y, z: x+y+z, [0, 1, 1, 0, 0], [-i for i in A31_5.koef], [i/3 for i in A33_5.koef])))
a31_5 = Polynom(list(map(lambda x, y, z: x+y+z, [9/4, -1/2, -7/4, 1, 0], [6*i for i in A31_5.koef], [-5*i/3 for i in A33_5.koef])))
A32_5 = Polynom(list(map(lambda x, y, z: x+y+z, [27/4, 7/2, -13/4, 0, 0], [10*i for i in A31_5.koef], [-i*7/3 for i in A33_5.koef])))



# b3_7 = Polynom([0,0, 0, 0, 0, 0.2832770571, 0])
# v_7 = Polynom(list(map(lambda x, y: x+y, [ 234.9572670, 394.3484507, 70.77505787,- 103.6661682,-16.05004245, 0, 1],[-2051.680795*i for i in b3_7.koef] )))
# b1_7 = Polynom(list(map(lambda x, y: x+y, [49.61953715,74.49719708, -0.4095507625, -24.83254417, 1.454666521, 1 , 0],[-362.2681653*i for i in b3_7.koef])))
# b2_7 = Polynom(list(map(lambda x, y: x+y, [-1.785101338, -2.059138572, 1.511064040, 2.059138444, 0.2740371697,0 ,0],[3.176274957*i for i in b3_7.koef])))
# B1_7 = Polynom(list(map(lambda x, y: x+y, [-25.23100648, -41.87813607,-7.366418603,10.97754508, 1.696834096, 0 , 0],[218.5239082*i for i in b3_7.koef])))
# B2_7 = Polynom(list(map(lambda x, y: x+y, [-122.1815063, -206.6663948,-38.30181724, 54.66952481, 8.486453532, 0 , 0],[1074.416391*i for i in b3_7.koef])))
# B3_7 = Polynom(list(map(lambda x, y: x+y, [-135.3791901, -218.2419783,-26.20833531, 60.79250406, 4.138051127, 0 , 0],[1116.832386*i for i in b3_7.koef])))
#
# u2_7 = Polynom([123.3220608,  269.6631935, 167.3602048, 20.01907199, 0, 1])
# A21_7 = Polynom([-12.77382835, -28.72412294,-18.12676082, -2.176466235, 0 ,0])
# A22_7 = Polynom([-65.72837241,-141.7268030,-86.26848878, -10.27005819, 0, 0])
# A23_7 = Polynom([-62.08024891,-140.8049812,-95.36921558,-16.64448334,0 ,0])
# a21_7 = Polynom([17.26038890,41.59271357,32.40426043,9.071935766,1,0])
#
# A31_7 = Polynom([0.0, 0.0, 0.0, 0.0,-33.59345315/0.9, 0.0])
#
# u3_7 = Polynom(list(map(lambda x, y: x+y, [4.369065346,2.177176780, -1.440599339,  -0.2487107731, 0, 1], [-9.312243139*i for i in A31_7.koef])))
# a31_7 = Polynom(list(map(lambda x, y: x+y, [-7.860743338,-14.89641960,-3.243999678, 4.791676582, 1,0], [-1.966609504*i for i in A31_7.koef])))
# a32_7 = Polynom(list(map(lambda x, y: x+y, [0.9037522185, 2.032240384, 1.282473809, 0.1539856443,0,0], [0.07075030239*i for i in A31_7.koef])))
# A33_7 = Polynom(list(map(lambda x, y: x+y, [ 6.458853455, 13.31683325, 1.891517955, -4.966461838,0,0], [5.365588176*i for i in A31_7.koef])))
# A32_7 = Polynom(list(map(lambda x, y: x+y, [-3.870927682,-2.629830815,1.510607252, 0.2695103849,0,0  ], [4.842514164*i for i in A31_7.koef])))

b3_7 = Polynom([0.3499106359 +8/2194.082430 - 20/2194.082430,-20/2194.082430, 0, 0, 0, -8/2194.082430 + 20/2194.082430 +20/2194.082430, 0])
v_7 = Polynom(list(map(lambda x, y: x+y, [ 288.895588, 506.4559816, 122.0148003,-121.7559885,-27.21039610, 0, 1],[-2194.082430*i for i in b3_7.koef] )))
b1_7 = Polynom(list(map(lambda x, y: x+y, [23.91141936,35.54827818, -1.533902420, -13.06696195,1.103799292, 1 , 0],[-134.7204256*i for i in b3_7.koef])))
b2_7 = Polynom(list(map(lambda x, y: x+y, [-1.71329009, -2.086612275, 1.33996796, 2.086612372, 0.37332222,0 ,0],[1.861768991*i for i in b3_7.koef])))
B1_7 = Polynom(list(map(lambda x, y: x+y, [-30.05645087, -52.17995984,-12.39975156,12.5145729, 2.79081550, 0 , 0],[226.5307268*i for i in b3_7.koef])))
B2_7 = Polynom(list(map(lambda x, y: x+y, [-145.3129148, -256.4582055,-63.08733633, 61.94828469, 13.89033031, 0 , 0],[1110.744475*i for i in b3_7.koef])))
B3_7 = Polynom(list(map(lambda x, y: x+y, [-135.7243525, -231.2794822,-46.33377797,58.27348043, 9.05212876, 0 , 0],[988.6658842*i for i in b3_7.koef])))

u2_7 = Polynom([154.6106735,  347.960678, 230.0893358, 35.73933116, 0, 1])
A21_7 = Polynom([-15.57427384, -35.90696814,-24.09111478, -3.758420471, 0 ,0])
A22_7 = Polynom([-79.48192330,-176.7368878,-115.0280057, -17.77304118, 0, 0])
A23_7 = Polynom([-65.98108904,-152.4840937,-107.024920,-20.52191563,0 ,0])
a21_7 = Polynom([6.42661266,17.16727145,16.05470491,6.314046125,1,0])

A31_7 = Polynom([0.0, 0.0, 0.0, 0.0,-33.46542706/0.86, 0.0])

u3_7 = Polynom(list(map(lambda x, y: x+y, [4.91438930, 2.831283095, -1.468835189,  -0.3857289763, 0, 1], [-9.611766544*i for i in A31_7.koef])))
a31_7 = Polynom(list(map(lambda x, y: x+y, [-5.963506002,-11.39852885,-3.110989359, 3.324033486, 1,0], [-0.7955503283*i for i in A31_7.koef])))
a32_7 = Polynom(list(map(lambda x, y: x+y, [0.887771122, 2.046783674, 1.373251571, 0.2142390198,0,0], [0.0570024087*i for i in A31_7.koef])))
A33_7 = Polynom(list(map(lambda x, y: x+y, [4.346849593, 9.65913547, 1.762074161, -3.550211720,0,0], [4.515648008*i for i in A31_7.koef])))
A32_7 = Polynom(list(map(lambda x, y: x+y, [-4.185504022,-3.138673398,1.444498815, 0.3976681907,0,0  ], [4.83466645*i for i in A31_7.koef])))


K1 = []
K2 = []
K3 = []

K1_7 = []
K2_7 = []
K3_7 = []

K1_5=[]
K2_5=[]
K3_5=[]

T_K1 = []
T_K2 = []

K_Begin = [[],[],[],[],[],[]]

Sols_on_tn = [init_f(t0)]
Sols_on_tn_for_another = [init_f(t0)]
Sols_on_tn_for_Tuzov = [init_f(t0)]
Sols_on_tn_5 =[init_f(t0)]
Sols_on_tn_7 = [init_f(t0)]
arr_tn = [t0]


def T_Y1(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return Tuzov_Method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1] >= t: num += 1
    return Sols_on_tn_for_Tuzov[num-1]

def T_Y2(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[- 1]:
        return Tuzov_Method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num-1])/h
    return (1 - T_u2.of(alpha))*Sols_on_tn_for_Tuzov[num- 2] + T_u2.of(alpha)*Sols_on_tn_for_Tuzov[num- 1] + \
            h*(T_A21.of(alpha)*T_K1[num - 2] + T_A22.of(alpha)*T_K2[num - 2]) + h*T_a21.of(alpha) * T_K1[num - 1]

def Y11(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return another_method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0: num+=1
    return Sols_on_tn_for_another[num - 1]

def Y22(t):
    if t <= t0: return init_f(t)
    if t<= arr_tn[-1]: return another_method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num-1])/h
    return init_f(t) if t<=t0 else Sols_on_tn_for_another[num-1] + h*a211.of(alpha)*K_Begin[0][num-1]

def Y33(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return another_method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num-1]) / h
    return init_f(t) if t <= t0 else Sols_on_tn_for_another[num-1] + h * a311.of(alpha) * K_Begin[0][num-1] + h*a322.of(alpha)*K_Begin[1][num - 1]

def Y44(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return another_method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num-1]) / h
    return init_f(t) if t <= t0 else Sols_on_tn_for_another[num-1] + h * a411.of(alpha) * K_Begin[0][num - 1] + h * a422.of(alpha) * K_Begin[1][num - 1]

def Y55(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return another_method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num-1]) / h
    return init_f(t) if t<=t0 else Sols_on_tn_for_another[num-1] + h*a511.of(alpha)*K_Begin[0][num -1] + h*a533.of(alpha)*K_Begin[2][num - 1] + h*a544.of(alpha)*K_Begin[3][num -1]

def Y66(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return another_method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num-1]) / h
    return init_f(t) if t<=t0 else Sols_on_tn_for_another[num-1] + h*a611.of(alpha)*K_Begin[0][num -1] + h*a633.of(alpha)*K_Begin[2][num -1] + h*a644.of(alpha)*K_Begin[3][num -1]


def Y1(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return my_method(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1] >= t: num += 1
    return Sols_on_tn[num - 1]

def Y2(t):
    if t < t0: return init_f(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num -1])/h
    if t <= (t0 + h) or t <= arr_tn[- 1]:
        return my_method(t)
    else:
        return (1 - u2.of(alpha))*Sols_on_tn[num- 2] + u2.of(alpha)*Sols_on_tn[num- 1] + \
               h*(A21.of(alpha)*K1[num - 2] + A22.of(alpha)*K2[num - 2] + A23.of(alpha)*K3[num -2]) + h*a21.of(alpha) * K1[num - 1]

def Y3(t):
    if t < t0: return init_f(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num - 1]) / h
    if (t <= (t0 + h) or t <= arr_tn[- 1]):
        return my_method(t)
    else:
        return (1 - u3.of(alpha))*Sols_on_tn[num- 2] + u3.of(alpha)*Sols_on_tn[num - 1] + \
                h*(A31.of(alpha)*K1[num- 2] + A32.of(alpha)*K2[num - 2] + A33.of(alpha)*K3[num - 2]) +\
                h*(a31.of(alpha)*K1[num- 1] + a32.of(alpha) * K2[num- 1])


def Y1_7(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return my_method_7(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1] >= t: num += 1
    return Sols_on_tn_7[num - 1]

def Y2_7(t):
    if t < t0: return init_f(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num -1])/h
    if t <= (t0 + h) or t <= arr_tn[- 1]:
        return my_method_7(t)
    else:
        return (1 - u2_7.of(alpha))*Sols_on_tn_7[num- 2] + u2_7.of(alpha)*Sols_on_tn_7[num- 1] + \
               h*(A21_7.of(alpha)*K1_7[num - 2] + A22_7.of(alpha)*K2_7[num - 2] + A23_7.of(alpha)*K3_7[num -2]) + h*a21_7.of(alpha) * K1_7[num - 1]

def Y3_7(t):
    if t < t0: return init_f(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1]>=t: num += 1
    alpha = (t - arr_tn[num - 1]) / h
    if (t <= (t0 + h) or t <= arr_tn[- 1]):
        return my_method_7(t)
    else:
        return (1 - u3_7.of(alpha))*Sols_on_tn_7[num- 2] + u3_7.of(alpha)*Sols_on_tn_7[num - 1] + \
                h*(A31_7.of(alpha)*K1_7[num- 2] + A32_7.of(alpha)*K2_7[num - 2] + A33_7.of(alpha)*K3_7[num - 2]) +\
                h*(a31_7.of(alpha)*K1_7[num- 1] + a32_7.of(alpha) * K2_7[num- 1])



def Y1_5(t):
    if t <= t0: return init_f(t)
    if t <= arr_tn[-1]: return my_method_5(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1] >= t: num += 1
    return Sols_on_tn_5[num - 1]

def Y2_5(t):
    if t < t0: return init_f(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1] >= t: num += 1
    alpha = (t - arr_tn[num - 1]) / h
    if t <= (t0 + h) or t <= arr_tn[- 1]:
        return my_method_5(t)
    else:
        return (1 - u2_5.of(alpha)) * Sols_on_tn_5[num - 2] + u2_5.of(alpha) * Sols_on_tn_5[num - 1] + \
               h * (A21_5.of(alpha) * K1_5[num - 2] + A22_5.of(alpha) * K2_5[num - 2] + A23_5.of(alpha) * K3_5[
            num - 2]) + h * a21_5.of(alpha) * K1_5[num - 1]

def Y3_5(t):
    if t < t0: return init_f(t)
    num = math.ceil((t - t0) / h)
    if (t - t0) % h == 0 and arr_tn[-1] >= t: num += 1
    alpha = (t - arr_tn[num - 1]) / h
    if (t <= (t0 + h) or t <= arr_tn[- 1]):
        return my_method_5(t)
    else:
        return (1 - u3_5.of(alpha)) * Sols_on_tn_5[num - 2] + u3_5.of(alpha) * Sols_on_tn_5[num - 1] + \
               h * (A31_5.of(alpha) * K1_5[num - 2] + A32_5.of(alpha) * K2_5[num - 2] + A33_5.of(alpha) * K3_5[num - 2]) + \
               h * (a31_5.of(alpha) * K1_5[num - 1] + a32_5.of(alpha) * K2_5[num - 1])

# Наш метод 5-го порядка

def my_method_5(t):
    if t <= t0:
        return init_f(t)
    num = math.ceil((t - t0) / h)
    if ((t - t0) % h == 0 and len(Sols_on_tn_5) >= num + 1): return Sols_on_tn_5[num]
    alpha = (t - arr_tn[num - 1]) / h
    if t <= (t0 + h):
        return decision(t)
    else:
        return (1 - v_5.of(alpha)) * Sols_on_tn_5[num - 2] + v_5.of(alpha) * Sols_on_tn_5[num - 1] + \
                   h * (B1_5.of(alpha) * K1_5[num - 2] + B2_5.of(alpha) * K2_5[num - 2] + B3_5.of(alpha) * K3_5[num - 2]) + \
                   h * (b1_5.of(alpha) * K1_5[num - 1] + b2_5.of(alpha) * K2_5[num - 1] + b3_5.of(alpha) * K3_5[num - 1])

# Наш метод 6-го порядка

def my_method(t):
        if t <= t0:
            return init_f(t)
        num = math.ceil((t - t0) / h)
        if ((t - t0) % h == 0 and len(Sols_on_tn) >= num + 1):return Sols_on_tn[num]
        alpha = (t - arr_tn[num - 1]) / h
        if t <= (t0 + h):
            return decision(t)
        else:
            return (1 - v.of(alpha)) * Sols_on_tn[num - 2] + v.of(alpha) * Sols_on_tn[num -1] + \
                  h * (B1.of(alpha) * K1[num - 2] + B2.of(alpha) * K2[num - 2] + B3.of(alpha) * K3[num - 2]) + \
                  h * (b1.of(alpha) * K1[num - 1] + b2.of(alpha) * K2[num - 1] + b3.of(alpha) * K3[num - 1])


# Наш метод 7-го порядка
# Нерабочий

def my_method_7(t):
    if t <= t0:
        return init_f(t)
    num = math.ceil((t - t0) / h)
    if ((t - t0) % h == 0 and len(Sols_on_tn_7) >= num + 1): return Sols_on_tn_7[num]
    alpha = (t - arr_tn[num - 1]) / h
    if t <= (t0 + h):
        return decision(t)
    else:
        return (1 - v_7.of(alpha)) * Sols_on_tn_7[num - 2] + v_7.of(alpha) * Sols_on_tn_7[num - 1] + \
               h * (B1_7.of(alpha) * K1_7[num - 2] + B2_7.of(alpha) * K2_7[num - 2] + B3_7.of(alpha) * K3_7[num - 2]) + \
               h * (b1_7.of(alpha) * K1_7[num - 1] + b2_7.of(alpha) * K2_7[num - 1] + b3_7.of(alpha) * K3_7[num - 1])

# Метод РК 4-го порядка

def another_method(t):
    if t <= t0:
        return init_f(t)
    num = math.ceil((t - t0) / h)
    alpha = (t - arr_tn[num-1]) / h
    return Sols_on_tn_for_another[num-1] + h * (b11.of(alpha) * K_Begin[0][num-1] + b55.of(alpha) * K_Begin[4][num - 1] + b66.of(alpha) * K_Begin[5][num - 1])

def Tuzov_Method(t):
    if t <= t0:
        return init_f(t)
    num = math.ceil((t - t0) / h)
    if ((t - t0) % h == 0 and len(Sols_on_tn_for_Tuzov) >= num + 1): return Sols_on_tn_for_Tuzov[num]
    alpha = (t - arr_tn[num - 1]) / h
    if t<= (t0 + h):
        return decision(t)
    else: return (1 - T_v.of(alpha))*Sols_on_tn_for_Tuzov[num - 2] + T_v.of(alpha)*Sols_on_tn_for_Tuzov[num - 1] +\
                h * (T_B1.of(alpha)*T_K1[num-2] + T_B2.of(alpha)*T_K2[num-2]) +\
                h * (T_b1.of(alpha)*T_K1[num-1] + T_b2.of(alpha)*T_K2[num-1])

def make_step_5(t):
    K1_5.append(f(t, Y1_5))
    K2_5.append(f(t + c2*h, Y2_5))
    K3_5.append(f(t + c3*h, Y3_5))
    Sols_on_tn_5.append(my_method_5(t + h))

def make_step(t):
    K1.append(f(t, Y1))
    K2.append(f(t + c2*h, Y2))
    K3.append(f(t + c3*h, Y3))
    Sols_on_tn.append(my_method(t + h))

def make_step_7(t):
    K1_7.append(f(t, Y1_7))
    K2_7.append(f(t + c2_7*h, Y2_7))
    K3_7.append(f(t + c3_7*h, Y3_7))
    Sols_on_tn_7.append(my_method_7(t + h))

def make_step_for_another(t):
    K_Begin[0].append(f(t, Y11))
    K_Begin[1].append(f(t + c22*h, Y22))
    K_Begin[2].append(f(t + c33*h, Y33))
    K_Begin[3].append(f(t + c44*h, Y44))
    K_Begin[4].append(f(t + c55*h, Y55))
    K_Begin[5].append(f(t + c66*h, Y66))
    Sols_on_tn_for_another.append(another_method(t + h))

def make_step_for_Tuzov(t):
    T_K1.append(f(t, T_Y1))
    T_K2.append(f(t + h,T_Y2))
    Sols_on_tn_for_Tuzov.append(Tuzov_Method(t+h))

def make_file(my_file, arr1,arr2,arr3,arr4):
    p1 = int(np.ceil(-arr1[0]))
    p2 = int(np.ceil(-arr2[0]))
    p3 = int(np.ceil(-arr3[0]))
    p4 = int(np.ceil(-arr4[0]))
    file.write(f"\\$2^{{{-1}}}$ &\t $%4.1f*10^{{{-p1}}} $&\t --- &\t$ %4.1f*10^{{{-p2}}} $&\t --- &\t$ %4.1f*10^{{{-p3}}} $&\t --- &\t $%4.1f*10^{{{-p4}}}$ &\t --- \\\\ \n"% ( 10 ** (arr1[0] + p1), 10 ** (arr2[0] + p2), 10 ** (arr3[0] + p3), 10 ** (arr4[0]) + p4))
    for i in range(1, len(arr1)):
        p1 = int(np.ceil(-arr1[i]))
        p2 = int(np.ceil(-arr2[i]))
        p3 = int(np.ceil(-arr3[i]))
        p4 = int(np.ceil(-arr4[i]))
        file.write(f"$2^{{{-i-1}}}$ &\t$ %4.1f*10^{{{-p1}}} $& \t %4.1f&\t $%4.1f*10^{{{-p2}}}$& \t %4.1f&\t  $%4.1f*10^{{{-p3}}}$ & \t %4.1f&\t $%4.1f*10^{{{-p4}}}$& \t %4.1f  \\\\ \n" %( 10**(arr1[i] + p1) , np.log2((10**arr1[i-1])/(10**arr1[i])), 10**(arr2[i]+ p2) , np.log2((10**arr2[i-1])/(10**arr2[i])), 10**(arr3[i] + p3) , np.log2((10**arr3[i-1])/(10**arr3[i])), 10**(arr4[i] + p4) , np.log2((10**arr4[i-1])/(10**arr4[i]))))
    file.write("\n\n")

global_error_Tuzov = []
global_error_another = []
global_error_my =[]
global_error_my_5 = []
# global_error_my_7 =[]

file = open("tab.txt", 'w')

h_arr = []
for i in range(1,8):

    h = (1/2)**i
    if h == 1/4:
        print("")
    h_arr.append(math.log10(h))
    K1 = []
    K2 = []
    K3 = []

    K1_7 = []
    K2_7 = []
    K3_7 = []

    K1_5 = []
    K2_5 = []
    K3_5 = []

    T_K1 = []
    T_K2 = []

    K_Begin = [[], [], [], [], [], []]

    Sols_on_tn_5 = [init_f(t0)]
    Sols_on_tn = [init_f(t0)]
    # Sols_on_tn_7 = [init_f(t0)]
    Sols_on_tn_for_another = [init_f(t0)]
    Sols_on_tn_for_Tuzov = [init_f(t0)]
    Sols_on_tn_for_decision = [init_f(t0)]

    arr_tn = [t0]
    K_Begin[0].append(f(t0, Y11))
    K_Begin[1].append(f(t0 + c22*h, Y22))
    K_Begin[2].append(f(t0 + c33*h, Y33))
    K_Begin[3].append(f(t0 + c44*h, Y44))
    K_Begin[4].append(f(t0 + c55*h, Y55))
    K_Begin[5].append(f(t0 + c66*h, Y66))
    Sols_on_tn_for_another.append(another_method(t0 + h))

    K1_5.append(f(t0, decision))
    K2_5.append(f(t0 + c2*h, decision))
    K3_5.append(f(t0 + c3*h, decision))
    Sols_on_tn_5.append(my_method_5(t0 + h))

    K1.append(f(t0, decision))
    K2.append(f(t0 + c2*h, decision))
    K3.append(f(t0 + c3*h, decision))
    Sols_on_tn.append(my_method(t0 + h))

    # K1_7.append(f(t0, decision))
    # K2_7.append(f(t0 + c2_7 * h, decision))
    # K3_7.append(f(t0 + c3_7 * h, decision))
    # Sols_on_tn_7.append(my_method_7(t0 + h))

    T_K1.append(f(t0, decision))
    T_K2.append(f(t0 + h, decision))
    Sols_on_tn_for_Tuzov.append(Tuzov_Method(t0 + h))
    arr_tn.append(t0 + h)
    var = t0 + h

    while(var < tn):
        Sols_on_tn_for_decision.append(decision(var))
        make_step_5(var)
        make_step_for_another(var)
        make_step(var)
        # make_step_7(var)
        make_step_for_Tuzov(var)
        arr_tn.append(var + h)
        var+=h

    Sols_on_tn_for_decision.append(decision(var))
    global_error_another.append(np.log10(abs(decision(tn) - another_method(tn))))
    global_error_Tuzov.append(np.log10(abs(decision(tn) - Tuzov_Method(tn))))
    global_error_my.append(np.log10(abs(decision(tn) - my_method(tn))))
    global_error_my_5.append(np.log10(abs(decision(tn) - my_method_5(tn))))
    # global_error_my_7.append(np.log10(abs(decision(tn) - my_method_7(tn))))

mn=np.linspace(t0, tn, 10000)
result_Tuzov = [Tuzov_Method(i) for i in mn]
result_another = [another_method(i) for i in mn]
result_my = [my_method(i) for i in mn]
result_my_5 = [my_method_5(i) for i in mn]
# result_my_7 = [my_method_7(i) for i in mn]

plt.plot(mn, [another_method(i) for i in mn], mn, [my_method(i)for i in mn])

make_file(file, global_error_another, global_error_Tuzov, global_error_my_5, global_error_my)


file.close()
plt.subplot(211)
plt.plot(mn, result_my_5, label='My_5')
plt.plot(mn, result_my, label='My')
plt.plot(mn, result_another, label='Runge-Kutta')
plt.plot(mn, result_Tuzov,label='Tuzov')
# plt.plot(mn, result_my_7, label='My_7')
plt.plot(mn, [decision(i) for i in mn], label ='True-decision')
plt.legend()

plt.subplot(212)
plt.plot(h_arr, global_error_my_5, label = '2-step RK 5')
plt.plot(h_arr, global_error_my, label = '2-step RK 6' )
plt.plot(h_arr, global_error_another, label = 'Runge_Kutta 4')
plt.plot(h_arr, global_error_Tuzov, label = 'Tuzov 4 ')
plt.grid()
# plt.plot(h_arr, global_error_my_7, label = '2-step RK 7' )

plt.legend()
plt.xlabel("log10(h)")
plt.ylabel("log10(g_error)")
plt.show()
