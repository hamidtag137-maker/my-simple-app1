"""
برنامه ساده اندروید با WebView - نسخه دیباگ
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import os
import webbrowser

class SimpleWebViewApp(App):
    def build(self):
        # تنظیم رنگ پس‌زمینه
        Window.clearcolor = (0.9, 0.9, 0.9, 1)
        
        # ایجاد layout اصلی
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # عنوان
        title = Label(
            text="برنامه WebView ساده",
            size_hint_y=0.2,
            font_size='24sp',
            color=(0.2, 0.2, 0.2, 1)
        )
        layout.add_widget(title)
        
        # بررسی وجود فایل HTML
        html_path = os.path.join(os.path.dirname(__file__), 'index.html')
        html_exists = os.path.exists(html_path)
        
        status = Label(
            text=f"فایل HTML: {'✅ وجود دارد' if html_exists else '❌ وجود ندارد'}",
            size_hint_y=0.1
        )
        layout.add_widget(status)
        
        if html_exists:
            # نمایش محتوای HTML به صورت متن
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # نمایش بخشی از محتوا
            preview = Label(
                text=f"پیش‌نمایش HTML:\n{html_content[:200]}...",
                size_hint_y=0.4,
                text_size=(Window.width-40, None),
                halign='left',
                valign='top'
            )
            layout.add_widget(preview)
            
            # دکمه باز کردن در مرورگر
            def open_in_browser(btn):
                webbrowser.open(f'file://{html_path}')
            
            btn = Button(
                text="باز کردن در مرورگر",
                size_hint_y=0.15,
                background_color=(0.2, 0.6, 0.2, 1)
            )
            btn.bind(on_press=open_in_browser)
            layout.add_widget(btn)
        
        # دکمه خروج
        exit_btn = Button(
            text="خروج",
            size_hint_y=0.15,
            background_color=(0.8, 0.2, 0.2, 1)
        )
        exit_btn.bind(on_press=lambda x: App.get_running_app().stop())
        layout.add_widget(exit_btn)
        
        return layout

if __name__ == '__main__':
    SimpleWebViewApp().run()