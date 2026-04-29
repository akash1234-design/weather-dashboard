import streamlit as st
import requests

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather Dashboard")
st.markdown("Hansi, Haryana ka live mausam dekho")

# API Key Streamlit Secrets se le rahe hain
try:
    
import requests

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather Dashboard")
st.markdown("Hansi, Haryana ka live mausam dekho")

# API Key Streamlit Secrets se le rahe hain
try:
    API_KEY = st.secrets["API_KEY"]
except:
    st.error("Bhai API_KEY set nahi hai 😅 Streamlit Cloud > Settings > Secrets me add karo")
    st.code('API_KEY = "teri_api_key"', language="toml")
    st.stop()

# City input
city = st.text_input("City ka naam daalo", "Hansi")

if st.button("Weather Check Karo") or city:
    if not city:
        st.warning("City ka naam to daal pehle")
    else:
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
                
                # Weather icon
                icon = data['weather'][0]['icon']
                st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png", width=100)
                
            elif data["cod"] == 401:
                st.error("API Key galat hai ya abhi activate nahi hui. 15-20 min wait karo")
            elif data["cod"] == 404:
                st.error("City nahi mili 😅 Spelling check kar")
            else:
                st.error(f"Kuch gadbad hai: {data['message']}")
                
        except Exception as e:
            st.error("Network error. Net check kar le")

st.markdown("---")
st.caption("Made with Streamlit | Data from OpenWeatherMap")
import requests

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather Dashboard")
st.markdown("Hansi, Haryana ka live mausam dekho")

# API Key Streamlit Secrets se le rahe hain
try:
    API_KEY = st.secrets["API_KEY"]
except:
    st.error("Bhai API_KEY set nahi hai 😅 Streamlit Cloud > Settings > Secrets me add karo")
    st.code('API_KEY = "teri_api_key"', language="toml")
    st.stop()

# City input
city = st.text_input("City ka naam daalo", "Hansi")

if st.button("Weather Check Karo") or city:
    if not city:
        st.warning("City ka naam to daal pehle")
    else:
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
                
                # Weather icon
                icon = data['weather'][0]['icon']
                st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png", width=100)
                
            elif data["cod"] == 401:
                st.error("API Key galat hai ya abhi activate nahi hui. 15-20 min wait karo")
            elif data["cod"] == 404:
                st.error("City nahi mili 😅 Spelling check kar")
            else:
                st.error(f"Kuch gadbad hai: {data['message']}")
                
        except Exception as e:
            st.error("Network error. Net check kar le")

st.markdown("---")
st.caption("Made with Streamlit | Data from OpenWeatherMap")
except:
    st.error("Bhai API_KEY set nahi hai 😅 Streamlit Cloud > Settings > Secrets me add karo")
    st.code('API_KEY = "teri_api_key"', language="toml")
    st.stop()

# City input
city = st.text_input("City ka naam daalo", "Hansi")

if st.button("Weather Check Karo") or city:
    if not city:
        st.warning("City ka naam to daal pehle")
    else:
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
                
                # Weather icon
                icon = data['weather'][0]['icon']
                st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png", width=100)
                
            elif data["cod"] == 401:
                st.error("API Key galat hai ya abhi activate nahi hui. 15-20 min wait karo")
            elif data["cod"] == 404:
                st.error("City nahi mili 😅 Spelling check kar")
            else:
                st.error(f"Kuch gadbad hai: {data['message']}")
                
        except Exception as e:
            st.error("Network error. Net check kar le")

st.markdown("---")
st.caption("Made with Streamlit | Data from OpenWeatherMap")
