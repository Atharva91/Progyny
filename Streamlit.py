import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import sqlite3

# Set the page title and layout
st.set_page_config(page_title=" Progyny Assessment ", layout="wide")

st.image("Progyny.png", width=150)

# Load Data
@st.cache_data
def load_data():
    data = pd.read_csv("Data_Progyny_1.csv")  # Adjust with your data file path
    metadata = pd.read_csv("Progyny_MetaData_1.csv")  # Adjust with your metadata file path
    return data, metadata

data, metadata = load_data()

@st.cache_data
def load_data(filename):
    return pd.read_csv(filename)

# Title and Introduction

st.title(" Revenue Data Analysis using Progyny's Data in order to Derive some Crucial Insights impacting Revenue ")
st.write(" Developed By - Atharva Deshpande ")
st.write(" This is a consolidated view of all the questions which were provided for Analysis using tools such as SQL and Python. ")
st.write(" My intution behind creating this application is an attempt to create a space where eveything could be viewed in one place making it easier for authorities reviewing my assessment ")

# Sidebar Navigation
st.sidebar.title("Navigation")
question_selection = st.sidebar.radio(
    "Select a Question to View",
    (
        "1. Questions about the Data",
        "2. Insights from the Data",
        "3. Clients Going Live Each Quarter (SQL)",
        "4. Annual Revenue Growth by Product Type (SQL)",
        "5. Breakdown of Organic Growth vs. New Sales by Product Type (SQL)",
        "6. Percentage of Clients with Product 2 by Year (SQL)",
        "7. Product 2 Revenue as a Percentage of Product 1 Revenue (SQL)",
        "8. Total Year Revenue by Product Type for 2021 (Python)",
        "9. Dollar Value of Upsell Opportunity by Year (Python)",
    )
)

