
# на данном этапе функция собирает список папок из корневого каталога "main_folder".
# После чего проходит по каждой папке и оптимизирует все изображения находящиеся в ней.
# Все оптимизированные изображения отправляются в папку opt в каждой папке отдельно

# нужно доработать так чтобы чтобы проверял папки 2 уровня и выше
from PIL import Image
import os
import sys
from progress.bar import Bar
import time

# Здесь прописываем путь до основной папки
main_folder = r'/Users/aleksejdementev/Documents/Оптимизация фото'



# создание папки
def create_folder(workspace, folder):
    path = os.path.join(workspace, folder)
    if not os.path.exists(path):
        os.makedirs(path)
        print (f"Папка {folder} создана")
    else:
        print (f"Папка {folder} существует")




# Получаем список папок в основном каталоге
def lokkig_folder(main_folder_):
    main_folder_name = main_folder_
    with os.scandir(main_folder_name) as files:
        global subdir
        subdir = [file.name for file in files if file.is_dir()]
        return subdir




# Получаем список папок в основном каталоге


def optimized_img():

    # запускаем обход корневого каталога main_folder
    for current_folder in subdir:

        #Вывод имени папки для тестов
        print(f"Имя папки: {current_folder}")

        image_path = main_folder + '/' + current_folder + '/'
        # Сканируем папку на наличе в ней изображений и собираем их в список
        unopt_images = [file for file in os.listdir(image_path) if file.endswith(('jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'heic', 'PNG'))]
        print(f'Список фото : {unopt_images}')


        if len(unopt_images) != 0:
            # создаем подкаталог в каталоге opt
            path_to_opt = main_folder + "-opt/"
            create_folder(path_to_opt, current_folder)
            print(path_to_opt+current_folder)



        for images in unopt_images:
            image_loc = images



            # создаем имя файла
            image_name_log = image_loc
            image_name = os.path.splitext(image_name_log)[0]

            # получаем данные по файлу
            image = Image.open(image_path + image_loc)

            # определяем соотношение сторон
            width = image.size[0]
            height = image.size[1]
            ratio = width / height


            #изменяем размеры изображения и помещаем в папку opt   (!!!Нужно доработать соотношение сторон)
            def resize_800():
                image800 = image.resize((800,800), resample=1)
                new_image_path = main_folder + current_folder+ '/opt/'
                new_image_loc = image_name + '-800.jpg'
                image800.save(new_image_path + new_image_loc)
                return
            # resize_800()


            #изменяем размеры изображения и помещаем в папку opt
            def resize_1920():
                max_height = 1000 #ТУТ устанавливаем высоту фото. на основании ее по соотношению строн высчиывается ширина
                new_width = int(max_height * ratio)
                image1920 = image.resize((new_width,max_height), resample=1)
                new_image_path = path_to_opt + current_folder
                new_image_loc = image_name + '.jpg'
                path_new_file = new_image_path + '/' +new_image_loc
                if not os.path.exists(path_new_file):
                    rgb_im = image1920.convert('RGB') #тут происходит конвертация in RGB чтобы сохранить в png to jpg
                    rgb_im.save(new_image_path + "/" + new_image_loc, optimize=True, quality=95)
                    print(f'Файл создан >>>>>>>>> {new_image_loc}')
                else:
                    print(f'Файл {new_image_loc} существует')

            resize_1920()


        
        print(f"Обработка папки {current_folder} завершена")




def main():
    # Создаем папку Opt в основной директории

    lokkig_folder(main_folder)
    # create_folder(main_folder, "opt")
    optimized_img()
    print('╋╋┏┓')
    print('╋╋┃┃')
    print('┏━┛┃┏━━┓┏━┓╋┏━━┓')
    print('┃┏┓┃┃┏┓┃┃┏┓┓┃┃━┫')
    print('┃┗┛┃┃┗┛┃┃┃┃┃┃┃━┫')
    print('┗━━┛┗━━┛┗┛┗┛┗━━┛')

if __name__ == '__main__':
    main()




