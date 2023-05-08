import tkinter as tk
from datetime import datetime

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=200)
        self.canvas.pack()
        
        # create timer text field
        self.timer_text = self.canvas.create_text(200, 50, text='00:00:00', font=('Arial', 24))
        
        # create input field for countdown time
        self.countdown_label = self.canvas.create_text(50, 100, text='Erän pituus:', font=('Arial', 12))
        self.countdown_entry = tk.Entry(master, width=10)
        self.canvas.create_window(180, 100, window=self.countdown_entry)
        
        # create input field for rest time
        self.rest_label = self.canvas.create_text(50, 130, text='Tauon pituus:', font=('Arial', 12))
        self.rest_entry = tk.Entry(master, width=10)
        self.canvas.create_window(180, 130, window=self.rest_entry)

        # create input field for countdown time
        self.count_label = self.canvas.create_text(50, 160, text='Erien määrä:', font=('Arial', 12))
        self.count_entry = tk.Entry(master, width=10)
        self.canvas.create_window(180, 160, window=self.count_entry)

        self.start_time = None
        self.remaining_time = None
        self.update_clock()
        
    def update_clock(self):
        # update timer text field as before
        if self.start_time is not None:
            elapsed_time = int((datetime.now() - self.start_time).total_seconds())
            if self.remaining_time is not None:
                remaining_time = self.remaining_time - elapsed_time
                if remaining_time <= 0:
                    self.canvas.itemconfig(self.timer_text, text='00:00:00')
                    self.remaining_time = None
                else:
                    minutes, seconds = divmod(remaining_time, 60)
                    hours, minutes = divmod(minutes, 60)
                    time_string = f'{hours:02}:{minutes:02}:{seconds:02}'
                    self.canvas.itemconfig(self.timer_text, text=time_string)
            else:
                self.remaining_time = int(self.countdown_entry.get())
            
        # call update_clock method every second
        self.master.after(1000, self.update_clock)
        
    def start(self):
        self.start_time = datetime.now()
        
    def stop(self):
        self.start_time = None
        
root = tk.Tk()
app = TimerApp(root)
start_button = tk.Button(root, text='Start', command=app.start)
start_button.pack(side='left')
stop_button = tk.Button(root, text='Stop', command=app.stop)
stop_button.pack(side='left')
reset_button = tk.Button(root, text='Reset', command=lambda: app.canvas.itemconfig(app.timer_text, text='00:00:00'))
reset_button.pack(side='left')
root.mainloop()
