print("=== Movie Recommendation System ===")

movies = {
    "avatar": ["Avengers", "Interstellar", "Guardians of the Galaxy"],
    "interstellar": ["Inception", "Gravity", "The Martian"],
    "avengers": ["Iron Man", "Thor", "Captain America"],
    "inception": ["Interstellar", "Tenet", "Shutter Island"],
    "thor": ["Avengers", "Iron Man", "Doctor Strange"],


    "iron man": ["Avengers", "Captain America", "Thor"]
}

while True:
    print("\nAvailable Movies:")
    for movie in movies.keys():
        print("-", movie.title())

    user_movie = input("\nEnter a movie name: ").lower().strip()

    if user_movie in movies:
        print("\nRecommended Movies:")
        for i, recommendation in enumerate(movies[user_movie], start=1):
            print(f"{i}. {recommendation}")
    else:
        print("\nMovie not found in database.")

    choice = input("\nDo you want another recommendation? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using the Movie Recommendation System!")
        break