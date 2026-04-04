from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# GENERATE PANDAS CODE


def generate_code(query):
    prompt = f"""
You are a pandas expert.

Convert the user query into ONE valid pandas expression.

Rules:
- dataframe name: df
- return ONLY python code
- no explanation
- no text
- no assignment (=)
- only expression

Examples:
Query: total revenue
Code: df['revenue'].sum()

Query: average demand forecast by category
Code: df.groupby('category')['demand_forecast'].mean()

Query: highest sales region
Code: df.groupby('region')['units_sold'].sum().idxmax()

Query: average price
Code: df['price'].mean()

Now:

Query: {query}
Code:
"""

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=prompt
    )

    code = response.text.strip()

    # CLEAN OUTPUT
    code = code.replace("Code:", "").strip()

    return code


# SAFE EXECUTION
def execute_code(code, df):
    try:
        if "=" in code or len(code) < 5:
            return "❌ Invalid code generated."

        local_vars = {"df": df}

        result = eval(code, {"__builtins__": {}}, local_vars)

        return result

    except Exception:
        return "❌ Could not process query with generated code."


# FINAL DATA AGENT
def smart_data_agent(query, df):
    code = generate_code(query)

    print("\n⚙️ Generated Code:\n", code)

    result = execute_code(code, df)

    # Optional formatting
    if isinstance(result, (int, float)):
        return f"Result: {result:,.2f}"

    return result
