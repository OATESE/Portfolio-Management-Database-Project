User
INSERT INTO [YourSchema].[Portfolios] 
    (Client_ID, Portfolio_Name, Portfolio_Description, Portfolio_Purpose, Portfolio_Init_Date)
VALUES 
    (1, 'Growth Fund', 'A portfolio focused on capital appreciation', 'Long-term growth', '2023-01-05'),
    (2, 'Income Portfolio', 'Designed to provide regular income through dividends and interest', 'Income generation', '2023-01-12'),
    (3, 'Retirement Fund', 'A conservative mix of assets for a nearing retirement investor', 'Preservation of capital', '2023-01-20'),
    (4, 'Tech Leaders', 'Comprises leading technology companies for high growth potential', 'Aggressive growth', '2023-02-01'),
    (5, 'Balanced Approach', 'A balanced mix of equities and bonds for moderate risk', 'Balanced risk and return', '2023-02-15');
    (6, 'Emerging Markets', 'Invests in rapidly growing countries for high potential returns', 'Growth', '2023-01-18'),
    (7, 'Real Estate Investment', 'Focused on real estate assets to diversify and hedge against inflation', 'Diversification', '2023-02-05'),
    (8, 'Commodity Focus', 'Investment in commodities like gold and oil for market hedging', 'Hedging', '2023-01-25'),
    (9, 'Global Tech', 'Tech companies around the globe, aiming for high growth', 'Growth', '2023-02-09'),
    (10, 'Value Investing', 'Pursues undervalued companies with strong fundamentals', 'Long-term value', '2023-01-15'),
    (11, 'High Yield Bonds', 'Focuses on bonds with higher yields in exchange for higher risk', 'Income', '2023-02-20'),
    (12, 'Sustainable Investments', 'Eco-friendly and sustainable companies with a positive impact', 'Sustainable growth', '2023-01-10'),
    (13, 'Blue Chip Stocks', 'Invests in large, reputable companies known for their stability', 'Stability', '2023-02-14'),
    (14, 'Aggressive Growth', 'Targets high-risk, high-reward investments for maximum growth', 'High risk & reward', '2023-01-22'),
    (15, 'Defensive Stocks', 'Focuses on companies with consistent earnings, less sensitive to market cycles', 'Low risk', '2023-02-02');

-- For clients with 2 portfolios, adding second portfolios
INSERT INTO [PRACTICE3].[Portfolios] 
    (Client_ID, Portfolio_Name, Portfolio_Description, Portfolio_Purpose, Portfolio_Init_Date)
VALUES 
    (3, 'Fixed Income', 'Invests primarily in government and corporate debt', 'Income', '2023-02-18'),
    (6, 'Healthcare Innovation', 'Biotech and healthcare companies with strong R&D', 'Growth', '2023-01-28'),
    (9, 'International Equity', 'Stocks across emerging and developed markets for diversification', 'Diversification', '2023-02-12'),
    (12, 'Technology and Innovation', 'Emerging tech startups and leaders in innovation', 'Speculative Growth', '2023-01-06'),
    (15, 'Dividend Growers', 'Companies with a history of increasing their dividends', 'Income & Growth', '2023-02-22');