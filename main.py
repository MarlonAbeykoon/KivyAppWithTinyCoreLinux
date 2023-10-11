from kivy.app import App
from kivy.uix.button import Button
import subprocess


class TinyCoreApp(App):

    def build(self):
        return Button(text="Start Tiny Core Linux", on_press=self.start_tinycore)

    def start_tinycore(self, instance):
        cmd = [
            "qemu-system-x86_64",
            "-cdrom", "/Users/admin/Downloads/TinyCore-current.iso",
            "-m", "512M"
        ]
        subprocess.Popen(cmd)


if __name__ == '__main__':
    TinyCoreApp().run()