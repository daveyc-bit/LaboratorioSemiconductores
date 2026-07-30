import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

menu = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["Inicio", "Distribución de Fermi-Dirac", "Estructura de Bandas de Energía", "2do Estructura de Bandas de Energía", "Union PN"]
)
#Inicio
#______________________________________________________________________________________________________________________________________________

if menu == "Inicio":

    st.title("Laboratorio Virtual de Física de Semiconductores")

    st.markdown("""
    ## Bienvenido(a)

    El presente entorno computacional interactivo constituye una herramienta digital
    diseñada para facilitar la comprensión teórica y experimental de los dispositivos
    electrónicos de estado sólido. A través del modelado numérico y la visualización
    dinámica, la plataforma permite abordar la física de semiconductores desde una
    perspectiva intuitiva y cuantitativa.
    """)

    st.write("""
    El estudio de esta disciplina representa un pilar en la formación en ciencias e
    ingeniería; no obstante, el nivel de abstracción de sus fenómenos suele dificultar la
    asimilación de los conceptos teóricos por parte de los estudiantes. Este laboratorio
    digital responde a esa necesidad mediante tres módulos de simulación interactiva
    """)

    st.subheader("Módulos disponibles")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        **Estadística de Portadores**
        
        Modelado de la función de distribución de Fermi-Dirac y su dependencia térmica.

        """)

        st.info("""
        **Estructura de Bandas de Energía**

        Análisis de las propiedades intrínsecas y extrínsecas, desplazamiento del nivel de Fermi y concentración de portadores.
        """)

    with col2:
        st.info("""
        **Comportamiento de la Unión P-N**

        Simulación del perfil electrostático, la barrera de potencial, el doblamiento de bandas, y la caracterización de la corriente mediante la curva I-V ante polarización directa y polarización inversa.
        """)

    st.write("A través de estas herramientas de simulación, el laboratorio ofrece un recurso educativo accesible para reforzar la comprensión mediante la experimentación virtual interactiva.")
    st.success(
        "👈 Selecciona uno de los módulos en el menú lateral para comenzar la simulación."
    )
# Distribución de Fermi-Dirac
#______________________________________________________________________________________________________________________________________________

elif menu == "Distribución de Fermi-Dirac":

    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    st.set_page_config(layout="wide")

    st.title("Distribución de Fermi-Dirac")

    

    # Creación de columnas
    col1, col2, col3, col4 = st.columns([3,5,2,2])

    K_B = 8.617333e-5

    #-----------------------------
    # Controles
    #-----------------------------
    with col1:

        st.header("Controles")

        E_f = st.slider(
            "Nivel de Fermi (Ef)",
            min_value=0.0,
            max_value=1.12,
            value=0.56,
            step=0.01
        )

        E_min = st.sidebar.slider(
        "Energía mínima del gráfico (eV)",
        min_value=-2.0,
        max_value=0.0,
        value=-0.5,
        step=0.1
        )

        E_max = st.sidebar.slider(
        "Energía máxima del gráfico (eV)",
        min_value=0.5,
        max_value=3.0,
        value=1.6,
        step=0.1
        )

        temperaturas = [
            st.slider("Temperatura 1", 0.001, 1000.0, 1.0),
            st.slider("Temperatura 2", 0.001, 1000.0, 100.0),
            st.slider("Temperatura 3", 0.001, 1000.0, 200.0),
            st.slider("Temperatura 4", 0.001, 1000.0, 300.0)
        ]

    #-----------------------------
    # Energía
    #-----------------------------
    E = np.linspace(E_min, E_max, 1000)

    #-----------------------------
    # Función de Fermi-Dirac
    #-----------------------------
    def fermi(E, Ef, T):
        return 1 / (1 + np.exp((E - Ef) / (K_B * T)))

    #-----------------------------
    # Gráfica
    #-----------------------------
    with col2:

        st.header("Gráfica")

        fig, ax = plt.subplots(figsize=(8,5))

        for T in temperaturas:
            ax.plot(E, fermi(E, E_f, T), linewidth=2, label=f"T = {T:.1f} K")

        ax.axvline(E_f, color='black', linestyle='--', label='Ef')

        # Bandas de energía
        Eg = 1.12
        Ev = 0.0
        Ec = Ev + Eg

        ax.set_title("Distribución de Fermi-Dirac")
        ax.set_xlabel("Energía (eV)")
        ax.set_ylabel("f(E)")
        
        ax.axvspan(E_min, Ev, alpha=0.1, color="red", label="Banda de Valencia")
        ax.axvspan(Ev, Eg, alpha=0.1, color="gray", label="Banda Prohibida")
        ax.axvspan(Eg, E_max, alpha=0.1, color="green", label="Banda de Conducción")
        ax.axhline(0.5, linestyle=":", color="purple", linewidth=1.5,label="f(E) = 0.5")
        ax.grid(True)
        ax.legend()

        st.pyplot(fig)

    #-----------------------------
    # Mostrar temperaturas
    #-----------------------------
    columnas = [col3, col4]

    for i, T in enumerate(temperaturas):

        with columnas[i // 2]:

            if i == 0:
                st.header("Niveles")
                st.write(f"Nivel de Fermi = {E_f:.2f} eV")

            elif i == 2:
                st.divider()

            st.metric(f"Temperatura {i+1}", f"{T:.1f} K")

            if T < 273.15:
                st.success("Temperatura baja")
            elif T < 323.15:
                st.warning("Temperatura media")
            else:
                st.error("Temperatura alta")

    #-----------------------------
    # Explicación
    #-----------------------------
    st.write("En este apartado se calcula y representa gráficamente la función de distribución de Fermi-Dirac. Mediante los controles de temperatura se puede observar cómo cambia la probabilidad de ocupación de los niveles de energía.")

    st.latex(r"f(E)=\frac{1}{1+e^{\left(\frac{E-E_f}{kT}\right)}}")
    st.write("""
    Donde:

    - $E$ es la energía
    - $E_f$ es el nivel de Fermi
    - $k$ es la constante de Boltzmann
    - $T$ es la temperatura en Kelvin
    """)
    st.write("El eje horizontal corresponde a los niveles energéticos disponibles para los electrones.")
    st.write("El eje vertical representa la probabilidad de ocupación de cada nivel energético.")

    st.write(
        "La distribución de Fermi-Dirac describe cómo se distribuyen los electrones en un material. "
        "A bajas temperaturas la transición es muy abrupta alrededor del nivel de Fermi; al aumentar "
        "la temperatura, la transición se vuelve más suave debido a la excitación térmica de los electrones."
    )

    st.write(
        "Los indicadores de temperatura muestran mediante los colores verde, amarillo y rojo si la "
        "temperatura seleccionada es baja, media o alta."
    )

#Estructura de Bandas de Energía
#______________________________________________________________________________________________________________________________________________


elif menu == "Estructura de Bandas de Energía":

    import streamlit as st
    import matplotlib.pyplot as plt
    st.set_page_config(layout="wide")

    st.title("Simulador de Estructura de Bandas de Energía")


# Columnas
    col1, col2, col3 = st.columns([2,5,5])

# Materiales
    materiales = {
        "Silicio (Si)": {"Eg0": 1.17, "alpha": 4.73e-4, "beta": 636, "Ed":0.045, "Ea":0.045},
        "Germanio (Ge)": {"Eg0": 0.7437, "alpha": 4.77e-4, "beta": 235, "Ed":0.010, "Ea":0.010},
        "Arseniuro de Galio (GaAs)": {"Eg0": 1.519, "alpha": 5.41e-4, "beta": 204, "Ed":0.006, "Ea":0.030}
    }

# Controles
    with col1:

        material = st.selectbox(
            "Material semiconductor",
            list(materiales.keys())
        )

# Temperatura
        T = st.slider(
            "Temperatura (K)",
            min_value=0,
            max_value=600,
            value=300
        )

# Tipo de semiconductor
        tipo = st.radio(
            "Tipo de semiconductor",
            ["Intrínseco", "Tipo N", "Tipo P"]
        )

# Parámetros del material
        Eg0 = materiales[material]["Eg0"]
        alpha = materiales[material]["alpha"]
        beta = materiales[material]["beta"]

# Ecuación de Varshni
        Eg = Eg0 - (alpha*T**2)/(T+beta)

# Bandas
        Ev = 0.0
        Ec = Eg

# Nivel de Fermi
        if tipo == "Intrínseco":

            Ef = Eg / 2

        elif tipo == "Tipo N":

            distancia = st.slider(
                "Distancia entre el nivel de Fermi y la banda de valencia (eV)",
                0.01,
                0.56,
                0.05,
                0.01
            )

            Ef = Ec - distancia

        else:

            distancia = st.slider(
                "Distancia entre el nivel de Fermi y la banda de valencia (eV)",
                0.01,
                0.56,
                0.05,
                0.01
            )

            Ef = Ev + distancia

        # Mantener Ef dentro del gap
        Ef = np.clip(Ef, Ev + 0.01, Ec - 0.01)

        # ---------------------------------------------------------------------
        # Niveles donadores y aceptores
        # ---------------------------------------------------------------------

        Ed = Ec-materiales[material]["Ed"]
        Ea = Ev+materiales[material]["Ea"]

        # ---------------------------------------------------------------------
        # Información
        # ---------------------------------------------------------------------

        st.metric("Eg", f"{Eg:.3f} eV")
        st.metric("Ef", f"{Ef:.3f} eV")

    # =========================================================================
    # DIAGRAMA DE BANDAS
    # =========================================================================

    with col2:

        st.header("Diagrama de Bandas")

        fig, ax = plt.subplots(figsize=(6,6))

        # Banda de conducción
        ax.plot(
            [0.2,0.8],
            [Ec,Ec],
            linewidth=5,
            color="royalblue",
            label="Banda de conducción (Ec)"
        )

        # Banda de valencia
        ax.plot(
            [0.2,0.8],
            [Ev,Ev],
            linewidth=5,
            color="darkred",
            label="Banda de valencia (Ev)"
        )

        # Nivel de Fermi
        ax.plot(
            [0.2,0.8],
            [Ef,Ef],
            "--",
            color="green",
            linewidth=2,
            label="Nivel de Fermi (Ef)"
        )

        # Donadores
        if tipo == "Tipo N":

            ax.plot(
                [0.3,0.7],
                [Ed,Ed],
                color="purple",
                linewidth=2,
                label="Donadores (Ed)"
            )

        # Aceptores
        if tipo == "Tipo P":

            ax.plot(
                [0.3,0.7],
                [Ea,Ea],
                color="orange",
                linewidth=2,
                label="Aceptores (Ea)"
            )

        # Flecha Eg
        ax.annotate(
            "",
            xy=(0.5,Ec),
            xytext=(0.5,Ev),
            arrowprops=dict(arrowstyle="<->")
        )

        ax.text(
            0.53,
            Eg/2,
            f"Eg = {Eg:.3f} eV",
            fontsize=11
        )

        ax.fill_between([0.2,0.8], Ev, Ec, color="lightgray", alpha=0.35)

        # Etiquetas

        ax.text(0.82, Ec, "Ec", va="center")
        ax.text(0.82, Ev, "Ev", va="center")
        ax.text(0.82, Ef, "Ef", va="center")

        if tipo == "Tipo N":
            ax.text(0.82, Ed, "Ed", va="center")

        if tipo == "Tipo P":
            ax.text(0.82, Ea, "Ea", va="center")

        ax.set_xlim(0,1)
        ax.set_ylim(-1,2)

        ax.set_xticks([])
        ax.set_ylabel("Energía (eV)")
        ax.set_title(material)
        ax.legend()

        st.pyplot(fig)

    # =========================================================================
    # DISTRIBUCIÓN DE FERMI-DIRAC
    # =========================================================================

    with col3:

        st.header("Distribución de Fermi-Dirac")

        kB = 8.617333262e-5      # eV/K

        E = np.linspace(Ev-0.20, Ec+0.20, 1000)

        f = 1/(1+np.exp((E-Ef)/(kB*T)))

        fig2, ax2 = plt.subplots(figsize=(6,6))

        ax2.plot(
            f,
            E,
            color="darkblue",
            linewidth=2
        )

        # Ec
        ax2.axhline(
            Ec,
            linestyle=":",
            color="red",
            label="Banda de conducción (Ec)"
        )

        # Ev
        ax2.axhline(
            Ev,
            linestyle=":",
            color="brown",
            label="Banda de valencia (Ev)"
        )

        # Ef
        ax2.axhline(
            Ef,
            linestyle="--",
            color="green",
            label="Nivel de Fermi (Ef)"
        )

        # Línea en f(E)=0.5
        ax2.axvline(
            0.5,
            linestyle=":",
            color="purple",
            linewidth=1.5,
            label="f(E)=0.5"
        )

        ax2.set_xlim(-0.02, 1.02)
        ax2.set_ylim(Ev - 0.20, Ec + 0.20)

        ax2.set_xlabel("Probabilidad de ocupación, f(E)")
        ax2.set_ylabel("Energía (eV)")

        ax2.set_title(
            f"Distribución de Fermi-Dirac\nT = {T} K"
        )

        ax2.grid(alpha=0.3)

        ax2.legend()

        st.pyplot(fig2)

        #-----------------------------
        # Explicación
        #-----------------------------
    st.write(
            "En este apartado se calcula y representa gráficamente la estructura de bandas de energía de un "
            "semiconductor. Mediante los controles de material, temperatura y tipo de semiconductor se puede "
            "observar cómo varían la banda de conducción, la banda de valencia, el nivel de Fermi y el ancho "
            "de la banda prohibida."
        )

    st.latex(r"E_g(T)=E_{g0}-\frac{\alpha T^2}{T+\beta}")

    st.write("""
        Donde:

        - $E_g(T)$ es el ancho de la banda prohibida a la temperatura $T$
        - $E_{g0}$ es el ancho de banda a $0 K$
        - $α$ y $β$ son constantes características del material
        - $T$ es la temperatura en Kelvin
        """)

    st.info(
            f"""
    ### Parámetros del material seleccionado: **{material}**

    - **Ancho de banda a 0 K ($E_{{g0}}$):** {Eg0:.4f} eV
    - **Constante de Varshni ($α$):** {alpha:.3e} eV/K²
    - **Constante de Varshni ($β$):** {beta} K

    Estas constantes son características de cada semiconductor y determinan cómo cambia el ancho de la banda prohibida con la temperatura. Un valor mayor de **α** implica una variación más pronunciada de $E_g$, mientras que **β** controla la rapidez con la que dicha variación ocurre conforme aumenta la temperatura.
    """
        )

    st.write(
            "La banda de conducción ($E_c$) representa los niveles de energía donde los electrones pueden "
            "moverse libremente y contribuir a la conducción eléctrica."
        )

    st.write(
            "La banda de valencia ($E_v$) contiene los electrones enlazados a los átomos del cristal. "
            "Entre ambas bandas se encuentra la banda prohibida ($E_g$), una región donde no existen "
            "estados electrónicos permitidos."
        )

    st.write(
            "El nivel de Fermi ($E_f$) indica el nivel de energía con una probabilidad de ocupación del 50 %. "
            "Su posición depende del tipo de semiconductor: en un material intrínseco se localiza aproximadamente "
            "en el centro de la banda prohibida; en un semiconductor tipo N se desplaza hacia la banda de conducción, "
            "mientras que en un semiconductor tipo P se acerca a la banda de valencia."
        )

    st.write(
            "En los semiconductores dopados también pueden observarse los niveles donadores ($E_d$) y aceptores "
            "($E_a$), asociados a las impurezas introducidas para modificar las propiedades eléctricas del material."
        )

    st.write(
            "Al aumentar la temperatura, el ancho de la banda prohibida disminuye de acuerdo con la ecuación de "
            "Varshni, facilitando la excitación de electrones desde la banda de valencia hacia la banda de conducción."
        )

    st.write(
            "Los indicadores muestran el valor actualizado del ancho de la banda prohibida ($E_g$) y la posición "
            "del nivel de Fermi ($E_f$), permitiendo visualizar el efecto de la temperatura y del dopaje sobre la "
            "estructura electrónica del semiconductor."
        )

#2da Estructura de Bandas de Energía
#______________________________________________________________________________________________________________________________________________


elif menu == "2do Estructura de Bandas de Energía":

    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt

    st.set_page_config(layout="wide")

    st.title("Fermi-Dirac con Dopaje")

    col1, col2 = st.columns([3,5])


    with col1:  

# CONTROLES
        dopaje = st.selectbox(
            "Tipo de dopaje",
            ["Intrínseco", "Tipo N", "Tipo P"]
        )

        if dopaje != "Intrínseco":

            exp_dopaje = st.slider(
                "Concentración de dopaje (10ˣ cm⁻³)",
                min_value=0,
                max_value=20,
                value=16
            )

            Nd = 10**exp_dopaje

            st.write(f"Concentración de dopaje = {Nd:.2e} cm⁻³")

        else:

            Nd = None

            st.info(
                "Semiconductor intrínseco: no existen impurezas dopantes.\n"
                "El nivel de Fermi depende únicamente del material y la temperatura."
            )

        T = st.slider("Temperatura",1.0,500.0,300.0)

# NIVELES DE ENERGÍA

        Ec = 1.8 #¿Para cuál material?
        Ev = 0.2 

# Nivel de Fermi según dopaje y concentración
        if dopaje == "Intrínseco":
            E_f = 1.0

        elif dopaje == "Tipo N":
# Entre 1.1 y 1.6 eV aproximadamente
            E_f = 1.0 + 0.5*(exp_dopaje-0)/(20-0) 

        elif dopaje == "Tipo P":
# Entre 0.9 y 0.4 eV aproximadamente
            E_f = 1.0 - 0.5*(exp_dopaje-0)/(20-0)

# ECUACIÓN FERMI-DIRAC
    kB = 8.617e-5

    E = np.linspace(0,2,1000)

    f = 1/(1+np.exp((E-E_f)/(kB*T)))

# GRÁFICA

    with col2:

        fig, ax = plt.subplots(figsize=(8,5))


# CURVA FERMI-DIRAC GIRADA

        ax.plot(f, E,
                linewidth=3,
                label="Fermi-Dirac")

# NIVELES DE ENERGÍA

        Ec = 1.8
        Ev = 0.2

# Banda de conducción
        ax.axhline(Ec,
                color='black',
                linewidth=3)

# Banda de valencia
        ax.axhline(Ev,
                color='black',
                linewidth=3)

# Nivel de Fermi
        ax.axhline(E_f,
                color='red',
                linestyle='--',
                linewidth=3,
                label='Ef')

# BANDA PROHIBIDA
        ax.axhspan(
            Ev,
            Ec,
            color='gray',
            alpha=0.2
        )

# ETIQUETAS

        ax.text(
            0.7,
            Ec + 0.03,
            "Banda de conducción",
        )

        ax.text(
            0.7,
            Ev - 0.08,
            "Banda de valencia",
        )

        ax.text(
            0.7,
            (Ec + Ev)/2,
            "Banda prohibida",
        )

# CONFIGURACIÓN

        ax.set_ylabel("Energía (E)")

        ax.set_xlabel("f(E)")

        ax.set_title(f"Dopaje: {dopaje}")

        ax.grid(True)

        ax.legend()

        st.pyplot(fig)

    # ------------------------------------------------------------------
    # Explicación Física
    # ------------------------------------------------------------------

    st.markdown("---")

    st.subheader("Explicación Física")

    st.write("""
    La distribución de **Fermi-Dirac** describe la probabilidad de que un estado
    de energía esté ocupado por un electrón a una temperatura determinada.

    El nivel de Fermi (**Ef**) representa la energía para la cual la probabilidad
    de ocupación es del **50 %**, es decir:
    """)

    st.latex(r"f(E_F)=0.5")

    st.write("""
    La posición del nivel de Fermi depende del tipo de semiconductor y de la
    concentración de impurezas dopantes.
    """)

    if dopaje == "Intrínseco":

        st.info("""
    **Semiconductor intrínseco**

    - No existen impurezas dopantes.
    - El número de electrones es igual al número de huecos.
    - El nivel de Fermi permanece aproximadamente en el centro de la banda prohibida.
    - La temperatura modifica la forma de la distribución de Fermi-Dirac, haciendo
    más gradual la transición entre estados ocupados y desocupados.
    """)

    elif dopaje == "Tipo N":

        st.info(f"""
    **Semiconductor tipo N**

    - Se agregan átomos donadores con una concentración aproximada de **{Nd:.2e} cm⁻³**.
    - Los donadores aportan electrones libres.
    - El nivel de Fermi se desplaza hacia la banda de conducción.
    - Conforme aumenta la concentración de dopaje, la probabilidad de encontrar
    electrones cerca de la banda de conducción también aumenta.
    """)

    elif dopaje == "Tipo P":

        st.info(f"""
    **Semiconductor tipo P**

    - Se agregan átomos aceptores con una concentración aproximada de **{Nd:.2e} cm⁻³**.
    - Los aceptores generan huecos en la banda de valencia.
    - El nivel de Fermi se desplaza hacia la banda de valencia.
    - Conforme aumenta la concentración de dopaje, disminuye la probabilidad de
    ocupación de estados cercanos a la banda de valencia, aumentando la cantidad de huecos.
    """)

    st.success("""
    **Interpretación de la gráfica**

    - La línea roja punteada representa el **nivel de Fermi (Ef)**.
    - Las líneas negras corresponden a los bordes de la **banda de conducción** y
    la **banda de valencia**.
    - La región sombreada representa la **banda prohibida**, donde no existen
    estados electrónicos permitidos.
    - La curva azul muestra la probabilidad de ocupación de cada nivel de energía.
    - A temperaturas bajas la transición es muy abrupta; conforme la temperatura
    aumenta, la curva se vuelve más suave debido al incremento de la energía térmica.
    """)

elif menu == "Union PN":
        import streamlit as st
        import numpy as np
        import matplotlib.pyplot as plt

        # Configuración y Constantes
        st.set_page_config(page_title="PN Master: Zoom Dinámico", layout="wide")
        ni, eg = 1.0e10, 1.12
        eps_si = 11.7 * 8.854e-14
        kb_t, q_elec = 0.0259, 1.602e-19
        area, Dp, Dn, Lp, Ln = 1e-4, 12, 35, 1e-3, 1e-3

        st.sidebar.header("Parámetros de la Unión PN")

        # Concentración de aceptores
        na = st.sidebar.number_input(
            "Concentración de aceptores Na (cm⁻³)",
            min_value=1.0e14,
            max_value=1.0e19,
            value=5.0e16,
            step=1.0e15,
            format="%.2e",
            help="Concentración de dopado tipo P."
        )

        # Concentración de donadores
        nd = st.sidebar.number_input(
            "Concentración de donadores Nd (cm⁻³)",
            min_value=1.0e14,
            max_value=1.0e19,
            value=5.0e16,
            step=1.0e15,
            format="%.2e",
            help="Concentración de dopado tipo N."
        )

        # Voltaje aplicado
        v_ext = st.sidebar.slider(
            "Voltaje aplicado (V)",
            min_value=-5.0,
            max_value=0.80,
            value=0.00,
            step=0.01,
            help="Polarización externa de la unión PN."
        )

        # Cálculos Físicos
        phi_p, phi_n = kb_t * np.log(na / ni), -kb_t * np.log(nd / ni)
        v_bi = abs(phi_p) + abs(phi_n)
        v_total = v_bi - v_ext
        w = np.sqrt((2 * eps_si * v_total / q_elec) * (1/na + 1/nd))
        xp, xn = (w * nd) / (na + nd), (w * na) / (na + nd)
        v_p, v_n = v_total * (nd / (na + nd)), v_total * (na / (na + nd))

        is_current = area * q_elec * (ni**2) * ((Dp / (Lp * nd)) + (Dn / (Ln * na)))
        i_actual = is_current * (np.exp(v_ext / kb_t) - 1)

        # Gráficas
        col1, col2 = st.columns(2)

        with col1:
            # Diagrama de bandas
            st.subheader("Diagrama de Bandas de Energía")
            x_pts = np.linspace(-xp*2.5, xn*2.5, 1000)
            ei = [phi_p if val <= -xp else (phi_p - v_total if val >= xn else 
                (phi_p - v_p * ((val + xp) / xp)**2 if val < 0 else 
                (phi_p - v_p) - v_n * (1 - (1 - val / xn)**2))) for val in x_pts]
            ei = np.array(ei)
            fig_b, ax_b = plt.subplots()
            ax_b.plot(x_pts*1e4, ei+eg/2, color="darkblue", label="Ec")
            ax_b.plot(x_pts*1e4, ei-eg/2, color="darkred", label="Ev")
            ax_b.hlines([0, v_ext], [x_pts[0]*1e4, 0], [0, x_pts[-1]*1e4], colors=['g','darkgreen'], ls='--')
            ax_b.set_title("Diagrama de Bandas")
            ax_b.set_xlabel("Posición (µm)")
            ax_b.set_ylabel("Energía (eV)")
            ax_b.grid(alpha=0.2)
            st.pyplot(fig_b)

        with col2:
            st.subheader("Curva Característica I-V")
            
            # Lógica de Zoom Dinámico
            if v_ext >= 0:
                v_min_p, v_max_p = -0.1, 0.8
                y_lims = (-is_current*2, is_current * (np.exp(0.7 / kb_t)))
                msg = "Modo: Directa (Zoom)"
            elif v_ext > -1.0:
                # ZOOM EN EL ORIGEN (LADO NEGATIVO)
                v_min_p, v_max_p = -1.0, 0.2
                y_lims = (-is_current * 1.5, is_current * 5)
                msg = "Modo: Inversa Cercana (Zoom al origen)"
            else:
                # VISTA PANORÁMICA INVERSA
                v_min_p, v_max_p = -16.0, 1.0
                y_lims = (-is_current * 5, is_current * 20)
                msg = "Modo: Inversa Profunda"

            st.caption(msg)
            v_range = np.linspace(v_min_p, v_max_p, 1000)
            i_range = is_current * (np.exp(v_range / kb_t) - 1)
            
            fig_iv, ax_iv = plt.subplots()
            ax_iv.plot(v_range, i_range, color='purple', lw=2)
            ax_iv.scatter(v_ext, i_actual, color='red', s=80, zorder=5)
            
            ax_iv.set_xlim(v_min_p, v_max_p)
            ax_iv.set_ylim(y_lims)
            ax_iv.axhline(0, color='black', lw=1)
            ax_iv.axvline(0, color='black', lw=1)
            ax_iv.set_xlabel("Voltaje (V)")
            ax_iv.set_ylabel("Corriente (A)")
            ax_iv.grid(True, alpha=0.2)
            st.pyplot(fig_iv)

        # Métricas rápidas
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("Vbi", f"{v_bi:.3f} V")
        c2.metric("W", f"{w*1e4:.3f} µm")
        c3.metric("I Actual", f"{i_actual:.2e} A")


        # EXPLICACIÓN FÍSICA

        st.divider()
        st.subheader("Interpretación Física")

        if abs(v_ext) < 1e-3:

            st.info(f"""
        ### Unión PN en equilibrio

        - No existe una fuente de voltaje externa.
        - La difusión inicial de electrones y huecos genera una **región de agotamiento**.
        - El campo eléctrico interno equilibra la difusión de portadores.
        - El **nivel de Fermi permanece constante** en todo el semiconductor, indicando equilibrio térmico.
        - El potencial interno es **Vbi = {v_bi:.3f} V**.
        - El ancho de la región de agotamiento es **W = {w*1e4:.2f} μm**.
        """)

        elif v_ext > 0:

            st.success(f"""
        ### Polarización directa

        - Se aplica un voltaje positivo al lado P.
        - La barrera de potencial disminuye de **{v_bi:.3f} V** a **{v_total:.3f} V**.
        - La región de agotamiento se hace más estrecha.
        - Los electrones del lado N y los huecos del lado P atraviesan la unión con mayor facilidad.
        - La corriente aumenta aproximadamente de forma exponencial según la ecuación de Shockley.
        - Aparecen dos **cuasi niveles de Fermi**, separados aproximadamente por el voltaje aplicado.
        """)

        else:

            st.warning(f"""
        ### Polarización inversa

        - Se aplica un voltaje negativo al lado P.
        - La barrera aumenta hasta **{v_total:.3f} V**.
        - La región de agotamiento se ensancha.
        - Los portadores mayoritarios son alejados de la unión.
        - La corriente permanece cercana a la corriente de saturación **Is**, hasta acercarse a la región de ruptura (no modelada completamente en esta simulación).
        """)