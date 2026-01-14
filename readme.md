## Database Comparison Report  
PostgreSQL vs MongoDB

## Introduction

This project compares a relational database (PostgreSQL) and a NoSQL database (MongoDB) by implementing the same backend logic using both systems. A Python-based CLI application was developed to analyze their performances.

The goal is to understand which database is better suited for a specific use case. 

## System Overview

The application was built in Python using a modular architecture and supports three use cases executed through a CLI:

- Project Structure Management  
- Project Activity / Audit Logs  
- Project Summary & Analytics  

Each use case was implemented separately for PostgreSQL and MongoDB using identical business logic.

## Use Case 1 – Project Structure Management

This use case models a project with a manager, multiple teams, and team members.

PostgreSQL stores this data in normalized tables using foreign keys to maintain relationships.  
MongoDB stores the same data as a single nested document.

## Use Case 2 – Activity / Audit Logs

This use case records actions such as adding members, assigning tasks, and reviewing progress.

PostgreSQL uses a structured audit table with fixed columns and timestamps.  
MongoDB stores flexible log documents, making inserts simpler and faster.

## Use Case 3 – Project Summary & Analytics

This use case generates project insights such as total teams, total members, and team-wise member counts.

PostgreSQL performs analytics using joins and aggregation queries.  
MongoDB computes summaries by traversing embedded documents in application logic.

## Benchmarking Methodology

Benchmarking was performed using Python’s time.perf_counter().

For each database, the following operations were measured:
- Insert operations  
- Read/query operations  
- Aggregation/report generation  

All benchmarks were executed on the same machine using identical datasets.

## Benchmark Results

### PostgreSQL (milliseconds)

- Insert Project Structure: 42.563  
- Read Project Structure: 11.149  
- Insert Activity Logs: 27.762  
- Read Activity Logs: 5.425  
- Generate Project Summary: 7.274  

### MongoDB (milliseconds)

- Insert Project Structure: 15.899  
- Read Project Structure: 3.406  
- Insert Activity Logs: 15.417  
- Read Activity Logs: 2.996  
- Generate Project Summary: 3.815  

## Performance Analysis

MongoDB showed better performance for insert-heavy and hierarchical read operations due to its document-based design. PostgreSQL required multiple relational inserts and joins, which increased execution time but ensured consistency.

PostgreSQL performed well for aggregation and analytical queries, while MongoDB required additional application-level logic for similar results.

## Data Integrity

PostgreSQL enforces strong data integrity through foreign keys and transactional guarantees. Invalid or inconsistent data is prevented at the database level.

MongoDB does not enforce relational constraints by default. Data consistency must be handled by the application, providing flexibility but requiring more care.

## Scalability

PostgreSQL scales well vertically and is suitable for transactional and analytical workloads. Horizontal scaling requires additional configuration.

MongoDB is designed for horizontal scaling and handles high write throughput efficiently, making it suitable for large and rapidly growing datasets.
