import json
import psycopg2
import random
from datetime import datetime


def generator(max_places, prev_occupied):
    occupied = random.randrange(max(prev_occupied - 5, 0), min(max_places, prev_occupied + 5))
    return occupied
    

def handler(event, context):
    connection = psycopg2.connect(
        database=<id>, # Идентификатор подключения
        user=<user>, # Пользователь БД
        password=context.token["access_token"],
        host="<id>.postgresql-proxy.serverless.yandexcloud.net", # Точка входа
        port=<port>,
        sslmode="require")

    places = {'Kronverkskii 2-nd floor': 48, 'Kronverkskii 3-rd floor': 61,
     'Lomonosova 2-nd floor': 18, 'Lomonosova 4-th floor': 72}

    prev_occupied = {'Kronverkskii 2-nd floor': 26, 'Kronverkskii 3-rd floor': 46,
     'Lomonosova 2-nd floor': 3, 'Lomonosova 4-th floor': 18}

    index = {'Kronverkskii 2-nd floor': 1, 'Kronverkskii 3-rd floor': 2,
     'Lomonosova 2-nd floor': 3, 'Lomonosova 4-th floor': 4}
    
    for k, v in places.items():
        places_occupied = generator(v, prev_occupied[k])
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO occupied_space (coworking_id, places_occupied, time)
                            values (%s, %s, %s);""", [index[k], places_occupied,
                            datetime.now().strftime("%Y-%m-%d %H:%M")])
            connection.commit()
        
    
    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'event': 1,
                'context': 2,
            }, 
            default=vars,
        ),
    }
