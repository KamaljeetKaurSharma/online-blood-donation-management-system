#!/usr/bin/env python3
"""
Online Blood Donation Management System - Database Simulation Engine
Demonstrates relational schema creation, data insertion, and search queries for donors/hospitals.
"""

import sqlite3

def initialize_database():
    # Setup an in-memory database using standard SQL operations (identical to MySQL logic)
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    print("[SYSTEM] Initializing Relational Database Tables...")

    # 1. Create Blood Banks Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blood_banks (
            bank_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            available_units_O_neg INTEGER DEFAULT 0
        )
    """)

    # 2. Create Hospitals Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitals (
            hospital_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            city TEXT NOT NULL
        )
    """)

    # 3. Create Donors Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors (
            donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            blood_type TEXT NOT NULL,
            last_donation_date TEXT,
            city TEXT NOT NULL,
            bank_id INTEGER,
            FOREIGN KEY (bank_id) REFERENCES blood_banks(bank_id)
        )
    """)
    
    conn.commit()
    return conn, cursor

def seed_sample_data(conn, cursor):
    print("[SYSTEM] Seeding sample relational data records...")
    
    # Insert Blood Banks
    cursor.execute("INSERT INTO blood_banks (name, city, available_units_O_neg) VALUES ('Central City Blood Bank', 'Anchorage', 45)")
    cursor.execute("INSERT INTO blood_banks (name, city, available_units_O_neg) VALUES ('Valley Medical Bank', 'Fairbanks', 12)")
    
    # Insert Hospitals
    cursor.execute("INSERT INTO hospitals (name, contact_number, city) VALUES ('Providence Hospital', '907-555-0199', 'Anchorage')")
    
    # Insert Donors
    cursor.execute("INSERT INTO donors (name, blood_type, last_donation_date, city, bank_id) VALUES ('Jane Doe', 'O-', '2026-04-12', 'Anchorage', 1)")
    cursor.execute("INSERT INTO donors (name, blood_type, last_donation_date, city, bank_id) VALUES ('John Smith', 'A+', '2026-05-30', 'Anchorage', 1)")
    
    conn.commit()

def query_emergency_supply(cursor, target_city):
    """
    Executes a joined query to match available blood bank stock with local city requirements.
    """
    print(f"\n[QUERY] Searching for available O- Negative Blood Reserves in: {target_city}...")
    
    query = """
        SELECT name, available_units_O_neg 
        FROM blood_banks 
        WHERE city = ? AND available_units_O_neg > 0
    """
    cursor.execute(query, (target_city,))
    results = cursor.fetchall()
    
    for row in results:
        print(f"📍 Facility: {row[0]} | Stock Level: {row[1]} units available.")

if __name__ == "__main__":
    print("=== BLOOD DONATION MANAGEMENT SYSTEM DATABASE CONTROLLER ===")
    
    # Run database pipeline simulation
    connection, db_cursor = initialize_database()
    seed_sample_data(connection, db_cursor)
    
    # Execute a business lookup logic example
    query_emergency_supply(db_cursor, "Anchorage")
    
    connection.close()
    print("\n[SYSTEM] Database session safely terminated.")
