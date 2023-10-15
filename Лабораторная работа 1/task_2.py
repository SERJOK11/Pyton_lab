# TODO Найдите количество книг, которое можно разместить на дискете
volume_floppy = 1.44
count_page = 100
count_row = 50
count_char = 25
BYTE_CHAR = 4

volume_book = BYTE_CHAR * count_char * count_row * count_page
volume_floppy = volume_floppy * (1024**2)

count = int(volume_floppy // volume_book)

print("Количество книг, помещающихся на дискету:", count)

