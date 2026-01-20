# ---------------------------------------------------------
# Importación de librerías
# ---------------------------------------------------------
import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# Inicialización de la tabla
# ---------------------------------------------------------
if "table_data" not in st.session_state:
    st.session_state.table_data = pd.DataFrame(
        columns=["producto", "precio", "cantidad", "subtotal", "impuesto", "total_con_impuesto"]
    )

# Flag para limpiar formulario
if "reset_form" not in st.session_state:
    st.session_state.reset_form = False

# ---------------------------------------------------------
# Función para calcular subtotal e impuestos
# ---------------------------------------------------------
def calcular_subtotal(nombre_producto, precio_producto, cantidad_producto, es_alcohol):
    subtotal = float(precio_producto) * float(cantidad_producto)
    impuesto = subtotal * (0.18 if es_alcohol else 0.15)
    total_con_impuesto = subtotal + impuesto

    nueva_fila = {
        "producto": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto,
        "subtotal": subtotal,
        "impuesto": impuesto,
        "total_con_impuesto": total_con_impuesto
    }

    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, pd.DataFrame([nueva_fila])],
        ignore_index=True
    )

# ---------------------------------------------------------
# Título
# ---------------------------------------------------------
st.title("Supermercado El más barato")

# ---------------------------------------------------------
# Si se presionó "Nuevo producto", limpiar valores ANTES de crear widgets
# ---------------------------------------------------------
if st.session_state.reset_form:
    st.session_state.producto_nombre = ""
    st.session_state.producto_precio = 0.0
    st.session_state.producto_cantidad = 1
    st.session_state.es_alcohol = False
    st.session_state.reset_form = False
    st.rerun()

# ---------------------------------------------------------
# Formulario
# ---------------------------------------------------------
with st.form("producto_form"):
    producto_nombre = st.text_input("Ingrese el nombre del producto", key="producto_nombre")
    producto_precio = st.number_input("Ingrese el precio del producto", min_value=0.0, key="producto_precio")
    producto_cantidad = st.number_input("Ingrese la cantidad de productos", min_value=1, key="producto_cantidad")
    es_alcohol = st.checkbox("¿Es bebida alcohólica? (18% impuesto)", key="es_alcohol")

    col1, col2 = st.columns(2)
    with col1:
        subtotal_button = st.form_submit_button("Comprar producto")
    with col2:
        nuevo_button = st.form_submit_button("Nuevo producto")

# ---------------------------------------------------------
# Lógica de botones
# ---------------------------------------------------------
if nuevo_button:
    st.session_state.reset_form = True
    st.rerun()

if subtotal_button:
    calcular_subtotal(producto_nombre, producto_precio, producto_cantidad, es_alcohol)

# ---------------------------------------------------------
# Mostrar tabla
# ---------------------------------------------------------
st.dataframe(st.session_state.table_data)

# ---------------------------------------------------------
# Total general
# ---------------------------------------------------------
if st.button("Calcular Total a Pagar"):
    total = st.session_state.table_data["total_con_impuesto"].sum()
    st.subheader("El precio Total")
    st.write(f"El precio total es: {total}")
