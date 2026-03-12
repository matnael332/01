import matplotlib.pyplot as plt

# יצירת נתוני דוגמה לגרף
categories = ['קטגוריה א', 'קטגוריה ב', 'קטגוריה ג', 'קטגוריה ד']
values = [23, 17, 35, 29]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')
plt.title('גרף עמודות לדוגמה')
plt.xlabel('קטגוריה')
plt.ylabel('ערך')
plt.tight_layout()
plt.show()