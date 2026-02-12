# Use pip package manager to add a Python package of your choice to your project (e.g., requests,
# numpy, matplotlib). Create a new file named task7.py and write a Python script that demonstrates
# how to use the chosen package to perform a specific task or function

# demonstrates using request to fetch a random dog image

import requests

def get_dog(save_path="random_dog.jpg"):
    url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url)

    # check if successful
    if response.status_code != 200:
        print("Error fetching dog image.")
        return

    # Convert JSON image to python dictionary
    data = response.json()

    # extract image with key
    image_url = data.get("message")

    print("Random Dog Image URL:", image_url)

    # download image file
    image_response = requests.get(image_url)

    #binary content of image
    image_data = image_response.content

    # open file to save image
    with open(save_path, "wb") as file:
        file.write(image_data)

    print(f"Image successfully saved as {save_path}")

if __name__ == "__main__":
    get_dog()