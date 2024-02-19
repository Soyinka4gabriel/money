from cgitb import text
from tkinter import dialog
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.clock import  Clock

Window.size=(320,600)
class MainWid(Screen):
    pass
       
class MoveByApp(MDApp):
    
    def build(self): 
        self.icon = "moveby.png"
        self.theme_cls.primary_palette ="Green"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style="Dark"
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("moveby.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("check.kv"))
        
        

        return screen_manager
    def on_start(self):
         Clock.schedule_once(self.login, 2)
         screen_manager.current = "welcome"
    def login(self, *args):
        screen_manager.current = "login"  
    def car(self):
        screen_manager.current = "check"    
        
MoveByApp().run()       