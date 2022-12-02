import qrcode
import PIL.Image
from tkinter import *

# Create object
root = Tk()

#Title
root.title('Ryan\'s QR Code Generator')
logo = PIL.Image.open('/Users/ryanleedom/Documents/QR/LL-Border.png')

# Adjust size
root.geometry( "550x300" )

def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')

def inventoryNumber():
    global logo
    basic = 150
    width_percentage = (basic/float(logo.size[0]))
    height_size = int((float(logo.size[1])*float(width_percentage)))
    logo = logo.resize((basic, height_size), PIL.Image.ANTIALIAS)
    qrc = qrcode.QRCode(
    version=1,
    box_size=15,
    border=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H)

    qrc.add_data(f'https://www.lelandlittle.com/items/{msg.get()}/')
    qrc.make()
    if not colorInput.get():
            qrc.make()
            gen_img = qrc.make_image(
                fill_color='black', 
                bg_color="#fff"
                ).convert('RGBA')
    else:
        gen_img = qrc.make_image(
            fill_color=f'{colorInput.get()}',
            bg_color="#fff"
            ).convert('RGBA')

    position = ((gen_img.size[0] - logo.size[0]) // 2, (gen_img.size[1] - logo.size[1]) // 2)

    gen_img.paste(logo, position)
    gen_img.save(f'/Users/ryanleedom/Documents/QR/Generated_QR_Codes/{msg.get()}'+'.png')

    saved.config(text='File saved in Generated_QR_Codes folder!')
    root.after(10000, lambda: saved.config(text=''))
    root.after(10000, lambda: msg.delete(0,END))
    root.after(10000, lambda: colorInput.delete(0,END))
    

def URL():
    global logo
    basic = 150
    width_percentage = (basic/float(logo.size[0]))
    height_size = int((float(logo.size[1])*float(width_percentage)))
    logo = logo.resize((basic, height_size), PIL.Image.ANTIALIAS)
    qrc = qrcode.QRCode(
    version=1,
    box_size=15,
    border=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H)

    qrc.add_data(msg.get())
    qrc.make()
    if not colorInput.get():
            qrc.make()
            gen_img = qrc.make_image(
                fill_color='black', 
                bg_color="#fff"
                ).convert('RGBA')
    else:
        gen_img = qrc.make_image(
            fill_color=f'{colorInput.get()}',
            bg_color="#fff"
            ).convert('RGBA')

    position = ((gen_img.size[0] - logo.size[0]) // 2, (gen_img.size[1] - logo.size[1]) // 2)

    gen_img.paste(logo, position)
    gen_img.save('/Users/ryanleedom/Documents/QR/Generated_QR_Codes/URL'+'.png')

    saved.config(text='File saved in Generated_QR_Codes folder!')
    root.after(10000, lambda: saved.config(text=''))
    root.after(10000, lambda: msg.delete(0,END))
    root.after(10000, lambda: colorInput.delete(0,END))

def generate_qr_inventory_number():
    if clicked.get() == "Inventory #":
        inventoryNumber()
    if clicked.get() == "URL":
        URL()
	

# Dropdown menu options
options = [
	"Inventory #",
	"URL"
]


# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Inventory #" )
saved = Label(fg='white')
saved.pack(pady=10)
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options ).pack(pady=45)

#URL/Inventory Input field
msg = Entry(bg='light gray', fg="black",disabledbackground="light gray",disabledforeground="black")
msg.pack(pady=10)
msg.insert(0, "Inventory # or URL: ")
msg.configure(state='disabled')
x_focus_in = msg.bind('<Button-1>', lambda x: on_focus_in(msg))
x_focus_out = msg.bind(
    '<FocusOut>', lambda x: on_focus_out(msg, 'Inventory # or URL: '))

#Color Input
colorInput = Entry(bg='light gray', fg="black",disabledbackground="light gray",disabledforeground="black")
colorInput.pack()
colorInput.insert(0, "QR Color: ")
colorInput.configure(state='disabled')
x_focus_in = colorInput.bind('<Button-1>', lambda x: on_focus_in(colorInput))
x_focus_out = colorInput.bind(
    '<FocusOut>', lambda x: on_focus_out(colorInput, 'QR Color: '))

# Create button, it will change label text
btn = Button(
    highlightthickness=0,
    text='Generate',
    command=generate_qr_inventory_number
).pack()
# Execute tkinter
root.mainloop()