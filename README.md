# Order Management API

## Overview
The Order Management API is a simple RESTful API built with FastAPI to manage orders for an online shop. This API allows users to create new orders, update the status of existing orders, and fetch order details with converted amounts in different currencies using external exchange rates.

## Features
- **Create Orders**: Add new orders with customer details and amount in PLN.
- **Update Order Status**: Change the status of an order (e.g., "pending", "shipped", "delivered").
- **Retrieve Order Details**: Fetch the details of an order along with the converted amount in a selected currency (e.g., EUR, USD).
- **Currency Conversion**: The API fetches the latest exchange rates from an external currency API for conversion.

## Technologies Used
- **FastAPI**: Web framework for building the API.
- **SQLAlchemy**: ORM for database communication (SQLite).
- **Pydantic**: For data validation and serialization.
- **SQLite**: Database for storing order information.
- **External API**: Fetches currency exchange rates for conversion (NBP API or other external sources).

## Setup Instructions

### Prerequisites
Make sure you have Python 3.7+ installed, along with the necessary dependencies. You can use a virtual environment for isolation.

### Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/sowinskipatryk/order-management-api
   cd order-management-api

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Set up the SQLite database (this is done automatically the first time you run the app).
4. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```
   
   The app will be available at http://127.0.0.1:8000.
   

# API Endpoints

## POST /orders/
Create a new order.

### Request Body:
```json
{
  "customer_name": "John Doe",
  "total_amount": 100.0,
  "currency": "USD",
  "status": "pending"
}
```
### Response:
```json
{
  "id": 1,
  "customer_name": "John Doe",
  "total_amount": 100.0,
  "currency": "USD",
  "converted_amount": 22.0,
  "status": "pending"
}
```
## PUT /orders/{order_id}/
Update the status of an existing order.

### Request Body:
```json
{
  "status": "shipped"
}
```
### Response:
```json
{
  "id": 1,
  "customer_name": "John Doe",
  "total_amount": 100.0,
  "currency": "USD",
  "converted_amount": 22.0,
  "status": "shipped"
}
```
## GET /orders/{order_id}/
Retrieve the details of an order, including the converted amount in the selected currency.
### Response:
```json
{
  "id": 1,
  "customer_name": "John Doe",
  "total_amount": 100.0,
  "currency": "USD",
  "converted_amount": 22.0,
  "status": "pending"
}
```
## GET /orders/
List all orders. You can filter by status if needed.
### Response:
```json
[
  {
    "id": 1,
    "customer_name": "John Doe",
    "total_amount": 100.0,
    "currency": "USD",
    "converted_amount": 22.0,
    "status": "pending"
  },
  {
    "id": 2,
    "customer_name": "Jane Smith",
    "total_amount": 200.0,
    "currency": "EUR",
    "converted_amount": 250.0,
    "status": "shipped"
  }
]
```

# Database Schema
The database stores the following order information:

- **id**: Unique order ID (auto-incremented).
- **customer_name**: Full name of the customer.
- **total_amount**: Total order amount in PLN.
- **currency**: The currency for conversion (e.g., "USD", "EUR").
- **status**: Current status of the order (e.g., "pending", "shipped", "delivered").

# External API for Currency Conversion
This application uses the NBP API (National Bank of Poland) to get the latest exchange rates for currency conversion. The exchange rate is fetched every time an order is retrieved or created.

# Error Handling
- **400 Bad Request**: If the data provided in the request body is invalid or missing required fields.
- **404 Not Found**: If the order with the specified order_id does not exist.
- **500 Internal Server Error**: If there is an error with the server or external API calls.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
