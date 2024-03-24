# Models
The following files are contained in this folder:
1.  ERD
2.  UML Use Case Diagram
3.  Logical Database Design


# [ERD](./DATABASE%20ERD%20Diagram.png)
Here's the cardinality and optionality for both sides of each relationship in the ERD:

## Clients to Portfolios:
- **Clients side**: One-to-Many (1:M), Optional. A client can have zero (optional) or many portfolios.
- **Portfolios side**: Many-to-One (M:1), Mandatory. A portfolio must be associated with exactly one client.

## Portfolios to Positions:
- **Portfolios side**: One-to-Many (1:M), Optional. A portfolio must be associated with one or many positions.
- **Positions side**: Many-to-One (M:1), Mandatory. A position must be associated with exactly one portfolio.

## Assets to Positions:
- **Assets side**: One-to-Many (1:M), Optional. An asset can have zero (optional) or many positions (across all portfolios).
- **Positions side**: Many-to-One (M:1), Mandatory. A position must be associated with exactly one asset.

## Assets to Prices:
- **Assets side**: One-to-Many (1:M), Optional. An asset must be have at one or many price records (over different dates).
- **Prices side**: Many-to-One (M:1), Mandatory. A price record must be associated with exactly one asset.

# [Use Case Diagram](./Use%20case%20diagram.png)

## Actors
- **Financial Advisor**: A professional who is in the client facing role in the investement company and offers the companies services to clients.
- **Clients**: Individuals who own portfolios and interact with the investement company to manage their investments.
- **Portfolio Managers**: Specialists responsible for making investment decisions and managing portfolio trading activities so that the portfolios reflect the goals determined by the financial advisor and client.
- **System Administrators**: Personnel responsible for maintaining the system's operational integrity.

## Use Cases
- **Define Portfolio**: Creating a new investment portfolio (Financial Advisor).
- **View Portfolio**: Accessing and reviewing portfolio details (Financial Advisor, Clients).
- **Update Client Contact Information**: Modifying client's personal contact details (Clients).
- **Perform Portfolio Performance Analysis**: Analyzing and reviewing the performance of investment portfolios (Financial Advisor, Portfolio Managers).
- **Generate Reports**: Creating reports on portfolios' performance, financial holdings, etc. (Financial Advisor, Portfolio Managers).
- **View Asset Prices**: Checking the current market prices of assets (Portfolio Managers).
- **Add/Update/Delete Position**: Managing (adding, updating, or removing) investment positions within a portfolio (Portfolio Managers). 
- **Perform System Maintenance**: Undertaking technical tasks to ensure the system is running correctly (System Administrators).


# [Logical Database Design](./Logical_Database_design.md)

Markdown document of how the database design has been checked against normalisation.

