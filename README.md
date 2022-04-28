# VideoGameSales

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


### Package diagram