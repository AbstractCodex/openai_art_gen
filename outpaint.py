import pip._vendor.requests as requests
import os

api_key = os.environ["STABLE_DIFF_KEY"]

# Set this prompt to what you want the final image to be like.
PROMPT = "An abstract image of painted thick puffy bright cloudy sky. Use a photorealistic painter style."
# Full path to file you want to extend
ORIGINAL_IMG = "D:/docs/tereya/images/house.png"
# Full path of where the modified file should be written
OUTPUT_IMG = "D:/docs/tereya/images/house_with_sky.png"
LEFT = 1000
UP = 1000


response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/edit/outpaint",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={
        "image": open(ORIGINAL_IMG, "rb")
    },
    data={
        "prompt": PROMPT,
        "output_format": "png",
        "left": LEFT,
        "up": UP
    },
)

if response.status_code == 200:
    with open(OUTPUT_IMG, 'wb') as file:
        file.write(response.content)
    
    print("Done!")
else:
    raise Exception(str(response.json()))
