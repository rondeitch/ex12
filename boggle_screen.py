import tkinter as tk


class Screen:
    def __init__(self, root, **kwargs):
        print(len(kwargs))
        self.__frame = tk.Frame(root, **kwargs)
        self.__objects = dict()

    @property
    def frame(self):
        return self.__frame

    @property
    def objects(self):
        return self.__objects

    def add(self, widget, name, **kwargs):
        self.__objects[name] = widget
        widget.pack(**kwargs)

    def remove(self, name):
        self.__objects[name].forget()
        self.__objects.pop(name)

    def pack(self, **kwargs):
        self.__frame.pack(**kwargs)

    def destroy(self):
        for widget in self.__frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    rt = tk.Tk()
    screen = Screen(rt)
    btn = tk.Button(screen, text="Start")
    screen.add(btn, "my_btn")
    rt.mainloop()
