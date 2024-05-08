from tkinter import *
import demoji
demoji.download_codes()


def emoji_to_text():
   emoji = entry.get()
   text1 = demoji.findall(emoji)
   l3.configure(text=str(text1))


# create a tkinter window
root = Tk()
root.geometry("400x400")
root.title("ProjectGurukul Emoji to Text")


frame = Frame(root)
frame.pack(pady=20)
label = Label(frame, text="Emoji to Text Converter",fg="blue",font=("Arial", 15,))
label.pack(side="left", padx=10)
# create input field for emoji
frame1 = Frame(root)
frame1.pack(pady=20)
l1 = Label(frame1, text="Enter Text:",bg="lightgreen",font=("Arial", 15))
l1.pack(side="left", padx=10)
entry = Entry(frame1, font=("Arial", 15), width=15)
entry.pack(side="left", pady=20)


# create button to convert emoji to text
button = Button(root, text="Convert", font=("Arial", 15),bg="lightgreen", command=emoji_to_text)
button.pack()


# create label to display the converted text
l2 = Label(root,text="Description:", font=("Arial", 15),bg="orange")
l2.pack(pady=20)
l3 = Label(root, font=("Arial", 15),bg="yellow")
l3.pack(pady=20)


# run the tkinter window
root.mainloop()