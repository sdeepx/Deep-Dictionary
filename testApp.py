import difflib as d
import json as j

data = j.load(open("data.json","r"))
data_keys = data.keys()


def App_translate(Word):
    word = Word.lower()

    match = d.get_close_matches(word, data_keys, n=5)

    if word in data:
        return data[word]
    elif len(word) <= 0:
        rtn = input( "Oops! I think you forgot to enter the word!!\ndo you wanna find the meaning of your word ? y or n : ")
        if rtn == "y" or rtn =="Y":
            print("\n")
            return main()
        elif rtn == "n" or rtn == "N":
            return "Ok then"
        else:
            return "[-] Umm You did something wrong !!"

    elif match[0] in data:
        ans = input("You mean '"+match[0]+"' instead of '"+word+"' ?? y (yes) or n (no) : ")
        if ans == "y" or ans == "Y" or ans == "yes" or ans == "Yes":
            return data[match[0]]
        elif len(ans) <= 0:
            return "OOPPS! I think you forgot to put the value !!"
        elif ans == "n" or ans == "N" or ans == "no" or ans == "No":

            #2nd match.................................................................................
            if match[1] in data:
                ans = input("Okay! You mean '"+match[1]+"' instead of '"+word+"' ?? y (yes) or n (no) : ")
                if ans == "y" or ans == "Y" or ans == "yes" or ans == "Yes":
                    return data[match[0]]
                elif len(ans) <= 0:
                    return "OOPPS! I think you forgot to put the value !!"
                elif ans == "n" or ans == "N" or ans == "no" or ans == "No":

                    #3rd match---------------------------------------------------------------------------
                    if match[2] in data:
                        ans = input("Umm! You mean '" + match[2] + "' instead of '" + word + "' ?? y (yes) or n (no) : ")
                        if ans == "y" or ans == "Y" or ans == "yes" or ans == "Yes":
                            return data[match[2]]
                        elif len(ans) <= 0:
                            return "OOPPS! I think you forgot to put the value !!"
                        elif ans == "n" or ans == "N" or ans == "no" or ans == "No":

                            #4th match______________________________________________________________________________
                            if match[3] in data:
                                ans = input(
                                    "I think You mean '" + match[3] + "' instead of '" + word + "' ?? y (yes) or n (no) : ")
                                if ans == "y" or ans == "Y" or ans == "yes" or ans == "Yes":
                                    return data[match[3]]
                                elif len(ans) <= 0:
                                    return "OOPPS! I think you forgot to put the value !!"
                                elif ans == "n" or ans == "N" or ans == "no" or ans == "No":

                                    #5th mathch +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    if match[4] in data:
                                        ans = input(
                                            "None of them!!? okk! You mean '" + match[
                                                4] + "' instead of '" + word + "' ?? y (yes) or n (no) : ")
                                        if ans == "y" or ans == "Y" or ans == "yes" or ans == "Yes":
                                            return data[match[4]]
                                        elif len(ans) <= 0:
                                            return "OOPPS! I think you forgot to put the value !!"
                                        elif ans == "n" or ans == "N" or ans == "no" or ans == "No":
                                            return "[-] Sorry we couldn't found the meaning of your word"
                                        else:
                                            return "[-] You entered a wrong value "
                                else:
                                    return "[-] You entered a wrong value "
                        else:
                            return "[-] You entered a wrong value "
                else:
                    return "[-] You entered a wrong value "
        else:
            return "[-] You entered a wrong value "
    else:
        return "[-] Word couldn't be found"



def main():
    try:

        Word = input("Enter Word: ")
        appword = App_translate(Word)

        if type(appword) == list:
            for i in appword:
                print("\n",i)
            print()
        else:
            print(appword)

        return "--------------------------------------------------------------------------------------------------------------------"
    except:
        print("[-] Sorry You entered a wrong word that doesn't exist ")

        return "--------------------------------------------------------------------------------------------------------------------"


if __name__ == '__main__':
    main()