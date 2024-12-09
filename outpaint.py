import pip._vendor.requests as requests
import os

api_key = os.environ["STABLE_DIFF_KEY"]

# Set this prompyt to what you want added
PROMPT = "An abstract image of painted thick puffy bright cloudy sky. Use a photorealistic painter style."
# Full path to file you want to extend
ORIGINAL_IMG = "D:/docs/tereya/images/house.png"
# Full path of where the modified file should be written
OUTPUT_IMG = "D:/docs/tereya/images/house_with_sky.png"


response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/edit/outpaint",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={
        "image": open(ORIGINAL_IMG, "rb"),
    },
    data={
        "prompt": PROMPT,
        "output_format": "png",
        "left": 1000,
        "up": 1000
    },
)

if response.status_code == 200:
    with open(OUTPUT_IMG, 'wb') as file:
        file.write(response.content)
    
    print("Done!")
else:
    raise Exception(str(response.json()))
