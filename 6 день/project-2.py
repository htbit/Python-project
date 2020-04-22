# Текстовый редактор
import tkinter
import os    
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *  
class Notepad:  
    __root = Tk()  
    # ширина и высота окна по умолчанию
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)      
    # Добавить полосу прокрутки
    __thisScrollBar = Scrollbar(__thisTextArea)     
    __file = None  
    def __init__(self,**kwargs):  
        # Установить значок
        try:
                self.__root.wm_iconbitmap("Notepad.ico") 
        except:
                pass  
        # Установить размер окна (по умолчанию 300x300)  
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass  
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
        # Установить текст окна
        self.__root.title("Untitled - Блокнот")
        # Центрировать окно
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()     
        # Для левых
        left = (screenWidth / 2) - (self.__thisWidth / 2)          
        # Право-союзник
        top = (screenHeight / 2) - (self.__thisHeight /2)        
        # Для верхней и нижней
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))  
        # Чтобы сделать текстовую область автоматически изменяемой
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        # Добавить элементы управления (виджет)
        self.__thisTextArea.grid(sticky = N + E + S + W)
        # Открыть новый файл
        self.__thisFileMenu.add_command(label="Новый",
                                        command=self.__newFile)    
        # Чтобы открыть уже существующий файл
        self.__thisFileMenu.add_command(label="Открыть",
                                        command=self.__openFile)
        # Сохранить текущий файл
        self.__thisFileMenu.add_command(label="Сохранить",
                                        command=self.__saveFile)    
        # Создать строку в диалоге
        self.__thisFileMenu.add_separator()                                         
        self.__thisFileMenu.add_command(label="Выйти",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="Файл",
                                       menu=self.__thisFileMenu)     
        # Чтобы придать черту
        self.__thisEditMenu.add_command(label="Вырезать",
                                        command=self.__cut)             
        # дать возможность копирования
        self.__thisEditMenu.add_command(label="Копировать",
                                        command=self.__copy)         
        # Чтобы добавить функцию вставки
        self.__thisEditMenu.add_command(label="Вставить",
                                        command=self.__paste)         
        # Чтобы дать возможность редактирования
        self.__thisMenuBar.add_cascade(label="Редактировать",
                                       menu=self.__thisEditMenu)     
        # Для создания функции описания блокнота
        self.__thisHelpMenu.add_command(label="О блокноте",
                                        command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Сделал",
                                       menu=self.__thisHelpMenu)
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                              
        # Полоса прокрутки будет регулироваться автоматически в зависимости от содержимого
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)     
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)         
    def __quitApplication(self):
        self.__root.destroy()
        # выход()
    def __showAbout(self):
        showinfo("Блокнот","Vita Stav")  
    def __openFile(self):          
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])  
        if self.__file == "":
            # нет файла для открытия
            self.__file = None
        else:              
            # Попробуй открыть файл
            # установить заголовок окна
            self.__root.title(os.path.basename(self.__file) + " - Блокнот")
            self.__thisTextArea.delete(1.0,END)
            file = open(self.__file,"r")
            self.__thisTextArea.insert(1.0,file.read())
            file.close()
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)
    def __saveFile(self):
        if self.__file == None:
            # Сохранить как новый файл
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
            if self.__file == "":
                self.__file = None
            else:                  
                # Попробуй сохранить файл
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()                  
                # Изменить заголовок окна
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>") 
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
    def run(self):
        # Запустить главное приложение
        self.__root.mainloop()
# Запустить главное приложение
notepad = Notepad(width=600,height=400)
notepad.run()