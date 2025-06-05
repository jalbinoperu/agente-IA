import streamlit as st
from docx import Document
from io import BytesIO

st.title("🤖 Asistente Pedagógico IA")
st.subheader("Generador de Sesiones de Aprendizaje (MVP)")

nombre = st.text_input("👩‍🏫 Nombre del docente")
colegio = st.text_input("🏫 Nombre del colegio")
grado = st.selectbox("📚 Grado", ["1°", "2°", "3°", "4°", "5°"])
competencia = st.text_area("🧠 Competencia")

if st.button("Generar sesión"):
    doc = Document()
    doc.add_heading('SESIÓN DE APRENDIZAJE', 0)

    doc.add_heading('Datos Generales', level=1)
    doc.add_paragraph(f'Docente: {nombre}')
    doc.add_paragraph(f'Institución Educativa: {colegio}')
    doc.add_paragraph(f'Grado: {grado}')
    doc.add_paragraph(f'Área: Ciencia y Tecnología')
    doc.add_paragraph(f'Competencia: {competencia}')

    doc.add_heading('Actividades', level=1)
    doc.add_paragraph("Inicio: Pregunta detonante y activación de saberes previos.")
    doc.add_paragraph("Desarrollo: Trabajo en equipo con experimentos simples.")
    doc.add_paragraph("Cierre: Conclusiones y reflexión guiada.")

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.success("✅ Sesión generada con éxito.")
    st.download_button("📥 Descargar Sesión Word", data=buffer, file_name="sesion_aprendizaje.docx")
