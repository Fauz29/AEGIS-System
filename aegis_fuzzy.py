import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Definisi Variabel Input & Output
# Input: Sisa Kuota per 10 hari (0 - 33.3 kWh)
sisa_kuota = ctrl.Antecedent(np.arange(0, 34, 0.1), 'sisa_kuota')
# Input: Waktu dalam siklus (Hari 1 - 10)
waktu = ctrl.Antecedent(np.arange(1, 11, 1), 'waktu')
# Output: Status Sistem (0: Kritis, 1: Waspada, 2: Normal)
status_aegis = ctrl.Consequent(np.arange(0, 3, 1), 'status_aegis')

# 2. Membership Function (Himpunan Fuzzy)
sisa_kuota['sedikit'] = fuzzy.trimf(sisa_kuota.universe, [0, 0, 12])
sisa_kuota['sedang'] = fuzzy.trimf(sisa_kuota.universe, [8, 16, 25])
sisa_kuota['banyak'] = fuzzy.trimf(sisa_kuota.universe, [20, 33.3, 33.3])

waktu['awal'] = fuzzy.trimf(waktu.universe, [1, 1, 4])
waktu['tengah'] = fuzzy.trimf(waktu.universe, [3, 5, 8])
waktu['akhir'] = fuzzy.trimf(waktu.universe, [7, 10, 10])

# Label Output Baru: Kritis, Waspada, Normal
status_aegis['kritis'] = fuzzy.trimf(status_aegis.universe, [0, 0, 1])
status_aegis['waspada'] = fuzzy.trimf(status_aegis.universe, [0, 1, 2])
status_aegis['normal'] = fuzzy.trimf(status_aegis.universe, [1, 2, 2])

# 3. Rule Base (Update Sesuai Diskusi)
rule1 = ctrl.Rule(sisa_kuota['sedikit'] & waktu['awal'], status_aegis['kritis'])
rule2 = ctrl.Rule(sisa_kuota['sedikit'] & waktu['tengah'], status_aegis['kritis'])
rule3 = ctrl.Rule(sisa_kuota['sedikit'] & waktu['akhir'], status_aegis['waspada'])
rule4 = ctrl.Rule(sisa_kuota['sedang'] & waktu['awal'], status_aegis['kritis'])
rule5 = ctrl.Rule(sisa_kuota['sedang'] & waktu['tengah'], status_aegis['waspada'])
rule6 = ctrl.Rule(sisa_kuota['sedang'] & waktu['akhir'], status_aegis['normal'])
rule7 = ctrl.Rule(sisa_kuota['banyak'] & waktu['awal'], status_aegis['waspada'])
rule8 = ctrl.Rule(sisa_kuota['banyak'] & waktu['tengah'], status_aegis['normal'])
rule9 = ctrl.Rule(sisa_kuota['banyak'] & waktu['akhir'], status_aegis['normal'])

# 4. Control System
aegis_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
simulasi = ctrl.ControlSystemSimulation(aegis_ctrl)

# 5. TEST RUN (Contoh Kasus: Hari ke-1, Kuota Sedang)
simulasi.input['sisa_kuota'] = 15.0 
simulasi.input['waktu'] = 1        

simulasi.compute()

# Output Display
hasil = simulasi.output['status_aegis']
print(f"Hasil Perhitungan (Defuzzifikasi): {hasil:.2f}")

if hasil < 0.8:
    print("STATUS AEGIS: >>> KRITIS <<< (Relay Putus, Hanya Kulkas Nyala)")
elif hasil < 1.5:
    print("STATUS AEGIS: >>> WASPADA <<< (Kirim Notifikasi ke Smartphone)")
else:
    print("STATUS AEGIS: >>> NORMAL <<< (Semua Ruangan Nyala)")

# Visualisasi Grafik
sisa_kuota.view()
waktu.view()
status_aegis.view(sim=simulasi)
plt.show()