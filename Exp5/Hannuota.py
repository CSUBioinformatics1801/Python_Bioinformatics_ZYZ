class Piece:
    def __init__(self, m, pillar):
        self.m = m
        self.pillar = pillar
        self.pillar.pull(self)

    def set_pillar(self, pillar):  # Set Pillar
        print(f"Move '{self.m}' from {self.pillar.name} to {pillar.name}")
        self.pillar.push(self)
        self.pillar = pillar
        self.pillar.pull(self)

    @staticmethod
    def make(n, pillar):
        for i in range(n):
            Piece(n - i, pillar)
        return

    def __str__(self):
        return str(self.m)

    def __repr__(self):
        return self.__str__()

class Pillar:
    def __init__(self, name):
        self.piece_list = []
        self.name = name

    def pull(self, new):
        if not self.piece_list:
            self.piece_list.append(new)
        elif self.piece_list[-1].m > new.m:
            self.piece_list.append(new)
        else:
            print(f"ERROR from pull: {self.piece_list[-1].m, new.m}")
            raise ValueError

    def push(self, new):
        if self.piece_list[-1] == new:
            self.piece_list.pop()
        else:
            print(f"ERROR from push: {self.piece_list, new}")
            raise ValueError

    def __str__(self):
        return str(self.piece_list)

    def __repr__(self):
        return self.__str__()


def __main__(from_list, from_, to_:Pillar, middle_:Pillar):
    step = 0
    from_list = tuple(from_list)  # Prevent from being edited

    if len(from_list) == 0:
        pass
    else:
        step += __main__(from_list[1:], from_, middle_, to_)
        piece = from_list[0]
        piece.set_pillar(to_)
        step += 1
        print_pillar()
        step += __main__(from_list[1:], middle_, to_, from_)
    return step


def print_pillar(message=""):
    print(message, end="")
    print(f"a_pillar: {a_pillar}")
    print(f"b_pillar: {b_pillar}")
    print(f"c_pillar: {c_pillar}")
    print("*" * 10)


if __name__ == "__main__":
    a_pillar = Pillar("a")
    b_pillar = Pillar("b")
    c_pillar = Pillar("c")
    try:
        Piece.make(int(input("Enter an number: ")), a_pillar)
    except ValueError:
        print("Sorry, you should give me an number.")
        Piece.make(3, a_pillar)  # default

    print_pillar("---start---\n")

    try:
        step = __main__(a_pillar.piece_list, a_pillar, c_pillar, b_pillar)
    except ValueError:
        print("Sorry There are some mistake")
    else:
        print_pillar("---end---\n")
        print(f"step: {step}")