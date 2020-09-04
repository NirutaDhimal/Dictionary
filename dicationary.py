import json
from difflib import get_close_matches
p = "y"
f = open('dictionary_folder/data.json',)
data = json.loads(f.read())
def get_meaning(word):
    if word in data:
        return(data[word])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif len(get_close_matches(word,data.keys())) > 0:
        print("Did you mean {} instead?".format(get_close_matches(word,data.keys())[0]))
        decide = input("Press y for yes and n for no. ")
        if decide == "y":
            return(data[get_close_matches(word,data.keys())[0]])
        elif decide == "n":
            return("The word doesn't exist")
        else:
            return("you entered a wrong input.Just enter y/n.")
    else:
        return("The word doesnot exist.")
  
while p == "y":
      key = (input("Enter the word you want to search: ")).lower()
      output = get_meaning(key)
      if type(output) == list:
          for item in output:
              print(item)
      else:
          print(output)
      p = input("Do you want to continue (y/n)? ")
f.close()