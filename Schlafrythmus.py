import streamlit as st
import datetime

# 1. Regelwerke / Daten
rules_1 = {
    'Getrennt': 0,
    'Zusammen': 1
}

rules_2 = {
    'Arbeitstage': {'Schlafstunden': 7, 'Einschlafzeit': 1},
    'Wochenende': {'Schlafstunden': 9, 'Einschlafzeit': 1}
}

# 2. Titel der App
st.title("Schlafrythmus")

# 3. Auswahlfelder (Dropdowns)
option_1 = st.selectbox(
    "Schlafmodus:",
    options=['Getrennt', 'Zusammen'],
    index=None,
    placeholder="Auswählen..."
)

option_2 = st.selectbox(
    "Tagesart:",
    options=['Arbeitstage', 'Wochenende'],
    index=None,
    placeholder="Auswählen..."
)

# 4. Aufstehzeit auswählen
st.write("**Wann aufstehen?**")
aufstehzeit = st.time_input(
    label="Aufstehzeit", 
    value=datetime.time(12, 0), 
    label_visibility="collapsed"
)

# 5. Berechnung und Button
if st.button("Berechnen", type="primary"):
    if option_1 is not None and option_2 is not None:
        add_presleep = rules_1[option_1]
        sleep_data = rules_2[option_2]
        
        einschlafzeit = sleep_data['Einschlafzeit'] + add_presleep
        schlafzeit = sleep_data['Schlafstunden']
        
        # Berechnung
        gesamtdauer = einschlafzeit + schlafzeit
        hour = aufstehzeit.hour
        minute = aufstehzeit.minute
        
        bedtime_hour = hour - gesamtdauer
        if bedtime_hour < 0:
            bedtime_hour = 24 + bedtime_hour
            
        # Formatierte Uhrzeit-Ausgabe (z. B. 22:00 Uhr)
        bedtime_str = f"{bedtime_hour:02d}:{minute:02d}"
        
        st.success(f"Du solltest um **{bedtime_str} Uhr** schlafen gehen!")
    else:
        st.error("Bitte überall etwas auswählen!")