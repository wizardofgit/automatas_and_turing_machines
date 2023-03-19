class TuringMachine:
    def czy_wejscie_zgodne(self, wejscie, *args):
        if args[0] is not None:
            for i in args:
                if i[0] == 'posrodku':
                    if wejscie[0] == i[1] or wejscie[-1] == i[1]:
                        raise ValueError('Wejście niezgodne z alfabetem!')

        for i in wejscie:
            if i not in self.alfabet:
                raise ValueError('Wejście niezgodne z alfabetem')

        return wejscie

    def __init__(self,stany, alfabet, stan_poczatkowy, stany_akceptacji, stany_odrzucenia, funkcja_przejsc):
        self.stany = stany.split(',')
        self.alfabet = alfabet.split(',')
        self.stan_poczatkowy = stan_poczatkowy
        self.stany_akceptacji = stany_akceptacji.split(',')
        self.stany_odrzucenia = stany_odrzucenia.split(',')
        self.funkcja_przejsc = funkcja_przejsc  # jestem_w_stanie: [(wyczytam_z_taśmy, zapiszę_na_taśmę, przejdę {L;R}, nowy_stan),..]
        self.pozycja = 0
        self.obecny_stan = stan_poczatkowy

    def uruchom(self, wejscie, dodatkowe=None):
        self.tasma = self.czy_wejscie_zgodne(wejscie.split(','), dodatkowe)
        self.tasma.append('_')
        self.halt = False

        while(not self.halt):
            print(f'Taśma: {self.tasma}, pozycja: {self.pozycja}, stan: {self.obecny_stan}')

            if self.obecny_stan in self.stany_akceptacji:
                self.halt = True
                print('Akceptacja')
                break
            elif self.obecny_stan in self.stany_odrzucenia:
                self.halt = True
                print('Odrzucenie')
                break

            x = self.tasma[self.pozycja]  # obecny symbol z taśmy

            for i in self.funkcja_przejsc[self.obecny_stan]:
                if i[0] == x:
                    if i[1] != '':
                        self.tasma[self.pozycja] = i[1]

                    if i[2] == 'R':
                        self.pozycja += 1
                    else:
                        if self.pozycja - 1 < 0:
                            self.pozycja = 0
                        else:
                            self.pozycja -= 1

                    self.obecny_stan = i[3]
                    break