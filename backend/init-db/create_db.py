#!/usr/bin/env python3
"""
Open Addons Database Setup Script
Creates database and tables for storing browser addon information
"""

import mysql.connector
from mysql.connector import Error

def create_database_connection(host='localhost', user='root', password=''):
    """Create a connection to MySQL server"""
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("✓ Successfully connected to MySQL server")
            return connection
    except Error as e:
        print(f"✗ Error connecting to MySQL: {e}")
        return None

def create_database(connection, db_name='open_addons_db'):
    """Create the database if it doesn't exist"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"✓ Database '{db_name}' created successfully")
        cursor.close()
    except Error as e:
        print(f"✗ Error creating database: {e}")

def create_addons_table(connection, db_name='open_addons_db'):
    """Create the addons table with all necessary fields"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {db_name}")
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS addons (
            addon_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            developer VARCHAR(255),
            developer_company VARCHAR(255),
            website VARCHAR(500),
            email VARCHAR(255),
            
            -- Ratings and popularity
            rating DECIMAL(2,1),
            total_ratings INT,
            users_count INT,
            featured BOOLEAN DEFAULT FALSE,
            
            -- Addon details
            version VARCHAR(50),
            size VARCHAR(50),
            language VARCHAR(100),
            category VARCHAR(100),
            addon_type VARCHAR(100),
            
            -- Dates
            updated_date DATE,
            published_date DATE,
            
            -- Description and features
            short_description TEXT,
            full_description TEXT,
            
            -- Permissions
            permission_web_history BOOLEAN DEFAULT FALSE,
            permission_user_activity BOOLEAN DEFAULT FALSE,
            permission_website_content BOOLEAN DEFAULT FALSE,
            
            -- URLs and resources
            icon_url VARCHAR(500),
            
            -- Additional metadata
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            
            INDEX idx_name (name),
            INDEX idx_rating (rating),
            INDEX idx_users (users_count),
            INDEX idx_developer (developer)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        
        cursor.execute(create_table_query)
        print("✓ Table 'addons' created successfully")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error creating table: {e}")

def create_reviews_table(connection, db_name='open_addons_db'):
    """Create a table for storing user reviews"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {db_name}")
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS reviews (
            id INT AUTO_INCREMENT PRIMARY KEY,
            addon_id VARCHAR(255) NOT NULL,
            user_name VARCHAR(255),
            rating INT CHECK (rating >= 1 AND rating <= 5),
            review_text TEXT,
            review_date DATE,
            helpful_count INT DEFAULT 0,
            
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            
            FOREIGN KEY (addon_id) REFERENCES addons(addon_id) ON DELETE CASCADE,
            INDEX idx_addon_id (addon_id),
            INDEX idx_rating (rating)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        
        cursor.execute(create_table_query)
        print("✓ Table 'reviews' created successfully")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error creating reviews table: {e}")

def main():
    """Main function to set up the database"""
    print("=" * 60)
    print("Open Addons Database Setup")
    print("=" * 60)
    
    # Configuration - Update these values as needed
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = ''  # Add your MySQL password here
    DB_NAME = 'open_addons_db'
    
    # Create connection
    connection = create_database_connection(HOST, USER, PASSWORD)
    
    if connection:
        # Create database
        create_database(connection, DB_NAME)
        
        # Create tables
        create_addons_table(connection, DB_NAME)
        create_reviews_table(connection, DB_NAME)
        
        # Close connection
        connection.close()
        print("\n" + "=" * 60)
        print("✓ Database setup completed successfully!")
        print("=" * 60)
    else:
        print("\n✗ Database setup failed!")

if __name__ == "__main__":
    main()