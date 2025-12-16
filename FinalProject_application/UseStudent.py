import requests
from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO

API_URL = "http://127.0.0.1:8000/image/"

# get Image from API

response = requests.get(API_URL)
print(response.status_code)
print(response.text)

data = response.json()


# Tkinter setup
root = Tk()
root.title("Image Viewer")
root.geometry("610x430")

image_list = []

#Get images from URLs
for item in data:
    img_url = item['Img']
    img_response = requests.get(img_url)
    img_data = BytesIO(img_response.content)
    img = Image.open(img_data).resize((600, 350))
    image_list.append(ImageTk.PhotoImage(img))

counter = 0

def nextImage():
    global counter
    counter = (counter + 1) % len(image_list)
    imageLabel.config(image=image_list[counter])
    infoLabel.config(text=f"Image {counter + 1} of {len(image_list)}")

imageLabel = Label(root, image=image_list[0])
infoLabel = Label(root, text=f"Image 1 of {len(image_list)}", font=("Helvetica", 14))
button = Button(root, text="Next", command=nextImage)

imageLabel.pack()
infoLabel.pack()
button.pack(pady=10)

root.mainloop()


#reference for code: https://dev.to/mooict/make-a-simple-image-gallery-using-tkinter-and-python-2p4j