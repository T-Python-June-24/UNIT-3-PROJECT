# 🏢 Inventory Plus

## 📦 Using Django to create a comprehensive system for managing corporate inventory!

`Inventory Plus` is a robust system designed to manage the inventory and stock of a corporation efficiently.

## ✨ Features List


### 📊 Dashboard
- 📋 Overview of critical metrics
- 📊 Stock levels and low stock products charts

### 📋 Product Management
- ➕ Add new products
- ✏️ Edit product details
- 🗑️ Delete products
- 📄 View products list
- 🔍 View product details
- 📦 Stock Management
- 🔎 Search products

### 🗂️ Category Management
- ➕ Add new categories
- ✏️ Edit category details
- 🗑️ Delete categories
- 📄 View categories list

### 📇 Supplier Management
- ➕ Add new suppliers
- ✏️ Edit supplier details
- 🗑️ Delete suppliers
- 📄 View suppliers list
- 🔍 View supplier details

### 📊 Reports and Analytics
- 📈 Generate inventory reports
- 📉 Generate supplier reports

### 📧 Notifications
- 📬 Low stock alerts 


### 📁 Import/Export Data
- 📥 Import product data from CSV
- 📤 Export inventory data to CSV

## 📜 Requirements

### ⚙️ Functional Requirements
- The system must allow the addition, modification, and deletion of products, categories, and suppliers.
- The system must provide search functionality for products and suppliers.
- The system must track stock levels and allow updating of stock quantities.
- The system must generate and display various reports related to inventory.
- The system must send notifications for low stock and approaching expiry dates (via email to manager's email).
- The system must allow importing and exporting data in CSV format (Bonus).

### 🛠️ Non-Functional Requirements
- The system should be responsive and work on various devices.
- The system should have a user-friendly interface.
- The system should handle concurrent users without performance degradation.
- The system should ensure data security and integrity.
- The system should provide detailed error messages and logging for debugging purposes.




## 🛠️ Models:
- **Product**
- **Category**
- **Supplier**

### 🔗 Relationships
- A product belongs to one category.
- A product can be supplied by multiple suppliers.

![IventoryPlusModels](https://github.com/user-attachments/assets/aab09584-2607-4e81-848a-d504399965b8)
