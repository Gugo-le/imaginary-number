import matplotlib.pyplot as plt
from numpy import *    # 지칭 없이 numpy 메소드 사용가능
 
r = 1
Z = [r*exp(1j*x*pi)*(1.6**x) for x in linspace(0,6,200)]
plt.plot(real(Z), imag(Z))   # numpy에서 real과 imag 메소드 사용
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.axis([-20,20,-20,20])
plt.axhline(y=0,color='black')
plt.axvline(x=0, color='black')
plt.show()