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
       
class MoneyApp(MDApp):
    
    def build(self): 
        self.icon = "moveby.png"
        self.theme_cls.primary_palette ="Blue"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style="Light"
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("welcome.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("dashboard.kv"))
        return screen_manager
    
    def on_start(self):
        Clock.schedule_once(self.login, 3)
        screen_manager.current = "welcome"
    def login(self, *args):
        screen_manager.current = "login"  
    def dash(self):
        screen_manager.current = "dashboard"   
    def show(self):
        dialog = MDDialog(type="simple",
                        text="Congratulation\nYou have successfully apply for your loan chech Email for more details")
        dialog.open() 
        
MoneyApp().run()       