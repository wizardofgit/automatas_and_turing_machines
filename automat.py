import networkx as ntx
import networkx as nx
from matplotlib import pyplot as plt

class Automat:
    def zgodny_z_alfabetem(self, wejscie):
        for i in wejscie:
            if i not in self.alfabet:
                return False

        return True

    def podaj_wejscie(self, wejscie):
        x = []
        for i in wejscie:
            x.append(i)

        return x

    def podaj_alfabet(self, alfabet):
        x = []

        for i in alfabet:
            x.append(i)

        return x

    def podaj_stany(self, stany):
        x = []
        s = stany.split(',')

        for i in s:
            x.append(i)

        return x

    def __init__(self, alfabet, stany, stany_akceptacji, funkcja_przejsc, stan_poczatkowy):
        self.alfabet = self.podaj_alfabet(alfabet)
        self.stan_poczatkowy = stan_poczatkowy
        self.stany = self.podaj_stany(stany)
        self.stany_akceptacji = self.podaj_stany(stany_akceptacji)
        self.funkcja_przejsc = funkcja_przejsc
        self.obecny_stan = stan_poczatkowy
        self.historia_stanow = [stan_poczatkowy]

    def uruchom_automat(self, wejscie, draw=False):
        self.historia_stanow = [self.stan_poczatkowy]
        w = self.podaj_wejscie(wejscie)
        if self.zgodny_z_alfabetem(w) is not True:
            raise ValueError('Wejście nie jest zgodne z alfabetem!')

        counter = 0
        if draw:
            G = ntx.MultiDiGraph()
            for i in self.stany:
                G.add_node(i)

        for i in w:
            for x in self.funkcja_przejsc[self.obecny_stan]:
                if x[0] == i:
                    previous = self.obecny_stan
                    self.obecny_stan = x[1]
                    self.historia_stanow.append(self.obecny_stan)

                    if draw:
                        G.add_edge(previous, self.obecny_stan, weight=counter)
                        counter += 1
                    break

            if draw:
                pos = ntx.shell_layout(G)
                ntx.draw(G, pos, with_labels=True, connectionstyle='Arc3, rad=0.1')
                ntx.draw_networkx_edge_labels(G, pos)
                plt.show()


        if self.obecny_stan in self.stany_akceptacji:
            print('Akceptacja')
        else:
            print('Odrzucenie')
        print(self.historia_stanow)
