# Use OpenAI DALLE-3 to generate an Image
from openai import OpenAI
from datetime import datetime
import base64

# Use the latest, greatest model (as of 2025-May-03).
MODEL = "gpt-image-1"
# N is the # of images to generate. For DALLE-3, only N=1 is supported as a parameter so we loop instead
N = 1

# The maximum PROMPT length is 32000 characters for gpt-image-1, 1000 characters for dall-e-2 and 4000 characters for dall-e-3.
# You can edit this hardcoded prompt
PROMPT = """Create image of a sword."""
# Or, even better, create a prompt.txt file and place your prompt inside.
FILENAME_PROMPT = "prompt.txt"
prompt = PROMPT
try:
    with open(FILENAME_PROMPT, 'r') as file:
        prompt = file.read()
except FileNotFoundError:
    print("prompt.txt file not found. Using PROMPT value hardcoded in the source file instead.")
    prompt = PROMPT


FILENAME_OUT_PREFIX = f'./output/openai_img_{datetime.now():%Y-%m-%d_%H%M%S%z}'

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.

    client = OpenAI()

    print(f"Generating {N} images...")

    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        n=N,
        quality="high",  # high, medium and low are supported for gpt-image-1.
        size="auto"  #  Must be one of 1024x1024, 1536x1024 (landscape), 1024x1536 (portrait), or auto (default value) for gpt-image-1
    )

    for i in range(0, N):
        image_base64 = result.data[i].b64_json
        image_bytes = base64.b64decode(image_base64)

        # Save the image to a file
        filename = FILENAME_OUT_PREFIX + "_" + str(i) + ".png"
        with open(filename, "wb") as f:
            f.write(image_bytes)
            print(f"Generated image {filename}")


