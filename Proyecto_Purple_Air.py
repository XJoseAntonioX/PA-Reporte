import streamlit as st

API_PA = st.Page("API_PA/Peticion.py", title="Petición de datos")

AireLNL = st.Page("Downloads/AireNL.py", title="AireLNL")

PurpleAir = st.Page("Downloads/PurpleAir.py", title="Purple Air")

Emparejados = st.Page("Downloads/Emparejamiento.py", title="Emparejados")

Introduccion = st.Page("Documentacion/Introduccion.py", title="Introduccion")

Desarrollo = st.Page("Documentacion/Desarrollo.py", title="Desarrollo")

Resultados = st.Page("Documentacion/Resultados.py", title="Resultados")

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJlPz6XVM4qiGY_37VJA_ygvuli2WcyBTaoQ&s);
            background-repeat: no-repeat;
            padding-top: 220px;
            background-position: 50px 30px;
        },
        [data-testid="collapsedControl"] {
        display: none
    }
    </style>
    """,
    unsafe_allow_html=True,
)

pg = st.navigation(
        {
            "🟣 Purple Air API": [API_PA],
            "📄 Descarga de documentos": [AireLNL, PurpleAir, Emparejados],
            "📊 Documentación": [Introduccion, Desarrollo, Resultados],
        }
    )

pg.run()