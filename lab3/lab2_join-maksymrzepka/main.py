import numpy as np
import pickle
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego id kategorii.
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(category_id, int):
        # txt = '''select film.title ,language.name , category.name                   
        #     from (((film_category                   
        #     inner join film                   
        #     on film_category.film_id = film.film_id)                  
        #     inner join language                   
        #     on language.language_id = film.language_id)                  
        #     inner join category                   
        #     on category.category_id = film_category.category_id)                  
        #     where film_category.category_id in (''' + str(category_id) + ''')  
        #     order by title, language.name asc'''


        x = """select film.title, language.name, category.name
                    from category 
                    inner join film_category using(category_id)
                    inner join film using(film_id)
                    inner join language using(language_id)
                    where category.category_id in (""" + str(category_id) + """)
                    order by film.title, language.name asc
                 """
        df = pd.read_sql(x, con=connection)
        df.columns = ['title', 'languge', 'category']
        
        return df
    else:
        return None
    
def number_films_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów w zadanej kategori przez id kategorii.
    Przykład wynikowej tabeli:
    |   |category   |count|
    |0	|Action 	|64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(category_id, int):
        x = """select category.name as "category", count(film.title)
                    from film 
                    inner join film_category on film.film_id = film_category.film_id 
                    inner join category on film_category.category_id = category.category_id
                    where category.category_id in (""" + str(category_id) + """)
                    group by category.name
                    order by category.name asc
                    """
        df = pd.read_sql(x, con=connection)
        df.columns = ['category', 'count']
        return df
    else:
        return None

def number_film_by_length(min_length: Union[int,float] = 0, max_length: Union[int,float] = 1e6 ) :
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów o dla poszczegulnych długości pomiędzy wartościami min_length a max_length.
    Przykład wynikowej tabeli:
    |   |length     |count|
    |0	|46 	    |64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    min_length (int,float): wartość minimalnej długości filmu
    max_length (int,float): wartość maksymalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(min_length,(int, float)) and isinstance(max_length,(int, float)) and min_length < max_length:
        x = """select film.length ,count(film.length) 
                 from film 
                 where film.length 
                 between """+str(min_length) + " and "+ str(max_length) +\
                "group by film.length"
        df = pd.read_sql(x, con=connection)

        return df
    else:
        return None

def client_from_city(city:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o listę klientów z zadanego miasta przez wartość city.
    Przykład wynikowej tabeli:
    |   |city	    |first_name	|last_name
    |0	|Athenai	|Linda	    |Williams
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    city (str): nazwa miaste dla którego mamy sporządzić listę klientów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(city, (str)):
        x = """select city.city, customer.first_name, customer.last_name
                        from customer 
                        inner join address on customer.address_id = address.address_id 
                        inner join city on address.city_id = city.city_id 
                        where city.city in ('""" + str(city) + """')
                        order by city asc"""
        df = pd.read_sql(x, con=connection)

        return df
    else:
        return None

def avg_amount_by_length(length:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o średnią wartość wypożyczenia filmów dla zadanej długości length.
    Przykład wynikowej tabeli:
    |   |length |avg
    |0	|48	    |4.295389
    
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    length (int,float): długość filmu dla którego mamy pożyczyć średnią wartość wypożyczonych filmów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(length, (int, float)):

        x = """select film.length as "length", avg(payment.amount) 
                    from payment 
                    inner join rental on payment.rental_id = rental.rental_id
                    inner join inventory on rental.inventory_id = inventory.inventory_id 
                    inner join film on inventory.film_id = film.film_id
                    where film.length = (""" + str(length) + """)
                    group by film.length
                    order by film.length asc
                    """
        df = pd.read_sql(x, con=connection)
        return df
    else:
        return None

def client_by_sum_length(sum_min:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o sumaryczny czas wypożyczonych filmów przez klientów powyżej zadanej wartości .
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |sum
    |0  |Brian	    |Wyman  	|1265
    
    Tabela wynikowa powinna być posortowane według sumy, imienia i nazwiska klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    sum_min (int,float): minimalna wartość sumy długości wypożyczonych filmów którą musi spełniać klient
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(sum_min, (int, float)):
        if sum_min > 0:
            x = """select customer.first_name, customer.last_name, sum(film.length)
                        FROM rental 
                        inner join inventory on rental.inventory_id = inventory.inventory_id 
                        inner join film on inventory.film_id = film.film_id
                        inner join customer on rental.customer_id = customer.customer_id
                        group by customer.first_name, customer.last_name
                        having sum(film.length) > (""" + str(sum_min) + """)
                        order by sum(film.length), customer.last_name, customer.first_name asc
                        """
            df = pd.read_sql(x, con=connection)
            return df
        else:
            return None 

def category_statistic_length(name:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o statystykę długości filmów w kategorii o zadanej nazwie.
    Przykład wynikowej tabeli:
    |   |category   |avg    |sum    |min    |max
    |0	|Action 	|111.60 |7143   |47 	|185
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    name (str): Nazwa kategorii dla której ma zostać wypisana statystyka
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(name, (str)):
        x = """select category.name, avg(film.length), sum(film.length), min(film.length), max(film.length) 
                    from film 
                    inner join film_category on film.film_id = film_category.film_id 
                    inner join category on film_category.category_id = category.category_id
                    where category.name in ('""" + str(name) + """')
                    group by category.name
                    order by category.name asc
                    """
        df = pd.read_sql(x, con=connection)     
        df.columns = ['category', 'avg','sum','min','max']
        return df
    else:
        return None


