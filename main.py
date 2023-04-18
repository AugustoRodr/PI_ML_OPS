from fastapi import FastAPI
import pandas as pd

app=FastAPI()

df= pd.read_csv('df_general.csv')

#Query 1

@app.get('/get_max_duration')
async def get_max_duration(anio:int, plat:str, tipo:str):
    try:
        if plat.lower() in df.Plataforma.unique():
            df_temp=df.loc[:,['title','release_year','Plataforma','duration_int','duration_type']].copy()
            filtro=df_temp[((df_temp.release_year==anio) & (df_temp.Plataforma==plat.lower()) & (df_temp.duration_type==tipo.lower()))].duration_int.idxmax()
            return df_temp.iloc[filtro].to_dict()
        else:
            return 'Ingreso una plataforma incorrecta.'
        
    except Exception:

        return 'ERROR. Revise los parametros ingresados.'


#Query 2

@app.get('/get_score_count')
async def get_score_count(plat:str,scored:float,anio:int):
    try:
        if plat.lower() in df.Plataforma.unique():
            df_temp=df.loc[:,['Plataforma','type','release_year','score']]
            return {f'Peliculas de {plat.capitalize()}': len(df_temp[((df_temp.release_year==anio)&(df_temp.type=="movie")&(df_temp.Plataforma==plat.lower())&(df_temp.score>scored))])}
        else:
            return 'Ingreso una plataforma incorrecta'
    except Exception:
        return 'ERROR. Revise los parametros ingresados.'


#Query 3

@app.get('/get_count_platform')
async def get_count_platform(plat:str):
    try:
        if plat.lower() in df.Plataforma.unique():
            df_temp=df.loc[:,['Plataforma','type']]
            return {f'Paliculas {plat.capitalize()}':len(df_temp[((df_temp.Plataforma==plat.lower())&(df_temp.type=="movie"))])}
        else:
            return f'Ingreso una plataforma incorrecta'
    except Exception:
        
        return f'ERROR. Revise los parametros ingresados.'


#Query 4

@app.get('/get_actor')
async def get_actor(plataforma:str,anio:int):
    try:
        # CREACION, CARGA Y CONTEO DE ACTORES SEGUN LOS FILTROS
        lista_anio=sorted(list(df.release_year.unique()))
        lista_plat=list(df.Plataforma.unique())
        act_dict={plat:{anio:{} for anio in lista_anio} for plat in lista_plat}
        for plat in lista_plat:
            df_temp=df[df.Plataforma==plat]
            for anios in lista_anio:
                df_temp2=df_temp[df_temp.release_year==anios]
                for i in df_temp2.cast:
                    if i != 'sin informacion':
                        actores=i.split(',')
                        for actor in actores:
                            actor=actor.strip()
                            if actor in act_dict[plat][anios]:
                                act_dict[plat][anios][actor]+=1
                            else:
                                act_dict[plat][anios][actor]=1
        # Creacion del df de actores
        tabla_actores=[]
        for plataformas in act_dict:
            for anios in act_dict[plataformas]:
                for actor in act_dict[plataformas][anios]:
                    tabla_actores.append([plataformas,anios,actor,act_dict[plataformas][anios][actor]])
        df_actores=pd.DataFrame(tabla_actores, columns=['Plataforma','Anios','Actor','Cantidad'])

        if plataforma.lower() in df_actores.Plataforma.unique():
            indice= df_actores[((df_actores.Plataforma==plataforma.lower())&(df_actores.Anios==anio))].Cantidad.idxmax()
            #return df_actores.iloc[indice].to_dict()
            return {'Actor':df_actores.iloc[indice].Actor}
        elif plataforma.lower()=='hulu':
            return'La Plataforma de Hulu no posee actores'
        else:
            return 'Ingreso una plataforma incorrecta'

    except Exception:
        return 'ERROR. Revise los parametros ingresado.'


#Query 5

@app.get('/prod_per_county')
async def prod_per_county(tipo:str,pais:str,anio:int):
    try:
        df_temp=df[df.type==tipo.lower()]
        lista_anio=sorted(list(df_temp.release_year.unique()))
        pais_dict={anio:{} for anio in lista_anio}

        for anios in lista_anio:
            df_temp2=df_temp[df_temp.release_year==anios]
            for i in df_temp2.country:
                if type(i)==str:
                    countries=i.split(',')
                    for country in countries:
                        country=country.strip()
                        if country in pais_dict[anios]:
                            pais_dict[anios][country]+=1
                        else:
                            pais_dict[anios][country]=1

        cont_paices=[]
        for anios in pais_dict:
            for country in pais_dict[anios]:
                cont_paices.append([anios,country,tipo.lower(),pais_dict[anios][country]])

        df_temp2=pd.DataFrame(cont_paices, columns=['Anios','Pais','Tipo','Cantidad'])

        filtro=df_temp2[((df_temp2.Pais==pais.lower())&(df_temp2.Anios==anio))].Cantidad.idxmax()
        return df_temp2.iloc[filtro].to_dict()

    except Exception:
        return 'ERROR. Revise los parametros ingresados.'
    

#Query 6

@app.get('/get_contents')
async def get_contents(rating:str):
    try:
        return {f'Total de Rating {rating}': len(df[df.rating==rating])}
    except Exception:
        return 'ERROR. Revise los parametros ingresados.'
    
