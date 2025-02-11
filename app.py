import streamlit as st

def calculate_co2_savings(battery_capacity_kwh, cycles_per_year, co2_grid_emission=350, usable_capacity=0.9, efficiency=0.95):
    """
    Berechnet die jährliche CO2-Einsparung durch eine Batterie, die mit Solarstrom geladen wird.
    
    :param battery_capacity_kwh: Kapazität der Batterie in kWh
    :param cycles_per_year: Anzahl der vollständigen Ladezyklen pro Jahr
    :param co2_grid_emission: CO2-Emission des Netzstroms in g CO2/kWh (Standard: 350 g/kWh)
    :param usable_capacity: Nutzbare Kapazität der Batterie (Standard: 90%)
    :param efficiency: Systemwirkungsgrad der Batterie (Standard: 95%)
    :return: Jährliche CO2-Einsparung in Tonnen
    """
    usable_energy_per_year = battery_capacity_kwh * cycles_per_year * usable_capacity * efficiency
    co2_savings_tons = (usable_energy_per_year * co2_grid_emission) / 1000 / 1000
    return co2_savings_tons

# Streamlit UI
col1, col2 = st.columns([4, 1])
with col2:
        st.image("logo.png", width=150)
st.title("CO2-Einsparungsrechner für Batteriespeicher")

battery_capacity = st.number_input("Batteriekapazität (kWh)", min_value=0.1, value=1288.0)
cycles = st.number_input("Ladezyklen pro Jahr", min_value=1, value=250)
co2_emission = st.number_input("CO2-Emission des Netzstroms (g/kWh)", min_value=0.0, value=380.0)

if st.button("Berechnen"):
    col1, col2, col3 = st.columns([1, 1, 1])
    savings = calculate_co2_savings(battery_capacity, cycles, co2_emission)
    savings_20_years = savings * 20
    people_equivalent = savings / 7.16
    
    with col1:
        st.success(f"Jährliche CO2-Einsparung: {savings:,.2f} Tonnen")
    with col2:
        st.success(f"CO2-Einsparung über 20 Jahre: {savings_20_years:,.2f} Tonnen")
    with col3:
        st.success(f"Das entspricht der CO2-Emission von {people_equivalent:,.2f} Personen pro Jahr")
