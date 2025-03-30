from reportlab.lib.pagesizes import A4  # Tamaño de la página
from reportlab.pdfgen import canvas  # Generación del PDF
from reportlab.lib.colors import black, blue  # Colores de texto
from reportlab.pdfbase import pdfmetrics  # Métricas de fuente
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch

class DiplomasAlumnos:
    def __init__(self, output_path):
        self.output_path = output_path  # Ruta de salida del PDF
        self.titulo_universidad = "UNIVERSIDAD TECNOLÓGICA NACIONAL"
        self.titulo_instituto = "Instituto General San Martín"
        self.texto_diploma = "El alumno {0} ha finalizado la Diplomatura en Desarrollo de Software exitosamente con un promedio de {1}."

    def generar_diploma(self, nombre, promedio):
        c = canvas.Canvas(self.output_path, pagesize=A4)
        width, height = A4  # Dimensiones de la página

        # Título de la universidad
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(blue)
        c.drawCentredString(width / 2, height - 100, self.titulo_universidad)

        # Título del instituto
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(black)
        c.drawCentredString(width / 2, height - 140, self.titulo_instituto)

        # Línea decorativa
        c.line(50, height - 150, width - 50, height - 150)

        # Texto central del diploma
        c.setFont("Helvetica", 14)
        texto = self.texto_diploma.format(nombre, promedio)

        # Ajustar y centrar el texto dentro de un área específica
        self._draw_text_wrapped(c, texto, width / 2, height / 2, line_height=20)

        # Guardar el PDF con el nombre del alumno
        c.showPage()
        c.save()

        print(f"Diploma generado en: {self.output_path}")

    def _draw_text_wrapped(self, c, text, x, y, max_width=A4[0] - 100, line_height=20):
        """
        Dibuja el texto centrado y ajustado en múltiples líneas si es necesario.
        """
        lines = self._wrap_text(text, max_width)
        start_y = y + (len(lines) * line_height) / 2  # Centrar verticalmente

        for line in lines:
            c.drawCentredString(x, start_y, line)  # Texto centrado
            start_y -= line_height  # Moverse hacia abajo

    def _wrap_text(self, text, max_width):
        """
        Divide el texto en líneas que no excedan el ancho máximo permitido.
        """
        words = text.split()
        lines = []
        current_line = words[0]

        for word in words[1:]:
            test_line = current_line + " " + word
            width = pdfmetrics.stringWidth(test_line, "Helvetica", 14)

            if width < max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        return lines


# Lista de alumnos
alumnos = [
    ("Juan Pérez", 9.5),
    ("María Gómez", 8.7),
    ("Carlos López", 7.9),
]

# Generar diplomas para cada alumno
for nombre_alumno, promedio in alumnos:
    ruta_salida = f"./diploma_{nombre_alumno.replace(' ', '_')}.pdf"
    diploma = DiplomasAlumnos(ruta_salida)
    diploma.generar_diploma(nombre_alumno, promedio)
