import numpy as np
import pandas as pd
import json
movie=pd.read_csv("tmdb_5000_movies.csv")
credit=pd.read_csv("tmdb_5000_credits.csv")
movie["genres"]=movie["genres"].apply(json.loads)
movie["keywords"]=movie["keywords"].apply(json.loads)
movie["production_companies"]=movie["production_companies"].apply(json.loads)
movie["production_countries"]=movie["production_countries"].apply(json.loads)
movie["spoken_languages"]=movie["spoken_languages"].apply(json.loads)
for index,i in zip(movie.index,movie["genres"]):
    list1=[]
    for j in range(len(i)):
        list1.append((i[j]["name"]))
    movie.loc[index,"genres"]=str(list1)
for index,i in zip(movie.index,movie["keywords"]):
    list2=[]
    for j in range(len(i)):
        list2.append((i[j]["name"]))
    movie.loc[index,"keywords"]=str(list2)
for index,i in zip(movie.index,movie["production_companies"]):
    list3=[]
    for j in range(len(i)):
        list3.append((i[j]["name"]))
    movie.loc[index,"production_companies"]=str(list3)
for index,i in zip(movie.index,movie["production_countries"]):
    list4=[]
    for j in range(len(i)):
        list4.append((i[j]["name"]))
    movie.loc[index,"production_countries"]=str(list4)
for index,i in zip(movie.index,movie["spoken_languages"]):
    list5=[]
    for j in range(len(i)):
        list5.append((i[j]["name"]))
    movie.loc[index,"spoken_languages"]=str(list5)

    for index,i in zip(credit.index,credit["crew"]):
    list7=[]
    for j in range(len(i)):
        list7.append(i[j]["name"])
    credit.loc[index,"crew"]=str(list7)
