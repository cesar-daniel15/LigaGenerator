# Function to register the teams to be drawn
def add_teams():
    # Reads the number of teams
    num_teams = int(input("Enter the number of teams to be drawn: "))

    # Array to store the teams
    teams = []

    # Loop to input each team's name
    for i in range(num_teams):
        while True:
            team = input(f"Enter the name of team {i + 1}: ")

            # Checks if the team has already been registered
            if team in teams:
                print("This team has already been registered. Please try again.")
            else:
                teams.append(team)
                break

    # Return teams
    return teams


teams_added = add_teams()
print("List of teams added:", teams_added)

# Function to calculate the number of possible rounds
def calculate_rounds(teams):
    # Total number of teams
    num_teams = len(teams)

    # Checks if the number of teams is even
    if num_teams % 2 != 0:
        teams.append("Bye")  # Add a "Bye" if the number of teams is odd
        num_teams += 1

    # Number of rounds
    round_number = 1

    # Maximum number of possible rounds
    num_rounds = len(teams) - 1

    # Number of games per round
    num_games = len(teams) // 2

    home_away = input("Are there home and away games against the same team? (yes/no): ")

    if home_away in ["no", "n", "No", "NO", "no"]:
        print("\n FIRST ROUND")
        for i in range(num_rounds):
            print(f"\t Round {i + 1}")
            for j in range(num_games):
                team1 = teams[j]
                team2 = teams[-(j + 1)]
                print(f"\t {team1} X {team2}")

            teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    elif home_away in ["yes", "y", "Yes", "YES"]:
        print("\n FIRST ROUND")
        for i in range(num_rounds):
            print(f"\n Round {i + 1}")
            for j in range(num_games):
                team1 = teams[j]
                team2 = teams[-(j + 1)]
                print(f"\t {team1} X {team2}")

            teams = [teams[0]] + [teams[-1]] + teams[1:-1]

        print("\n SECOND ROUND")
        for i in range(num_rounds):
            print(f"\n Round {i + 1 + num_rounds}:")
            for j in range(num_games):
                team1 = teams[-(j + 1)]
                team2 = teams[j]
                print(f"\t {team1} X {team2}")

            teams = [teams[0]] + [teams[-1]] + teams[1:-1]


rounds = calculate_rounds(teams_added)
