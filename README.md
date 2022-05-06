# VideoGameSales

### Web Service API
[Google docs](https://docs.google.com/document/d/1wVD14oyxRpuizfZ0eygW_ZdIu9lC_etwJ7h18_kag_8/edit?usp=sharing)

### Installation Instruction

1. Clone the respository to your machine or PC.

    ```
   git clone https://github.com/ParnThanatibordee/VideoGameSales.git
    ```
2. Change directory to the local repository by typing this command.

    ```
   cd VideoGameSales
    ```
3. Install virtualenv to your machine or PC by this command.

    ```
   py -m pip install virtualenv
    ```
4. Create virtual environment for VideoGameSales directory.

    ```
   py -m venv venv
    ```
5. Activate virtual environment.

    For Mac OS / Linux
    ```
   source venv\Scripts\activate
    ```
    
    For Window
    ```
   venv\Scripts\activate
    ```
6. Install all require packages by this command.

    ```
   pip install -r requirements.txt
    ```
7. Create database schema and import data

    ```
   sqlite3 vgsales.db < vgsales.schema
   sqlite3 vgsales.db
   
   sqlite> .mode csv
   sqlite> .import data/video_game.csv video_game
   sqlite> .import data/sales.csv sales
   sqlite> .quit
    ```
8. Start the Application in main.py

    ```
   main.py
    ```
   

### UML class
![UML](https://user-images.githubusercontent.com/64191096/165668031-e420556a-e74e-4bf5-9860-d7685559f063.png)


### Package diagram
![Package](https://user-images.githubusercontent.com/64191096/165671098-e96400d1-5dbe-43fc-bf87-cd33f354e3ae.png)
