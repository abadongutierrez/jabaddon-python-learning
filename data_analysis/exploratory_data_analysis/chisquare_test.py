import pandas as pd
from scipy.stats import chi2_contingency

# Suppose a researcher wants to determine if there is an association between gender (male, female)
# and preference for a new product (like, dislike). The researcher surveys 100 people and records
# the following data:

# Category	Like	Dislike	Total
# Male	    20	    30	    50
# Female	25	    25	    50
# Total	    45	    55	    100

# Create the contingency table
data = [[20, 30],  # Male: [Like, Dislike]
        [25, 25]]  # Female: [Like, Dislike]
print(data)

# Create a DataFrame for clarity
df = pd.DataFrame(data, columns=["Product_Like", "Product_Dislike"], index=["Male", "Female"])

print(df)

chi2, p, dof, expected = chi2_contingency(df)
# Display results
print("Chi-square Statistic:", chi2)
print("Degrees of Freedom:", dof)
print("P-value:", p)
print("Expected Frequencies:\n", expected) 