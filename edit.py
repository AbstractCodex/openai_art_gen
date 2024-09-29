import pip._vendor.requests as requests
import os

api_key = os.environ["STABILITY_DIFF_KEY"]

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/edit/inpaint",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={
        "image": open("D:/docs/tereya/images/official-openapi-licensed/edits/Lantir-vs-skeletal-xylax_masked_wings.png", "rb"),
    },
    data={
        "prompt": "A photorealistic image of an undead skeletal tiger",
        "output_format": "png",
    },
)

if response.status_code == 200:
    with open("D:/docs/tereya/images/official-openapi-licensed/edits/Lantir-vs-skeletal-xylax-stable-diff-wings4.png", 'wb') as file:
        file.write(response.content)
    
    print("Done!")
else:
    raise Exception(str(response.json()))
