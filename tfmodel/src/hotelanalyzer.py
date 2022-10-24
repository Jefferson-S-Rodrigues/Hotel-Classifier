import numpy as np
import tensorflow as tf

from src.dao import DAO


def get_model():
    """ Return model architecture and weights """

    local_models = 'models'

    # Import embeddings model and weights
    model = tf.keras.models.load_model(f"{local_models}/embeddings_v2.h5")
    model.load_weights(f"{local_models}/embeddings_v2_weights.h5")
    return model


def get_weights(model, index_name):
    # Extract embeddings
    city_layer = model.get_layer("city_embedding")
    city_weights = city_layer.get_weights()[0]
    country_layer = model.get_layer("country_embedding")
    country_weights = country_layer.get_weights()[0]
    hotel_layer = model.get_layer("hotel_embedding")
    hotel_weights = hotel_layer.get_weights()[0]
    rating_layer = model.get_layer("rating_embedding")
    rating_weights = rating_layer.get_weights()[0]
    locality_layer = model.get_layer("locality_embedding")
    locality_weights = locality_layer.get_weights()[0]
    price_layer = model.get_layer("price_embedding")
    price_weights = price_layer.get_weights()[0]
    landmark_layer = model.get_layer("landmark_embedding")
    landmark_weights = landmark_layer.get_weights()[0]

    # Normalize the embeddings so that we can calculate cosine similarity
    if index_name == 'city':
        return city_weights / np.linalg.norm(city_weights, axis=1).reshape((-1, 1))
    if index_name == 'country':
        return country_weights / np.linalg.norm(country_weights, axis=1).reshape((-1, 1))
    if index_name == 'hotel_name':
        return hotel_weights / np.linalg.norm(hotel_weights, axis=1).reshape((-1, 1))
    if index_name == 'rating':
        return rating_weights / np.linalg.norm(rating_weights, axis=1).reshape((-1, 1))
    if index_name == 'locality':
        return locality_weights / np.linalg.norm(locality_weights, axis=1).reshape((-1, 1))
    if index_name == 'price':
        return price_weights / np.linalg.norm(price_weights, axis=1).reshape((-1, 1))
    if index_name == 'landmark':
        return landmark_weights / np.linalg.norm(landmark_weights, axis=1).reshape((-1, 1))


class Hotel:

    def __init__(self):
        self.dao = DAO()

    def find_similar_hotels(self, hoteldata):
        name = hoteldata['name']
        index_name = "hotel_name" if "index_name" not in hoteldata else hoteldata["index_name"]
        n = 20 if "n" not in hoteldata else hoteldata["n"]
        filter_name = "filter_name" if "filter_name" not in hoteldata else hoteldata["filter_name"]
        hotels_df = self.dao.get_hotel_df()
        weights = get_weights(get_model(), index_name)
        # Select index and reverse index
        if index_name == "city":
            index, rindex = self.dao.get_city()
        if index_name == "country":
            index, rindex = self.dao.get_country()
        if index_name == "hotel_name":
            index, rindex = self.dao.get_hotel()
        if index_name == "rating":
            index, rindex = self.dao.get_rating()
        if index_name == "locality":
            index, rindex = self.dao.get_locality()
        if index_name == "price":
            index, rindex = self.dao.get_price()
        if index_name == "landmark":
            index, rindex = self.dao.get_landmark()

        # Check name is in index
        try:
            # Calculate dot product between item/property and all others
            distances = np.dot(weights, weights[index[name]])
        except KeyError:
            print(" {} Not Found.".format(name))
            return

        # Sort distances from smallest to largest
        sorted_distances = np.argsort(distances)

        # Find the most similar
        closest = sorted_distances[-n:-1]

        # Limit results by filtering
        filter_ = None
        filtered_results = []
        results_dict = {}
        if len(filter_name):
            for idxs, rows in hotels_df.iterrows():
                if hotels_df.at[idxs, index_name] == name:
                    filter_ = hotels_df.at[idxs, filter_name]
                    break
            match_df = hotels_df[hotels_df[filter_name].str.match(filter_)]
            match_df = match_df.reset_index(drop=True)
            match_df["distance"] = None
            for idxs, rows in match_df.iterrows():
                item = match_df.at[idxs, index_name]
                distance = np.dot(weights[index[item]], weights[index[name]])
                match_df.loc[match_df.index[idxs], "distance"] = distance
            match_df = match_df.sort_values(by=["distance"], axis=0, ascending=False)
            results_dict = match_df.to_dict(orient="list")
            list_of_filtered_results = match_df[index_name].to_list()
            for item in list_of_filtered_results:
                if item not in filtered_results:
                    filtered_results.append(item)
            return filtered_results

        # Find the most similar
        closest = sorted_distances[-n:-1]
        results = []

        for c in reversed(closest):
            results.append(rindex[c])
        return results
