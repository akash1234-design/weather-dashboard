import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600;700&display=swap');
html, body, [class*="css"] { background-color: #0a0a1a; color: #fff; font-family: 'Inter', sans-serif; }
.stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.hero {
    background: linear-gradient(135deg, #FF6B00 0%, #FFA500 50%, #1a0a4a 100%);
    padding: 2.5rem; border-radius: 20px; margin-bottom: 2rem; text-align: center;
    box-shadow: 0 8px 32px rgba(255,107,0,0.3);
}
.hero h1 { font-family:'Bebas Neue',sans-serif; font-size:3.5rem; letter-spacing:4px; color:#fff; margin:0; }
.hero p { color:#ffcc99; margin-top:0.5rem; }
.metric-card {
    background: linear-gradient(135deg,#1a1a2e,#16213e); border:1px solid #FF6B00;
    border-radius:16px; padding:1.3rem; text-align:center; margin-bottom:1rem;
    box-shadow:0 4px 15px rgba(255,107,0,0.15);
}
.metric-number { font-family:'Bebas Neue',sans-serif; font-size:2.5rem; color:#FF6B00; }
.metric-label { color:#aaa; font-size:0.8rem; text-transform:uppercase; letter-spacing:2px; }
.section-title {
    font-family:'Bebas Neue',sans-serif; font-size:1.8rem; color:#FF6B00;
    letter-spacing:3px; border-left:4px solid #FF6B00; padding-left:12px; margin:1.5rem 0 1rem 0;
}
[data-testid="stSidebar"] { background-color:#0d0d1a !important; border-right:1px solid #FF6B00; }
.stTabs [data-baseweb="tab-list"] { background-color:#1a1a2e; border-radius:10px; }
.stTabs [aria-selected="true"] { color:#FF6B00 !important; border-bottom:2px solid #FF6B00; }
.stButton > button {
    background:linear-gradient(135deg,#FF6B00,#cc4400); color:white; border:none;
    border-radius:10px; font-weight:700; padding:0.6rem 2rem; transition:all 0.2s;
}
.stButton > button:hover { transform:scale(1.03); }
#MainMenu, footer, header { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🌤️ WEATHER DASHBOARD</h1>
    <p>Real-Time Weather • Forecasts • Air Quality • Analytics</p>
</div>
""", unsafe_allow_html=True)

API_KEY = st.secrets.get("OPENWEATHER_API_KEY", "")

with st.sidebar:
    st.markdown("## 🌍 Weather Search")
    st.markdown("---")
    city = st.text_input("🏙️ City ka naam likho", "Delhi", label_visibility="collapsed")
    st.markdown("---")
    st.info(f"API Key Status: {'✅ Connected' if API_KEY else '⚠️ Add OPENWEATHER_API_KEY to Secrets'}")

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        return None
    except:
        return None

def get_forecast(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        return None
    except:
        return None

def get_aqi(lat, lon):
    try:
        url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        return None
    except:
        return None

weather = get_weather(city) if API_KEY else None
if weather:
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']
    wind_speed = weather['wind']['speed']
    description = weather['weather'][0]['description'].title()
    feels_like = weather['main']['feels_like']
    pressure = weather['main']['pressure']

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="metric-card"><div class="metric-number">{int(temp)}°C</div><div class="metric-label">Temperature</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><div class="metric-number">{humidity}%</div><div class="metric-label">Humidity</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-card"><div class="metric-number">{wind_speed} m/s</div><div class="metric-label">Wind Speed</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="metric-card"><div class="metric-number">{pressure} mb</div><div class="metric-label">Pressure</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📍 Location Map")

    lat = weather['coord']['lat']
    lon = weather['coord']['lon']
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Current", "Forecast", "AQI", "Details"])

    with tab1:
        st.markdown(f"### {city}, {weather['sys']['country']}")
        st.markdown(f"**{description}**")
        st.metric("Feels Like", f"{int(feels_like)}°C")

    with tab2:
        forecast = get_forecast(city)
        if forecast:
            st.subheader("5-Day Forecast")
            for item in forecast['list'][:5]:
                date = item['dt_txt']
                temp_f = item['main']['temp']
                desc_f = item['weather'][0]['description'].title()
                st.markdown(f"**{date}** - {int(temp_f)}°C, {desc_f}")
        else:
            st.warning("Forecast data nahi mila")

    with tab3:
        aqi_data = get_aqi(lat, lon)
        if aqi_data:
            aqi = aqi_data['list'][0]['main']['aqi']
            aqi_text = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
            st.subheader("Air Quality Index")
            st.metric("AQI Level", f"{aqi} - {aqi_text.get(aqi, 'Unknown')}")
            components = aqi_data['list'][0]['components']
            st.markdown("**Pollutants:**")
            st.json(components)
        else:
            st.warning("AQI data nahi mila")

    with tab4:
        st.markdown("### Additional Details")
        info = pd.DataFrame({
            'Parameter': ['Sunrise', 'Sunset', 'Visibility', 'Cloudiness'],
            'Value': [
                datetime.fromtimestamp(weather['sys']['sunrise']).strftime('%H:%M'),
                datetime.fromtimestamp(weather['sys']['sunset']).strftime('%H:%M'),
                f"{weather.get('visibility', 0)/1000} km",
                f"{weather['clouds']['all']}%"
            ]
        })
        st.dataframe(info, use_container_width=True, hide_index=True)

else:
    if not API_KEY:
        st.error("❌ API Key missing! Add OPENWEATHER_API_KEY to Streamlit Secrets")
        st.info("Steps:\n1. Jao openweathermap.org\n2. Free API Key lo\n3. Streamlit Cloud → Settings → Secrets")
    else:
        st.warning(f"⚠️ '{city}' city nahi mili. City name check karo!")

st.markdown("---")
st.markdown('<p style="text-align:center;color:#444;font-size:0.8rem;">🌤️ Weather Dashboard | Powered by OpenWeatherMap</p>', unsafe_allow_html=True)
