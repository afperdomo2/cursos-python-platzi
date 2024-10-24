path = "./file.txt"

# r = read, w = write, a = append, r+ = read and write
with open(path, "r+") as file:
    for line in file:
        print(line)
    # Escribe en el archivo
    file.write("\nHello World")
