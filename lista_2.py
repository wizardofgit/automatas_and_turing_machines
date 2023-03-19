from automat import Automat
import pickle

# zad 1
delta1 = {'q0': [('0', 'q1'), ('1', 'q0')],
         'q1': [('0', 'q3'), ('1', 'q2')],
         'q2': [('0', 'q2'), ('1', 'q0')],
         'q3': [('0', 'q2'), ('1', 'q2')]
         }
automat_1 = Automat(alfabet='0,1', stany='q0,q1,q2,q3', stany_akceptacji='q3', funkcja_przejsc=delta1, stan_poczatkowy='q0')
automat_1.uruchom_automat(wejscie='00')

# zad 2
delta2 = {'q0': [('a', 'q2'),('b', 'q2'),('c', 'q2')],
          'q1': [('a', 'q4'), ('b', 'q0'), ('c', 'q3')],
          'q2': [('a', 'q1'), ('b', 'q1'), ('c', 'q6')],
          'q3': [('a', 'q3'), ('b', 'q3'), ('c', 'q3')],
          'q4': [('a', 'q0'), ('b', 'q5'), ('c', 'q5')],
          'q5': [('a', 'q4'), ('b', 'q4'), ('c', 'q4')],
          'q6': [('a', 'q3'), ('b', 'q3'), ('c', 'q3')]
          }
automat_2 = Automat(alfabet='a,b,c', stany='q0,q1,q2,q3,q4,q5,q6', stany_akceptacji='q3,q5', funkcja_przejsc=delta2, stan_poczatkowy='q0')
automat_2.uruchom_automat('abacaa', draw=True)

# zad 3
delta3 = {'q0': [('0', 'q1'), ('1', 'q0'), ('a', 'q3')],
         'q1': [('0', 'q0'), ('1', 'q2'), ('a', 'q0')],
         'q2': [('0', 'q2'), ('1', 'q0'), ('a', 'q1')],
         'q3': [('0', 'q1'), ('1', 'q2'), ('a', 'q0')]
         }
automat_3 = Automat(alfabet='0,1,a', stany='q0,q1,q2,q3', stany_akceptacji='q2,q3', funkcja_przejsc=delta3, stan_poczatkowy='q0')
automat_3.uruchom_automat(wejscie='a0010a')

# zad 4
delta4 = {'q0': [('a', 'q0'), ('b', 'q1'), ('c', 'q2'), ('d', 'q3')],
         'q1': [('a', 'q1'), ('b', 'q0'), ('c', 'q1'), ('d', 'q0')],
         'q2': [('a', 'q0'), ('b', 'q2'), ('c', 'q0'), ('d', 'q1')],
         'q3': [('a', 'q3'), ('b', 'q1'), ('c', 'q0'), ('d', 'q2')]
         }
automat_4 = Automat(alfabet='a,b,c,d', stany='q0,q1,q2,q3', stany_akceptacji='q2,q3', funkcja_przejsc=delta4, stan_poczatkowy='q0')
automat_4.uruchom_automat(wejscie='aaabcddd')

# q = {
#   "alfabet": "a,b,c, d",
#   "stany": "q0,q1,q2, q3",
#   "stany_akceptacji": "q2,q3",
#   "stan_poczatkowy": "q0",
#   "funkcja_przejsc": {'q0': [('a', 'q0'), ('b', 'q1'), ('c', 'q2'), ('d', 'q3')],
#          'q1': [('a', 'q1'), ('b', 'q0'), ('c', 'q1'), ('d', 'q0')],
#          'q2': [('a', 'q0'), ('b', 'q2'), ('c', 'q0'), ('d', 'q1')],
#          'q3': [('a', 'q3'), ('b', 'q1'), ('c', 'q0'), ('d', 'q2')]
#          }
# }
#
# pickle.dump(q, open('automat.pkl', 'wb'))

# zad 5
plik = pickle.load(open('automat.pkl', 'rb'))
automat_4 = Automat(plik['alfabet'], plik['stany'], plik['stany_akceptacji'], plik['funkcja_przejsc'], plik['stan_poczatkowy'])
automat_4.uruchom_automat(wejscie='aaabcddd')