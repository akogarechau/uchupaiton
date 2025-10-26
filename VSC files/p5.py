import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import mannwhitneyu

# Загрузка данных
df = pd.read_excel('Для диаграмм с усами (1).xlsx', sheet_name='Лист2')

# Очистка данных
df = df.dropna(subset=['Инсульт'])
df['Инсульт'] = df['Инсульт'].astype(int)

# Показатели для анализа
indicators = ['PSV', 'ED', 'TAV', 'Ri', 'PI']

# Функция для расчета доверительного интервала медианы
def median_confidence_interval(data, confidence=0.95):
    n = len(data)
    if n == 0:
        return np.nan, np.nan
    sorted_data = np.sort(data)
    z = 1.96  # Для 95% доверительного интервала
    
    k = math.floor(n/2 - z * np.sqrt(n)/2)
    k = max(0, k)
    lower_idx = k
    upper_idx = n - k - 1
    
    return sorted_data[lower_idx], sorted_data[upper_idx]

# Создание графиков
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, indicator in enumerate(indicators):
    ax = axes[idx]
    
    # Разделение данных по группам
    groups = []
    medians = []
    conf_intervals = []
    p_values = []
    
    for group in sorted(df['Инсульт'].unique()):
        group_data = df[df['Инсульт'] == group][indicator].dropna()
        groups.append(f'Группа {group}')
        
        # Расчет медианы
        median = np.median(group_data)
        medians.append(median)
        
        # Доверительный интервал
        lower, upper = median_confidence_interval(group_data)
        conf_intervals.append((median - lower, upper - median))
    
    # Расчет p-value между группами
    if len(df['Инсульт'].unique()) > 1:
        group0_data = df[df['Инсульт'] == 0][indicator].dropna()
        group1_data = df[df['Инсульт'] == 1][indicator].dropna()
        _, p_value = mannwhitneyu(group0_data, group1_data, alternative='two-sided')
    else:
        p_value = np.nan
    
    # Построение столбчатой диаграммы
    x_pos = np.arange(len(groups))
    bars = ax.bar(x_pos, medians, yerr=np.array(conf_intervals).T, 
                  capsize=5, alpha=0.7, color=['skyblue', 'lightcoral'])
    
    # Настройка графика
    ax.set_xlabel('Группы')
    ax.set_ylabel(indicator)
    ax.set_title(f'{indicator}\nP-value: {p_value:.4f}')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(groups)
    ax.grid(True, alpha=0.3)
    
    # Добавление значений на столбцы
    for bar, median in zip(bars, medians):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{median:.1f}', ha='center', va='bottom')

# Удаление пустого subplot
fig.delaxes(axes[-1])

plt.tight_layout()
plt.savefig('medians_with_confidence_intervals.png', dpi=300, bbox_inches='tight')
plt.show()

# Дополнительная текстовая информация
print("Статистика по группам:")
for indicator in indicators:
    print(f"\n{indicator}:")
    for group in sorted(df['Инсульт'].unique()):
        group_data = df[df['Инсульт'] == group][indicator].dropna()
        median = np.median(group_data)
        lower, upper = median_confidence_interval(group_data)
        print(f"  Группа {group}: Медиана = {median:.2f}, 95% ДИ = [{lower:.2f}, {upper:.2f}]")