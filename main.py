import os
import shutil


dir = "./Musics"
counter = 0
final_data = ""


def mk_metadata(filename):
    global final_data
    
    data = '''
"<counter>" : {
    "Title" : "<filename>"
},
'''
    data = data.replace("<counter>", str(counter))
    data = data.replace("<filename>", filename)

    final_data += data

    return data


def main():
    global counter
    for (root, directories, files) in os.walk(dir):
        for file in files:
            counter += 1
            mk_metadata(file)
            os.mkdir(f"Data/{counter}")
            shutil.move(os.path.join(root, file), f"./Data/{counter}")
            os.rename(f"Data/{counter}/{file}", f"Data/{counter}/musics.mp3")
    
    files = open("./Data/metadata.js", 'w+')
    files.write(f"const max_music = {counter}\n\n" + "const metadata = {\n" + final_data + "\n}")
    files.close()
    
    return


if __name__ == '__main__':
    main()