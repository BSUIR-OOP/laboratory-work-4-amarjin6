class Transient():
    ...


if __name__ == '__main__':
    t1 = Transient()
    t2 = Transient()

    print(id(t1))
    print(id(t2))
