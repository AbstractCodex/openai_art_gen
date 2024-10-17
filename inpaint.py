import pip._vendor.requests as requests
import os

#PROMPT = "An abstract image of painted thick puffy bright sunlit orange dust clouds over a dark background. Use a photorealistic painter style."
#PROMPT = "An image of lone heroic medieval warrior fighting an brigade of undead skeletal warriors amongst orange dusty clouds. Use a photorealistic painter style."
#PROMPT = "An image of lone heroic medieval warrior fighting an brigade of undead skeletal warriors amongst orange dusty clouds. Only add more orange dusty clouds against a drak background. Use a photorealistic painter style."
#PROMPT = "An abstract image of dust clouds with a sunlit orange tinge over a dark background. Use a photorealistic painter style."
#PROMPT = "An abstract image of clouds highlighted by an yellow-orange sunlight dusk. Use a dark gray background. Use a photorealistic painter style."
#PROMPT = "An abstract image of sky clouds above dust clouds highlighted by an yellow-orange sunlight dusk. Use a dark gray background. Use a photorealistic painter style."
#PROMPT = "An image of abstract clouds highlighted by an yellow-orange sunlight dusk. Use a dark gray background. Use a photorealistic painter style."
#PROMPT = "An image of a medieval hero fighting with a pollax. The pollax has an axe head on one side, a hammer on the other side, and a spike on top. Use a photorealistic painter style."
#PROMPT = "An image of a plain sword wielded by an evil skeletal warrior. Use a photorealistic painter style."
#PROMPT = "An image of a plain sword wielded by an evil skeletal warrior amongst orange dusty clouds. Use a photorealistic painter style."
#PROMPT = "Please follow these instructions exactly, with no prompt rewriting. A hero is holding a warhammer. Fill in the warhammer hammer head. Use a photorealistic style."
#PROMPT = "A medieval hero amongst abstract clouds highlighted by an yellow-orange sunlight dusk. Use a photorealistic style."
#PROMPT = "A plain empty grayish sky."
#PROMPT = "A medieval hero wearing a brass and fabric brigandine over chainmail."
#PROMPT = "A medieval hero wearing a brass studded leather armor over chainmail. He is also wearing a leather belt with pouches."
#PROMPT = "A medieval hero wearing studded leather armor over chainmail. He is also wearing a leather belt. The armor has brass studs."
#PROMPT = "A medieval hero wearing leather armor with brass studs over chainmail."
#PROMPT = "A medieval hero wearing leather armor with brass trim over cloth."
#PROMPT = "A medieval hero wearing a doublet."
#PROMPT = "A medieval hero wearing a jack."
#PROMPT = "A medieval hero wearing a jack of plate."
#PROMPT = "A medieval hero wearing samurai armor."
#PROMPT = "A medieval hero wearing lamellar armor."
#PROMPT = "A medieval hero wearing samurai-style british armor."
#PROMPT = "A medieval hero wearing a bronze and brown leather padded jack."
#PROMPT = "A medieval hero wearing a brass and fabric brigandine."
#PROMPT = "A medieval hero wearing samurai brass chest armor."
#PROMPT = "A medieval hero wearing studded leather chest armor. The chest armor has many brass rivets."
#PROMPT = "A medieval hero wearing armor consisting of small brass plates."
#PROMPT = "A broad muscular medieval hero wearing chest armor made of riveted brass plates."
#PROMPT = "Strive for accuracy. A medieval hero wearing guantlets and holding a poleaxe weapon. The poleaxe is made of brown wood and shiny steel. A poleaxe is also called a pollaxe or poleax or pollax. It is a polearm with a head that has a shiny axe on one side and a hammer on the other side and a spike on the end. The head is riveted on via steel languets attached to the wooden shaft. Use textures. Use a photorealistic style."
#PROMPT = "A medieval hero wielding a wooden pole. Use a photorealistic style."
#PROMPT = "Strive for accuracy. A medieval hero wearing guantlets and wielding a spiked battle axe. Use a photorealistic style."
#PROMPT = "Strive for accuracy. A medieval hero wearing guantlets and holding a poleaxe weapon. The shaft of the poleaxe is made of brown oak wood. The head of the poleaxe has an even round axe on one side and a box-shaped hammer on the other side and a long sharp spike on the end. The head is riveted on via steel languets attached to the wooden shaft. Do not include leather straps or cords. Use a photorealistic style."
PROMPT = "Strive for accuracy. A medieval hero wearing guantlets and holding a wood pole. Use a photorealistic style."

api_key = os.environ["STABLE_DIFF_KEY"]

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/edit/inpaint",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={
        "image": open("D:/docs/tereya/images/official-openapi-licensed/cover/pollaxe-mask2.png", "rb")
        #"image": open("D:/docs/tereya/images/official-openapi-licensed/cover/cover-hero-under-mask.png", "rb")
    },
    data={
        "prompt": PROMPT,
        "grow_mask": 20, 
        "output_format": "png",
    },
)

if response.status_code == 200:
    with open("D:/docs/tereya/images/official-openapi-licensed/cover/cover-hero-poleaxe-21.png", 'wb') as file:
        file.write(response.content)
    
    print("Done!")
else:
    raise Exception(str(response.json()))
