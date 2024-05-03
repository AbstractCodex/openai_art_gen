from openai import OpenAI

# Default is dalle-2. As of 2024-04-13, Dalle-3 does not support image to image transformations
MODEL = "dall-e-3"
# N is the # of images to generate. For DALLE-3, only N=1 is supported as a parameter so we loop instead
N = 3

# The maximum prompt length is 1000 characters for dall-e-2 and 4000 characters for dall-e-3
PROMPT = "A photrealistic image of a group of medieval heroes battling a giant monster. The monster has claws and tentacles."

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.

    client = OpenAI()

    print("Generating ", N, " images...")

    for i in range(0, N):
        response = client.images.generate(
            model=MODEL,
            prompt=PROMPT,
            size="1792x1024",  #"1024x1024",  # DALLE-3 supported sizes: 1024x1024, 1792x1024, or 1024x1792
            quality="hd",  # hd or standard (default)
            response_format="url",  # url or b64_json. URLs are only valid for 60 mins after the image gen.
            style="vivid"  # vivid (default) or natural
        )

        print("Images generated #", (i+1))
        num_images = len(response.data)
        for j in range(0,num_images):
            image_url = response.data[j].url
            print(image_url)

