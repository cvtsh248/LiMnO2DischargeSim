import math
import matplotlib.pyplot as plt


Li = 0.1
MnO_2 = 0.45
MnOOLi = 0

#CONSTANTS
R = 8.314
F = 96500

#MOLAR MASSES
mrLi = 6.941
mrMnO_2 = 86.937
mrMnOOLi = 93.879

class ButtonCell:
    def __init__(self, mo, l, m, temperature, nominal_v, load, t, cu):
        self.alive = True
        self.T = temperature
        self.n = 1
        self.ecell = nominal_v
        self.real_v = 3.0
        self.MnOOLi = mo
        self.Li = l
        self.MnO_2 = m
        self.Li_L = []
        self.MnO_2_L = []
        self.MnOOLi_L = []
        self.V_L = []
        self.resistance = load
        self.q = self.MnOOLi/(self.MnO_2+self.Li) #reaction quotient
        self.i = nominal_v/load
        self.delta_t = t
        self.current_time = 0
        self.cutoff = cu
        self.end = False

    def timeStep(self):
        mole_Li = self.Li/mrLi
        mole_MnO_2 = self.MnO_2/mrMnO_2
        mole_MnOOLi = self.MnOOLi/mrMnOOLi

        charge = self.i*self.delta_t
        mole_electron = charge/F

        mole_Li -= mole_electron
        mole_MnO_2 -= mole_electron
        mole_MnOOLi += mole_electron

        self.Li = mole_Li*mrLi
        self.MnO_2 = mole_MnO_2*mrMnO_2
        self.MnOOLi = mole_MnOOLi*mrMnOOLi

        self.q = self.MnOOLi/(self.MnO_2+self.Li)
        if self.q > 0:
            self.real_v = self.ecell - ((R*self.T)/(self.n*F))*math.log(self.q)
        elif self.q < 0:
            self.end = True

        print(self.q)
        self.V_L.append(self.real_v)

        self.current_time+=1
    def main(self):
        while self.end == False:
            print(self.end)
            self.timeStep()



B = ButtonCell(MnOOLi,Li,MnO_2,298,3.0,300,60,2)
B.main()

plt.plot(B.V_L)

plt.show()