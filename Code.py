import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv (r'Seed Yield.csv')
print (df)
sns.set_theme(style="whitegrid")
# Draw a nested barplot by cultivar and irrigation
g = sns.catplot(
    data=df, kind="bar",
    x="Cultivar", y="Seed Yield", hue="Irrigation",
    ci="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=False)
g.set_axis_labels("", "Seed Yield (kg)")
g.legend.set_title("Irrigation")
plt.show()
