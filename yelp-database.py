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
	
    db = mongoClient["yelp"]
    business_collection = db["business"]
    review_collection = db["review"]
    
    # print menu
    while (True):
        print_options(user_options)
        option = int(input('Please enter your choice: '))
        
        match option:
            case 1:
                find_all_restaurants(business_collection)
            case 2:
                find_all_reviews(business_collection, review_collection)
            case 3:
                find_5_or_more_useful(business_collection, review_collection)
            case 4:
                find_5_or_more_funny(business_collection, review_collection)
            case 5:
                find_5_or_more_cool(business_collection, review_collection)
            case 6: 
                add_review(business_collection, review_collection)
            case 7:
                update_review(business_collection, review_collection)
            case 8:
                delete_review(business_collection, review_collection)
            case 9:
                print("TODO")
            case 10:
                print("TODO")
            case 11:
                print("TODO")
            case 12: 
                print("TODO")
            case 13:
                print("TODO")
            case 14:
                print("TODO")
            case 15: 
                print("TODO")
            case 16:
                mongoClient.close()
                print("Bye!")
                sys.exit()
            case _:
                print("Invalid option. Please choose again!\n\n")

# user options implementation
def find_all_restaurants(business_collection):
    print("TODO")
    
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



