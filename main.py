

import control as ct
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['figure.figsize'] = (16,10)
plt.rcParams['figure.dpi'] = 350
plt.rcParams['xtick.major.size'] = 16
plt.rcParams['ytick.major.size'] = 16
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16


m1 = 250
m2 = 50
b = 60.6
k1 = 30
k2 = 15

sys = ct.tf([k2*b,k1*k2],[m1*m2,(m1+m2)*b,(k2*m2 + (m1+m2)*k1),k2*b,k1*k2])


response = ct.step_response(sys)
plt.plot(response.time, response.outputs)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.savefig("step response")



omega = sys.damp()[0]



zeta = sys.damp()[1]



Poles = sys.damp()[2]


ct.step_info(sys)


ct.pzmap(sys)
plt.savefig('pole-zero')

