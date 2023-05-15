import tkinter as tk
import threading
import time

class FocusTimer:
    def __init__(self, minutes):
        self.seconds = minutes * 60
        self.window = tk.Tk()
        self.label = tk.Label(self.window, text="", font=("Arial", 24))
        self.label.pack(padx=20, pady=20)
        self.start_button = tk.Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        self.window.title("Focus Timer")
        self.window.resizable(False, False)
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            threading.Thread(target=self.timer_thread).start()

    def timer_thread(self):
        while self.seconds > 0 and self.timer_running:
            self.update_label()
            time.sleep(1)
            self.seconds -= 1
        
        self.timer_running = False
        self.update_label()
        self.stop_timer()

    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_label(self):
        minutes_remaining = self.seconds // 60
        seconds_remaining = self.seconds % 60
        timer_display = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
        self.label.config(text=timer_display)

    def run(self):
        self.window.mainloop()

# 使用示例：设置一个25分钟的专注时钟
focus_timer = FocusTimer(25)
focus_timer.run()
