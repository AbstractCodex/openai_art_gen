import pip._vendor.requests as requests
import os

# Set this prompt to what you want added.
PROMPT = "A medieval hero wearing a brass and fabric brigandine over chainmail."
# Full path to file you want to make changes to.
ORIGINAL_IMG = "D:/docs/tereya/images/cover-hero-armor-mask.png"
# Full path of where the modified file should be written.
OUTPUT_IMG = "D:/docs/tereya/images/cover-img-modified.png"


api_key = os.environ["STABLE_DIFF_KEY"]

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/edit/inpaint",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={
        "image": open(ORIGINAL_IMG, "rb")
    },
    data={
        "prompt": PROMPT,
        "grow_mask": 1, 
        "output_format": "png",
    },
)

if response.status_code == 200:
    with open(OUTPUT_IMG, 'wb') as file:
        file.write(response.content)
    
    print("Done!")
else:
    raise Exception(str(response.json()))
