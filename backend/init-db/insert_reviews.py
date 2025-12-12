#!/usr/bin/env python3
"""
Open Addons Reviews Insertion Script
Reads data from reviews.json and inserts into the database
Usage: python insert_reviews.py [reviews.json]
"""

import mysql.connector
from mysql.connector import Error
import json
import sys
from datetime import datetime

def create_database_connection(host='localhost', user='root', password='', database='open_addons_db'):
    """Create a connection to MySQL database"""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("✓ Successfully connected to database")
            return connection
    except Error as e:
        print(f"✗ Error connecting to database: {e}")
        return None

def load_json_data(json_file):
    """Load data from JSON file"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ Successfully loaded data from {json_file}")
        return data
    except FileNotFoundError:
        print(f"✗ Error: File '{json_file}' not found")
        return None
    except json.JSONDecodeError as e:
        print(f"✗ Error parsing JSON: {e}")
        return None

def parse_date(date_string):
    """Parse date string to date object"""
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except:
        return None

def insert_reviews(connection, reviews_data):
    """Insert reviews for addons"""
    try:
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO reviews (
            addon_id, user_name, rating, review_text, review_date, helpful_count
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        for review in reviews_data:
            values = (
                review.get('addon_id'),
                review.get('user_name'),
                review.get('rating'),
                review.get('review_text'),
                parse_date(review.get('review_date')),
                review.get('helpful_count', 0)
            )
            cursor.execute(insert_query, values)
            print(f"✓ Inserted review by: {review.get('user_name')}")
        
        connection.commit()
        print(f"\n✓ Successfully inserted {len(reviews_data)} reviews")
        cursor.close()
        
    except Error as e:
        print(f"✗ Error inserting reviews: {e}")
        connection.rollback()

def main():
    """Main function to insert reviews from JSON file"""
    print("=" * 60)
    print("Open Addons Reviews Insertion")
    print("=" * 60)
    
    # Get JSON file from command line argument or use default
    reviews_file = sys.argv[1] if len(sys.argv) > 1 else 'reviews.json'
    
    # Configuration - Update these values as needed
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = ''  # Add your MySQL password here
    DATABASE = 'open_addons_db'
    
    # Load reviews JSON data
    print(f"\nLoading reviews data from: {reviews_file}")
    print("-" * 60)
    reviews_data = load_json_data(reviews_file)
    
    if not reviews_data:
        print("\n✗ Failed to load reviews data from JSON file!")
        sys.exit(1)
    
    # Create database connection
    connection = create_database_connection(HOST, USER, PASSWORD, DATABASE)
    
    if connection:
        # Insert reviews data
        if 'reviews' in reviews_data:
            print("\nInserting Reviews...")
            print("-" * 60)
            insert_reviews(connection, reviews_data['reviews'])
        
        # Close connection
        connection.close()
        
        print("\n" + "=" * 60)
        print("✓ All reviews inserted successfully!")
        print("=" * 60)
        print(f"\nTotal inserted:")
        print(f"  • {len(reviews_data.get('reviews', []))} reviews")
    else:
        print("\n✗ Reviews insertion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()