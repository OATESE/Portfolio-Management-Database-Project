# SQL Files & Database Schema Setup for CW1

This directory contains a series of SQL scripts used to set up the database schema for the CW1 financial portfolio management system. Below is an outline of each file and its purpose.

## SQL Files Overview

- [AssetAllocationView.sql](./AssetAllocationView.sql) - Creates a view for asset allocation.
- [ClientSummaryView.sql](./ClientSummaryView.sql) - Summarizes client information.
- [Constraints_and_FKeys.sql](./Constraints_and_FKeys.sql) - Defines constraints and foreign keys.
- [CreateSchema.sql](./CreateSchema.sql) - Sets up the initial database schema.
- [CreateTables.sql](./CreateTables.sql) - Creates base tables for the database.
- [ExecuteStoredProcedure.sql](./ExecuteStoredProcedure.sql) - Template to execute stored procedures.
- [PortfolioHistoricalPerformanceView.sql](./PortfolioHistoricalPerformanceView.sql) - Tracks historical portfolio performance.
- [StoredProcedures.sql](./StoredProcedures.sql) - Contains stored procedures.
- [Triggers.sql](./Triggers.sql) - Defines database triggers.

### Initial Data Inserts
This folder contains files that populate the database with initial data necessary for the application to function properly. It should be executed after all tables have been created and before the application is used for the first time.

- [InsertClients.sql](./Data%20Generating%20Files/InsertClients.sql) - Inserts records into the `Clients` table.
- [InsertPortfolios.sql](./Data%20Generating%20Files/InsertPortfolios.sql) - Populates the `Portfolios` table.
- [InsertPositions.sql](./Data%20Generating%20Files/InsertPositions.sql) - Provides initial asset positions.
- [InsertPrices.sql](./Data%20Generating%20Files/InsertPrices.sql) - Contains historical price data.




