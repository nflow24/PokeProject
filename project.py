import requests, random, os, json, time

# can use timeit library to run program multiple times
# import timeit
#
# runtime = timeit.timeit("main()", setup="from __main__ import main", number=1)
# print(f"Runtime: {runtime:.2f} seconds")

start = time.time()
PokeAPI = "https://pokeapi.co/api/v2/pokemon?limit=151" # url to PokeAPI

def getAllPokemon():
    """
    Performs GET requests to PokeAPI and formats names and sprites of the original 151 pokemon into a json file
    and dictionary for use in main()

    Args:
        none
    Returns:
        pokedex(list of dict):
            each dict contains two key-value pairs:
                name(str): pokemon name
                sprite(str): path to png stored in 'sprites' folder
    """
    if not os.path.exists("pokedex.json") or not os.path.exists("sprites"):
        response = requests.get(PokeAPI) # Send GET request
        if response.status_code == 200:
            data = response.json() #converts json file to python dictionary
        if not os.path.exists("sprites"):
            os.makedirs("sprites", exist_ok=True)
            print("Downloading pokemon sprites...")
            for i, pokemon in enumerate(data["results"], start=1):
                print(f"{i}/151 sprites downloaded...", end = "\r", flush=True)
                url_reponse = requests.get(pokemon["url"])
                if url_reponse.status_code == 200:
                    url_data = url_reponse.json()
                    sprite_url = url_data["sprites"]["front_default"]
                    pokemon["sprite"] = sprite_url
                    if sprite_url:
                        sprite_response = requests.get(sprite_url)
                        if sprite_response.status_code == 200:
                            with open(f"sprites/{pokemon['name']}.png", "wb") as f:
                                f.write(sprite_response.content)
            print("Done downloading sprites!\n")

        if not os.path.exists("pokedex.json"):
            print("Getting pokedex.json...")
            pokedex_list = []
            for i, pokemon in enumerate(data["results"], start=1):
                pokedex_list.append({
                    "name": pokemon["name"],
                    "sprite": f"sprites/{pokemon['name']}.png"
                })
            with open("pokedex.json", "w") as file:
                json.dump(pokedex_list, file, indent=4)
            print("pokedex.json created!")

    with open("pokedex.json", "r") as file:
        pokedex = json.load(file)
        print("reading pokedex.json\n")
        return pokedex

def main():
    pokeInfo = getAllPokemon()
    # extracts (name, sprite) tuples from pokedex.json into a list of tuples
    print("Program start\n")
    print("Menu:")
    print("\t1) Randomize Team")
    print("\t2) View Hall of Fame")
    print("\t3) Quit")
    while True:
        option = input("What would you like to do? (enter 1, 2, or 3): ")
        print(option)
        if pokeInfo:
            if option == "1":
                allPokemon = [] # list where tuples are stored
                for p in pokeInfo:
                    allPokemon.append((p["name"], p["sprite"]))
                team = random.sample(allPokemon, 6) # gets 6 random tuples from the list

                save_team = []
                for name, sprite in team:
                    print(f"- {name.capitalize()}") # prints pokemon into a team
                    save_team.append(name.capitalize())
                if os.path.exists("history.json"):
                    with open(f"history.json", "r") as file:
                            history = json.load(file)
                else:
                    history = {"teams   axc": []}
                history["teams"].append(save_team)
                with open(f"history.json", "w") as file:
                    json.dump(history, file, indent=4)
            elif option == "2":
                pass
            elif option == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option!")

main()
end = time.time()
print(f"\nStatistics:\n\tRuntime: {end - start:.2f} seconds") # gets runtime of single program run