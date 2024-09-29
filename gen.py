# Use OpenAI DALLE-3 to generate an Image
from openai import OpenAI

# Default is dalle-2. As of 2024-04-13, Dalle-3 does not support image to image transformations
MODEL = "dall-e-3"
# N is the # of images to generate. For DALLE-3, only N=1 is supported as a parameter so we loop instead
N = 3

# The maximum prompt length is 1000 characters for dall-e-2 and 4000 characters for dall-e-3
#PROMPT = "An evil knight in with demonic corruption in spiked red armor and a helmet and glowing red eyes and a skull pendant and wielding a spiked mace is battling against a heroic man in bronze armor who wields a poleaxe. They are inside a dark medieval stone castle with an eerie teal mist. The camera is far and a side view of the two combantants. Use a photorealistic painting style."
#PROMPT = "The arm of an evil undead skeleton clawing upwards and to the left as an attack. The view is from behind. The orange light source is from the right. Use a plain brown-orange background. Use a photorealistic painting style."
#PROMPT = "A magical purple portal with electric sparks. Use a plain black background. Use a photorealistic style."
#PROMPT = "A photorealistic image. A medieval hero is wearing a brigandine and brass shoulder pauldrons. He is wielding a poleaxe. He opens a magic portal to fire golden cubes. He is battling against an evil skeletal undead skeleton monster in the shape of a large cat made of just bone. Orange dust clouds swirl around. The monster has teal lights in its joints."
#PROMPT = "A photorealistic image. A medieval hero is wearing a brigandine and brass shoulder pauldrons. He is wielding a poleaxe. He is battling against an evil skeletal undead skeleton monster in the shape of a large cat made of just bone. Orange dust clouds swirl around. The monster has teal lights in its joints."
#PROMPT = "A medieval english hero is wearing a brigandine and brass shoulder pauldrons. He is wielding a poleaxe. He is in an epic battle against an evil skeletal undead skeleton monster in the shape of a sabre-tooth tiger skeleton. Sunlight gleams on the hero's armor and weapon. Use a photorealistic painting style."
PROMPT = "A pollaxe against a plain gray background. The pollaxe an axes on one side and a hammer on the other. It has a long top spike. It has a wooden shaft with steel langets. Use a photorealistic style."

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.

    client = OpenAI()

    print("Generating ", N, " images...")

    for i in range(0, N):
        response = client.images.generate(
            model=MODEL,
            prompt=PROMPT,
            size="1024x1792",  #"1024x1024",  # DALLE-3 supported sizes: 1024x1024, 1792x1024, or 1024x1792
            quality="hd",  # hd or standard (default)
            response_format="url",  # url or b64_json. URLs are only valid for 60 mins after the image gen.
            style="vivid"  # vivid (default) or natural
        )

        print("Images generated #", (i+1))
        num_images = len(response.data)
        for j in range(0,num_images):
            image_url = response.data[j].url
            print(image_url)

