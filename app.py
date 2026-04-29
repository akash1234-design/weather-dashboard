import streamlit as st
import requests

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather Dashboard")
st.markdown("Hansi, Haryana ka live mausam dekho")

# API Key - OpenWeatherMap se free me milegi
API_KEY = "YOUR_API_KEY" 

# City input
city = st.text_input("City ka naam daalo", "Hansi")

if st.button("Weather Check Karo") or city:
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Temperature", f"{round(data['main']['temp'])}°C")
            with col2:
                st.metric("Humidity", f"{data['main']['humidity']}%")
            with col3:
                st.metric("Wind Speed", f"{data['wind']['speed']} m/s")
            
            st.subheader(f"{data['name']}, {data['sys']['country']}")
            st.write(f"**Mausam:** {data['weather'][0]['description'].title()}")
            st.write(f"**Feels Like:** {round(data['main']['feels_like'])}°C")
            st.write(f"**Pressure:** {data['main']['pressure']} hPa")
            
            # Weather icon
            icon = data['weather'][0]['icon']
            st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
            
        else:
            st.error("City nahi mili 😅 Spelling check kar")
            
    except Exception as e:
        st.error("Kuch gadbad ho gayi. API key check kar")

st.markdown("---")
st.caption("Made with Streamlit | Data from OpenWeatherMap")
