import pandas as pd
import numpy as np
df = pd.read_csv("data.txt", sep ="\t")
volume_block = 10*10*10 #m3
density = 2.7 #ton/m3
ton = volume_block * density
df['ton'] = ton
total_ton = df['ton'].sum()
cut_off_grade = np.arange(0, 1.05, 0.05)
tonnage = []
Average_grade = []
for ley_corte in cut_off_grade:
    df_sel = df[df["ley"] >= ley_corte]
    total_ton_corte = df_sel["ton"].sum()
    average_grade = ((df_sel["ley"] * df_sel["ton"]).sum() / total_ton_corte)
    tonnage.append(total_ton_corte)
    Average_grade.append(average_grade) 

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(figsize=(10, 5))

#Eje vertical
ax1.set_xlabel('Ley de Corte (%)')
ax1.set_ylabel('Total Tonelaje (ton)', color = 'tab:red')
ax1.plot(cut_off_grade, tonnage, color = 'tab:red', label = 'Total ton', linewidth = 2)
ax1.tick_params(axis = 'y', labelcolor = 'tab:red')

#segundo eje vertical
ax2 = ax1.twinx()
ax2.set_ylabel('Ley Media(%)', color = 'tab:blue')
ax2.plot(cut_off_grade, Average_grade, color = 'tab:blue', label = 'Average grade', linestyle = '--')
ax2.tick_params(axis = 'y', labelcolor = 'tab:blue')

plt.title('Curva Tonalaje Ley')
fig.tight_layout()
plt.show()

df_nuevo = pd.DataFrame({"Cut_off_grade": cut_off_grade, "Tonnage": tonnage, "Average_grade": Average_grade})
print(df_nuevo)