import difflib as df
import json as j

data = j.load(open("data.json", "r"))
data_keys = data.keys()


def word(w):
    word1 = w.lower()
    if word1 in data:
        return data[word1]


def f_match(match):
    return match


def main():
    word1 = input("Enter word : ")
    print(word(word1))

    def match():
        match1 = df.get_close_matches(word1, data_keys)
        f_match(match1)
        if match1[0] in data:
            print(data[match1[0]])
    match()


main()
