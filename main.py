import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/DevNi/PycharmProjects/projetoPai/DPS_1.6mm_350C_175Csec_modified.csv'
data = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))


plt.plot(data.index, data['Force'], label='Force (kN)', color='blue', linewidth=2)
plt.plot(data.index, data['Heat'], label='Heat', color='red', linewidth=2)
plt.plot(data.index, data['Stress'], label='Stress (MPa)', color='green', linewidth=2)
plt.plot(data.index, data['TC1'], label='TC1 (C)', color='orange', linestyle='--')
plt.plot(data.index, data['TC1.setpoint'], label='TC1.setpoint (C)', color='purple', linestyle='--')


plt.title('Gráfico de Force, Heat, Stress, e TC1')
plt.xlabel('Índice (tempo aproximado)')
plt.ylabel('Valores')

plt.legend()

plt.grid(True)
plt.show()
