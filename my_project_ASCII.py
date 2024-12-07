# Импортируем библиотеку для рпботы с изображениями
from PIL import Image

# Открываем изображение и преобразуем в оттенки серого
image = Image.open(r"C:\Users\renax\OneDrive\Pictures\My_pro_ASCII\Mona_Lisa.jpg").convert("L")

# Масштабируем изображение
new_width = 300
new_height = int(new_width * image.size[1] / image.size[0] * 0.5)
optimal_size_image = image.resize((new_width, new_height))

# Определяем ASCII-шкалу
ascii_simbols = "@%$#*+=-:. "

# Преобразуем изображение в ASCII-графику
def image_in_ascii(optimal_size_image, ascii_simbols):
    width, height = optimal_size_image.size
    pixels = optimal_size_image.load()
    result = ""

    for y in range(height):
        line = ""
        for x in range(width):
            light = pixels[x, y]
            index = int(light / 256 * len(ascii_simbols))
            one_simbol = ascii_simbols[min(index, len(ascii_simbols) - 1)]
            line += one_simbol
        result += line + "\n"
    return result

# Пример использования
if __name__ == "__main__":
    ascii_graphics = image_in_ascii(optimal_size_image, ascii_simbols)
    print(ascii_graphics)
    with open("ascii_art.txt", "w", encoding="utf-8") as result_image:
        result_image.write(ascii_graphics)
