#1
def main():
    print_intro()
    length, width = get_dimensions()
    amt_needed = compute_amount(length, width)
    print_report(length, width, amt_needed)

def print_intro():
    print("Welcome to the area calculator!")
    print("This program will help you calculate the amount needed based on the dimensions you provide.")

def get_dimensions():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    return length, width

def compute_amount(length, width):
    area = length * width
    return area

def print_report(length, width, amt_needed):
    print("\n--- Report ---")
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Amount Needed (Area): {amt_needed}")
if __name__ == "__main__":
    main()

#2
import random

def main():
    best_of_n = int(input("Enter the number of games for best of (e.g., 3, 5, 7): "))
    player_a_score, player_b_score = 0, 0
    games_needed = (best_of_n // 2) + 1

    for game_number in range(1, best_of_n + 1):
        print(f"\n--- Game {game_number} ---")
        winner = play_game('A' if game_number % 2 == 1 else 'B')
        
        if winner == 'A':
            player_a_score += 1
        else:
            player_b_score += 1

        print(f"Player A: {player_a_score}, Player B: {player_b_score}")

        if player_a_score == games_needed:
            print("Player A wins the match!")
            return
        elif player_b_score == games_needed:
            print("Player B wins the match!")
            return

def play_game(serving_player):
    score_a, score_b = 0, 0

    while score_a < 15 and score_b < 15:
        winner = random.choice(['A', 'B'])
        if winner == 'A':
            score_a += 1
        else:
            score_b += 1

    return 'A' if score_a > score_b else 'B'

if __name__ == "__main__":
    main()

#3
import random

def main():
    best_of_n = int(input("Enter the number of games for best of (e.g., 3, 5, 7): "))
    results = {'A': {'wins': 0, 'shutouts': 0}, 'B': {'wins': 0, 'shutouts': 0}}

    for game_number in range(1, best_of_n + 1):
        print(f"\n--- Game {game_number} ---")
        winner, score_a, score_b = play_game('A' if game_number % 2 == 1 else 'B')
        results[winner]['wins'] += 1
        results[winner]['shutouts'] += (score_a == 0 if winner == 'A' else score_b == 0)

        print(f"Final Score - Player A: {score_a}, Player B: {score_b}")

    report_results(results, best_of_n)

def play_game(serving_player):
    score_a, score_b = 0, 0
    while score_a < 15 and score_b < 15:
        winner = random.choice(['A', 'B'])
        if winner == 'A':
            score_a += 1
        else:
            score_b += 1
    return ('A' if score_a > score_b else 'B', score_a, score_b)

def report_results(results, total_games):
    print("\n--- Match Results ---")
    for player in ['A', 'B']:
        wins = results[player]['wins']
        shutouts = results[player]['shutouts']
        win_percentage = (wins / total_games) * 100
        shutout_percentage = (shutouts / wins * 100) if wins > 0 else 0
        print(f"Player {player}: {wins} wins ({win_percentage:.2f}%), {shutouts} shutouts ({shutout_percentage:.2f}%)")

if __name__ == "__main__":
    main()

#4

#An API (Application Programming Interface) is a set of protocols that enables different software systems to communicate and exchange data, acting as a bridge between them. APIs work through endpoints, which are specific URLs where requests are made and responses are returned. Each endpoint corresponds to a particular resource or functionality offered by the API. For example, the Waze API provides endpoints such as `https://www.waze.com/api/traffic` that allow developers to access real-time traffic data, incidents, and route information. With this API, third-party applications can integrate Waze's traffic and navigation features, helping users get real-time traffic alerts, road conditions, and optimal driving routes. APIs like Waze’s enable seamless integration of navigation and traffic services into other apps, improving user experience with live, dynamic data.


#5

#A programming language is a set of rules and syntax that allows developers to write instructions that a computer can understand and execute. It is the foundation for creating software applications. For instance, Python is a popular programming language used to write the logic and functionality of web applications. In contrast, a framework is a collection of pre-built tools, libraries, and guidelines that help developers build applications more quickly and efficiently by providing reusable components and structures. A framework is built on top of a programming language and simplifies tasks like routing, database management, authentication, and security. For example, Laravel is a framework built using the PHP programming language, and it provides developers with a ready-made structure to create dynamic web applications without having to start from scratch. Frameworks help reduce development time and minimize errors, but they also come with some trade-offs, such as potential limitations in flexibility and reliance on framework updates. A real-world company that uses Django, a Python-based framework, is Spotify. Spotify uses Django to manage its user data, music recommendations, and streaming features for millions of users worldwide.