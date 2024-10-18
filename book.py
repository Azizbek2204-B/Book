class Book:
    def __init__(self, id, name, author, count, price):
        self.id = id
        self.name = name
        self.author = author
        self.count = count
        self.price = price

    def kitob_yozish(self):
        with open("Book.txt", "a") as f:
            f.write(f"{self.id},{self.name},{self.author},{self.count},{self.price}\n")

    def kitob_ochirish(self, id_to_remove):
        with open("Book.txt", "r") as f:
            lines = f.readlines()
        with open("Book.txt", "w") as f:
            for line in lines:
                id_ = line.split(',')[0]
                if id_ != str(id_to_remove):
                    f.write(line)

while True:
    print("1. Kitob yozish\n2. Kitoblarni o'chirish\n3. Chiqish")
    a = int(input("Tanlovingiz: "))

    if a == 1:
        b = Book(
            int(input("Id: ")),
            input("Name: "),
            input("Author: "),
            int(input("Nechta: ")),
            int(input("Price: "))
        )
        b.kitob_yozish()

    elif a == 2:
        x = int(input("O'chiriladigan kitob ID sini kiriting: "))
        b = Book(0, "", "", 0, 0)
        b.kitob_ochirish(x)
        print("Kitob o'chirildi.")

    elif a == 3:
        print("Chiqish...")
        break

    else:
        print("Noto'g'ri tanlov!")
        break