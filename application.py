from statistics import mean
import constants
import time


teams_data = constants.TEAMS
players_data = constants.PLAYERS
panthers = []
bandits = []
warriors = []
experienced_height_list = []
inexperienced_height_list = []
guardian_list_ex = []
guardian_list_inex = []
panthers_guardians = []
bandits_guardians = []
warriors_guardians = []


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
            print("\nThanks for your consideration")
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
                  f"\nTotal players: {len(panthers)}"
                  f"\nTotal experienced: 3"
                  f"\nTotal inexperienced: 3")
            average_height = mean(experienced_height_list[choice2-1::3]) + mean(inexperienced_height_list[choice2-1::3])
            print(f"Average height: {average_height/2}\n")
            print("Players on Team:")
            print(" " + ", ".join(panthers))
            print("\nGuardians: ")
            print(" " + ", ".join(str(item) for inner_list in panthers_guardians for item in inner_list))
            break
        elif choice2 == 2:
            print(f""
                  f"\nTeam: {teams_data[1]} Stats"
                  f"\n--------------------"
                  f"\nTotal players: {len(bandits)}"
                  f"\nTotal experienced: 3"
                  f"\nTotal inexperienced: 3")
            average_height = mean(experienced_height_list[choice2 - 1::3]) +\
                             mean(inexperienced_height_list[choice2 - 1::3])
            print(f"Average height: {round(average_height / 2)}\n")
            print("Players on Team:")
            print(" " + ", ".join(bandits))
            print("\nGuardians: ")
            print(" " + ", ".join(str(item) for inner_list in bandits_guardians for item in inner_list))
            break
        elif choice2 == 3:
            print(f""
                  f"\nTeam: {teams_data[2]} Stats"
                  f"\n--------------------"
                  f"\nTotal players: {len(warriors)}"
                  f"\nTotal experienced: 3"
                  f"\nTotal inexperienced: 3")
            average_height = mean(experienced_height_list[choice2 - 1::3]) + \
                             mean(inexperienced_height_list[choice2 - 1::3])
            print(f"Average height: {round(average_height / 2)}\n")
            print("Players on Team:")
            print(" " + ", ".join(warriors))
            print("\nGuardians: ")
            print(" " + ", ".join(str(item) for inner_list in warriors_guardians for item in inner_list))
            break
    if count == 0:
        press()


def press():
    time.sleep(2)
    choice1 = input("\nWould you like to play again? Y/N ")
    if choice1.lower() == "y":
        print("\n")
        menu()
    else:
        print("Thanks for playing our game!!")
        time.sleep(1.5)


def clean_data(data):
    cleaned = []
    for item in data:
        guard = item["guardians"].split(" and ")
        item["height"] = item["height"].split()[0]
        item["height"] = int(item["height"])
        if item["experience"] == "YES":
            experienced_height_list.append(item["height"])
            guardian_list_ex.append(guard)
            experience = True
        else:
            inexperienced_height_list.append(item["height"])
            guardian_list_inex.append(guard)
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
    inexperienced_players = [item["name"] for item in players_data if item["experience"] == "NO"]
    experienced_players = [item["name"] for item in players_data if item["experience"] == "YES"]
    for i in range(3):
        panthers.append(experienced_players.pop(0))
        panthers.append(inexperienced_players.pop(0))
        panthers_guardians.append(guardian_list_ex.pop(0))
        panthers_guardians.append(guardian_list_inex.pop(0))
        bandits.append(experienced_players.pop(0))
        bandits.append(inexperienced_players.pop(0))
        bandits_guardians.append(guardian_list_ex.pop(0))
        bandits_guardians.append(guardian_list_inex.pop(0))
        warriors.append(experienced_players.pop(0))
        warriors.append(inexperienced_players.pop(0))
        warriors_guardians.append(guardian_list_ex.pop(0))
        warriors_guardians.append(guardian_list_inex.pop(0))


if __name__ == "__main__":
    clean_data(players_data)
    balance_teams()
    menu()
