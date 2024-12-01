"""Testing wiki API"""
import wikipedia

search_phrase = input("Enter search phrase: ")
while search_phrase != "":
    try:
        print(wikipedia.summary(search_phrase))
        print(wikipedia.API_URL)
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f"{search_phrase} does not match any pages. Try another query!")
    print()
    search_phrase = input("Enter search phrase: ")
print("Thank you")
