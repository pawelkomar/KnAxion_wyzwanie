import numpy as m
def X (stan):
    m_X = m.array([
        [0, 1], 
        [1, 0]
    ])
    return m_X @ stan
def R_Y (stan, theta):
    m_R_Y = m.array([
        [m.cos(theta/2), -m.sin(theta/2)], 
        [m.sin(theta/2), m.cos(theta/2)]
    ])
    return m_R_Y @ stan
def Z (stan):
    m_Z = m.array([
        [1, 0], 
        [0, -1]
    ])
    return m_Z @ stan
def H (stan):
    m_H = (1/m.sqrt(2)) * m.array([
        [1, 1],
        [1, -1]
    ])
    return m_H @ stan
def CNOT (stan):
    m_CNOT = m.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])
    return m_CNOT @ stan
def pomiar (stan):
    p_0 = (m.abs(stan[0]))**2
    p_1 = (m.abs(stan[1]))**2
    return m.random.choice([0, 1], p=[p_0, p_1])

stan_0 = m.array([1.0, 0.0], dtype = complex)
stan_1 = m.array([0.0, 1.0], dtype = complex)
stan_plus = m.array(H(stan_0), dtype = complex)
stan_minus = m.array(H(X(stan_0)), dtype = complex)
stan_i = m.array([1/m.sqrt(2), (1/m.sqrt(2))*1j], dtype = complex)
stan_minus_i = m.array([1/m.sqrt(2), -(1/m.sqrt(2))*1j], dtype = complex)
print(H(stan_0))
print(pomiar(H(stan_0)))
print(H(H(stan_0)))



# Jeśli chodzi o to co doczytałem to pobawiłem się bardziej sferą blocha, bo na
# wykładzie było jej dosyć mało :C. Oprócz tego poświęciłem trochę czasu na 
# przetrawienie konwersji z notacji diraca na sferę Blocha 