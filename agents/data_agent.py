def data_agent(query, df):
    query = query.lower()

    try:
        if "revenue" in query:
            return f"Total revenue is {df['revenue'].sum():,.2f}"

        elif "average" in query or "mean" in query:
            return f"Average units sold is {df['units_sold'].mean():.2f}"

        elif "region" in query:
            region = df.groupby("region")["revenue"].sum().idxmax()
            return f"The region with highest sales is {region}"

        elif "product" in query:
            product = df.groupby("product_id")["revenue"].sum().idxmax()
            return f"The top performing product is {product}"

        else:
            return "This query requires deeper analysis. Try rephrasing with revenue, sales, region, or product."

    except Exception as e:
        return "Error processing data query."
