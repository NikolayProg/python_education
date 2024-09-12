import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

def encrypt():
    filepath = askopenfilename()
    path = Path(filepath)
    pdf = PdfFileReader(str(path), strict=False)
    pdf_writer = PdfFileWriter()
    pdf_writer.appendPagesFromReader(pdf)
    value = str(ent.get())
    pdf_writer.encrypt(user_pwd=value)
    saving_path = asksaveasfilename()
    filepath_save = Path(saving_path + ".pdf")
    with filepath_save.open(mode="wb") as output_file:
        pdf_writer.write(output_file)
        
                                   
def nocrypt():
    filepath_d = askopenfilename()
    path_d = Path(filepath_d)
    pdf_reader_d = PdfFileReader(str(path_d), strict=False)
    pwd = str(ent.get())
    pdf_reader_d.decrypt(password=pwd)
    pdf_writer_d = PdfFileWriter()
    pdf_writer_d.appendPagesFromReader(pdf_reader_d)
    save_path = asksaveasfilename()
    filepath_save_d = Path(save_path + ".pdf")
    with filepath_save_d.open(mode="wb") as output_file_d:
        pdf_writer_d.write(output_file_d) 

window = tk.Tk()
window.title("ParolSetter")
window.rowconfigure([0,2], minsize=150, weight=1)
window.columnconfigure(0, minsize=200, weight=1)
window['background'] = '#856ff8'

encrypt_button = tk.Button(window, bg="lime", text="Encrypt", command=encrypt)
encrypt_button.grid(row=0, column = 0, padx=2, pady=2)

decrypt_button = tk.Button(window, bg="lime", text="Decrypt", command=nocrypt)
decrypt_button.grid(row=1,column=0, padx=2, pady=2)

ent_frame = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
ent_frame.grid(row=2, column=0, sticky="ew")
ent_frame['background'] = 'blue'

lbl = tk.Label(ent_frame, text="Password:")
lbl['background'] = 'yellow'
lbl.pack()

ent = tk.Entry(ent_frame)
ent.pack()

window.mainloop()