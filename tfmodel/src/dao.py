from itertools import chain

from src.load_data import load_df


class DAO:

    def __init__(self):
        self.hotels_df = load_df()

    def get_hotel_df(self):
        return self.hotels_df

    def get_city(self):
        city_list = self.hotels_df["city"].tolist()

        # Find set of unique cities and convert to a list
        unique_cities = list(set(city_list))

        # Create indexes for each city
        city_index = {city: idx for idx, city in enumerate(unique_cities)}
        index_city = {idx: city for city, idx in city_index.items()}
        return city_index, index_city

    def get_country(self):
        country_list = self.hotels_df["country"].tolist()

        # Find set of unique countries and convert to a list
        unique_countries = list(set(country_list))

        # Create indexes for each property
        country_index = {country: idx for idx, country in enumerate(unique_countries)}
        index_country = {idx: country for country, idx in country_index.items()}

        return country_index, index_country

    def get_hotel(self):
        # Create hotel names list
        hotels_list = self.hotels_df["hotel_name"].tolist()

        # Unique hotels
        unique_hotels = list(set(hotels_list))

        # Create indexes for each hotel
        hotel_index = {hotel: idx for idx, hotel in enumerate(unique_hotels)}
        index_hotel = {idx: hotel for hotel, idx in hotel_index.items()}

        return hotel_index, index_hotel

    def get_rating(self):
        rating_list = self.hotels_df["rating"].tolist()

        # Find set of unique ratings and convert to a list
        unique_ratings = list(set(rating_list))

        # Create indexes for each rating
        rating_index = {rating: idx for idx, rating in enumerate(unique_ratings)}
        index_rating = {idx: rating for rating, idx in rating_index.items()}

        return rating_index, index_rating

    def get_locality(self):
        # Create hotel names list
        locality_list = self.hotels_df["locality"].tolist()
        unique_localities = list(set(locality_list))

        # Create indexes for each hotel
        locality_index = {locality: idx for idx, locality in enumerate(unique_localities)}
        index_locality = {idx: locality for locality, idx in locality_index.items()}

        return locality_index, index_locality

    def get_price(self):
        price_list = self.hotels_df["price"].tolist()

        # Unique prices
        unique_prices = list(set(price_list))

        # Create indexes for each price
        price_index = {price: idx for idx, price in enumerate(unique_prices)}
        index_price = {idx: price for price, idx in price_index.items()}

        return price_index, index_price

    def get_landmark(self):
        # Create hotel names list
        landmark_list = self.hotels_df["landmark"].tolist()

        # Find set of unique properties and convert to a list
        # unique_landmarks = list(chain(*[list(set(landmarks)) for landmarks in landmark_list]))
        # unique_landmarks = list(np.unique(landmark_list))
        unique_landmarks = list(chain(*[list(set(landmarks)) for landmarks in landmark_list]))
        unique_landmarks = list(set(unique_landmarks))

        # Create indexes for each hotel
        landmark_index = {landmark: idx for idx, landmark in enumerate(unique_landmarks)}
        index_landmark = {idx: landmark for landmark, idx in landmark_index.items()}

        return landmark_index, index_landmark