# Define sections based on the selected question
if question_selection == "1. Questions about the Data":
    st.header(" Questions about the Data (Top 5) ")
    st.write("""
             
1. Do we have any information on the demographics or firmographics of our clients, like the industries they’re in, 
   the size of their companies, or where they’re located?
             
    Motivation to bring up this question - Knowing more about who our clients are—whether they’re large tech firms in 
    competitive talent markets or smaller companies in regions with high demand for family-building benefits—could help us understand patterns in how different clients use and adopt our services. For example, companies in industries with a strong focus on employee well-being, like tech or healthcare, may be more open to adopting a full suite of Progyny’s offerings.
    By learning about these unique client characteristics, we could:
             
    a.) Better tailor our services to different client profiles, making our offerings more relevant and accessible.
             
    b.) Improve our cross-selling efforts by focusing on clients most likely to need additional support or complementary products.
             
    c.) Expand our reach in high-demand regions where fertility benefits are especially valued, helping us connect with clients who may benefit most from our programs.
             
2. What factors typically drive a client's decision to adopt Product 2? Are there specific milestones or triggers that indicate a readiness for Product 2?
             
    Motivation to bring up this question - Knowing what drives clients to adopt Product 2 can provide context for upsell 
    opportunities and help identify clients likely to convert. This insight could refine the approach to upselling and optimize 
    timing for engagement efforts.
             
3. Is there any history of price changes or discounts offered for Products 1 and 2 over the years?

    Motivation to bring up this question - Price changes or discounts could influence revenue trends and client behavior. 
    If discounts are significant, they may inflate or reduce revenue growth artificially. This information can help interpret 
    revenue trends more accurately and adjust upsell projections.
             
4. Are there any known seasonal trends or cycles in client onboarding or product adoption?

    Motivation to bring up this question - If there are known seasonal or cyclical patterns, understanding them can help 
    distinguish between short-term fluctuations and long-term growth trends. This information could improve the accuracy of 
    annual revenue forecasts and highlight periods with higher upsell potential. 
             
5. Is there a marketing or sales effort tracking database available that indicates whether clients have been targeted for Product 2 
   upselling efforts?
             
    Motivation to bring up this question - Understanding which clients have already been targeted for 
    upselling to Product 2 can clarify how much of the upsell potential has been realized versus untapped. This could help tailor 
    future upsell efforts and refine revenue projections based on clients yet to be approached.
             
6. Are there specific usage patterns or engagement metrics that differentiate clients who stay long-term versus those who leave?
             

    Motivation: Identifying the behaviors and engagement levels associated with long-term clients could help predict churn and inform retention strategies. For example, clients with high engagement in early months might indicate a strong commitment, while clients who underuse the services may be at higher risk of leaving.
    By understanding these patterns, we could:
             
    a) Develop early-warning signals for at-risk clients, allowing for proactive retention efforts.
             
    b) Tailor retention strategies based on the engagement levels and preferences of different client segments.
             
    c) Encourage higher engagement by providing targeted support or onboarding resources to clients who appear to be underutilizing the services.
             
7. Are there correlations between the client’s employee demographic (e.g., age, gender) and their usage or satisfaction with our services?


    Motivation: Knowing how client demographics correlate with product usage or satisfaction could allow us to better understand which groups benefit most from our services. For instance, companies with younger workforces or high proportions of female employees might have higher engagement in family-building benefits.
    Insights gained could allow us to:
             
    a) Refine product positioning and messaging based on the demographic makeup of a client's workforce.
             
    b) Tailor marketing efforts to emphasize features that resonate with key demographic segments.
             
    c) Anticipate future demand by understanding which workforce demographics drive higher engagement.
             
8. Are there common characteristics among clients who consistently engage with ancillary services (e.g., consultations, wellness programs) in addition to core products?
             
    Motivation: Clients who use ancillary services may represent a highly engaged segment with potential for cross-selling and upselling. Recognizing the traits of these clients could inform efforts to promote ancillary services to others.
    By identifying these characteristics, we could:
             
    a) Increase ancillary service adoption by targeting clients with similar profiles who are not yet using these services.
             
    b) Tailor marketing for ancillary services to focus on the needs of highly engaged segments.
             
    c) Develop bundled offerings that combine core products and ancillary services, especially for clients who are most likely to benefit from additional resources.
        
9. Do clients who use complementary programs or wellness benefits from other providers show higher engagement or satisfaction with Progyny’s offerings?
             
    
    Motivation: Clients who already prioritize wellness and family-building benefits may see Progyny’s offerings as complementary, leading to higher engagement. Understanding this correlation can help identify clients with high potential for adoption and satisfaction.
    Insights gained could help:
             
    a) Target clients in wellness-focused industries or regions for new sales or expanded offerings.
             
    b) Position Progyny’s services as a natural addition to clients’ existing wellness programs, boosting appeal.
             
    c) Create bundled offerings or partnerships that align with other wellness providers for clients likely to value comprehensive benefits.
             
10. How can we measure and improve the long-term impact of our offerings on client employee satisfaction, retention, and overall well-being?
             
    
    Motivation: Understanding the long-term benefits of Progyny’s offerings not only enhances the value proposition but also strengthens relationships with clients by demonstrating measurable impact. If our services positively influence client employee satisfaction and retention, this becomes a powerful case for continued investment and growth in our offerings.
    By exploring this question, we could:
             
    a) Partner with clients to gather data on how our services impact their employee satisfaction and retention over time.
             
    b) Develop client success stories and data-driven case studies to showcase the broader, long-term value of Progyny’s offerings.
             
    c) Identify opportunities to improve our offerings by understanding which aspects contribute most to client and employee satisfaction.
             
    """)
    
