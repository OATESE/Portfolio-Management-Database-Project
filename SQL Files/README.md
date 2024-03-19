# SQL Files, Database Schema for CW1

This repository contains a series of SQL scripts used to set up the database schema for the CW1 financial portfolio management system. Below is an outline of each file and its purpose.

## SQL Files Overview

## Initial Data Inserts
This folder contains files that populate the database with initial data necessary for the application to function properly. It should be executed after all tables have been created and before the application is used for the first time.

### InsertClients.sql
Inserts records into the `Clients` table. It includes the dummy-fake personal information of the 15 clients that will be managed within the system.

### InsertPortfolios.sql
Populates the `Portfolios` table with dummy portfolio data, linking clients to their respective investment portfolios. Although the portfolios seem to have somewhat realistic names and aims the positions that each portfolio consist of are all randomly generated. 

### InsertPositions.sql
Provides the initial asset positions within each client's portfolio. This script should be run after `InsertPortfolios.sql` as it relies on the portfolios being previously defined. The positions represent "long trades" and range from 1st jan 2023 untill the end of 2023 as i wanted them to replicate activley managed portfolios, as it would mean more interesting graphs. 

### InsertPrices.sql
Contains historical price data for the various assets within the system. This is crucial for calculating portfolio values over time. This is real data retreived from yahoo finance. The data was downloaded then written into sql insert statements using the python (file link here)

### AssetAllocationView.sql
Creates a view in the database that presents the asset allocation of each portfolio, showing the distribution of asset types across a portfolio for each date.

### ClientSummaryView.sql
Creates a view that summarizes information at the client level, providing a snapshot of each client's total investments, returns, and diversification level.

### Constraints_and_FKeys.sql
Defines the constraints and foreign key relationships between tables. This ensures data integrity across the database.

### CreateSchema.sql
Initial script for setting up the schema where all other database objects will be contained.

### CreateTables.sql
Script to create the base tables for the CW1 database. This script must be executed before inserting any data into the database.

### ExecuteStoredProcedure.sql
SQL required to execute the stored procedure. This should be done regularly. Business logic would suggest doing this after every non-trading day in order to fill in the missing price data for exchange traded assets. 

### PortfolioHistoricalPerformanceView.sql
Sets up a view that tracks the historical performance of each portfolio by displaying the total value on each date.

### StoredProcedures.sql
Contains the stored procedure. The stored procudere is needed to fill in asset prices for assets that are not traded daily. Without this there are regular dips in the portfolio value on weekends as the position is worth 0. 

### Triggers.sql
Defines the triggers used to auto assign the purchasing price based on the date of the position and the closing price of the asset that day.

## Usage

To set up the database:

1. Execute `CreateSchema.sql` to establish the database schema.
2. Run `CreateTables.sql` to create all necessary tables.
3. Apply `Constraints_and_FKeys.sql` to define the data integrity rules.
4. Populate the tables with initial data by running `InitialDataInserts.sql`, followed by the insert scripts in the following order: `InsertClients.sql`, `InsertPortfolios.sql`, `InsertPositions.sql`, and `InsertPrices.sql`.
5. Set up the views by executing `AssetAllocationView.sql` and `PortfolioHistoricalPerformanceView.sql`.
6. Create stored procedures with `StoredProcedures.sql` and set up any required triggers with `Triggers.sql`.
7. Use `ExecuteStoredProcedure.sql` as a template for running stored procedures within your application or for testing purposes.
