#!/usr/bin/env python3
"""
Open Addons Insertion Script
Reads data from addons.json and inserts into the database
Usage: python insert_addons.py [addons.json]
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

def insert_addons(connection, addons_data):
    """Insert multiple addons into the database"""
    try:
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO addons (
            addon_id, name, developer, developer_company, website, email,
            rating, total_ratings, users_count, featured,
            version, size, language, category, addon_type,
            updated_date, short_description, full_description,
            permission_web_history, permission_user_activity, permission_website_content
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s
        )
        """
        
        for addon in addons_data:
            values = (
                addon.get('addon_id'),
                addon.get('name'),
                addon.get('developer'),
                addon.get('developer_company'),
                addon.get('website'),
                addon.get('email'),
                addon.get('rating'),
                addon.get('total_ratings'),
                addon.get('users_count'),
                addon.get('featured', False),
                addon.get('version'),
                addon.get('size'),
                addon.get('language'),
                addon.get('category'),
                addon.get('addon_type'),
                parse_date(addon.get('updated_date')),
                addon.get('short_description'),
                addon.get('full_description'),
                addon.get('permission_web_history', False),
                addon.get('permission_user_activity', False),
                addon.get('permission_website_content', False)
            )
            
            cursor.execute(insert_query, values)
            print(f"✓ Inserted addon: {addon.get('name')}")
        
        connection.commit()
        print(f"\n✓ Successfully inserted {len(addons_data)} addons")
        cursor.close()
        
    except Error as e:
        print(f"✗ Error inserting addons: {e}")
        connection.rollback()

def main():
    """Main function to insert addons from JSON file"""
    print("=" * 60)
    print("Open Addons Insertion")
    print("=" * 60)
    
    # Get JSON file from command line argument or use default
    addons_file = sys.argv[1] if len(sys.argv) > 1 else 'addons.json'
    
    # Configuration - Update these values as needed
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = ''  # Add your MySQL password here
    DATABASE = 'open_addons_db'
    
    # Load addons JSON data
    print(f"\nLoading addons data from: {addons_file}")
    print("-" * 60)
    addons_data = load_json_data(addons_file)
    
    if not addons_data:
        print("\n✗ Failed to load addons data from JSON file!")
        sys.exit(1)
    
    # Create database connection
    connection = create_database_connection(HOST, USER, PASSWORD, DATABASE)
    
    if connection:
        # Insert addons data
        if 'addons' in addons_data:
            print("\nInserting Addons...")
            print("-" * 60)
            insert_addons(connection, addons_data['addons'])
        
        # Close connection
        connection.close()
        
        print("\n" + "=" * 60)
        print("✓ All addons inserted successfully!")
        print("=" * 60)
        print(f"\nTotal inserted:")
        print(f"  • {len(addons_data.get('addons', []))} addons")
    else:
        print("\n✗ Addons insertion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()