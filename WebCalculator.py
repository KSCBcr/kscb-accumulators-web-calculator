import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="ACCUMULATORS CORE", page_icon="📈", layout="centered")

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #12182b;
        color: #ffffff;
    }
    .titulo {
        text-align: center;
        color: #06b6d4;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: bold;
    }
    .subtitulo {
        text-align: center;
        color: #94a3b8;
        font-size: 14px;
        letter-spacing: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown("<h1 class='titulo'>ACCUMULATORS</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>D E R I V  T R A D I N G  S Y S T E M</p>", unsafe_allow_html=True)
st.divider()

# --- FORMULARIO DE ENTRADA ---
stake = st.number_input("STAKE (INVERSIÓN USD)", min_value=0.0, value=15.0, step=1.0)
tasa = st.radio("CRECIMIENTO (TASA %)", options=[1, 2, 3, 4, 5], index=4, horizontal=True)
ticks = st.number_input("PROYECCIÓN: CANTIDAD DE TICKS", min_value=1, value=6, step=1)

# --- BOTÓN Y LÓGICA ---
if st.button("EJECUTAR ANÁLISIS ALGORÍTMICO", type="primary"):
    # Cálculos
    tasa_decimal = tasa / 100
    payout = stake * (1 + tasa_decimal)**ticks
    ganancia = payout - stake
    
    st.success("ANÁLISIS COMPLETADO - KSCB PRODUCTIONS")
    
    # Mostrar resultados en tarjetas destacadas
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="PAGO TOTAL", value=f"${payout:.2f}")
    with col2:
        st.metric(label="GANANCIA NETA", value=f"${ganancia:.2f}", delta=f"${ganancia:.2f}")