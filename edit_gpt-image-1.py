# Use OpenAI DALLE-3 to generate an Image
from openai import OpenAI
from datetime import datetime
import base64

# Use the latest, greatest model (as of 2025-May-03).
MODEL = "gpt-image-1"
# N is the # of images to generate. For DALLE-3, only N=1 is supported as a parameter so we loop instead
N = 1

# The maximum PROMPT length is 32000 characters for gpt-image-1, 1000 characters for dall-e-2 and 4000 characters for dall-e-3.
# My initial prompt
# PROMPT = """Create image of a book cover for a middle grade medieval fantasy. The book is "Zelf Swiftblade Slayer of Undead". 
#     Zelf is the main hero and should be depicted on the cover. He is a tall 14 year old boy. He is half elf and half Ukti. 
#     An Ukti is like a dwarf mixed with an orc or rock golem. Zelf looks like a blue elf, with black hair. 
#     His Ukti inheritence gives him natural plating on his knuckles. Zelf wiedls a long sword and shield. 
#     Zelf has a sister, Elyssara, who is short and can open magic portals to launch lightning bolts. 
#     Elyssara looks like a blue elf, but short. She has long black hair. She is cute with big eyes. She is unarmed.
#     Zelf has another companion named Levan. Levan is a short fat lizard boy. Levan is a bard who carries a lute. 
#     Levan is frightened. Mavis is another companion on the cover. Mavis is a human rogue girl who is also around 14 years old. She is pretty. 
#     Mavis is slender and tall. Mavis dual wields daggers. Mavis is agile. 
#     The setting should be a swamp with ruins and skeleton warriors."""

# Bad prompt from Grok
# PROMPT = """Create a vibrant book cover for Zelf Swiftblade Slayer of Undead, a middle-grade medieval fantasy. 
# Depict an action-packed swamp scene at twilight, with misty ruins, glowing fungi, and alabaster-white skeleton warriors. 
# Center Zelf, a tall 14-year-old half-elf/half-Ukti boy with blue skin, black hair, and rocky knuckles, 
# wielding a longsword and shield, striking a skeleton. His Devotus armor bears a crest. 
# Elyssara, his short, serious sister with blue skin and long black hair, conjures a crackling lightning portal behind him. 
# Mavis, a tall, sly human rogue girl, leaps with dual daggers, aiming a throwing knife. 
# Levan, a chubby lizard boy, cowers behind a ruin, clutching his lute, eyes wide with fear. 
# Use bold colors, with the portal's blue light illuminating the scene. The title, in yellow, frames the action. 
# Emphasize Zelf's heroism, the group's camaraderie, and a touch of humor through smirks and fright, keeping it thrilling but not gory."""

PROMPT = """Create image of a book cover for a middle grade medieval fantasy. The book is "Zelf Swiftblade Slayer of Undead". 
    Zelf is the main hero and should be depicted on the cover. He is a tall 14 year old boy. He is half elf and half Ukti. 
    An Ukti is like a dwarf mixed with an orc or rock golem. Zelf looks like a blue elf, with black hair. He is cute.
    His Ukti inheritence gives him natural plating on his knuckles. 
    Zelf wields a sharp long sword and holds a round shield.
    Zelf is wearing a gambeson and trousers tucked into boots. His shield has a cross symbol.
    Zelf is in an action pose. His expression is determined.
    Zelf has four companions, that should be on the cover as well: Elyssara, Levan, Mavis and Lucee. 
    Elyssara looks like a blue elf, but short with long black hair. Elyssara is cute with big eyes that glow a magic purple. Elyssara is unarmed. 
    Elyssara is firing a blue lightning bolt from a small round portal at one of the skeleton warriors.
    Elyssara is serious and innocent.
    Levan is a short fat lizard boy. His skin is a grayish green. Levan is a bard who carries a lute. He wears clothes typical of a medieval bard. Levan is innocent and wide-eyed. 
    Levan is frightened, so he might be hiding behind a piece of the ruins. Levan has a scared open-mouth epxression.
    Mavis is a pretty human rogue girl who is also around 14 years old. She has shoulder-length brown or auburn hair.
    Mavis is slender and tall. Mavis is agile and dual wields daggers.
    Mavis has a sly smirk.
    Lucee is an overgrown wolf puppy. She is a fantasy type of wolf creature, so she has antlers. Lucee is cute with big eyes. 
    Lucee is dirty with moss hanging off of her.
    The setting should be a large swamp with skeleton warriors amongst old ruins.
    A menacing snake with multiple heads is peeking from behind the ruins in the background.
    The skeleton warriors have ragged armor and swords or axes. 
    One of the stones has an engraved symbol of a crescent moon shape.
    Use a hand painted, detailed, high quality style appealing for twelve and thirteen year olds.
    The reference image was generated with the above prompt by gpt-image-1 and is good, but has the following mistakes that I would like you to correct by doing the following:
    Enlarge Elyssara and change her dress to brown or orange and white. Remove teh polearm from Mavis. Give her daggers instead.
    Enlarge Lucee. Remove the snakes from the top title area.
    
    """


INPUT_FILENAME = f'./output/openai_img_2025-05-03_173023_0.png'
OUTPUT_FILENAME = f'{INPUT_FILENAME}.edited'

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.

    client = OpenAI()

    print(f"Generating {N} images...")

    result = client.images.edit(
        model=MODEL,
        image=open(INPUT_FILENAME, "rb"),
        prompt=PROMPT,
        n=N,
        # quality="high",  # high, medium and low are supported for gpt-image-1.
        # size="auto"  #  Must be one of 1024x1024, 1536x1024 (landscape), 1024x1536 (portrait), or auto (default value) for gpt-image-1
    )

    for i in range(0, N):
        image_base64 = result.data[i].b64_json
        image_bytes = base64.b64decode(image_base64)

        # Save the image to a file
        filename = OUTPUT_FILENAME + "_" + str(i) + ".png"
        with open(filename, "wb") as f:
            f.write(image_bytes)


