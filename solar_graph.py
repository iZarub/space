import matplotlib.pyplot as plt
import numpy as np

from solar_model import gravitational_constant


class Graph:
    def __init__(self):
        self.t = []

        self.planet_vx = []
        self.planet_vy = []
        self.planet_x = []
        self.planet_y = []
        self.planet_v = []

        self.star_x = []
        self.star_y = []
        self.star_vx = []
        self.star_vy = []
        self.star_v = []

        self.r = []
        self.f = False

    def gain_data(self, objs, time):
        for obj in objs:
            if obj.type == 'Planet':

                self.planet_x.append(obj.x)
                self.planet_y.append(obj.y)
                self.planet_vx.append(obj.Vx)
                self.planet_vy.append(obj.Vy)
                self.t.append(time)
                self.f = True

            if obj.type == 'Star':
                self.star_x.append(obj.x)
                self.star_y.append(obj.y)
                self.star_vx.append(obj.Vx)
                self.star_vy.append(obj.Vy)
                self.f = True

        if self.f:
            self.write_data()

    def write_data(self):
        self.planet_v.append((self.planet_vx[-1]**2 + self.planet_vy[-1]**2)**0.5)
        self.r.append(((self.planet_x[-1] - self.star_x[-1])**2 + (self.planet_y[-1] - self.star_y[-1])**2)**0.5)
        self.star_v.append((self.star_vx[-1] ** 2 + self.star_vy[-1] ** 2) ** 0.5)

    def show_plot(self):
        plt.figure(figsize=(8, 6))

        self.t = np.array(self.t)
        self.planet_v = np.array(self.planet_v)
        self.r = np.array(self.r)
        self.star_v = np.array(self.star_v)

        sp = plt.subplot(311)
        plt.plot(self.t, self.planet_v, 'g', label='Скорость от времени')
        plt.legend(loc='best', fontsize=8)
        plt.grid()
        plt.xlabel('$t$, с')
        plt.ylabel('$V$, м/с')

        sp = plt.subplot(312)
        plt.plot(self.t, self.r, 'r', label='Расстояние до звезды от времени')
        plt.legend(loc='best', fontsize=8)
        plt.grid()
        plt.xlabel('$t$, с')
        plt.ylabel(r'$\rho$, м')

        sp = plt.subplot(313)
        plt.plot(self.r, self.planet_v, label='Скорость планеты от расстояния до звезды')
        plt.legend(loc='best', fontsize=8)
        plt.grid()
        plt.xlabel(r'$\rho$, м')
        plt.ylabel('$V$, м/с')

        plt.show()


if __name__ == '__main__':
    print('This module is not for direct run!')