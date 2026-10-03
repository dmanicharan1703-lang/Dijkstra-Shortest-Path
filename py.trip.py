
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Araku Valley Trip Planner",
    page_icon="🏞️",
    layout="wide"
)

# Title
st.title("🏞️ Araku Valley Trip Planner")
st.subheader("Your personalized travel plan from Hyderabad")

st.write(
    "Plan your Araku Valley trip with a complete itinerary, "
    "budget calculator, sightseeing schedule, and travel checklist."
)

# Sidebar settings
st.sidebar.header("⚙️ Trip Settings")

travelers = st.sidebar.number_input(
    "Number of Travelers",
    min_value=1,
    max_value=20,
    value=4
)

budget = st.sidebar.number_input(
    "Total Group Budget (₹)",
    min_value=10000,
    value=150000,
    step=5000
)

departure_date = st.sidebar.date_input(
    "Departure Date"
)

transport = st.sidebar.selectbox(
    "Transport",
    ["Train + Local Cab", "Private Car", "Bus + Local Cab"]
)

# Route
st.header("🗺️ Travel Route")

st.info(
    "Hyderabad → Visakhapatnam → Borra Caves → "
    "Katiki Waterfalls → Araku Village → "
    "Padmapuram Gardens → Galikonda Viewpoint → "
    "Visakhapatnam → Hyderabad"
)

# Itinerary
st.header("📅 Complete Trip Itinerary")

itinerary = {
    "Day 0 - Overnight Journey": [
        ("Evening", "Board the overnight train from Hyderabad to Visakhapatnam."),
        ("Night", "Rest on the train and keep tickets, ID, and essentials ready.")
    ],

    "Day 1 - Borra Caves, Katiki Falls and Araku": [
        ("Morning", "Arrive in Visakhapatnam and have breakfast."),
        ("10:30 AM - 12:00 PM", "Explore Borra Caves."),
        ("12:00 PM - 1:00 PM", "Lunch and travel toward Katiki Waterfalls."),
        ("1:00 PM - 4:00 PM", "Visit Katiki Waterfalls. Access may involve a jeep ride and trek. Check local weather and access conditions."),
        ("Late Afternoon", "Drive to Araku Valley and check into the hotel."),
        ("Evening", "Dinner and relaxation.")
    ],

    "Day 2 - Explore Araku Valley": [
        ("8:30 AM - 10:30 AM", "Explore Araku Village."),
        ("10:30 AM - 12:30 PM", "Visit Padmapuram Gardens / Araku Park."),
        ("12:30 PM - 3:30 PM", "Lunch and rest."),
        ("Afternoon", "Enjoy Araku coffee and local shopping."),
        ("4:30 PM - 6:15 PM", "Visit Galikonda Viewpoint for sunset. Adjust timing according to sunset and weather."),
        ("Evening", "Return to hotel and have dinner.")
    ],

    "Day 3 - Shopping and Return": [
        ("Morning", "Breakfast, hotel checkout, and shopping."),
        ("12:30 PM - 2:00 PM", "Final lunch featuring Bongu chicken biryani. Confirm availability with the restaurant in advance."),
        ("Afternoon", "Drive from Araku to Visakhapatnam."),
        ("Night", "Board the overnight train to Hyderabad.")
    ]
}

for day, activities in itinerary.items():

    with st.expander(day, expanded=True):

        for time, activity in activities:

            st.markdown(f"**{time}**")

            st.write(activity)

            st.divider()

# Budget calculator
st.header("💰 Trip Budget Calculator")

budget_items = {
    "Train Tickets (Round Trip)": 16000,
    "Local Cab": 32000,
    "Hotel (2 Rooms x 2 Nights)": 24000,
    "Food and Meals": 24000,
    "Entry Tickets and Activities": 12000,
    "Station Transfers": 10000,
    "Snacks and Extras": 8000,
    "Emergency Reserve": 24000
}

budget_df = pd.DataFrame(
    list(budget_items.items()),
    columns=["Expense", "Estimated Cost (₹)"]
)

total_cost = budget_df["Estimated Cost (₹)"].sum()

per_person = total_cost / travelers

remaining = budget - total_cost

st.dataframe(
    budget_df,
    use_container_width=True,
    hide_index=True
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Estimated Cost",
    f"₹{total_cost:,.0f}"
)

col2.metric(
    "Cost Per Person",
    f"₹{per_person:,.0f}"
)

col3.metric(
    "Budget Remaining",
    f"₹{remaining:,.0f}",
    delta_color="normal" if remaining >= 0 else "inverse"
)

if remaining < 0:
    st.error("Your estimated expenses exceed your budget!")
else:
    st.success("Your estimated expenses are within your budget.")

st.caption(
    "Note: These are planning estimates, not live prices. "
    "Confirm fares, hotel rates, entry fees, and cab charges before booking."
)

# Expense chart
st.subheader("📊 Expense Distribution")

st.bar_chart(
    budget_df.set_index("Expense")
)

# Travel checklist
st.header("✅ Travel Checklist")

checklist = [
    "Book round-trip train tickets",
    "Confirm hotel rooms",
    "Book local cab",
    "Check Borra Caves access and timings",
    "Check Katiki Falls weather and access",
    "Carry comfortable walking shoes",
    "Pack rain protection and water",
    "Carry basic medicines",
    "Confirm final lunch menu",
    "Keep emergency cash",
    "Share itinerary with family"
]

for item in checklist:
    st.checkbox(item)

# Download itinerary
st.header("📥 Download Your Trip Plan")

itinerary_rows = []

for day, activities in itinerary.items():

    for time, activity in activities:

        itinerary_rows.append({
            "Day": day,
            "Time": time,
            "Activity": activity
        })

itinerary_df = pd.DataFrame(itinerary_rows)

csv_data = itinerary_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Complete Itinerary (CSV)",
    data=csv_data,
    file_name="araku_trip_itinerary.csv",
    mime="text/csv"
)

st.success("Your Araku Valley Trip Planner is ready!")