import random
def primary():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    a = random.randint(0, 16)
    print(quotes[a])
    b = -(random.randint(0, 16))
    print(quotes[b])


if __name__ == "__main__":
    primary()
