from openai import OpenAI

#PROMPT = "A skeletal monster surrounded by clouds lit orange. The monster is an undead skeleton in the shape of a tiger. Use a photorealistic painting style."
#PROMPT = "Fluffy stirred up dust cloud lit orange. Use a photorealistic painting style."
PROMPT  = "An image of a medieval hero fighting with a steel poleaxe. The poleaxe has an axe head on one side, a hammer on the other side, and a spike on top. The poleaxe has steel languets. Use a photorealistic painter style."

N = 2

# Default is dalle-2. As of 2024-10-01, Dalle-3 does not support image to image transformations
#MODEL = "dall-e-3"
MODEL = "dall-e-2"

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.

    client = OpenAI()

    response = client.images.edit(
        model=MODEL,
        image=open("D:/docs/tereya/images/official-openapi-licensed/cover/cover-hero-polaxe-sq.png", "rb"),
        mask=open("D:/docs/tereya/images/official-openapi-licensed/cover/cover-hero-polaxe-sq-masked.png", "rb"),
        prompt=PROMPT,
        n=N,
        size="1024x1024",  #"1024x1024",  # DALLE-3 supported sizes: 1024x1024, 1792x1024, or 1024x1792
    )

    num_results = len(response.data)
    print("Image edited. Num results = ", num_results)
    for i in range(0, N):
        image_url = response.data[i].url
        print(image_url)