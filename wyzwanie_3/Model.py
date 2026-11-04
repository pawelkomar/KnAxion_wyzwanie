import numpy as m
def R_Y (stan, theta):
    m_R_Y = m.array([
        [m.cos(theta/2), -m.sin(theta/2)], 
        [m.sin(theta/2), m.cos(theta/2)]
    ])
    return m_R_Y @ stan

def koszt(stan):
    return stan[0]**2

stan_0 = m.array([1.0, 0.0])
ułamek = m.random.uniform(0, 2 * m.pi, 20)
roznice = []
roznice_bez_sin = []
for theta in m.linspace(0, 2 * m.pi, 100):
    # print("theta = " + str(theta))
    for i in range(20):
        wprzod = theta + ułamek[i]
        wtyl = theta - ułamek[i]
        wprzod_std = theta + (m.pi / 2)
        wtyl_std = theta - (m.pi / 2)
        a = R_Y(stan_0, wprzod) 
        b = R_Y(stan_0, wtyl)
        c = R_Y(stan_0, wprzod_std)
        d = R_Y(stan_0, wtyl_std)
        parameter_shift = (koszt(c)-koszt(d))/2
        parameter_shift_testowy = (koszt(a)-koszt(b))/(2*m.sin(ułamek[i]))
        parameter_shift_testowy_bez_sinusa = (koszt(a)-koszt(b))/2
        # print("ułamek = " + str(ułamek[i]) + " parameter_shift = " + str(parameter_shift) + " parameter_shift_testowy = " + str(parameter_shift_testowy))
        roznica = abs(parameter_shift - parameter_shift_testowy)
        roznice.append(roznica)
        roznica_bez_sin = abs(parameter_shift - parameter_shift_testowy_bez_sinusa)
        roznice_bez_sin.append(roznica_bez_sin)

for i in range(len(roznice)):
    if(roznice[i]>0.0000000000001):
        print (str(roznice[i]))
# pętla powyżej nie wypisuj nic - *dosyć duże zdziwienie* - bardzo mała różnica między parameter_shift_testowy i parameter_shift
print("oddzielenie")

licz = 0
for i in range(len(roznice_bez_sin)):
    if(roznice_bez_sin[i]>0.00001):
        licz += 1
        print (str(roznice_bez_sin[i]))
print(str(licz))
# różnica parameter_shift i parameter_shift_testowy_bez_sinusa jest większa od 0.00001 aż w +-1960 przypadkach na 2000 