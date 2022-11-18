import pymongo
from pymongo import MongoClient
import sys

user_options = {1: 'Find all restaurants near me', 
               2: 'Find all reviews by chosen restaurant', 
               3: 'Find all reviews having 5 or more useful votes',
               4: 'Find all reviews having 5 or more funny votes', 
               5: 'Find all reviews having 5 or more cool votes', 
               6: 'Add a review',
               7: 'Update a review',
               8: 'Delete a review',
               9: '',
               10: '',
               11: '',
               12: '',
               13: '',
               14: '',
               15: '',
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
	
    # db = mongoClient["yelp"]
    db = mongoClient["restaurantdb"]
    collection = db["restaursntcollection"]
    business_collection = db["business"]
    review_collection = db["review"]
    
    # print menu
    while (True):
        print_options(user_options)
        option = int(input('Please enter your choice: '))
        
        if option==1:
            #find_all_restaurants(business_collection)
            find_all_restaurants(collection)
        elif option==2:
            find_all_reviews(business_collection, review_collection)
        elif option==3:
            find_5_or_more_useful(business_collection, review_collection)
        elif option==4:
            find_5_or_more_funny(business_collection, review_collection)
        elif option==5:
            find_5_or_more_cool(business_collection, review_collection)
        elif option==6:
            add_review(business_collection, review_collection)
        elif option==7:
            update_review(business_collection, review_collection)
        elif option==8:
            delete_review(business_collection, review_collection)
        elif option==9:
            print("TODO")
        elif option==10:
            print("TODO")
        elif option==11:
            print("TODO")
        elif option==12:
            print("TODO")
        elif option==14:
            print("TODO")
        elif option==15:
            print("TODO") 
        elif option==16:
            print("TODO")
        else:
            print("Invalid option. Please choose again!\n\n")

# user options implementation
def find_all_restaurants(business_collection):
    output = business_collection.find().limit(10)
    for doc in output:
        print(doc)
    
def find_all_reviews(business_collection, review_collection):
    print("TODO")
    
def find_5_or_more_useful(business_collection, review_collection):
    print("TODO")
    
def find_5_or_more_funny(business_collection, review_collection):
    print("TODO")
    
def find_5_or_more_cool(business_collection, review_collection):
    print("TODO")
    
def add_review(business_collection, review_collection):
    print("TODO")
    
def update_review(business_collection, review_collection):
    print("TODO")
    
def delete_review(business_collection, review_collection):
    print("TODO")

if __name__ == "__main__":
    main()



