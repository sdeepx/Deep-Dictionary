import difflib as df
import json as j
import banner
__author__ = "Shubhadeep"
__version__ = 0.2


banner.banner()

data = j.load(open("data.json", "r"))
data_keys = data.keys()


def deep_dict(w):
    word = w.lower()
    match = df.get_close_matches(word, data_keys, n=4)
    if word in data:
        return data[word]

    def first_match():
        if match[0] in data:
            ans = input("\n You mean {} instead? y (yes) n (no) : ".format(match[0]))
            if len(ans) == 0:
                print("[-] You didn't enter any value \n")
                return first_match()
            elif ans == "y" or ans == "Y" or ans == "yes":
                return data[match[0]]
            elif ans == "n" or ans == "N" or ans == "no":

                def second_match():
                    if match[1] in data:
                        ans1 = input("\n You mean {} instead? y (yes) n (no) : ".format(match[1]))
                        if len(ans1) == 0:
                            print("[-] You didn't enter any value \n")
                            return second_match()
                        elif ans1 == "y" or ans1 == "Y" or ans1 == "yes":
                            return data[match[1]]
                        elif ans1 == "n" or ans1 == "N" or ans1 == "no":

                            def third_match():
                                if match[2] in data:
                                    ans2 = input("\n You mean {} instead? y (yes) n (no) : ".format(match[2]))
                                    if len(ans2) == 0:
                                        print("[-] You didn't enter any value \n")
                                        return third_match()
                                    elif ans2 == "y" or ans2 == "Y" or ans2 == "yes":
                                        return data[match[2]]
                                    elif ans2 == "n" or ans2 == "N" or ans2 == "no":

                                        def fourth_match():
                                            if match[3] in data:
                                                ans3 = input(
                                                    "\n You mean {} instead? y (yes) n (no) : ".format(match[3]))
                                                if len(ans3) == 0:
                                                    print("[-] You didn't enter any value \n")
                                                    return fourth_match()
                                                elif ans3 == "y" or ans3 == "Y" or ans3 == "yes":
                                                    return data[match[3]]
                                                elif ans3 == "n" or ans3 == "N" or ans3 == "no":
                                                    print("\n [-] sorry we couldn't find the meaning of that word \n")
                                                    return again()
                                                else:
                                                    print(
                                                        "[-] You enter a wrong value. \n Please enter y(yes) or n(no) ")
                                                    return fourth_match()
                                        if __name__ == '__main__':
                                            oup0 = fourth_match()
                                            if type(oup0) == list:
                                                banner.line()
                                                for _ in oup0:
                                                    print(_)
                                                banner.line()
                                            else:
                                                return oup0
                                            return again()
                                    else:
                                        print("[-] You enter a wrong value. \n Please enter y(yes) or n(no) ")
                                        return third_match()
                            if __name__ == '__main__':
                                oup1 = third_match()
                                if type(oup1) == list:
                                    banner.line()
                                    for ll in oup1:
                                        print(ll)
                                    banner.line()
                                else:
                                    return oup1
                                return again()
                        else:
                            print("[-] You enter a wrong value. \n Please enter y(yes) or n(no) ")
                            return second_match()
                if __name__ == '__main__':
                    oup2 = second_match()
                    if type(oup2) == list:
                        banner.line()
                        for i in oup2:
                            print(i)
                        banner.line()
                    else:
                        return oup2
                    return again()
            else:
                print("[-] You enter a wrong value. \n Please enter y(yes) or n(no) ")
                return first_match()
    if __name__ == '__main__':
        oup = first_match()
        if type(oup) == list:
            banner.line()
            for l in oup:
                print(l)
            banner.line()
        else:
            return oup
        return again()


def inp():
    try:
        word = input('''               
                           ▌   
            ▌  ▌ ▞▀▖ ▙▀▖ ▞▀▌ ▐▌
            ▐▐▐  ▌ ▌ ▌   ▌ ▌ ▗▖
             ▘▘  ▝▀  ▘   ▝▀▘ ▝▘ ''')

        if len(word) == 0:
            print("[-] You didn't the word \n")
            return inp()
        oup = deep_dict(word)
        if type(oup) == list:
            banner.line()
            for l in oup:
                print(l)
            banner.line()
        else:
            return oup

    except IndexError or TypeError or ValueError or KeyError:
        print("[-] It's no a word. \n please enter a word ")
        return inp()
    return again()


def again():
    ag = input("\n Find another word ? y(yes) or n(n) : ")
    if len(ag) == 0:
        print("[-] Please say y( yes ) or n ( no )")
        return again()
    elif ag == "y" or ag == "Y" or ag == "yes":
        return inp()
    elif ag == "n" or ag == "N" or ag == "no":
        print(" \n {*} Thanks for using DeepDictionary")
        banner.line()

    else:
        print("You put a wrong value \n")
        return again()


if __name__ == '__main__':
    inp()
