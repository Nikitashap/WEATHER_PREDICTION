from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QWidget,	QPushButton,	QLabel,	QWidget,	QCheckBox,	QVBoxLayout,
QButtonGroup, QRadioButton ) 
import pygame
from tkinter import * 
from tkinter import ttk 
import tkinter as tk
from PyQt5.QtCore import QTextCodec 
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import Qt
class Window1(QWidget):
	def init(self): 
		super(Window1, self).init()
		self.setWindowTitle('MAK') 
		self.setMinimumWidth(500) 
		self.setMinimumHeight(500) 
		self.button = QPushButton(self) 
		self.button.setText('START') 
		self.button.move(200,210)
		self.button.setStyleSheet("background-color: light gray;")
		self.button.show()

pixmap = QPixmap('tex.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label = QLabel(self)
label.setPixmap(pixmap)
label.setGeometry(110, 105, pixmap.width(), pixmap.height())
pixmap2 = QPixmap('2023.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label2 = QLabel(self)
label2.setPixmap(pixmap2)
label2.setGeometry(0, 300, pixmap2.width(), pixmap2.height())
pixmap3 = QPixmap('2024.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label3 = QLabel(self)
label3.setPixmap(pixmap3)
label3.setGeometry(300, 300, pixmap3.width(), pixmap3.height())
pixmap4 = QPixmap('sun.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label4 = QLabel(self)
label4.setPixmap(pixmap4)
label4.setGeometry(150, 0, pixmap4.width(), pixmap4.height())
pixmap5 = QPixmap('dgd.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label5 = QLabel(self)
label5.setPixmap(pixmap5)
label5.setGeometry(60, 415, pixmap5.width(), pixmap5.height())
pixmap6 = QPixmap('dgd2.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label6 = QLabel(self)
label6.setPixmap(pixmap6)
label6.setGeometry(370, 415, pixmap6.width(), pixmap6.height())
pixmap7 = QPixmap('w.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label7 = QLabel(self)
label7.setPixmap(pixmap7)
label7.setGeometry(0, 0, pixmap7.width(), pixmap7.height())
pixmap8 = QPixmap('w1.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label8 = QLabel(self)
label8.setPixmap(pixmap8)
label8.setGeometry(330, 0, pixmap8.width(), pixmap8.height())
pixmap9 = QPixmap('sneg.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label9 = QLabel(self)
label9.setPixmap(pixmap9)
label9.setGeometry(15, 160, pixmap9.width(), pixmap9.height())
pixmap10 = QPixmap('sneg1.jpg')
# Создаем объект QLabel и устанавливаем на него изображение label10 = QLabel(self)
label10.setPixmap(pixmap10)
label10.setGeometry(370, 160, pixmap10.width(), pixmap10.height())
		self.butt = QRadioButton("march 2023")
		layout = QVBoxLayout() 
		layout.addWidget(self.butt)
		self.butt1 = QRadioButton("april 2023")
		#layout = QVBoxLayout() layout.addWidget(self.butt1)
		self.butt2 = QRadioButton("may 2023")
		#layout = QVBoxLayout() layout.addWidget(self.butt2)
		layout.setAlignment(Qt.AlignBottom | Qt.AlignHCenter) 
		layout.setSpacing(60)
		# Устанавливаем QVBoxLayout на QWidget self.setLayout(layout)
	def show_window_2(self): #self.w2 = Window2() #self.w2.show() global tp
		if self.butt.isChecked(): 
			tp=1
		if self.butt1.isChecked(): 
			tp=2
		if self.butt2.isChecked(): 
			tp=3
		pygame.init()
		screen = pygame.display.set_mode((500,500)) 
		pygame.display.set_caption("graph")
		all_sprites=pygame.sprite.Group() 
		clock = pygame.time.Clock() 
		running = True
		fps=60
		class Line(pygame.sprite.Sprite): 
			def init(self,pos,x,y,ln):
				pygame.sprite.Sprite.init(self) 
				if pos=="x":
					self.image=pygame.Surface((3,ln)) 
					self.image.fill((0,0,0))
					self.rect = self.image.get_rect() 
					self.rect.centerx = x 
					self.rect.centery = y
				elif pos=="y": 
					self.image=pygame.Surface((ln,3)) 
					self.image.fill((0,0,0))
					self.rect = self.image.get_rect() 
					self.rect.centerx = x 
					self.rect.centery = y
		class Dot(pygame.sprite.Sprite): 
			def init(self,x,y,c):
				pygame.sprite.Sprite.init(self) 
				self.image=pygame.surface.Surface((5,5)) 
				if c==1:
					self.image.fill((0,0,0)) 
				if c==2:
					self.image.fill((255,0,0))
				if c==3:
					self.image.fill((252,15,192)) 
				if c==4:
					self.image.fill((0,191,255)) 
				self.rect=self.image.get_rect() 
				self.rect.centerx=x 
				self.rect.centery=y
		per=7.5
		def Calc(func): 
			d=30
			if tp==1:
				night=[-6, -4, -1, -2, -1, -3, -3, -8, -2, -6, -6, 1, -5, -3, 5, 3, 1, -4, -2,
				-5, 3, 4, 5, 8, 4, 7, 4, 3, 4, 6, 7]
				day=[-2, -2, 1, 1, -1, -1, 1, -2, -2, -4, -3, 4, -3, 6, 8, 3, 5, 5, 4, 8, 8,
				6, 11, 8, 9, 7, 9, 9, 8, 4, 5]
				d=31
			if tp==2:
				night=[0, 6, 7, 7, 5, 5, 3, 1, 5, 6, 7, 4, 7, 4, 1, 3, 8, 9, 9, 5, 5, 6, 5, 7,
				10, 11, 7, 9, 4, 2]
				day=[8, 10, 13, 13, 11, 14, 11, 13, 14, 12, 15, 17, 18, 9, 9, 13, 14,
				13, 17, 16, 16, 15, 19, 21, 19, 14, 18, 13, 11, 12]
				d=30
			if tp==3:
				night=[6, 2, 10, 4, 7, 1, 0, -1, 0, 7, 9, 7, 10, 11, 6, 9, 9, 11, 14, 11,
				10, 10, 11, 16, 14, 13, 16, 11, 9, 12, 13 ]
				day=[7, 15, 14, 15, 6, 6, 8, 10, 13, 16, 12, 21, 22, 16, 20, 20, 24,
				25, 17, 15, 17, 19, 16, 21, 18, 23, 21, 16, 21, 22, 21]
				d=31
				i=0
			while i<d:
				dot=Dot(30+(i+1)*per*2,250-night[i]*per, 1)
				all_sprites.add(dot) 
				dot=Dot(30+(i+1)*per*2,250-day[i]*per, 2) 
				all_sprites.add(dot)
				ytro=(night[i]+day[i])/2 
				dot=Dot(30+(i+1)*per*2,250-ytro*per, 3) 
				all_sprites.add(dot)
				if i<d-1: 
					vecher=((night[i+1]+day[i])/2)
					dot=Dot(30+(i+1)*per*2,250-vecher*per, 4) 
					all_sprites.add(dot)
				i=i+1
		func="6"
		line = Line("y",250,250, 470) 
		all_sprites.add(line)
		line1 = Line("x",30,250, 470) 
		all_sprites.add(line1)
		i=0
		while i<7:
			line2 = Line("y",30,250-i*per*5, 15) 
			all_sprites.add(line2)
			line2 = Line("y",30,250+i*per*5, 15) 
			all_sprites.add(line2)
			line2 = Line("x",30+i*per*10,250, 15) 
			all_sprites.add(line2)
			i=i+1
		calc = Calc(func) 
		while running:
			clock.tick(fps)
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					running = False 
			screen.fill((255,255,255))
			font=pygame.font.Font(None,30) 
			text=font.render("t",True, (28, 28, 28))
			screen.blit(text, (80,30))
			font1=pygame.font.Font(None,30) 
			text1=font1.render("date",True, (28, 28, 28))
			screen.blit(text1, (420,280))
			image=pygame.image.load("leg.jpg") 
			x,y=270,320
			screen.blit(image,(x,y))
			font2=pygame.font.Font(None,20) 
			text2=font2.render("0",True, (0, 0, 255))
			screen.blit(text2, (44,260))
			for i in range(5,35,5):
				font3=pygame.font.Font(None,20) 
				text3=font3.render(str(i),True, (0, 0, 255))
				screen.blit(text3, (30+i*per*2,260))
				text3=font3.render(str(i),True, (0, 0, 255)) 
				screen.blit(text3, (46,250-i*per))
				text3=font3.render("-"+str(i),True, (0, 0, 255)) 
				screen.blit(text3, (40,250+i*per))
			all_sprites.draw(screen) 
			pygame.display.flip()
	pygame.quit()
	if __name__ == '__main__':
		app = QApplication(sys.argv)
		w = Window1()

		w.setStyleSheet("background-color: white;") #ФОН w.button.clicked.connect(w.show_window_2) w.button.clicked.connect(w.close)
		w.show()
		sys.exit(app.exec)
