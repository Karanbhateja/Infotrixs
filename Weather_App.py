import requests
import time

# Replace with your OpenWeather API key
API_KEY = "112eaf604d778ca2a1dc6ec7fc7a6da2"

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"Weather in {city}: {weather.capitalize()}, Temperature: {temp}°C"
    else:
        return f"City not found: {city}"

def main():
    favorites = []

    while True:
        print("\nWeather Application")
        print("1. Get Weather")
        print("2. Add to Favorites")
        print("3. Remove from Favorites")
        print("4. List Favorites")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            print(get_weather(city))
        elif choice == "2":
            city = input("Enter city name to add to favorites: ")
            if city not in favorites:
                favorites.append(city)
                print(f"{city} added to favorites.")
            else:
                print(f"{city} is already in your favorites.")
        elif choice == "3":
            city = input("Enter city name to remove from favorites: ")
            if city in favorites:
                favorites.remove(city)
                print(f"{city} removed from favorites.")
            else:
                print(f"{city} is not in your favorites.")
        elif choice == "4":
            print("Favorite Cities:")
            for city in favorites:
                print(city)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Automatically update weather every 15 seconds
        time.sleep(15)

if __name__ == "__main__":
    main()
