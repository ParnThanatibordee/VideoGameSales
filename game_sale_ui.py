import tkinter as tk
from tkinter import ttk

from dao.sales_dao import SaleDao
from dao.video_game_dao import VideoGameDao
from game_sale import GameSale
from model.update_models import UpdateVideoGame, UpdateSale


class GameSaleUI(tk.Tk):
    def __init__(self, game_sale: GameSale):
        super().__init__()
        self.game_sale = game_sale
        self.title("Video Game Sales")
        self.game_sale.set_factory('video_game')

        self.search_GameID = tk.StringVar()
        self.update_Name = tk.StringVar()
        self.update_Platform = tk.StringVar()
        self.update_Year = tk.StringVar()
        self.update_Genre = tk.StringVar()
        self.update_Publisher = tk.StringVar()

        self.update_NA = tk.StringVar()
        self.update_EU = tk.StringVar()
        self.update_JP = tk.StringVar()
        self.update_Other = tk.StringVar()
        self.update_Global = tk.StringVar()

        self.init_components()

    def init_components(self):
        table_bar = tk.Menu(self)
        self.config(menu=table_bar)

        table_menu = tk.Menu(table_bar, tearoff=0)
        table_bar.add_cascade(menu=table_menu, label='Table')
        table_menu.add_command(label='video game', command=lambda x=None: self.set_table('video_game'))
        table_menu.add_command(label='sale', command=lambda x=None: self.set_table('sales'))
        table_menu.add_separator()
        table_menu.add_command(label='Exit', command=self.quit)

        # search/update
        self.search_field = tk.Entry(self, width=20, textvariable=self.search_GameID)
        convert_button = tk.Button(self, text='search/update', command=self.search_window)
        self.search_field.grid(row=0, column=0, padx=5, pady=5)
        convert_button.grid(row=0, column=1, padx=5, pady=5)

        # display table

    def set_table(self, table):
        self.game_sale.set_factory(table)

    def search_window(self):
        if self.search_field.get() != "":
            self.top = tk.Toplevel(self)
            self.top.title("search/update")
            self.top.transient(self)
            self.top.grab_set()

            try:
                tk.Label(self.top, text=self.game_sale.get(int(self.search_field.get()))).grid(row=0, column=0, padx=5, pady=5)
            except:
                tk.Label(self.top, text="Not found.").grid(row=0, column=0, padx=5, pady=5)
                return None

            if isinstance(self.game_sale.current_factory, VideoGameDao):
                self.name_label = tk.Label(self.top, text="Name:").grid(row=1, column=0, padx=5, pady=5)
                self.platform_label = tk.Label(self.top, text="Platform:").grid(row=2, column=0, padx=5, pady=5)
                self.year_label = tk.Label(self.top, text="Year:").grid(row=3, column=0, padx=5, pady=5)
                self.genre_label = tk.Label(self.top, text="Genre:").grid(row=4, column=0, padx=5, pady=5)
                self.publisher_label = tk.Label(self.top, text="Publisher:").grid(row=5, column=0, padx=5, pady=5)
                self.name_field = tk.Entry(self.top, width=20, textvariable=self.update_Name)
                self.name_field.grid(row=1, column=1, padx=5, pady=5)
                self.platform_field = tk.Entry(self.top, width=20, textvariable=self.update_Platform)
                self.platform_field.grid(row=2, column=1, padx=5, pady=5)
                self.year_field = tk.Entry(self.top, width=20, textvariable=self.update_Year)
                self.year_field.grid(row=3, column=1, padx=5, pady=5)
                self.genre_field = tk.Entry(self.top, width=20, textvariable=self.update_Genre)
                self.genre_field.grid(row=4, column=1, padx=5, pady=5)
                self.publisher_field = tk.Entry(self.top, width=20, textvariable=self.update_Publisher)
                self.publisher_field.grid(row=5, column=1, padx=5, pady=5)

            elif isinstance(self.game_sale.current_factory, SaleDao):
                self.NA_label = tk.Label(self.top, text="NA sales:").grid(row=1, column=0, padx=5, pady=5)
                self.EU_label = tk.Label(self.top, text="EU sales:").grid(row=2, column=0, padx=5, pady=5)
                self.JP_label = tk.Label(self.top, text="JP sales:").grid(row=3, column=0, padx=5, pady=5)
                self.Other_label = tk.Label(self.top, text="Other sales:").grid(row=4, column=0, padx=5, pady=5)
                self.Global_label = tk.Label(self.top, text="Global sales:").grid(row=5, column=0, padx=5, pady=5)
                self.NA_field = tk.Entry(self.top, width=20, textvariable=self.update_NA)
                self.NA_field.grid(row=1, column=1, padx=5, pady=5)
                self.EU_field = tk.Entry(self.top, width=20, textvariable=self.update_EU)
                self.EU_field.grid(row=2, column=1, padx=5, pady=5)
                self.JP_field = tk.Entry(self.top, width=20, textvariable=self.update_JP)
                self.JP_field.grid(row=3, column=1, padx=5, pady=5)
                self.Other_field = tk.Entry(self.top, width=20, textvariable=self.update_Other)
                self.Other_field.grid(row=4, column=1, padx=5, pady=5)
                self.Global_field = tk.Entry(self.top, width=20, textvariable=self.update_Global)
                self.Global_field.grid(row=5, column=1, padx=5, pady=5)

            update_button = tk.Button(self.top, text='update',
                                      command=lambda x=None: self.update_data(int(self.search_field.get())))
            update_button.grid(row=5, column=2, padx=5, pady=5)

            self.wait_window(self.top)

    def update_data(self, game_id):
        if isinstance(self.game_sale.current_factory, VideoGameDao):
            try:
                name_get = self.name_field.get()
            except:
                name_get = None
            try:
                platform_get = self.platform_field.get()
            except:
                platform_get = None
            try:
                year_get = int(self.year_field.get())
            except:
                year_get = None
            try:
                genre_get = self.genre_field.get()
            except:
                genre_get = None
            try:
                publisher_get = self.publisher_field.get()
            except:
                publisher_get = None

            update_model = UpdateVideoGame(Name=name_get, Platform=platform_get, Year=year_get, Genre=genre_get,
                                           Publisher=publisher_get)

        elif isinstance(self.game_sale.current_factory, SaleDao):
            try:
                na_get = float(self.NA_field.get())
            except:
                na_get = None
            try:
                eu_get = float(self.EU_field.get())
            except:
                eu_get = None
            try:
                jp_get = float(self.JP_field.get())
            except:
                jp_get = None
            try:
                other_get = float(self.Other_field.get())
            except:
                other_get = None
            try:
                global_get = float(self.Global_field.get())
            except:
                global_get = None

            update_model = UpdateSale(NA_Sales_in_millions=na_get, EU_Sales_in_millions=eu_get
                                      , JP_Sales_in_millions=jp_get, Other_Sales_in_millions=other_get,
                                      Global_Sales_in_millions=global_get)

        self.game_sale.current_factory.update(game_id, update_model)

        self.top.destroy()
        self.search_window()

    def run(self):
        self.mainloop()
