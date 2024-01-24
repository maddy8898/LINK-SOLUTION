from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
import sqlite3
import pyodbc as pyo

class LoginScreen(Screen):
    pass
class SuccessScreen(Screen):
    pass
class SalesScreen(Screen):
    pass
class PurchaseScreen(Screen):
    pass

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "A700"
        return Builder.load_file("login_app.kv")

    def on_login(self, username, password):
        conn_string = ('Driver={SQL Server}; server=MAHESH\SQLEXPRESS; database=KARAN_LINK;Trusted_connection=yes;')
        my_conn = pyo.connect(conn_string,autocommit=True)
        cursor = my_conn.cursor()
        cursor.execute(' select * from comp_user where uname=? and upass=? ',(username,password))
        data = cursor.fetchall()
        my_conn.close()
        if data:
            self.root.current = "success_screen"
        else:
            self.root.ids.status_label.text = "Invalid credentials"
    
    def on_press_sales(self,screen_name):
        if screen_name == "sales_screen":
            self.root.current = "sales_screen"
        
    def on_press_purchase(self,screen_name):
        if screen_name == "purchase_screen":
            self.root.current = "purchase_screen"

if __name__ == "__main__":
    LoginApp().run()
