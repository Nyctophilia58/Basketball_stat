from statistics import mean
import constants


teams_data = constants.TEAMS
players_data = constants.PLAYERS
panthers = []
bandits = []
warriors = []
height_list_panthers = []
height_list_bandits = []
height_list_warriors = []


def menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MENU----\n")
    print(f"Here are your choices:"
          f"\n\t1) Display Team Stats"
          f"\n\t2) Quit\n"
          )
    while True:
        count = 0
        try:
            choice1 = int(input("Enter an option: "))
        except ValueError:
            print("Invalid input, try again! ")
            continue
        if choice1 == 1:
            print(f"\nThe teams are:"
                  f"\n\t1) Panthers"
                  f"\n\t2) Bandits"
                  f"\n\t3) Warriors\n"
                  )
        elif choice1 == 2:
            print("Thanks for your consideration")
            count = 1
            break
        else:
            continue
        i = True
        choice2 = None
        while i:
            choice2 = input("Enter an option: ")
            if (choice2 == '1') | (choice2 == '2') | (choice2 == '3'):
                i = False
                choice2 = int(choice2)
            elif not type(choice2) is int:
                print("Invalid number! try again!")
        if choice2 == 1:
            print(f"\nTeam: {teams_data[0]} Stats"
                  f"\n--------------------"
                  f"\nTotal players: {len(panthers)}\n")
            avg_height = mean(height_list_panthers)
            print(f"The average height of the team: {avg_height}\n")
            print("Players on Team:")
            print(" " + ", ".join(panthers))
            break
        elif choice2 == 2:
            print(f""
                  f"\nTeam: {teams_data[1]} Stats"
                  f"\n--------------------"
                  f"\nTotal players: {len(bandits)}\n")
            avg_height = mean(height_list_bandits)
            print(f"The average height of the team: {avg_height}\n")
            print("Players on Team:")
            print(" " + ", ".join(bandits))
            break
        elif choice2 == 3:
            print(f""
                  f"\nTeam: {teams_data[2]} Stats"
                  f"\n--------------------"
                  f"\nTotal players: {len(warriors)}"
                  f"\nTotal experienced: 3"
                  f"\nTotal inexperienced: 3")
            avg_height = mean(height_list_warriors)
            print(f"The average height of the team: {avg_height}\n")
            print("Players on Team:")
            print(" " + ", ".join(warriors))
            break
    if count == 0:
        press()


def press():
    key = input("\nPress ENTER to continue...")
    if not key:
        print("")
        menu()
    else:
        print("See ya!!")


def clean_data(data):
    cleaned = []
    for item in data:
        guard = item["guardians"].split(" and ")
        item["height"] = item["height"].split()[0]
        item["height"] = int(item["height"])
        if item["experience"] == "YES":
            experience = True
        else:
            experience = False
        cleaned.append(
            {
                "name": item["name"],
                "guardians": guard,
                "experience": experience,
                "height": int(item["height"])
            }
        )
    return cleaned


def balance_teams():
    num_players = len(players_data) // len(teams_data)
    for i in range(num_players):
        panthers.append(players_data.pop(0)["name"])
        height_list_panthers.append(players_data.pop(0)["height"])
        bandits.append(players_data.pop(0)["name"])
        height_list_bandits.append(players_data.pop(0)["height"])
        warriors.append(players_data.pop(0)["name"])
        height_list_warriors.append(players_data.pop(0)["height"])


if __name__ == "__main__":
    clean_data(players_data)
    balance_teams()
    menu()
