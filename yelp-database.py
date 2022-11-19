import pymongo
from pymongo import MongoClient
import sys

user_options = {1: 'Find restaurant by name', 
               2: 'Find all reviews by restaurant name', 
               3: 'Find all reviews having 5 or more useful votes',
               4: 'Find all reviews having 5 or more funny votes', 
               5: 'Find all reviews having 5 or more cool votes', 
               6: 'Find all reviews having 3 stars or higher',
               7: 'Find all businesses in California',
               8: 'Find all businesses with more than 500 reviews',
               9: 'Find all businesses that still open',
               10: '',
               11: '',
               12: '',
               13: 'Add a review',
               14: 'Update a review',
               15: 'Delete a review',
               16: 'Exit'}


def print_options(user_options):
    for key, value in user_options.items():
        print(key, ": ", value)

def main():
    mongoClient = None
    try:
        mongoClient = MongoClient("localhost:27017")
        print("MongoDB connected successfully!")
    except:
        print("Error: Could not connect to MongoDB")
	
    db = mongoClient["yelp"]
    business_collection = db["business"]
    review_collection = db["review"]
    
    # print menu
    while (True):
        print_options(user_options)
        option = int(input('Please enter your choice: '))
        
        if option==1:
            find_restaurant(business_collection)
        elif option==2:
            find_all_reviews(business_collection, review_collection)
        elif option==3:
            find_5_or_more_useful(business_collection, review_collection)
        elif option==4:
            find_5_or_more_funny(business_collection, review_collection)
        elif option==5:
            find_5_or_more_cool(business_collection, review_collection)
        elif option==6:
            find_3_or_more_stars(business_collection, review_collection)
        elif option==7:
            find_ca_businesses(business_collection)
        elif option==8:
            find_500_or_more_reviews(business_collection, review_collection)
        elif option==9:
            find_open_businesses(business_collection)
        elif option==10:
            print("TODO")
        elif option==11:
            print("TODO")
        elif option==12:
            print("TODO")
        elif option==13:
            add_review(business_collection, review_collection)
        elif option==14:
            update_review(business_collection, review_collection)
        elif option==15:
            delete_review(business_collection, review_collection)
        elif option==16:
            mongoClient.close()
            print("Bye!")
            sys.exit()
        else:
            print("Invalid option. Please choose again!\n\n")

# user options implementation
def find_restaurant(business_collection):
    name = input("Please enter restaurant name: ")
    output = business_collection.find({"name": {"$regex": name}},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(5)
    for doc in output:
        print(doc)
    
def find_all_reviews(business_collection, review_collection):
    name = input("Please enter restaurant name: ")
    
def find_5_or_more_useful(business_collection, review_collection):
    name = input("Please enter restaurant name: ")
    
def find_5_or_more_funny(business_collection, review_collection):
    name = input("Please enter restaurant name: ")
    
def find_5_or_more_cool(business_collection, review_collection):
    name = input("Please enter restaurant name: ")
    
def find_3_or_more_stars(business_collection, review_collection):
    name = input("Please enter restaurant name: ")
    
def find_ca_businesses(business_collection):
    output = business_collection.find({"state": "CA"},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(10)
    for doc in output:
        print(doc)
    
def find_500_or_more_reviews(business_collection):
    print("TODO")
    
def find_open_businesses(business_collection):
    output = business_collection.find({"is_open": 1},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(10)
    for doc in output:
        print(doc)
    
def add_review(business_collection, review_collection):
    print("TODO")
    
def update_review(business_collection, review_collection):
    print("TODO")
    
def delete_review(business_collection, review_collection):
    print("TODO")

if __name__ == "__main__":
    main()



