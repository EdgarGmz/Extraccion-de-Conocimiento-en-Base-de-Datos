import cv2
from matplotlib import pyplot as plt


def show_or_save(output_name):
    backend = plt.get_backend().lower()
    if 'agg' in backend:
        plt.savefig(output_name, dpi=150, bbox_inches='tight')
        print(f"Grafica guardada en: {output_name}")
        plt.close()
    else:
        plt.show()


def plot_histogram(img, title, color='grey', equalize=False):
    """
    Funcion para calcular y graficar el histograma de una imagen
    
    Parametros:
        img(numpy.ndarray): La imagen en escala de grises o color.
        title(str): Titulo para el grafico.
        color(str o tuple): Color de histograma. Para imagenes en color, se usa ('b', 'g', 'r').
        equalize(bool): Si es True, se aplica ecualizacion del histograma.

    """

    if equalize:
        if len(img.shape) == 2:
            img = cv2.equalizeHist(img) # Ecualizar el histograma en grises
        else:
            # Ecualizacion por canal para imagenes en color
            canales = cv2.split(img)
            img = cv2.merge([cv2.equalizeHist(canal) for canal in canales])

    if len(img.shape) == 2: # Si la imagen es en escalas grises
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
    else: # Si la imagen es en color
        for i, c in enumerate(color):
            hist = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(hist, color=c)
            plt.xlim([0, 256])

    plt.title(title)
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    output_name = f"{title.lower().replace(' ', '_')}.png"
    show_or_save(output_name)

    
def main():
    # Cargar las imagenes
    img1 = cv2.imread('image1.jpeg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('image2.jpeg', cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread('image3.jpeg')

    # Verificar si las imagenes se cargaron correctamente
    if img1 is None or img2 is None or img3 is None:
        print("Error: No se pudo cargar una o mas imagenes.")
        return
    
    # Mostrar las imagenes usando Matplotlib para evitar dependencias GUI de OpenCV/Qt
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(img1, cmap='gray')
    plt.title('Imagen 1 - Escala de Grises')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.equalizeHist(img2), cmap='gray')
    plt.title('Imagen 2 - Escala de Grises Ecualizada')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
    plt.title('Imagen 3 - Color')
    plt.axis('off')
    plt.tight_layout()
    show_or_save('imagenes_originales.png')
    
    # Graficar los histogramas
    plot_histogram(img1, 'Histograma de Imagen 1', color='grey')
    plot_histogram(img2, 'Histograma de Imagen 2', color='grey', equalize=True)
    plot_histogram(img3, 'Histograma de Imagen 3', color=('b', 'g', 'r'))

if __name__ == "__main__":
    main()