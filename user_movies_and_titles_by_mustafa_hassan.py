import requests

api_key = '1ddec0a7'
base_url = f'http://www.omdbapi.com/?apikey={api_key}&'



search_controll = 5



def get_movie_info(title):
    url = f'{base_url}t={title}'
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()
        if movie_data.get("Response") == "True":
            return movie_data
        else:
            print(" Filmen hittades inte.")
            return None
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None



def key_word(keyword):
    url = f'{base_url}s={keyword}'
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()
        if movie_data.get("Response") == "True":
            print("\nHittade filmer:")
            for index, movie in enumerate(movie_data['Search'], start=1):
                print(f"{index}. {movie['Title']} ({movie['Year']})")
        else:
            print(" Inga filmer hittades med det sökordet.")
    else:
        print(f"Failed to retrieve data: {response.status_code}")



def main():
    search_history = []  

    print("Välkommen till mitt program där kan du söka om filmer och få info\n")

    while True:
        print("\n1: Sök efter en film/serie")
        print("2: Se sökhistorian")
        print("3: Sök med keyword")
        print("4: Avsluta")

        user_choice = input("Välj ett av alternativen: ")

        if user_choice == '1':
            movie_title = input("Enter movie title: ")
            movie_info = get_movie_info(movie_title)

            if movie_info:
                print(f"\nTitle: {movie_info['Title']}")
                print(f"Year: {movie_info['Year']}")
                print(f"Rated: {movie_info['Rated']}")
                print(f"Genre: {movie_info['Genre']}")
                print(f"Director: {movie_info['Director']}")


                search_history.append(movie_title)
                if len(search_history) > search_controll:
                    search_history.pop(0)

        elif user_choice == '2':
            print("\nSökhistorik (senaste 5 sökningar):")
            if search_history:
                for index, title in enumerate(search_history, start=1):
                    print(f"{index}. {title}")
            else:
                print("Ingen sökhistorik ännu.")

        elif user_choice == '3':
            print("Sök efter en film/serie med nyckelord:")
            user_keyword = input("Enter keyword: ")
            key_word(user_keyword)

        elif user_choice == '4':
            print("Tack och hej!")
            break

        else:
            print("Ogiltigt val. Vänligen välj ett alternativ från menyn.")



main()
