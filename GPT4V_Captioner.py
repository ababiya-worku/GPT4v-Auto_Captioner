from colorama import init, Fore, Style
import os
import base64
import requests
import openai
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import random

# Initialize colorama
init()

print(Fore.GREEN + r"""
   _____ _____ _______  __      _______  _____ _____ ____  _   _ 
  / ____|  __ \__   __| \ \    / /_   _|/ ____|_   _/ __ \| \ | |
 | |  __| |__) | | |     \ \  / /  | | | (___   | || |  | |  \| |
 | | |_ |  ___/  | |      \ \/ /   | |  \___ \  | || |  | | . ` |
 | |__| | |      | |       \  /   _| |_ ____) |_| || |__| | |\  |
  \_____|_|      |_|        \/   |_____|_____/|_____\____/|_| \_|
                                                                                                                              
""" + Style.RESET_ALL)

print()  # Add an empty line for better readability

print(Fore.GREEN + "DEV-BY" + Style.RESET_ALL)

# Link
print("https://linktr.ee/ababiya")
print()  # Add an empty line for better readability

print(Fore.GREEN + """A powerful script that allows you to Caption a single image or batch process any number of images that exist in your directory where you run the script!""" + Style.RESET_ALL)
print()  # Add an empty line for better readability

def is_image_file(filename):
    try:
        with Image.open(filename) as img:
            return True
    except:
        return False

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def describe_image(image_path, api_key):
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "As an AI image tagging expert, please provide precise tags for these images to enhance CLIP model's understanding of the content. Employ succinct keywords or phrases, steering clear of elaborate sentences and extraneous conjunctions. Prioritize the tags by relevance. Your tags should capture key elements such as the main subject, setting, artistic style, composition, image quality, color tone, filter, and camera specifications, and any other tags crucial for the image. When tagging photos of people, include specific details like gender, nationality, attire, actions, pose, expressions, accessories, makeup, composition type, age, etc. For other image categories, apply appropriate and common descriptive tags as well. Recognize and tag any celebrities, well-known landmark or IPs if clearly featured in the image. Your tags should be accurate, non-duplicative, and within a 20-75 word count range. These tags will use for image re-creation, so the closer the resemblance to the original image, the better the tag quality. Tags should be comma-separated. Exceptional tagging will be rewarded with $10 per image."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return response.json()['choices'][0]['message']['content']

def add_user_words(txt_files, user_words):
    for txt_file in txt_files:
        with open(txt_file, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(user_words + ', ' + content)

def random_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return f"hsl({random.randint(0, 360)}, {random.randint(50, 100)}%, {random.randint(30, 70)}%)"

def create_word_banner(txt_files, output_filename="word_banner.png"):
    # Collect all words from txt files
    all_words = []
    for txt_file in txt_files:
        with open(txt_file, 'r', encoding='utf-8') as f:
            words = f.read().replace('\n', ' ').split(',')
            all_words.extend([word.strip() for word in words if word.strip()])

    # Count word frequencies
    word_frequencies = Counter(all_words)

    # Create WordCloud object
    wordcloud = WordCloud(width=3840, height=2160, background_color='black', 
                          max_words=200, prefer_horizontal=0.5, 
                          color_func=random_color_func, random_state=42)

    # Generate word cloud
    wordcloud.generate_from_frequencies(word_frequencies)

    # Save the image
    plt.figure(figsize=(48, 27), dpi=80)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(output_filename, bbox_inches='tight', facecolor='black', edgecolor='none')
    plt.close()

    print(f"Word cloud saved as: {output_filename}")

def main():
    print("Welcome to the Automatic Image Tagger/Captioner Tool using OpenAI's Vision AI!")
    
    # Ask user for API key
    api_key = input("Please enter your OpenAI API key: ")
    openai.api_key = api_key

    current_directory = os.getcwd()
    image_files = [f for f in os.listdir(current_directory) if is_image_file(os.path.join(current_directory, f))]
    
    if not image_files:
        print("No image files found in the current directory.")
        return
    
    print(f"Found {len(image_files)} image(s) in the current directory.")
    
    txt_files = []
    for image_file in image_files:
        image_path = os.path.join(current_directory, image_file)
        txt_file = os.path.splitext(image_file)[0] + ".txt"
        txt_path = os.path.join(current_directory, txt_file)
        
        print(f"\nProcessing: {image_file}")
        
        try:
            description = describe_image(image_path, api_key)
            
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(description)
            
            txt_files.append(txt_path)
            print(f"Description saved to: {txt_file}")
        except Exception as e:
            print(f"An error occurred while processing {image_file}: {str(e)}")
    
    print("\nAll images have been processed.")

    # Ask user if they want to add their own words
    user_input = input("Do you want to add your own words to the beginning of all .txt files? (yes/no): ").lower()
    if user_input == 'yes':
        user_words = input("Enter the words you want to add (comma-separated): ")
        add_user_words(txt_files, user_words)
        print("Your words have been added to all .txt files.")
    
    # Create word banner
    create_word_banner(txt_files)
    print("Word cloud banner has been created.")

if __name__ == "__main__":
    main()
