# Use OpenAI DALLE-3 to generate an Image
from openai import OpenAI
from datetime import datetime
import base64

# Use the latest, greatest model (as of 2025-May-03).
MODEL = "gpt-image-1"
# N is the # of images to generate. For DALLE-3, only N=1 is supported as a parameter so we loop instead
N = 1

# The maximum length is 32000 characters for gpt-image-1, 1000 characters for dall-e-2 and 4000 characters for dall-e-3.
PROMPT = "Create image of a book cover for a middle grade medieval fantasy. The book is \"Zelf Swiftblade Slayer of Undead\". \
    Zelf is the main hero and should be depicted on the cover. He is a tall 14 year old boy. He is half elf and half Ukti. \
    An Ukti is like a dwarf mixed with an orc or rock golem. Zelf looks like a blue elf, with black hair. \
    His Ukti inheritence gives him natural plating on his knuckles. Zelf wiedls a sword and shield. \
    Zelf has a sister, Elyssara, who is short and can open magic portals to launch lightning bolts. \
    Elyssara looks like a blue elf, but short. She has long black hair.\
    Zelf has another companion named Levan. Levan is a short fat lizard boy. Levan is a bard who carries a lute. \
    Levan is frightened. Mavis is another companion on the cover. Mavis is a human rogue girl who is also around 14 years old. \
    Mavis is slender and tall. Mavis dual wields daggers. Mavis is agile. \
    The setting should be a swamp with ruins and skeleton warriors."

FILENAME = f'./output/openai_img_{datetime.now():%Y-%m-%d_%H:%M:%S%z}'

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.

    client = OpenAI()

    print(f"Generating {N} images...")

    result = client.images.generate(
        model=MODEL,
        prompt=PROMPT,
        #background="auto", # Set to transparent, auto, or opaque
        #moderation="auto", # low or auto
        n=N,
        #output_format="png", # png, jpeg, or webp
        quality="high",  # high, medium and low are supported for gpt-image-1.
        size="auto"  #  Must be one of 1024x1024, 1536x1024 (landscape), 1024x1536 (portrait), or auto (default value) for gpt-image-1
    )

    for i in range(0, N):
        image_base64 = result.data[i].b64_json
        image_bytes = base64.b64decode(image_base64)

        # Save the image to a file
        filename = FILENAME + "_" + str(i) + ".png"
        with open(filename, "wb") as f:
            f.write(image_bytes)


