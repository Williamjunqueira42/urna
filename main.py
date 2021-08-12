#  urna eletronica usando python
#  William junqueira e Anna clara lelis

from tkinter import *
from pygame import *
import mysql.connector




bt_config = {
    'font': 'arial 12', 'width': '10', 'height': '3', 'padx': '10', 'pady': '10',  'bg': 'black', 'fg': 'white'
}

class Urna():
    
    def __init__(self, master):
        self.master = master

        
        
        #  Frames
        self.displayframe = Frame(self.master, width=450, height=500)
        self.keyframe = Frame(self.master, width=450, height=500)


        self.displayframe.pack(side='left', expand=1, fill='y', anchor='center')
        self.keyframe.pack(side='right', expand=1,)


#  buttons
        self.bt1 = Button(self.keyframe, bt_config, text='1', command= lambda: self.bt_press(1))
        self.bt2 = Button(self.keyframe, bt_config, text='2', command= lambda: self.bt_press(2))
        self.bt3 = Button(self.keyframe, bt_config, text='3', command= lambda: self.bt_press(3))
        self.bt4 = Button(self.keyframe, bt_config, text='4', command= lambda: self.bt_press(4))
        self.bt5 = Button(self.keyframe, bt_config, text='5', command= lambda: self.bt_press(5))
        self.bt6 = Button(self.keyframe, bt_config, text='6', command= lambda: self.bt_press(6))
        self.bt7 = Button(self.keyframe, bt_config, text='7', command= lambda: self.bt_press(7))
        self.bt8 = Button(self.keyframe, bt_config, text='8', command= lambda: self.bt_press(8))
        self.bt9 = Button(self.keyframe, bt_config, text='9', command= lambda: self.bt_press(9))
        self.bt0 = Button(self.keyframe, bt_config, text='0', command= lambda: self.bt_press(0))
        
        self.bt_branco = Button(self.keyframe, bt_config, text='BRANCO', bg='white', fg='black', command= self.branco)
        self.bt_corrige = Button(self.keyframe, bt_config, text='CORRIGE', bg='#ff4a03', fg='black', command=self.corrige)
        self.bt_confirma = Button(self.keyframe, bt_config, text='CONFIRMA', bg='#2dff0d', fg='black', command=self.confirma)
        
        
        self.bt1.grid(row=0, column=0, padx=5, pady=5)
        self.bt2.grid(row=0, column=1, padx=5, pady=5)
        self.bt3.grid(row=0, column=2, padx=5, pady=5)
        self.bt4.grid(row=1, column=0, padx=5, pady=5)
        self.bt5.grid(row=1, column=1, padx=5, pady=5)
        self.bt6.grid(row=1, column=2, padx=5, pady=5)
        self.bt7.grid(row=2, column=0, padx=5, pady=5)
        self.bt8.grid(row=2, column=1, padx=5, pady=5)
        self.bt9.grid(row=2, column=2, padx=5, pady=5)
        self.bt0.grid(row=3, column=1, padx=5, pady=5)
        
        self.bt_branco.grid(row=4, column=0, padx=5, pady=5)
        self.bt_corrige.grid(row=4, column=1, padx=5, pady=5)
        self.bt_confirma.grid(row=4, column=2, padx=5, pady=5)
       
#  Entry
        self.entry1 = Entry(self.displayframe, width='4', font='arial 20', justify='center')
        self.entry2 = Entry(self.displayframe, width='4', font='arial 20', justify='center')
        
        self.entry1.grid(row=0, column=1, pady=20) 
        self.entry2.grid(row=0, column=2, pady=20) 

 
#  Labels       
        self.photo_label = Label(self.displayframe)
        self.photo_label.grid(row=1, column=0, sticky='we')
        
        self.nome_label = Label(self.displayframe, font='arial 12')
        self.nome_label.grid(row=1, column=1)
        
   
       
        
#  Metodos   
    
    def bt_press(self, bt,):  #  Metodo para quando um botão numerico for pressionado

            if self.entry1.get() == '': self.entry1.insert(0, f'{bt}')                    
            else: self.entry2.insert(0, f'{bt}')    
            self.checkCandidate()
     
            
    def checkCandidate(self):
        
        if  self.entry1.get() == '' or self.entry2.get() == '': 
            return
      
        self.n = self.entry1.get() + self.entry2.get() 
        
        if self.n == '42':  
            self.img = PhotoImage(file='42100.png')
            self.nome_label['text'] = 'Douglas Adams'
        
        elif self.n == '70':
            self.img = PhotoImage(file='70100.png')
            self.nome_label['text'] = 'J. K. Rowling'
                  
        elif self.n == '50':
            self.img = PhotoImage(file='50100.png')
            self.nome_label['text'] = 'Rick Riordan'
    
        else: 
            self.img = ''
            self.nome_label['text'] = 'Voto nulo'
        self.photo_label['image'] = self.img
        self.photo_label.image = self.img
            
            
    def branco(self):  #  Metodo pora quando o botão branco for pressionado
         pass
  
    
    def corrige(self):  #  Metodo pora quando o botão corrige for pressionado
        self.entry1.delete(0)
        self.entry2.delete(0)
        self.photo_label['image'] = ''
        self.nome_label['text'] = ''
        

    def confirma(self):  #  Metodo pora quando o botão confirmar for pressionado
        
        if self.n == '42': self.addVoto(1)
        if self.n == '70': self.addVoto(2)
        if self.n == '50': self.addVoto(3)
        
        
        
        mixer.init()
        mixer.music.load('som.mp3')
        mixer.music.play()
        self.fim()
     
        
    def conexãoBd(self): # Metodo para fazer a ligação com o banco de dados
        try:
            self.conn = mysql.connector.connect(host = "127.0.0.1", user = "root", database = "urna")      
        except: 
            print('Erro de conexão')
     
        
    def addVoto(self, candidato): 
        
        self.conexãoBd()
          
        if candidato == 1:
    
            cursor = self.conn.cursor()
            cursor.execute(f'UPDATE candidatos SET qtd_votos={1} WHERE id={1};')
       
               
        elif candidato == 2:
            pass
        
        elif candidato == 3:
            pass
    
        
        
    def fim(self): 
        pass
        
        
    
root = Tk()
Urna(root)
root.geometry('900x500')
root.resizable(False,False)  #  fixar janela 
root.mainloop()