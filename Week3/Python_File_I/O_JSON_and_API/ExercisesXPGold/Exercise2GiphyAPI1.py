# Instruction
# Hint: For this exercise, check out the documentation of the Giphy API

# You will work with this part of the documention

# You will use this Gif URL: https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
# Explanation of the Gif URL

# q Request Paramater: Search query term or phrase. We are searching for “hilarious” gifs

# rating Request Paramater: Filters results by specified rating. We are searching for Level 1 gifs. Check out the ratings documentation

# api_key Request Paramater : GIPHY API Key. Our API KEY is hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
# Fetch the giphs from the Gif URL provided above.

# Use f-strings and variables to build the URL string we’re using for the fetch.
# If the status code is 200 return the result as a JSON object.
# Only return gifs which have a height bigger then 100.
# Return the length of the object you received in the previous question.
# Only return the first 10 gifs. Hint: In the Giphy Documentation, check out the relevant Request Parameters.



import requests


def fetch_gifs():
    api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
    query = "hilarious"
    rating = "g"
    limit = 10

    url = f"https://api.giphy.com/v1/gifs/search?q={query}&rating={rating}&api_key={api_key}&limit={limit}"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}")

    data = response.json()

    gifs = data.get("data", [])

    filtered_gifs = []
    for gif in gifs:
        height = int(gif["images"]["original"]["height"])
        if height > 100:
            filtered_gifs.append(gif)

    print("Number of gifs with height > 100:", len(filtered_gifs))
    return filtered_gifs


if __name__ == "__main__":
    result = fetch_gifs()
    print("First gif title:", result[0]["title"] if result else "No gifs found")
