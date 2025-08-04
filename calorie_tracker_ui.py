import tkinter as tk
from tkinter import messagebox, ttk

# Full food_data with sweets
food_data = {
    "breakfast": {
        "poha": 180, "upma": 200, "idli": 70, "vada": 150, "dosa": 160,
        "uttapam": 180, "paratha": 250, "plain paratha": 200, "stuffed paratha": 300,
        "chai": 100, "coffee": 110, "milk": 130, "bread butter": 170,
        "toast": 120, "cornflakes": 140, "muesli": 180, "sprouts": 100, "boiled eggs": 150
    },
    "lunch": {
        "roti": 100, "chapati": 100, "paratha": 250, "rice": 200, "jeera rice": 220,
        "dal": 180, "rajma": 220, "chole": 240, "bhaji": 250, "paneer ": 300,
        "palak paneer": 280, "mix veg": 150, "bhindi fry": 120, "aloo gobi": 170,
        "sambar": 150, "rasam": 100, "curd": 90, "pickle": 50, "papad": 80,
        "buttermilk": 70, "baingan ka bharta": 180
    },
    "snacks": {
        "samosa": 260, "pakora": 180, "kachaudi": 250, "kachori": 270, "chaat": 200,
        "pani puri": 150, "sev puri": 160, "dahi puri": 180, "bhel puri": 150,
        "aloo tikki": 220, "vada pav": 300, "dhokla": 120, "khandvi": 110,
        "cutlet": 210, "masala peanuts": 200, "banana chips": 250,
        "tea": 100, "coffee": 110, "biscuits": 150
    },
    "dinner": {
        "roti": 100, "rice": 200, "dal": 180, "sabzi": 140, "khichdi": 220,
        "veg pulao": 240, "chicken curry": 350, "mutton curry": 400,
        "fish curry": 300, "paneer curry": 280, "curd": 90, "salad": 60,
        "buttermilk": 70, "vegetable soup": 120, "egg curry": 250
    },
    "fast_food": {
        "burger": 500, "pizza slice": 350, "noodles": 400, "manchurian": 300,
        "french fries": 350, "pav bhaji": 400, "fried rice": 360,
        "spring roll": 280, "momos": 220, "frankie": 300, "chilli potato": 320,
        "pasta" : 131       ,
    },
    "healthy_food": {
        "boiled eggs": 150, "grilled paneer": 250, "vegetable salad": 80,
        "fruit salad": 120, "smoothie": 180, "oats": 160, "sprouts": 100,
        "quinoa": 140, "grilled chicken": 300, "tofu stir fry": 220,
        "millet khichdi": 180
    },
    "sweets": {
        "gulab jamun": 350, "rasgulla": 186, "jalebi": 400, "ladoo (boondi)": 450,
        "kaju katli": 500, "barfi (milk)": 380, "halwa (sooji)": 400,
        "mysore pak": 550, "peda": 320, "modak": 270, "sandesh": 240,
        "malpua": 400, "cham cham": 300, "besan ladoo": 420, "badam halwa": 560,
        "rabri": 150, "shrikhand": 200, "phirni": 120, "kalakand": 350,
        "ice cream": 700
    }
}

# Flatten the food items into one searchable dictionary
all_items = {}
for category in food_data:
    for item in food_data[category]:
        all_items[item.strip().lower()] = food_data[category][item]

# App Class
class CalorieTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Indian Food Calorie Tracker")
        self.root.geometry("600x500")
        self.total = 0
        self.items = []

        # Input label and combo box
        tk.Label(root, text="Type Food Item:", font=("Segoe UI", 12)).pack(pady=5)
        self.entry = ttk.Combobox(root, values=list(all_items.keys()), font=("Segoe UI", 12))
        self.entry.set("poha")
        self.entry.pack(pady=5)

        # Add Button
        self.add_btn = tk.Button(root, text="➕ Add Food", command=self.add_food,
                                 bg="#4CAF50", fg="white", font=("Segoe UI", 12))
        self.add_btn.pack(pady=5)

        # List of added items
        self.listbox = tk.Listbox(root, width=50, height=10, font=("Segoe UI", 11))
        self.listbox.pack(pady=10)

        # Total Calories Label
        self.total_label = tk.Label(root, text=" Total Calories: 0", font=("Segoe UI", 14, "bold"))
        self.total_label.pack()

        # Summary Button
        self.finish_btn = tk.Button(root, text=" Finish & Summary", command=self.show_summary,
                                    bg="#2196F3", fg="white", font=("Segoe UI", 12))
        self.finish_btn.pack(pady=10)

    def add_food(self):
        item = self.entry.get().strip().lower()
        if item in all_items:
            cal = all_items[item]
            self.total += cal
            self.items.append((item, cal))
            self.listbox.insert(tk.END, f"{item.title()} - {cal} cal ")
            self.total_label.config(text=f" Total Calories: {self.total}")
        else:
            messagebox.showerror("Not Found", f"'{item}' not found in database.")

    def show_summary(self):
        if not self.items:
            messagebox.showinfo("No Items", "You haven't added any food items.")
            return

        summary = "\n".join([f"{item.title()} - {cal} cal" for item, cal in self.items])
        summary += f"\n\n Total Calories: {self.total} cal\n"

        # Lifestyle suggestions
        if self.total < 1200:
            summary += "\n Too Low! Eat more to stay energized."
        elif self.total > 2500:
            summary += "\n High intake! Consider balancing meals."
        else:
            summary += "\nGreat! You're within a healthy range."

        summary += "\n\n Tip: Stay hydrated, eat mindfully, and exercise daily!"

        messagebox.showinfo(" Meal Summary", summary)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalorieTrackerApp(root)
    root.mainloop()