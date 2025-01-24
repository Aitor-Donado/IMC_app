import streamlit as st

# Título de la aplicación
st.title("Calculadora de IMC (Índice de Masa Corporal)")

# Descripción de la aplicación
st.write("""
Esta es una aplicación sencilla para calcular el Índice de Masa Corporal (IMC).
Ingresa tu peso y altura para obtener tu IMC.
""")

# Inputs del usuario
peso = st.number_input("Ingresa tu peso (en kg):", min_value=0.0, format="%.2f")
altura = st.number_input("Ingresa tu altura (en metros):", min_value=0.0, format="%.2f")

# Calcular el IMC
if st.button("Calcular IMC"):
    if altura > 0:
        imc = peso / (altura ** 2)
        st.write(f"Tu IMC es: **{imc:.2f}**")

        # Interpretación del IMC
        if imc < 18.5:
            st.write("**Bajo peso**")
        elif 18.5 <= imc < 24.9:
            st.write("**Peso normal**")
        elif 25 <= imc < 29.9:
            st.write("**Sobrepeso**")
        else:
            st.write("**Obesidad**")
    else:
        st.error("La altura debe ser mayor que 0.")