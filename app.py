import streamlit as st
import pandas as pd
import joblib
pipeline = joblib.load("life_expectancy_pipeline.pkl")
st.title("Life Expectancy Prediction System")

st.write(
    "Enter socioeconomic indicators to predict life expectancy."
)
hdi_score = st.slider(
    "HDI Score",
    0.0,
    1.0,
    0.75
)

urban_population_pct = st.slider(
    "Urban Population (%)",
    0,
    100,
    70
)

internet_penetration_pct = st.slider(
    "Internet Penetration (%)",
    0,
    100,
    75
)

social_protection_coverage_pct = st.slider(
    "Social Protection Coverage (%)",
    0,
    100,
    60
)

clean_water_access_pct = st.slider(
    "Clean Water Access (%)",
    0,
    100,
    90
)

electricity_access_pct = st.slider(
    "Electricity Access (%)",
    0,
    100,
    95
)

literacy_rate_pct = st.slider(
    "Literacy Rate (%)",
    0,
    100,
    85
)

gdp_per_capita_usd = st.number_input(
    "GDP Per Capita (USD)",
    min_value=0
)

poverty_rate_pct = st.slider(
    "Poverty Rate (%)",
    0,
    100,
    20
)

child_mortality_per_1000 = st.slider(
    "Child Mortality per 1000",
    0,
    100,
    15
)
input_data = pd.DataFrame({

    'hdi_score':[hdi_score],
    'urban_population_pct':[urban_population_pct],
    'internet_penetration_pct':[internet_penetration_pct],
    'social_protection_coverage_pct':[social_protection_coverage_pct],
    'clean_water_access_pct':[clean_water_access_pct],
    'electricity_access_pct':[electricity_access_pct],
    'literacy_rate_pct':[literacy_rate_pct],
    'gdp_per_capita_usd':[gdp_per_capita_usd],
    'poverty_rate_pct':[poverty_rate_pct],
    'child_mortality_per_1000':[child_mortality_per_1000]

})
if st.button("Predict Life Expectancy"):

    prediction = pipeline.predict(input_data)

    st.success(
        f"Predicted Life Expectancy: {prediction[0]:.2f} Years"
    )
