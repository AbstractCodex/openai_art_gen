import pip._vendor.requests as requests
import os

api_key = os.environ["STABLE_DIFF_KEY"]

#PROMPT = "An image of lone heroic medieval warrior fighting an brigade of undead skeletal warriors amongst orange dusty clouds. Use a photorealistic painter style."
#PROMPT = "An abstract image of painted thick bright sunlit orange dust clouds over a dark background. Use a photorealistic painter style."
PROMPT = "An abstract image of painted thick puffy bright sunlit orange dust clouds over a dark background. Use a photorealistic painter style."


response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/edit/outpaint",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={
        "image": open("D:/docs/tereya/images/official-openapi-licensed/edits/cover-art11-right-side.png", "rb"),
    },
    data={
        "prompt": PROMPT,
        "output_format": "png",
        "left": 1000,
        "up": 1000
    },
)

if response.status_code == 200:
    with open("D:/docs/tereya/images/official-openapi-licensed/edits/cover-art-right-extended-12.png", 'wb') as file:
        file.write(response.content)
    
    print("Done!")
else:
    raise Exception(str(response.json()))
