import pymongo
from pymongo import MongoClient
import sys
import datetime

user_options = {1: 'Find business by name', 
               2: 'Find reviews by restaurant name', 
               3: 'Find reviews having 5 or more useful votes',
               4: 'Find reviews having 5 or more funny votes', 
               5: 'Find reviews having 5 or more cool votes', 
               6: 'Find reviews having 3 stars or higher',
               7: 'Find businesses in California',
               8: 'Find businesses with more than 500 reviews',
               9: 'Find businesses that still open',
               10: 'Find businesses by categories',
               11: 'Find businesses that allow dogs',
               12: 'Find reviews that mention a specific word',
               13: 'Add a review',
               14: 'Update business name',
               15: 'Delete a business',
               16: 'Exit'}


def print_options(user_options):
    print("\n\n")
    for key, value in user_options.items():
        print(key, ": ", value)

def main():
    mongoClient = None
    try:
        mongoClient = MongoClient("mongodb://ec2-54-164-108-204.compute-1.amazonaws.com:47968")
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
            find_business(business_collection) 
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
            find_500_or_more_reviews(business_collection)
        elif option==9: 
            find_open_businesses(business_collection)
        elif option==10:
            find_by_categories(business_collection)
        elif option==11:
            find_businesses_allow_dogs(business_collection)
        elif option==12:
            find_reviews_by_keyword(business_collection, review_collection)
        elif option==13: 
            add_review(business_collection, review_collection)
        elif option==14: 
            update_business(business_collection)
        elif option==15: 
            delete_business(business_collection)
        elif option==16:
            mongoClient.close()
            print("Bye!")
            sys.exit()
        else:
            print("Invalid option. Please choose again!\n\n")

# user options implementation
def find_business(business_collection):
    name = input("Please enter business name: ")
    output = business_collection.find({"name": {"$regex": name}},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(10)
    for doc in output:
        print(doc)


def find_all_reviews(business_collection, review_collection):
    name = input("Please enter business name: ")
    business = business_collection.find_one({"name": {"$regex": name}})

    output = review_collection.find({"business_id": business["business_id"]},
                                     {"stars": 1, "date": 1,
                                      "text": 1, "useful": 1,
                                      "funny": 1, "cool": 1}).limit(10)

    for doc in output:
        print(doc)


def find_5_or_more_useful(business_collection, review_collection):
    name = input("Please enter business name: ")
    business = business_collection.find_one({"name": {"$regex": name}})

    output = review_collection.find({"business_id": business["business_id"],
                                     "useful": {"$gte": 5}},
                                    {"stars": 1, "date": 1, "text": 1,
                                     "useful":
                                         1}).limit(10)

    for doc in output:
        print(doc)


def find_5_or_more_funny(business_collection, review_collection):
    name = input("Please enter business name: ")
    business = business_collection.find_one({"name": {"$regex": name}})

    output = review_collection.find({"business_id": business["business_id"],
                                     "funny": {"$gte": 5}},
                                    {"stars": 1, "date": 1, "text": 1,
                                     "funny": 1}).limit(10)

    for doc in output:
        print(doc)


def find_5_or_more_cool(business_collection, review_collection):
    name = input("Please enter business name: ")
    business = business_collection.find_one({"name": {"$regex": name}})

    output = review_collection.find({"business_id": business["business_id"],
                                     "cool": {"$gte": 5}},
                                    {"stars": 1, "date": 1, "text": 1,
                                     "cool": 1}).limit(10)
    for doc in output:
        print(doc)
    
def find_3_or_more_stars(business_collection, review_collection):
    name = input("Please enter business name: ")
    business = business_collection.find_one({"name": {"$regex": name}})

    output = review_collection.find({"business_id": business["business_id"],
                                     "stars": {"$gte": 3}},
                                    {"stars": 1, "date": 1, "text": 1}).limit(10)

    for doc in output:
        print(doc)
    
def find_ca_businesses(business_collection):
    output = business_collection.find({"state": "CA"},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(10)
    for doc in output:
        print(doc)
    
def find_500_or_more_reviews(business_collection):
    output = business_collection.find({"review_count": {"$gte": 500}},
                                      {"name": 1, "address": 1, "city": 1,
                                       "state": 1, "postal_code": 1,
                                       "stars": 1, "review_count": 1}).limit(10)

    for doc in output:
        print(doc)
    
def find_open_businesses(business_collection):
    output = business_collection.find({"is_open": 1},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(10)
    for doc in output:
        print(doc)
   
def find_by_categories(business_collection):
    category = input("Please enter a category: ")
    output = business_collection.find({"categories": { "$regex": category }}, 
                                      {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                                       "stars": 1, "review_count": 1}).limit(10)
    for doc in output:
        print(doc)
    
def find_businesses_allow_dogs(business_collection):
    output = business_collection.find({"attributes.DogsAllowed": "True"}, {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1, "stars": 1, "review_count": 1}).limit(10)
    for doc in output:
        print(doc)
   
def find_reviews_by_keyword(business_collection, review_collection):
    name = input("Please enter business name: ")
    keyword = input("Please enter key word: ")
    
    business = business_collection.find_one({"name": {"$regex": name}})
    output = review_collection.find({"business_id": business["business_id"],
                                     "text": {"$regex": keyword}},
                                    {"stars": 1, "useful": 1, "funny": 1, 
                                     "cool": 1, "date": 1, "text": 1}).limit(10)
    
    for doc in output:
        print(doc)

def add_review(business_collection, review_collection):
    name = input("Please enter business name: ")
    star = input("Please enter number of stars you would give this business: ")
    review = input("Please enter review: ")
    
    business = business_collection.find_one({"name": {"$regex": name}})
    new_review = {"business_id": business["business_id"], "stars": star, "text": review, "date": datetime.datetime.now()}
    
    try:
        review_collection.insert_one(new_review)
        print("Successfully added review!")
        return True
    except Exception as e:
        print("An exception occurred ::", e)
        return False
    
def update_business(business_collection):
    business_id = input("Please enter business id: ")
    new_name = input("Please enter new business name: ")
    try:
        business_collection.update_one({"business_id": business_id}, {"$set": {"name": new_name}})
        print("Successfully updated business!")
        return True
    except Exception as e:
        print("An exception occurred ::", e)
        return False
    
def delete_business(business_collection):
    business_id = input("Please enter business id: ")
    try:
        business_collection.delete_one({"business_id": business_id})
        print("Successfully deleted business!")
        return True
    except Exception as e:
        print("An exception occurred ::", e)
        return False
    

if __name__ == "__main__":
    main()



