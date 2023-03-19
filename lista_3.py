import pickle
from maszyna_turinga import TuringMachine

#zad 1
delta_1 = {
    'q0': [('_', '', 'L', 'qr'), ('a', 'b', 'R', 'q1')],
    'q1': [('c', '', 'R', 'q1'), ('_', '', 'L', 'qa'), ('a', '', 'L', 'q2')],
    'q2': [('c', '', 'L', 'q2'), ('b', '', 'L', 'q3')],
    'q3': [('c', '','R','q3'),('b', '', 'R', 'q4'),('a', '', 'R', 'q4'),('_', '', 'L', 'q6')],
    'q4': [('c', '', 'R', 'q4'),('_', '', 'L', 'qr'),('a', 'c', 'R', 'q5')],
    'q5': [('c', '', 'R', 'q5'), ('_', '', 'L', 'qr'), ('a', 'c', 'R', 'q3')],
    'q6': [('a', '', 'L', 'q6'), ('c', '', 'L', 'q6'), ('b','', 'R', 'q1')]
}   # jestem_w_stanie: [(wyczytam, zapiszę, przejdę {L;R}, nowy_stan),..]
    # a - a, b - a z kropeczką, c - a przekreślone; _ - symbol pusty
maszyna_1 = TuringMachine(alfabet='a,b,c', stany='q0,q1,q2,q3,q4,q5,q6,qa,qr', stan_poczatkowy='q0', stany_akceptacji='qa', stany_odrzucenia='qr', funkcja_przejsc=delta_1)
maszyna_1.uruchom('a,a,a')

delta_2 = {
    'q0': [('b', '', 'R', 'q1'), ('0', 'x', 'R', 'q2'), ('1', 'y', 'R', 'q3')],
    'q1': [('x', '', 'R', 'q1'), ('y', '', 'R', 'q1'), ('_', '', 'L', 'qa'), ('0', '', 'L', 'qr'), ('1', '', 'L', 'qr')],
    'q2': [('_', '', 'R', 'qr'), ('0', '', 'R', 'q2'), ('1', '', 'R', 'q2'), ('b', '', 'R', 'q4')],
    'q3': [('_', '', 'R', 'qr'), ('0', '', 'R', 'q3'), ('1', '', 'R', 'q3'), ('b', '', 'R', 'q5')],
    'q4': [('x', '', 'R', 'q2'), ('y', '', 'R', 'q2'), ('_', '', 'R', 'qr'), ('1', '', 'R', 'qr'), ('0', 'x', 'L', 'q6')],
    'q5': [('x', '', 'R', 'q5'), ('y', '', 'R', 'q5'), ('_', '', 'R', 'qr'), ('0', '', 'R', 'qr'), ('1', 'y', 'L', 'q6')],
    'q6': [('x', '', 'L', 'q6'), ('y', '', 'L', 'q6'), ('b', '', 'L', 'q7')],
    'q7': [('x', '', 'R', 'q0'), ('y', '', 'R', 'q0'), ('0', '', 'L', 'q7'), ('1', '', 'L', 'q7')]
}   #x - przekreślone 0, y - przekreślone 1
maszyna_2 = TuringMachine(alfabet='0,1,b', stany='q0,q1,q2,q3,q4,q5,q6,q7,qa,qr', stan_poczatkowy='q0', stany_akceptacji='qa' ,stany_odrzucenia='qr', funkcja_przejsc=delta_2)
maszyna_2.uruchom('0,1,1,0')

#zad 3
delta_3 = {
    'q0': [('a', 'b', 'R', 'q1'), ('b', '', 'L', 'q0'), ('x', '', 'R', 'qr')],
    'q1': [('a', '', 'R', 'q2'), ('b', '', 'L', 'q1'), ('x', '', 'R', 'qr')],
    'q2': [('a', '', 'R', 'qa'), ('b', '', 'R', 'qa'), ('x', '', 'L', 'q1')]
}
maszyna_3 = TuringMachine(alfabet='a,x,b', stany='q0,q1,q2', stany_akceptacji='qa', stany_odrzucenia='qr', stan_poczatkowy='q0', funkcja_przejsc=delta_3)
maszyna_3.uruchom(wejscie='a,x,b,b',dodatkowe=('posrodku', 'x'))

#zad 5
# q = {
#   "alfabet": "0,1,b",
#   "stany": "q0,q1,q2,q3,q4,q5,q6,q7,qa,qr",
#   "stany_akceptacji": "qa",
#   "stan_poczatkowy": "q0",
#   "stany_odrzucenia": "qr",
#   "funkcja_przejsc": {
#     'q0': [('b', '', 'R', 'q1'), ('0', 'x', 'R', 'q2'), ('1', 'y', 'R', 'q3')],
#     'q1': [('x', '', 'R', 'q1'), ('y', '', 'R', 'q1'), ('_', '', 'L', 'qa'), ('0', '', 'L', 'qr'), ('1', '', 'L', 'qr')],
#     'q2': [('_', '', 'R', 'qr'), ('0', '', 'R', 'q2'), ('1', '', 'R', 'q2'), ('b', '', 'R', 'q4')],
#     'q3': [('_', '', 'R', 'qr'), ('0', '', 'R', 'q3'), ('1', '', 'R', 'q3'), ('b', '', 'R', 'q5')],
#     'q4': [('x', '', 'R', 'q2'), ('y', '', 'R', 'q2'), ('_', '', 'R', 'qr'), ('1', '', 'R', 'qr'), ('0', 'x', 'L', 'q6')],
#     'q5': [('x', '', 'R', 'q5'), ('y', '', 'R', 'q5'), ('_', '', 'R', 'qr'), ('0', '', 'R', 'qr'), ('1', 'y', 'L', 'q6')],
#     'q6': [('x', '', 'L', 'q6'), ('y', '', 'L', 'q6'), ('b', '', 'L', 'q7')],
#     'q7': [('x', '', 'R', 'q0'), ('y', '', 'R', 'q0'), ('0', '', 'L', 'q7'), ('1', '', 'L', 'q7')]}
# }
# pickle.dump(q, open('TM.pkl', 'wb'))

plik = pickle.load(open('TM.pkl', 'rb'))
maszyna_5 = TuringMachine(plik['stany'], plik['alfabet'], plik['stan_poczatkowy'], plik['stany_akceptacji'], plik['stany_odrzucenia'], plik['funkcja_przejsc'])
maszyna_5.uruchom('0,1,1,0')