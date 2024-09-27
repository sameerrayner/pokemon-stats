import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager as fm

prop = fm.FontProperties(fname = r"C:\Users\Sameer\OneDrive\Documents\Pokemon Classic.ttf")

df = pd.read_excel('pkmndb.ods', sheet_name = 'Full')

conn = sqlite3.connect('pkmn_types_stats.db')
df.to_sql('data', conn, if_exists = 'replace')
type_avg_df = pd.read_sql("SELECT 'Normal' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Normal' IN (Type1, Type2) UNION SELECT 'Grass' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Grass' IN (Type1, Type2) UNION SELECT 'Water' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Water' IN (Type1, Type2) UNION SELECT 'Fire' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Fire' IN (Type1, Type2) UNION SELECT 'Flying' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Flying' IN (Type1, Type2) UNION SELECT 'Fighting' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Fighting' IN (Type1, Type2) UNION SELECT 'Bug' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Bug' IN (Type1, Type2) UNION SELECT 'Electric' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Electric' IN (Type1, Type2) UNION SELECT 'Ground' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Ground' IN (Type1, Type2) UNION SELECT 'Rock' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Rock' IN (Type1, Type2) UNION SELECT 'Ice' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Ice' IN (Type1, Type2) UNION SELECT 'Poison' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Poison' IN (Type1, Type2) UNION SELECT 'Psychic' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Psychic' IN (Type1, Type2) UNION SELECT 'Ghost' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Ghost' IN (Type1, Type2) UNION SELECT 'Dragon' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Dragon' IN (Type1, Type2) UNION SELECT 'Dark' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Dark' IN (Type1, Type2) UNION SELECT 'Steel' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Steel' IN (Type1, Type2) UNION SELECT 'Fairy' as Type, AVG(HP), AVG(Attack), AVG(Defence), AVG(`Special Attack`), AVG(`Special Defence`), AVG(`Speed`), AVG(Total) FROM data WHERE 'Fairy' IN (Type1, Type2);", conn, index_col = 'Type')

conn.close()

fig, (ax1,ax2) = plt.subplots(ncols = 2, figsize = (11,8), width_ratios = [5,2.5])

fig.suptitle('Average Base Stats per Type', fontproperties = prop, fontsize = 20)

sns.heatmap(data = type_avg_df.drop('AVG(Total)', axis = 1), 
            cmap = 'Blues', annot = True, fmt='.0f', linewidths = 1, cbar = False, ax = ax1)
ax1.set_ylabel('')
ax1.xaxis.tick_top()
ax1.xaxis.set_label_position('top')
ax1.set_xticklabels(['HP','Attack','Defense','Sp. Att', 'Sp. Def', 'Speed'], fontproperties = prop, fontsize = 10)
ax1.set_yticklabels(ax1.get_yticklabels(), fontproperties = prop, fontsize = 9)

sns.heatmap(data = type_avg_df[['AVG(Total)']], 
            cmap = 'Blues', annot = True, fmt = '.0f', linewidths = 1, cbar = False, 
            yticklabels = False, ax = ax2)
ax2.set_ylabel('')
ax2.xaxis.tick_top()
ax2.xaxis.set_label_position('top')
ax2.set_aspect(0.15)
ax2.set_xticklabels(['Base Stat Total'], fontproperties = prop, fontsize = 10)

fig.tight_layout()
fig.savefig('average_stats.png', transparent = True, bbox_inches = 'tight')