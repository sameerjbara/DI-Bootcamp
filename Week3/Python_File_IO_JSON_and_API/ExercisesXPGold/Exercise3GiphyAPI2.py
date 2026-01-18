# Instructions
# Hint: For this exercise, You will work with this part of the documention
# You will use this API KEY : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My

# Create a small Python program which asks the user for a term or phrase and returns all the relevant gifs. (Example: all the “hilarious” gifs)
# If the term or phrase doesn’t exist or if the user didn’t enter a correct term or phrase, return the trending gifs of the day and a message stating that you couldn’t find the requested term or phrase.
# Note from the documentation : GIPHY Trending returns a list of the most relevant and engaging content each and every day.



import requests


API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"


def fetch_search_gifs(query, limit=25, rating="g"):
    url = (
        f"https://api.giphy.com/v1/gifs/search"
        f"?api_key={API_KEY}&q={query}&limit={limit}&rating={rating}"
    )
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Search request failed: {response.status_code}")

    return response.json()


def fetch_trending_gifs(limit=25, rating="g"):
    url = (
        f"https://api.giphy.com/v1/gifs/trending"
        f"?api_key={API_KEY}&limit={limit}&rating={rating}"
    )
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Trending request failed: {response.status_code}")

    return response.json()


def print_gif_links(data):
    gifs = data.get("data", [])
    if not gifs:
        print("No gifs returned.")
        return

    for i, gif in enumerate(gifs, start=1):
        title = gif.get("title", "No title")
        gif_url = gif.get("url", "No url")
        print(f"{i}. {title}")
        print(f"   {gif_url}")


def main():
    term = input("Enter a term or phrase to search gifs: ").strip()

    if not term:
        print("You did not enter a valid term. Showing trending gifs instead.")
        data = fetch_trending_gifs(limit=10)
        print_gif_links(data)
        return

    data = fetch_search_gifs(term, limit=10)

    if len(data.get("data", [])) == 0:
        print(f"Could not find gifs for '{term}'. Showing trending gifs instead.")
        data = fetch_trending_gifs(limit=10)

    print_gif_links(data)


if __name__ == "__main__":
    main()
