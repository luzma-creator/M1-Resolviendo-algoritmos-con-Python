from PIL import Image

def recortar_por_relacion_aspecto(imagen_path, ancho_deseado, alto_deseado, output_path):
    """Recorta una imagen para que se ajuste a la relación de aspecto deseada."""
    with Image.open(imagen_path) as img:
        # Obtener dimensiones de la imagen original
        ancho_original, alto_original = img.size

        # Calcular la relación de aspecto deseada
        ratio_deseado = ancho_deseado / alto_deseado

        # Calcular la relación de aspecto de la imagen original
        ratio_original = ancho_original / alto_original

        if ratio_original > ratio_deseado:
            # La imagen es más ancha que la deseada
            nuevo_ancho = int(alto_deseado * ratio_original)
            nuevo_alto = alto_deseado
        else:
            # La imagen es más alta que la deseada
            nuevo_ancho = ancho_deseado
            nuevo_alto = int(ancho_deseado / ratio_original)

        # Calcular recorte
        left = (ancho_original - nuevo_ancho) / 2
        top = (alto_original - nuevo_alto) / 2
        right = (ancho_original + nuevo_ancho) / 2
        bottom = (alto_original + nuevo_alto) / 2

        # Realizar el recorte
        img_cortada = img.crop((left, top, right, bottom))
        img_cortada = img_cortada.resize((ancho_deseado, alto_deseado), Image.ANTIALIAS)

        # Guardar la imagen recortada
        img_cortada.save(output_path)
        print(f"Imagen recortada guardada en {output_path}")
\
# Ejemplo de uso
imagen_path = input("Ingresa la ruta de la imagen: ")
ancho_deseado = int(input("Ingresa el ancho deseado para el recorte: "))
alto_deseado = int(input("Ingresa el alto deseado para el recorte: "))
output_path = input("Ingresa la ruta de salida para la imagen recortada: ")
recortar_por_relacion_aspecto(imagen_path, ancho_deseado, alto_deseado, output_path)

