import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, int):
        x = """SELECT film.title, language.name, category.name
               FROM film
               INNER JOIN language USING(language_id)
               INNER JOIN film_category USING(film_id)
               INNER JOIN category USING(category_id) 
               WHERE category_id IN (""" + str(category) + """)
               ORDER BY film.title, language.name ASC
            """
        df = pd.read_sql(x, con=connection)
        df.columns = ['title', 'languge', 'category']
        
        return df

    elif isinstance(category, str):
        xx = """SELECT film.title, language.name, category.name
                FROM film
                INNER JOIN language USING(language_id)
                INNER JOIN film_category USING(film_id)
                INNER JOIN category USING(category_id) 
                WHERE category.name IN """ + "('" + category + "')"
        xx += """ ORDER BY film.title, language.name ASC """
        df = pd.read_sql(xx, con=connection)
        df.columns = ['title', 'languge', 'category']

        return df
    else:
        return None
  
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, int):
        x = """SELECT film.title, language.name , category.name 
               FROM film  
               INNER JOIN language USING(language_id)
               INNER JOIN film_category USING(film_id)
               INNER JOIN category USING(category_id) 
               WHERE category_id IN (""" + str(category) + """)
               ORDER BY film.title, language.name ASC 
            """
        df = pd.read_sql(x, con=connection)
        df.columns = ['title', 'languge', 'category']
        return df

    elif isinstance(category, str):
        xx = """SELECT film.title, language.name, category.name
                FROM film 
                INNER JOIN language USING(language_id)
                INNER JOIN film_category USING(film_id)
                INNER JOIN category USING(category_id) 
                WHERE category.name  ~* """ + "'" + (category) + "'"         
        xx += """ ORDER BY film.title, language.name ASC """
        df = pd.read_sql(xx, con=connection)
        df.columns = ['title', 'languge', 'category']
        return df
    else:
        return None
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(title, str):
        x = """ SELECT actor.first_name, actor.last_name
                FROM film  
                INNER JOIN film_actor USING(film_id)
                INNER JOIN actor USING(actor_id)
                WHERE film.title IN """ + "('" + (title) +"') "
        x += """ ORDER BY  actor.last_name asc, actor.first_name """
        df = pd.read_sql(x, con=connection)
        return df
    else:
        return None
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    