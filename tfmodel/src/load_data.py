import os
import pymongo
import pandas as pd

user = os.environ.get('MONGO_USERNAME')
password = os.environ.get('MONGO_PASSWORD')
host = 'mongo'
port = '27017'

myclient = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")

mydb = myclient["mlphotel"]

url_data = "https://media.githubusercontent.com/media/fpleoni/where_do_we_go_from_here/master/data/hotels_com_scrape_v3.csv"


def loaded() -> bool:
    collist = mydb.list_collection_names()
    return "hoteldf" in collist


def loaded() -> bool:
    collist = mydb.list_collection_names()
    return "hoteldf" in collist


def load_df():
    if not loaded():
        hotels_df = pd.read_csv(url_data, header=None)
        hotels_df.rename({0: "location", 1: "hotel_name", 2: "rating", 3: "popularity_rating",
                          4: "address", 5: "locality", 6: "landmark",
                          7: "price", 8: "URL"}, inplace=True, axis=1)

        # Split location
        location_df = hotels_df["location"].str.split(",", expand=True)

        # Rename landmark columns
        location_df.rename({0: "city", 1: "country"}, inplace=True, axis=1)

        # Merge landmarks_df with hotels_df
        hotels_df = pd.merge(location_df, hotels_df[["hotel_name", "rating", "address",
                                                     "locality", "price", "landmark", "URL"]],
                             left_index=True,
                             right_index=True, how="right")

        hotels_df["city"] = hotels_df["city"].apply(lambda x: x.lower())
        hotels_df["country"] = hotels_df["country"].apply(lambda x: x.lower())
        hotels_df["hotel_name"] = hotels_df["hotel_name"].apply(lambda x: x.lower())
        hotels_df["locality"] = hotels_df["locality"].apply(lambda x: x.lower())

        # Convert all landmarks to strings
        hotels_df["landmark"] = hotels_df["landmark"].apply(lambda x: str(x))

        # Convert all landmarks to lowercase
        hotels_df["landmark"] = hotels_df["landmark"].apply(lambda x: x.lower())

        # Split landmark
        hotels_df["landmark"] = hotels_df["landmark"].str.split("\n")

        hotels_dict = hotels_df.to_dict(orient='records')

        mycol = mydb["hoteldf"]

        mycol.insert_many(hotels_dict)

        return hotels_df

    else:
        mycol = mydb["hoteldf"]

        hotelfromdb = list(mycol.find())
        hotels_df = pd.DataFrame(hotelfromdb)

        return hotels_df
