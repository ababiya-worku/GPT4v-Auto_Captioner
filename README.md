
---

[@ababiya_worku](https://linktr.ee/ababiya)

## GPT4V_Captioner

A powerful script that allows you to caption a single image or batch process any number of images within a directory. This script utilizes OpenAI's GPT-4 model to generate precise tags for images to enhance the CLIP model's understanding.


## Features
- **User Friendly**: You can put or copy paste the Script anywhere you like where you want to caption the images.
- **Single and Batch Image Processing**: Caption one image or multiple images in a directory.
- **Base64 Encoding**: Converts images to base64 for API processing.(Must have Open AI's API key)
- **GPT-4 Integration**: Uses OpenAI's GPT-4 model for generating image captions.
- **Adding your own Captions**: After Vision done captioning your images, it will ask you to add your own custom Tags to add on top of the .txt file for all .txt files at once. (Optional)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ababiya-worku/GPT4v-Auto_Captioner.git
    
    cd GPT4V_Captioner
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your OpenAI API key**:
    Obtain your API key from [OpenAI](https://openai.com/api) and put the key when asked:

## Before Running the script, Manually install this in CMD
```sh
pip install openai requests
```

```sh
pip install openai requests pillow
```

```sh
pip install --upgrade openai
```
## For Banner Image creation install this:
```sh
pip install wordcloud matplotlib
```

```sh
pip install colorama openai pillow wordcloud matplotlib
```

## Usage

1. **Single Image Captioning**:
    ```sh
    python GPT4V_Captioner.py single /path/to/your/image.jpg
    ```

2. **Batch Image Captioning**:
    ```sh
    python GPT4V_Captioner.py batch /path/to/your/directory
    ```
3. **Use the .Bat File**: Simply Put both the script & bat file in your images directory & double-click on the bat file, and let it do the Magic!
    ```sh
     GPT4V_Captioner.bat
    ```

## Functions

- `is_image_file(filename)`: Checks if the provided file is a valid image.
- `encode_image(image_path)`: Encodes the image to a base64 string.
- `describe_image(image_path, api_key)`: Sends the image to OpenAI's GPT-4 model for captioning.

---


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://openai.com/) for the GPT-4 model.
- [Colorama](https://pypi.org/project/colorama/) for terminal text formatting.

---
