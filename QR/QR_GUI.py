import qrcode
import PIL.Image
from tkinter import *


ws = Tk()
ws.title('Ryan\'s QR Code Generator')
ws.geometry('400x300')
ws.configure(bg='#003140')


logo = PIL.Image.open('/Users/ryanleedom/Desktop/QR/TRL.png')
    
def generate_qr_url():
    global logo
    basic = 100
    width_percentage = (basic/float(logo.size[0]))
    height_size = int((float(logo.size[1])*float(width_percentage)))
    logo = logo.resize((basic, height_size), PIL.Image.ANTIALIAS)
    qrc = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    qrc.add_data(msg.get())
    qrc.make()
    gen_img = qrc.make_image(
        fill_color='black', 
        bg_color="#fff"
        ).convert('RGBA')

    position = ((gen_img.size[0] - logo.size[0]) // 2, (gen_img.size[1] - logo.size[1]) // 2)

    gen_img.paste(logo, position)
    gen_img.save('/Users/ryanleedom/Desktop/QR/Generated_QR_Codes/URL'+'.png')
    saved.config(text='File saved in Generated_QR_Codes folder!')
    ws.after(10000, lambda: saved.config(text=''))
    ws.after(10000, lambda: msg.delete(0,END))

frame = Frame(ws,bg='#003140')
frame.pack(expand=True)

Label(frame, text='URL',bg='#003140').grid(row=0, column=0)
msg = Entry(frame, bg='light gray', fg="black")
msg.grid(row=0, column=1)

btn = Button(
    frame,
    highlightthickness=0,
    bg='#003140',
    text='Generate',
    command=generate_qr_url
)
btn.grid(row=4, column=1, pady=10)

saved = Label(ws, fg='white',bg='#003140')
saved.pack(pady=45)


ws.mainloop()