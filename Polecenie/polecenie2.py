import os

verbose = True


class RenameFile:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        if verbose:
            print(f"[renaming '{self.src}' to '{self.dest}']")
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print(f"[renaming '{self.dest}' back to '{self.src}']")
        os.rename(self.dest, self.src)


def delete_file(path):
    if os.path.exists(path):                                 #4.3.2 dodanie funkcji os.path.exists()
        if verbose:
            print(f"deleting file {path}")
        os.remove(path)
    else:
        print('Nie ma takiej ścieżki')


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, mode='w+', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print(f"[reading file '{self.path}']")
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


# def check():
#     if 1 < 0:
#         return false

def main():
    orig_name, new_name = 'file1', 'file2'

    commands = (CreateFile(orig_name),
                ReadFile(orig_name),
                RenameFile(orig_name, new_name))

    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n] ')

    if answer not in 'yY':
        print(f"the result is {new_name}")
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print("Error", str(e))


if __name__ == '__main__':
    main()

# 4.3.2 Zadanie 2
# Jeśli spróbujemy zmienić nazwę pliku, który nie istnieje wyskakuje błąd. Możemy to naprawić sprawdzając wcześniej
# czy plik istnieje.
# Nie można zmienić nazwy plików, do których nie mamy odpowiednich uprawnień.