import streamlit as st

# Custom styles for large, bold, black text with background
st.markdown("""
<style>
body {
    background-image: url('https://images.unsplash.com/photo-1570129477492-45c003edd2be');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
}

.stApp {
    background-color: rgba(255, 255, 255, 0.75);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(2px);
    color: #000000;
    font-weight: bold;
    font-size: 20px;
}

h1, .stApp h1 {
    font-size: 3rem !important;
    color: #000000 !important;
    font-weight: bold !important;
    text-align: center !important;
    margin-bottom: 2rem !important;
    text-shadow: 1px 1px 2px #999 !important;
}

label, .stSlider label, .stSelectbox label, .stTextInput label {
    color: #000000;
    font-weight: bold;
    font-size: 20px;
}

.stButton>button {
    background-color: #ffc107;
    color: #000000;
    font-weight: bold;
    font-size: 18px;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 8px;
    margin-top: 1rem;
}

.stButton>button:hover {
    background-color: #e0a800;
}

.stMarkdown > div {
    font-size: 22px;
    font-weight: bold;
    color: #000000;
    background-color: rgba(255, 255, 255, 0.95);
    padding: 1.2rem;
    border-radius: 12px;
    border: 2px solid #000000;
    box-shadow: 3px 3px 12px rgba(0, 0, 0, 0.2);
    margin-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🏡 Satara District Real Estate Price Estimator")

# Satara taluka-wise rate map (sample prices per sqft)
satara_rate_map = {
    "Satara": 7500,
    "Karad": 6800,
    "Wai": 7200,
    "Mahabaleshwar": 9500,
    "Patan": 5000,
    "Phaltan": 6400,
    "Khatav": 5800,
    "Koregaon": 6100,
    "Man": 5300,
    "Jaoli": 5500,
    "Khandala": 6000  # Newly added
}

# UI components
taluka = st.selectbox("🏘️ Select Taluka in Satara", sorted(satara_rate_map.keys()))
area_sqft = st.slider("📏 Enter Property Area (in sqft)", 300, 5000, 1000)

# Price Calculation
rate_per_sqft = satara_rate_map[taluka]
estimated_price = rate_per_sqft * area_sqft

# Estimate Button
if st.button("💡 Estimate Price"):
    st.success(f"🏷️ **Rate**: ₹{rate_per_sqft:,} per sqft")
    st.success(f"💰 **Estimated Property Price in {taluka}, Satara**: ₹{estimated_price:,.0f}")
