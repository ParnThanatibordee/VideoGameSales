import tkinter as tk
from tkinter import ttk, RIGHT, BOTTOM, Y, X, NO, CENTER

from dao.sales_dao import SaleDao
from dao.video_game_dao import VideoGameDao
from game_sale import GameSale
from model.update_models import UpdateVideoGame, UpdateSale


class GameSaleUI(tk.Tk):
    def __init__(self, game_sale: GameSale, factory_name):
        super().__init__()
        self.game_sale = game_sale
        self.title("Video Game Sales")
        self.game_sale.set_factory(factory_name)

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
        table_frame = tk.Frame(self)
        table_frame.grid(row=1, column=0, padx=5, pady=5)

        # scrollbar
        table_scroll = tk.Scrollbar(table_frame)
        table_scroll.pack(side=RIGHT, fill=Y)

        table_scroll = tk.Scrollbar(table_frame, orient='horizontal')
        table_scroll.pack(side=BOTTOM, fill=X)

        my_table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set, xscrollcommand=table_scroll.set)

        my_table.pack()

        table_scroll.config(command=my_table.yview)
        table_scroll.config(command=my_table.xview)

        # define column
        if isinstance(self.game_sale.current_factory, VideoGameDao):
            my_table['columns'] = ('GameID', 'Name', 'Platform', 'Year', 'Genre', 'Publisher')

            # format our column
            my_table.column("#0", width=0, stretch=NO)
            my_table.column("GameID", anchor=CENTER, width=80)
            my_table.column("Name", anchor=CENTER, width=80)
            my_table.column("Platform", anchor=CENTER, width=80)
            my_table.column("Year", anchor=CENTER, width=80)
            my_table.column("Genre", anchor=CENTER, width=80)
            my_table.column("Publisher", anchor=CENTER, width=80)

            # Create Headings
            my_table.heading("#0", text="", anchor=CENTER)
            my_table.heading("GameID", text="GameID", anchor=CENTER)
            my_table.heading("Name", text="Name", anchor=CENTER)
            my_table.heading("Platform", text="Platform", anchor=CENTER)
            my_table.heading("Year", text="Year", anchor=CENTER)
            my_table.heading("Genre", text="Genre", anchor=CENTER)
            my_table.heading("Publisher", text="Publisher", anchor=CENTER)

            # add data
            game_records = self.game_sale.get_all()
            for i, record in enumerate(game_records):
                my_table.insert(parent='', index='end', iid=i, text='',
                                values=(f'{record.GameID}', f'{record.Name}', f'{record.Platform}', f'{record.Year}',
                                        f'{record.Genre}', f'{record.Publisher}'))
        elif isinstance(self.game_sale.current_factory, SaleDao):
            my_table['columns'] = ('GameID', 'NA Sales', 'EU Sales', 'JP Sales', 'Other Sales', 'Global Sales')

            # format our column
            my_table.column("#0", width=0, stretch=NO)
            my_table.column("GameID", anchor=CENTER, width=80)
            my_table.column("NA Sales", anchor=CENTER, width=80)
            my_table.column("EU Sales", anchor=CENTER, width=80)
            my_table.column("JP Sales", anchor=CENTER, width=80)
            my_table.column("Other Sales", anchor=CENTER, width=80)
            my_table.column("Global Sales", anchor=CENTER, width=80)

            # Create Headings
            my_table.heading("#0", text="", anchor=CENTER)
            my_table.heading("GameID", text="GameID", anchor=CENTER)
            my_table.heading("NA Sales", text="NA Sales", anchor=CENTER)
            my_table.heading("EU Sales", text="EU Sales", anchor=CENTER)
            my_table.heading("JP Sales", text="JP Sales", anchor=CENTER)
            my_table.heading("Other Sales", text="Other Sales", anchor=CENTER)
            my_table.heading("Global Sales", text="Global Sales", anchor=CENTER)

            # add data
            game_records = self.game_sale.get_all()
            for i, record in enumerate(game_records):
                my_table.insert(parent='', index='end', iid=i, text='',
                                values=(f'{record.GameID}', f'{record.NA_Sales_in_millions}',
                                        f'{record.EU_Sales_in_millions}',
                                        f'{record.JP_Sales_in_millions}',
                                        f'{record.Other_Sales_in_millions}',
                                        f'{record.Global_Sales_in_millions}'))

    def set_table(self, table):
        self.destroy()
        self.__init__(self.game_sale, table)

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
        self.destroy()
        if isinstance(self.game_sale.current_factory, VideoGameDao):
            self.__init__(self.game_sale, 'video_game')
        elif isinstance(self.game_sale.current_factory, SaleDao):
            self.__init__(self.game_sale, 'sales')
        self.search_window()

    def run(self):
        self.mainloop()
