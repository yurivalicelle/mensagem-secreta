import os

def rename_files():
    file_list = os.listdir("./mensagem")
    saved_path = os.getcwd()
    os.chdir("./mensagem")

    translation_table = str.maketrans("0123456789", "          ", "0123456789")
    for file_name in file_list:
        print("Nome Antigo - "+file_name)
        print("Novo Nome - "+file_name.translate(translation_table))
        os.rename(file_name, file_name.translate(translation_table))
    os.chdir(saved_path)

rename_files()
