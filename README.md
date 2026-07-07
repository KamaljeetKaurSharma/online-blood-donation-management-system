# online-blood-donation-management-system
A relational database management system to connect blood donors, hospitals, and blood banks using Python and MySQL.

# Online Blood Donation Management System

## 🩸 Project Overview
The **Online Blood Donation Management System** is a relational database-driven platform designed to bridge the critical gap between blood donors, hospitals, and blood banks. The system provides users with real-time visibility into local blood availability while streamlining donor tracking, health metrics, and inventory logistics.

## 🛠️ Core Competencies Demonstrated
* **Database Management:** Relational Schema Design, SQL Queries, Data Normalization (MySQL).
* **Systems Architecture:** User Role Separation (Donors, Hospitals, Admins), Inventory Tracking.
* **Backend Automation:** Database Connectivity, Schema Deployment Scripts.

---

## 🗄️ Relational Database Schema Design
The system organizes information utilizing three foundational core data entities:

1. **Donors Table:** Tracks donor demographics, blood types, eligibility statuses, and historical donation intervals.
2. **Hospitals Table:** Manages healthcare facility locations, contact points, and urgent blood request orders.
3. **Blood Banks Table:** Tracks centralized inventory levels, storage capacities, and expiration logging by blood group.

---

## 🚀 Key Features Simulated
* **Donor Inventory Search:** Allows hospitals to query available blood units by blood group type within specific geographic perimeters.
* **Information Dashboards:** Centralized lookups for public users seeking active blood banks or participating hospitals.
* **Data Integrity Operations:** Scripted relational structure schemas to prevent invalid blood type entries or orphan data records.

---

## 📁 Repository Directory Structure
* `README.md` — Structural architecture documentation and database schema summaries.
* `blood_bank_db.py` — Python simulation engine deploying the relational schema and executing core SQL query operations.