elif question_selection == "2. Insights from the Data":
    st.header("Insights from the Data")
    st.write("Here is a summary of additional key insights derived from the analysis:")

    # Ensure Rev is numeric by removing commas and coercing errors
    data['Rev'] = pd.to_numeric(data['Rev'].str.replace(',', ''), errors='coerce')

    # New insights
    st.subheader("Additional Insights")
    
    # Insight 1: Total Revenue by Product Type
    st.write("""
    - Total Revenue by Product Type: Analyzing the total revenue generated by each product type helps
      identify which products are driving the most revenue, informing product-focused strategies.
    """)
    st.code("""
    # Example Code for Revenue Analysis by Product Type
    total_revenue_by_product = data.groupby('Type')['Rev'].sum().reset_index()
    """, language="python")

    # Calculate and plot total revenue by product type
    total_revenue_by_product = data.groupby('Type')['Rev'].sum().reset_index()

    st.write("### Total Revenue by Product Type")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=total_revenue_by_product, x='Type', y='Rev', ax=ax)
    ax.set_title("Total Revenue by Product Type")
    ax.set_xlabel("Product Type")
    ax.set_ylabel("Total Revenue")
    st.pyplot(fig)

    # Explanation for Insight 1
    st.write("""
             
    Insight: This bar chart shows that Product 1 generates significantly more revenue than Product 2. This suggests that Product 1 is the primary revenue driver for the business, while Product 2 has a smaller contribution in comparison.
             
    Business Implication: Since Product 1 contributes the majority of revenue, it may be beneficial to continue focusing resources on Product 1 to maintain and grow this revenue stream. However, the lower revenue for Product 2 indicates potential for growth. Progyny could explore strategies to increase the adoption or usage of Product 2, perhaps by cross-selling to existing Product 1 customers or offering bundles that encourage clients to use both products. Understanding the reasons behind the revenue gap could also reveal areas where Product 2 might need refinement or additional marketing support.
   
              """)

    # Insight 2: Churn Risk Identification based on Revenue Decline
    st.write("""
    - Churn Risk Identification: Identifying clients with a significant revenue drop can help identify
      potential churn risk, allowing for targeted retention efforts.
    """)
    st.code("""
    # Example Code for Churn Risk Identification
    churn_risk = data[data['Rev'].pct_change() < -0.2]
    """, language="python")

    # Filter for potential churn risk
    churn_risk = data[data['Rev'].pct_change() < -0.2]

    st.write("### Clients at Risk of Churning")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(churn_risk['Rev'], bins=10, ax=ax)
    ax.set_title("Revenue Distribution for At-Risk Clients")
    ax.set_xlabel("Revenue")
    ax.set_ylabel("Number of At-Risk Clients")
    st.pyplot(fig)

    # Explanation for Insight 2
    st.write("""
             
    Insight: This histogram shows that a large number of at-risk clients (those experiencing a revenue drop) have relatively low revenue, with a few clients showing higher revenue figures. The skew towards lower revenue suggests that the majority of clients at risk of churning may not be significant revenue contributors individually.
             
    Business Implication: Since most at-risk clients contribute lower individual revenue, the business might focus retention efforts selectively. Prioritizing high-revenue clients who are at risk could be more impactful for overall revenue preservation. For lower-revenue clients, it may be more cost-effective to implement automated or scaled retention strategies rather than personalized outreach. Identifying patterns among these lower-revenue clients could also help prevent churn and improve satisfaction across the broader client base.
   
              """)

    # Insight 3: Monthly Seasonal Revenue Analysis for Promotion Planning
    st.write("""
    - Monthly Seasonal Revenue Analysis: Analyzing average monthly revenue by product type
      reveals seasonal patterns, guiding optimal timing for promotional efforts.
    """)
    st.code("""
    # Example Code for Monthly Seasonal Revenue Analysis
    data['DOS'] = pd.to_datetime(data['DOS'], errors='coerce')
    data['Month'] = data['DOS'].dt.month
    monthly_revenue = data.groupby(['Type', 'Month'])['Rev'].mean().reset_index()
    """, language="python")

    # Calculate and plot monthly revenue trends
    data['DOS'] = pd.to_datetime(data['DOS'], errors='coerce')
    data['Month'] = data['DOS'].dt.month
    monthly_revenue = data.groupby(['Type', 'Month'])['Rev'].mean().reset_index()

    st.write("### Monthly Seasonal Revenue Analysis by Product Type")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=monthly_revenue, x='Month', y='Rev', hue='Type', ax=ax)
    ax.set_title("Seasonal Revenue Analysis by Product Type")
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Revenue")
    st.pyplot(fig)

    # Explanation for Insight 3
    st.write("""
             
    Insight: The line chart shows seasonal trends for average monthly revenue by product type. Product 1 has a visible fluctuation, with peaks and dips throughout the year, whereas Product 2 appears more stable but at a consistently lower revenue level.
   
    Business Implication: Seasonal trends in Product 1’s revenue indicate opportunities for strategic timing of promotions. For example, running targeted marketing campaigns or promotional offers during low-revenue months could help boost engagement and revenue. For Product 2, the relatively stable revenue suggests that there might be less seasonality to leverage. Instead, the business might explore ways to boost overall engagement and awareness of Product 2 year-round, possibly targeting the months where Product 1’s revenue is lower to diversify the revenue base.
    
             """)
    
    # Insight 4: Merging Client Data and Monthly Revenue Trend Analysis
    st.subheader("Insight 4: Merged Data and Monthly Revenue Trend Analysis")

    # Ensure necessary columns are selected in the merged dataset
    st.write("### Merged Data for Analysis")
    st.write("""
    - Purpose: To analyze the relationship between revenue and the go-live dates of each product by merging data with metadata.
    - We keep only necessary columns: 'Client Key', 'Type', 'Treatment Type', 'DOS', 'Rev', 'Product 1 Go Live Date', and 'Product 2 Go Live Date'.
    """)

    # Rename go live date columns for easier handling
    meta_data_progyny = metadata.rename(columns={
    'Product 1 Go Live Date': 'Product1_Go_Live_Date',
    'Product 2 Go Live Date': 'Product2_Go_Live_Date'
    })

    # Merge data based on 'Client Key'
    merged_data = pd.merge(
    data[['Client Key', 'Type', 'Treatment Type', 'DOS', 'Rev']],
    meta_data_progyny[['Client Key', 'Product1_Go_Live_Date', 'Product2_Go_Live_Date']],
    on='Client Key', how='left'
    )

    # Convert Go Live Dates to datetime for comparison
    merged_data['Product1_Go_Live_Date'] = pd.to_datetime(merged_data['Product1_Go_Live_Date'])
    merged_data['Product2_Go_Live_Date'] = pd.to_datetime(merged_data['Product2_Go_Live_Date'])

    # Display the merged data preview
    st.write("#### Preview of Merged Data")
    st.write(merged_data.head())

    st.write("""
    Insight: This merged dataset includes client information, revenue, treatment type, and go-live dates for each product, which allows for a deeper analysis of how revenue trends may align with product adoption.
    """)

    # Monthly Revenue Trend Analysis
    st.write("### Monthly Revenue Trend Analysis")

    # Calculate monthly revenue trends
    monthly_revenue_trend = merged_data.groupby(merged_data['DOS'].dt.to_period("M"))['Rev'].sum().reset_index()
    monthly_revenue_trend['DOS'] = monthly_revenue_trend['DOS'].dt.to_timestamp()

    # Plot the monthly revenue trend
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(monthly_revenue_trend['DOS'], monthly_revenue_trend['Rev'], marker='o')
    ax.set_title('Monthly Revenue Trend')
    ax.set_xlabel('Date')
    ax.set_ylabel('Revenue')
    ax.grid(True)
    st.pyplot(fig)

    # Explanation for Monthly Revenue Trend
    st.write("""

    Business Insights:

    1.) Steady Growth Over Time: The upward trend in revenue shows that the business has been growing steadily. This could be due to attracting more clients or increasing engagement with existing ones. It's a good sign that things are on the right track!

    2.) Seasonal Patterns: We can see some dips in certain months, especially around late 2019 and early 2020. This could suggest that business is affected by seasonal factors – perhaps clients have specific times of the year when they’re more active. Understanding these patterns can help in planning resources and campaigns more effectively.

    3.) Impact of Major Events: Early 2020 shows a sharp drop, likely linked to the COVID-19 pandemic. This reminds us of how global events can suddenly impact revenue. Recognizing these shifts can help the business be more resilient and adaptable to unexpected changes in the future.
    
             """)
    
    # Insight 5: Treatment Popularity - Frequency and Total Revenue for Each Treatment Type
    st.subheader("Insight 5: Treatment Popularity - Frequency and Total Revenue")

    # Calculate treatment popularity by frequency and total revenue
    treatment_popularity = merged_data.groupby('Treatment Type').agg(
    Treatment_Count=('Treatment Type', 'size'),
    Total_Revenue=('Rev', 'sum')
    ).reset_index()

    # Sort treatments by frequency
    treatment_popularity = treatment_popularity.sort_values(by='Treatment_Count', ascending=False)

    # Plot treatment popularity by frequency
    st.write("### Treatment Popularity by Frequency")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(treatment_popularity['Treatment Type'], treatment_popularity['Treatment_Count'], color='skyblue')
    ax.set_title('Treatment Popularity')
    ax.set_xlabel('Treatment Type')
    ax.set_ylabel('Frequency')
    plt.xticks(rotation=45)
    ax.grid(axis='y')
    st.pyplot(fig)

    # Display Business Insights
    st.write("""
             
    Business Insights:

    1. IVF Treatments Are in High Demand: The "IVF Freeze-All" and "IVF FET" treatments have the highest frequency among clients, indicating that IVF-related services are a primary driver of client engagement. Focusing resources, marketing, and enhancements on these services could strengthen their impact.

    2. Consultations and Ancillary Services Are Also Popular: "Initial Consult & Ancillaries" ranks high, suggesting that clients value guidance or initial consultations before starting treatments. Providing an informative and supportive experience for these services can enhance client satisfaction.

    3. Opportunities for Niche Services: Treatments like "Frozen Oocyte" are less frequent, serving a more niche audience. Targeted promotion of these treatments to specific audiences or offering them as value-added options could help reach clients with unique needs.
    
    """)

    # Insight 6: Top 10% High-Value Clients by Revenue
    st.subheader("Insight 6: Top 10% High-Value Clients by Revenue")

    # Calculate total revenue per client
    client_revenue = data.groupby('Client Key')['Rev'].sum().reset_index()
    client_revenue = client_revenue.sort_values(by='Rev', ascending=False)

    # Determine top 10% clients by revenue
    top_clients = client_revenue.head(int(len(client_revenue) * 0.1))

    # Display the top clients data
    st.write("### Top 10% High-Value Clients by Revenue")
    st.write(top_clients)

    # Visualize the top 10% high-value clients by revenue
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(top_clients['Client Key'], top_clients['Rev'], color='salmon')
    ax.set_title('Top 10% High-Value Clients by Revenue')
    ax.set_xlabel('Client Key')
    ax.set_ylabel('Total Revenue')
    plt.xticks(rotation=45)
    ax.grid(axis='y')
    st.pyplot(fig)

    # Display Business Insights
    st.write("""
             
    Business Insights:

    1. Revenue Concentration Among Top Clients: A small group of clients (the top 10%) contributes a substantial portion of total revenue, with the highest client alone generating over $25 million. This concentration suggests that these high-value clients are critical to the business's financial health. Retaining these clients should be a priority, as they provide a significant share of revenue.

    2. Potential for Personalized Engagement: The wide disparity in revenue among the top clients indicates an opportunity for targeted, personalized engagement. Offering dedicated account managers, loyalty programs, or customized service packages to these top clients could strengthen relationships, ensuring they remain long-term partners and potentially increasing their spending.

    3. Risk of Revenue Volatility: With revenue heavily dependent on a few key clients, there’s an inherent risk if any of these clients decide to reduce their spending or leave. This insight underscores the importance of diversifying the client base by acquiring new clients or increasing the revenue contribution from mid-tier clients to minimize the business’s exposure to revenue volatility.
    
    """)

    # Insight 7: Treatment Popularity and Seasonality Analysis
    st.subheader("Insight 7: Treatment Popularity and Seasonality Analysis")

    data['Month'] = pd.to_datetime(data['DOS']).dt.month

    # Group by Treatment Type and Month to find seasonal trends
    treatment_seasonality = data.groupby(['Treatment Type', 'Month']).size().unstack(fill_value=0)

    # Plot the seasonal trends for each treatment type
    st.write("### Seasonal Trends in Treatment Types")
    fig, ax = plt.subplots(figsize=(20, 10))
    treatment_seasonality.plot(kind='bar', stacked=True, colormap='tab20', ax=ax)
    ax.set_title('Seasonal Trends in Treatment Types')
    ax.set_xlabel('Treatment Type')
    ax.set_ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels to avoid overlap
    ax.legend(title="Month", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  # Adjust layout to fit all elements
    st.pyplot(fig)

    # Display Business Insights
    st.write("""
             
    Business Insights:

    1. Consistent Demand Across Treatments: Most treatment types show relatively consistent distribution across months, suggesting that demand remains steady year-round. This allows the business to maintain consistent staffing and resource levels without major seasonal adjustments.

    2. Higher Demand for Egg Freezing in Specific Months: "Egg Freezing" shows peak demand in specific months like March. This may indicate a client preference to schedule this service at particular times of the year, allowing the business to prepare for increased demand by scheduling additional staff or launching targeted campaigns.

    3. Opportunities for Targeted Promotions in Off-Peak Months: Treatments like "Donor and Surrogacy Embryology" and "Storage" show slightly lower activity in certain months. This presents an opportunity to run targeted promotions during slower months to encourage more clients to use these services. For example, discounts or bundled services could help smooth demand and increase utilization.
    
    """)

elif question_selection == "3. Clients Going Live Each Quarter (SQL)":
    st.header("Clients Going Live Each Quarter")
    st.code(""" SELECT 
    Year,
    Quarter,
    COUNT(DISTINCT `Client Key`) AS Unique_Clients
FROM (
    -- Product 1 go-live dates
    SELECT 
        `Client Key`,
        YEAR(STR_TO_DATE(`Product 1 Go Live Date`, '%m/%d/%Y')) AS Year,
        QUARTER(STR_TO_DATE(`Product 1 Go Live Date`, '%m/%d/%Y')) AS Quarter
    FROM Progyny_MetaData_1
    WHERE `Product 1 Go Live Date` IS NOT NULL

    UNION

    -- Product 2 go-live dates
    SELECT 
        `Client Key`,
        YEAR(STR_TO_DATE(`Product 2 Go Live Date`, '%m/%d/%Y')) AS Year,
        QUARTER(STR_TO_DATE(`Product 2 Go Live Date`, '%m/%d/%Y')) AS Quarter
    FROM Progyny_MetaData_1
    WHERE `Product 2 Go Live Date` IS NOT NULL
) AS combined_go_live_dates
GROUP BY Year, Quarter
ORDER BY Year, Quarter;
""", language="sql")
    results_df = load_data("Clients_per_Quarter.csv")
    st.write("### Results")
    st.dataframe(results_df)



elif question_selection == "4. Annual Revenue Growth by Product Type (SQL)":
    st.header("Annual Revenue Growth by Product Type")
    st.code("""
    SELECT 
    Year,
    Type,
    SUM(Revenue) AS Annual_Revenue,
    LAG(SUM(Revenue)) OVER (PARTITION BY Type ORDER BY Year) AS Previous_Year_Revenue,
    (SUM(Revenue) - LAG(SUM(Revenue)) OVER (PARTITION BY Type ORDER BY Year)) / LAG(SUM(Revenue)) OVER (PARTITION BY Type ORDER BY Year) * 100 AS Revenue_Growth_Percentage
FROM (
    -- Extract year and revenue for each product type
    SELECT 
        `Client Key`,
        YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) AS Year,
        `Type`,
        CAST(REPLACE(`Rev`, ',', '') AS DECIMAL(15, 2)) AS Revenue
    FROM Data_Progyny_1
    WHERE `Rev` IS NOT NULL
) AS annual_revenue_data
GROUP BY Year, Type
ORDER BY Type, Year;
            """, language="sql")
    results_df = load_data("Q4.csv")
    st.write("### Results")
    st.dataframe(results_df)


elif question_selection == "5. Breakdown of Organic Growth vs. New Sales by Product Type (SQL)":
    st.header("Breakdown of Organic Growth vs. New Sales by Product Type")
    st.code("""
    WITH Client_First_Year AS (
    -- Step 1: Determine the first year of revenue for each client and type
    SELECT 
        `Client Key`,
        `Type`,
        MIN(YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y'))) AS First_Year
    FROM Data_Progyny_1
    GROUP BY `Client Key`, `Type`
),
Revenue_Breakdown AS (
    -- Step 2: Categorize revenue as new or returning for each client, year, and type
    SELECT 
        YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) AS Year,
        d.`Type`,
        CASE 
            WHEN YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) = cf.First_Year THEN 'New Sales'
            ELSE 'Organic Growth'
        END AS Revenue_Type,
        CAST(REPLACE(d.`Rev`, ',', '') AS DECIMAL(15, 2)) AS Revenue
    FROM Data_Progyny_1 AS d
    JOIN Client_First_Year AS cf
    ON d.`Client Key` = cf.`Client Key` AND d.`Type` = cf.`Type`
    WHERE d.`Rev` IS NOT NULL
)
-- Step 3: Aggregate revenue by year, type, and revenue type
SELECT 
    Year,
    Type,
    Revenue_Type,
    SUM(Revenue) AS Total_Revenue
FROM Revenue_Breakdown
GROUP BY Year, Type, Revenue_Type
ORDER BY Type, Year, Revenue_Type;
            """, language="sql")
    results_df = load_data("Q5.csv")
    st.write("### Results")
    st.dataframe(results_df)

elif question_selection == "6. Percentage of Clients with Product 2 by Year (SQL)":
    st.header("Percentage of Clients with Product 2 by Year")
    st.code("""
    WITH Yearly_Client_Count AS (
    -- Step 1: Count total unique clients per year
    SELECT 
        YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) AS Year,
        COUNT(DISTINCT `Client Key`) AS Total_Clients
    FROM Data_Progyny_1
    WHERE `DOS` IS NOT NULL
    GROUP BY Year
),
Yearly_Product2_Client_Count AS (
    -- Step 2: Count unique clients with Product 2 per year
    SELECT 
        YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) AS Year,
        COUNT(DISTINCT `Client Key`) AS Product_2_Clients
    FROM Data_Progyny_1
    WHERE `DOS` IS NOT NULL AND `Type` = 'Product 2'
    GROUP BY Year
)
-- Step 3: Calculate the percentage of clients with Product 2 per year
SELECT 
    yc.Year,
    yc.Total_Clients,
    p2c.Product_2_Clients,
    (p2c.Product_2_Clients / yc.Total_Clients) * 100 AS Product_2_Percentage
FROM Yearly_Client_Count AS yc
JOIN Yearly_Product2_Client_Count AS p2c
ON yc.Year = p2c.Year
ORDER BY yc.Year;
            """, language="sql")
    results_df = load_data("Q6.csv")
    st.write("### Results")
    st.dataframe(results_df)
    

elif question_selection == "7. Product 2 Revenue as a Percentage of Product 1 Revenue (SQL)":
    st.header("Product 2 Revenue as a Percentage of Product 1 Revenue")
    st.code("""
    WITH Client_Product_Revenue AS (
    -- Step 1: Calculate total revenue per client for each product type
    SELECT 
        `Client Key`,
        `Type`,
        SUM(CAST(REPLACE(`Rev`, ',', '') AS DECIMAL(15, 2))) AS Total_Revenue
    FROM Data_Progyny_1
    WHERE `Rev` IS NOT NULL
    GROUP BY `Client Key`, `Type`
),
Clients_With_Product_2 AS (
    -- Step 2: Filter to include only clients who have Product 2
    SELECT DISTINCT `Client Key`
    FROM Client_Product_Revenue
    WHERE `Type` = 'Product 2'
)
-- Step 3: Calculate Product 2 revenue as a percentage of Product 1 revenue for clients with Product 2
SELECT 
    cwp.`Client Key`,
    COALESCE(p1.Total_Revenue, 0) AS Product_1_Revenue,
    p2.Total_Revenue AS Product_2_Revenue,
    CASE 
        WHEN COALESCE(p1.Total_Revenue, 0) > 0 THEN (p2.Total_Revenue / p1.Total_Revenue) * 100
        ELSE NULL
    END AS Product_2_As_Percent_of_Product_1
FROM Clients_With_Product_2 AS cwp
LEFT JOIN Client_Product_Revenue AS p1 ON cwp.`Client Key` = p1.`Client Key` AND p1.`Type` = 'Product 1'
JOIN Client_Product_Revenue AS p2 ON cwp.`Client Key` = p2.`Client Key` AND p2.`Type` = 'Product 2';
            """, language="sql")
    results_df = load_data("Q7.csv")
    st.write("### Results")
    st.dataframe(results_df)
  

elif question_selection == "8. Total Year Revenue by Product Type for 2021 (Python)":
    st.header("Total Year Revenue by Product Type for 2021")
    
    # Ensure the 'DOS' column is in datetime format and extract the year
    data['DOS'] = pd.to_datetime(data['DOS'], errors='coerce')
    data['Year'] = data['DOS'].dt.year

    # Filter for the year 2021 and calculate total revenue by type, converting the revenue column to numeric
    revenue_2021 = (
        data[data['Year'] == 2021]
        .groupby('Type')
        .agg(Total_Revenue=('Rev', lambda x: pd.to_numeric(x.str.replace(',', ''), errors='coerce').sum()))
        .reset_index()
    )

    # Display the results
    st.write("### Results")
    st.dataframe(revenue_2021)

elif question_selection == "9. Dollar Value of Upsell Opportunity by Year (Python)":
    st.header("Dollar Value of Upsell Opportunity by Year")
    
    data['Rev'] = pd.to_numeric(data['Rev'].str.replace(',', ''), errors='coerce')
    data['DOS'] = pd.to_datetime(data['DOS'], errors='coerce')
    data['Year'] = data['DOS'].dt.year

    # Step 2: Calculate the average revenue per client for Product 2 in each year
    avg_product2_revenue = (
        data[data['Type'] == 'Product 2']
        .groupby('Year')['Rev']
        .mean()
        .loc[[2019, 2020, 2021]]  # Focus on the specific years
    )

    # Step 3: Identify clients who have only Product 1 in each year and calculate the upsell opportunity
    product1_clients = (
        data[data['Type'] == 'Product 1']
        .groupby(['Year', 'Client Key'])
        .size()
        .reset_index(name='Product 1 Count')
    )

    product2_clients = (
        data[data['Type'] == 'Product 2']
        .groupby(['Year', 'Client Key'])
        .size()
        .reset_index(name='Product 2 Count')
    )

    # Merge and filter for clients who have only Product 1 in each year
    only_product1_clients = (
        product1_clients.merge(product2_clients, on=['Year', 'Client Key'], how='left', indicator=True)
        .query('_merge == "left_only"')
        .groupby('Year')
        .size()
        .loc[[2019, 2020, 2021]]
    )

    # Step 4: Calculate upsell value as number of Product 1-only clients * average Product 2 revenue per client
    upsell_opportunity = (only_product1_clients * avg_product2_revenue).reset_index(name='Upsell_Value')

    # Display the results
    st.write("### Results")
    st.dataframe(upsell_opportunity)


