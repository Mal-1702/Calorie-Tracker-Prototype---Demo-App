import streamlit as st

# --- Calorie Data ---
food_data = {
    "breakfast": {
        "poha": 180, "upma": 200, "idli": 70, "vada": 150, "dosa": 160,
        "uttapam": 180, "paratha": 250, "plain paratha": 200, "stuffed paratha": 300,
        "chai": 100, "coffee": 110, "milk": 130, "bread butter": 170,
        "toast": 120, "cornflakes": 140, "muesli": 180, "sprouts": 100, "boiled eggs": 150
    },
    "lunch": {
        "roti": 100, "chapati": 100, "paratha": 250, "rice": 200, "jeera rice": 220,
        "dal": 180, "rajma": 220, "chole": 240, "bhaji": 250, "paneer": 300,
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
        "veg pulao": 240, "chicken curry": 350, "mutton curry": 400
    },
    "sweets": {
        "gulab jamun": 150, "rasgulla": 120, "jalebi": 200, "halwa": 250,
        "barfi": 180, "laddu": 200, "kheer": 220, "ice cream": 210,
        "cake": 240, "chocolate": 150
    }
}

# --- Streamlit UI ---
st.set_page_config(page_title="Calorie Tracker", page_icon="🍛")
st.title("🍽️ Indian Food Calorie Tracker")
st.markdown("Track what you eat and monitor your calorie intake!")

# Initialize session state
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

# Meal selection
meal_type = st.selectbox("Select Meal Type", list(food_data.keys()))

# Item selection
selected_item = st.selectbox("Select Food Item", list(food_data[meal_type].keys()))
cal = food_data[meal_type][selected_item]
st.write(f"**Calories:** {cal} kcal")

# Add button
if st.button("Add to Tracker"):
    st.session_state.selected_items.append((selected_item, cal))
    st.success(f"✅ Added {selected_item.title()} to your tracker!")

# Display tracked items
if st.session_state.selected_items:
    st.markdown("### 🍛 Items You Ate")
    total_calories = 0
    for item, cal in st.session_state.selected_items:
        st.write(f"- {item.title()} ➤ {cal} kcal")
        total_calories += cal

    st.markdown(f"### 🔥 Total Calories: **{total_calories} kcal**")

    # --- Suggestions ---
    st.markdown("### 🧠 Health Suggestion:")
    if total_calories < 1200:
        st.info("Your intake is very low. Try eating more for energy ⚡")
    elif total_calories > 2000:
        st.warning("You've eaten quite a lot. Consider lighter meals next ⛔")
    else:
        st.success("You're on track! Good job 👍")

    # --- Clear Tracker ---
    if st.button("Clear Tracker"):
        st.session_state.selected_items = []
        st.rerun()
