import matplotlib.pyplot as plt  # pyright: ignore[reportMissingImports]

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

# הוספת ערכי נתונים על כל עמודה, שדרוג צבעים וגריד

# בחר צבעים ייחודיים לכל עמודה
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFD700']

plt.figure(figsize=(10, 7))
bars = plt.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)

# הוספת ערך מספרי מעל כל עמודה
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        bar.get_height() + 0.5, 
        f'{bar.get_height()}', 
        ha='center', 
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

plt.title('גרף עמודות משודרג', fontsize=18, fontweight='bold', color='#333333')
plt.xlabel('קטגוריה', fontsize=14)
plt.ylabel('ערך', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
