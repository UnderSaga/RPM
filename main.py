if __name__ == '__main__':
    from tkinter import *
    from tkinter import messagebox
    from tkinter import ttk

    window = Tk()
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2.3
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 3
    window.wm_geometry("+%d+%d" % (x, y))
    window.geometry('{}x{}'.format(int(window.winfo_screenwidth() * 0.3), int(window.winfo_screenheight() * 0.53)))
    window.resizable(False, False)
    window.title('БуйКоин')

    MiningWind = LabelFrame(window,
                            width=int(window.winfo_screenwidth() * 0.3), height=int(window.winfo_screenheight() * 0.55),
                            bd=0)
    ShopWind = LabelFrame(window,
                          text='Магазин',
                          width=int(window.winfo_screenwidth() * 0.3), height=int(window.winfo_screenheight() * 0.2),
                          bd=0,
                          font='25')

    # Переменные
    with open('C:\BuyCoin\save.txt') as f:
        lines = f.read().splitlines()
    counter = float(lines[0])
    count = float(lines[1])
    S = float(lines[2])
    Buyok = float(lines[3])
    Coin = PhotoImage(file=r"C:\BuyCoin\Image\b_coin.png")
    Clic = PhotoImage(file=r"C:\BuyCoin\Image\upgrade_click.png")
    MiningUper = PhotoImage(file=r"C:\BuyCoin\Image\upgrade_mining_power.png")
    achiv = float(lines[4])
    r_var = IntVar()
    r_var.set(0)

    # Функции
    def Click():
        global S, count, achiv
        count += S
        Score['text'] = "%.1f" % count
        if count == achiv + 100:
            messagebox.showinfo("Молодец", "Ну ты и кликер")
            achiv = count + 100

    def Night():
        ButClick['bg'] = '#29313D'
        ButClick['fg'] = '#fff'
        ButClick['activebackground'] = '#29313D'
        Score['bg'] = '#29313D'
        Score['fg'] = '#fff'
        label['bg'] = '#29313D'
        label['fg'] = '#fff'
        MiningOn['bg'] = '#29313D'
        MiningOn['activebackground'] = '#29313D'
        MiningOn['fg'] = '#ff0000'
        MiningOn['disabledforeground'] = '#00e600'
        MiningOff['bg'] = '#29313D'
        MiningOff['activebackground'] = '#29313D'
        MiningOff['fg'] = '#ff0000'
        MiningOff['disabledforeground'] = '#00e600'
        window['bg'] = '#29313D'
        ShopWind['bg'] = '#29313D'
        ShopWind['fg'] = '#fff'
        MiningWind['bg'] = '#29313D'
        OnClick['bg'] = '#29313D'
        OnClick['fg'] = '#fff'
        OnSek['bg'] = '#29313D'
        OnSek['fg'] = '#fff'

    def white():
        ButClick['bg'] = '#fff'
        ButClick['fg'] = '#000'
        ButClick['activebackground'] = '#fff'
        Score['bg'] = '#fff'
        Score['fg'] = '#000'
        label['bg'] = '#fff'
        label['fg'] = '#000'
        MiningOn['bg'] = '#fff'
        MiningOn['activebackground'] = '#fff'
        MiningOn['fg'] = '#000'
        MiningOff['bg'] = '#fff'
        MiningOff['activebackground'] = '#fff'
        MiningOff['fg'] = '#000'
        window['bg'] = '#fff'
        ShopWind['bg'] = '#fff'
        ShopWind['fg'] = '#000'
        MiningWind['bg'] = '#fff'
        OnClick['bg'] = '#fff'
        OnClick['activebackground'] = '#fff'
        OnClick['fg'] = '#000'
        OnSek['bg'] = '#fff'
        OnSek['fg'] = '#000'

    def Green():
        ButClick['bg'] = '#215B46'
        ButClick['fg'] = '#000'
        ButClick['activebackground'] = '#215B46'
        Score['bg'] = '#215B46'
        Score['fg'] = '#000'
        label['bg'] = '#215B46'
        label['fg'] = '#000'
        MiningOn['bg'] = '#215B46'
        MiningOn['activebackground'] = '#215B46'
        MiningOn['fg'] = '#ff0000'
        MiningOn['disabledforeground'] = '#00e600'
        MiningOff['bg'] = '#215B46'
        MiningOff['activebackground'] = '#215B46'
        MiningOff['fg'] = '#ff0000'
        MiningOff['disabledforeground'] = '#00e600'
        window['bg'] = '#215B46'
        ShopWind['bg'] = '#215B46'
        ShopWind['fg'] = '#000'
        MiningWind['bg'] = '#215B46'
        OnClick['bg'] = '#215B46'
        OnClick['fg'] = '#000'
        OnSek['bg'] = '#215B46'
        OnSek['fg'] = '#000'

    def MiningOn():
        global running
        running = True
        counter_label(label)
        MiningOn['state'] = 'disabled'
        MiningOff['state'] = 'normal'

    def MiningOff():
        global running
        running = False
        counter_label(label)
        MiningOn['state'] = 'normal'
        MiningOff['state'] = 'disabled'

    def counter_label(label):
        def count():
            if running:
                global counter
                display = str(counter)
                label['text'] = display
                label.after(1000, count)
                counter += Buyok
                pb.start()
                pb.step(1)
        count()

    def ButUper():
        global S, counter
        if counter >= 100:
            S *= 1.1
            counter -= 100
            OnClick['text'] = 'за клик:' + "%.1f" % S

    def upMining():
        global Buyok, count
        if count >= 150:
            Buyok += 1
            count -= 150
            Score['text'] = "%.1f" % count
            OnSek['text'] = str(Buyok) + '/сек'

    def Save():
        global counter
        with open('C:\BuyCoin\save.txt', 'w+') as file:
            file.write(str(counter) + '\n')
            file.write(str(count) + '\n')
            file.write(str(S) + '\n')
            file.write(str(Buyok) + '\n')
            file.write(str(achiv) + '\n')

    # Объекты
    MiningOn = Radiobutton(MiningWind,
                           text='С майнингом',
                           command=MiningOn,
                           fg='#f00',
                           disabledforeground='#00e600',
                           activebackground='#fff',
                           variable=r_var, value=1)

    MiningOff = Radiobutton(MiningWind,
                            text='С майнингом',
                            command=MiningOff,
                            fg='#f00',
                            disabledforeground='#00e600',
                            activebackground='#fff',
                            variable=r_var, value=0)

    Score = Label(MiningWind,
                  text=count,
                  font='25')

    OnClick = Label(ShopWind,
                    text='за клик:' + str(S),
                    font='20')

    OnSek = Label(ShopWind,
                  text=str(Buyok) + '/сек',
                  font='20')

    ButClick = Button(MiningWind,
                      text='Click',
                      width=256, height=256,
                      font='25',
                      bd=0,
                      command=Click,
                      image=Coin)

    label = Label(MiningWind,
                  text="",
                  fg="black",
                  font="Verdana 12 bold")

    ButUp = Button(ShopWind,
                   text='Улучшить',
                   width=184, height=92,
                   font='30',
                   command=ButUper,
                   image=Clic,
                   bg='#29313D',
                   activebackground='#29313D',
                   bd=5)

    ButMiningUper = Button(ShopWind,
                           width=184, height=92,
                           command=upMining,
                           image=MiningUper,
                           bg='#29313D',
                           activebackground='#29313D',
                           bd=5)

    pb = ttk.Progressbar(MiningWind, orient='horizontal',
                     mode='determinate',
                     maximum=380, value=0,
                     length=200)

    # Меню
    menu = Menu(window)
    window.config(menu=menu)

    FrameMenu = Menu(menu)
    ColorMenu = Menu(menu)
    ColorMenu.add_command(label='Тёмная', command=Night)
    ColorMenu.add_command(label='Светлая', command=white)
    ColorMenu.add_command(label='Зелёная', command=Green)
    menu.add_cascade(label='Темы', menu=ColorMenu)
    menu.add_command(label='Сохранение', command=Save)

    # Спавн объектов
    ButClick.pack()
    Score.pack()
    label.pack()
    MiningOn.pack()
    MiningOff.pack()
    pb.pack()
    ButUp.grid(row=0, column=0)
    OnClick.grid(row=1, column=0)
    ButMiningUper.grid(row=0, column=1)
    OnSek.grid(row=1, column=1)
    ShopWind.pack(side=BOTTOM)
    MiningWind.pack(side=TOP)

    window.mainloop()