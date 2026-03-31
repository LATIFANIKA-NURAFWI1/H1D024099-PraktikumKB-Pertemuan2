import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kipas = ctrl.Consequent(np.arange(0, 101, 1), 'kipas')

suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['panas']  = fuzz.trimf(suhu.universe, [30, 40, 40])

kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['sedang'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['lembap'] = fuzz.trimf(kelembapan.universe, [60, 100, 100])

kipas['lambat'] = fuzz.trimf(kipas.universe, [0, 0, 50])
kipas['sedang'] = fuzz.trimf(kipas.universe, [30, 50, 70])
kipas['cepat']  = fuzz.trimf(kipas.universe, [60, 100, 100])

rule1 = ctrl.Rule(suhu['dingin'], kipas['lambat'])
rule2 = ctrl.Rule(suhu['normal'] | kelembapan['sedang'], kipas['sedang'])
rule3 = ctrl.Rule(suhu['panas'] | kelembapan['lembap'], kipas['cepat'])

sistem_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
sistem = ctrl.ControlSystemSimulation(sistem_ctrl)

suhu_input = int(input("Masukkan suhu (0-40): "))
kelembapan_input = int(input("Masukkan kelembapan (0-100): "))

sistem.input['suhu'] = suhu_input
sistem.input['kelembapan'] = kelembapan_input

sistem.compute()
print("\nKecepatan kipas:", sistem.output['kipas'])

kipas.view(sim=sistem)
plt.show()