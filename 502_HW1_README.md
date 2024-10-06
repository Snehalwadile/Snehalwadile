## Q.1
1. Importing Libraries:
math: This library provides access to mathematical functions, including log2 which is used to compute entropy.
pandas: A powerful data manipulation and analysis library, here it is used to store the dataset in a DataFrame.

2. Training Data (Employee Dataset):
This section creates a pandas DataFrame to hold the dataset.
The dataset has four columns:
department: The employee’s department (e.g., sales, systems, marketing, secretary).
status: Whether the employee is senior or junior.
age: The age range of the employee (e.g., 21-30, 31-40).
salary: The salary category (Low, Medium, or High). This is the target attribute (class) we're trying to predict using decision tree splitting.

3. Entropy Calculation:
Entropy measures the uncertainty or impurity in a dataset.
Steps:
value_counts gives the count of each unique value in the target column (e.g., how many instances are High, Low, or Medium salary).
prob = count / total calculates the probability of each class.
entropy_value -= prob * math.log2(prob) applies the entropy formula.
The function returns the calculated entropy.
For example, if the dataset has 5 Medium, 4 Low, and 2 High salaries, the entropy reflects the impurity of this distribution.

4. Information Gain Calculation:
Information Gain (IG) measures the reduction in entropy achieved by splitting the dataset based on an attribute.
Steps:
Calculate the total entropy of the dataset (using the target column).
For each unique value in the attribute, create a subset of the dataset and calculate its entropy.
Multiply the subset’s entropy by the probability of the subset (i.e., the fraction of the dataset it represents).
Sum the weighted entropies for each subset.
Subtract this sum from the total entropy to get the Information Gain.
For example, if splitting on the "department" attribute gives subsets with lower entropy, the Information Gain will be high.

5. Split Information (SI) Calculation:
Split Information (SI) is used to penalize attributes with many unique values, preventing overfitting.
Steps:
Find the unique values in the attribute.
For each value, calculate its probability.
Apply the entropy formula to get the Split Information.

6. Gain Ratio Calculation:
Gain Ratio adjusts the Information Gain by dividing it by the Split Information.
Gain Ratio= SI/IG
This prevents overfitting by favoring attributes that not only give high Information Gain but also don't excessively split the dataset into many small subsets.

7. Calculating Gain Ratios for Attributes:
This block evaluates the Gain Ratio for the attributes department, status, and age.
The loop calls the gain_ratio() function for each attribute, computes the value, and prints the Gain Ratio.
The attribute with the highest Gain Ratio is the best candidate for the first split in the decision tree.


## Q.2
This code implements a Naive Bayes Classifier using a dataset about weather conditions and whether someone will play tennis (the "Play" column). The goal is to predict the class (whether to play or not) given new data using Bayes' Theorem.

Steps Involved:
1. Sample Dataset:
The dataset includes 5 features: Outlook, Temperature, Humidity, Windy, and Play.
"Play" is the target variable, with values "yes" or "no".
Each row represents a combination of weather conditions and whether tennis was played.
Example: 'Outlook': ['sunny', 'sunny', 'overcast', 'rainy', ...]

2. Convert Data to DataFrame:
The dataset is stored in a pandas DataFrame called df.

3. Prior Probabilities Calculation:
The function calculate_prior calculates the prior probabilities for each class label in the target column "Play".
P(Class)=  Number of instances of class/ Total instances

4. Likelihood Calculation:
The function calculate_likelihood calculates the likelihood for each feature value given the class label.
P(Feature | Class)= Instances of feature value in class/ Total instances of class

​Example: 
𝑃(Outlook=sunny | Play=yes)
P(Outlook=sunny | Play=yes).​

5. Naive Bayes Classifier:
The function naive_bayes_classifier calculates the posterior probability for each class using Bayes' Theorem:
Bayes' Theorem:
𝑃(Class | Features) = 𝑃(Class) × ∏ 𝑃(Feature | Class)
P(Class | Features)=P(Class)×∏P(Feature | Class)
It starts with the prior probabilities and multiplies them by the likelihoods of the feature values for each class. The result is normalized to get the posterior probabilities.
The class with the highest posterior probability is selected as the predicted class.

6. Prediction:
The new data point for which we want to predict the class is:
new_data = {'Outlook': 'sunny', 'Temperature': 'cool', 'Humidity': 'high', 'Windy': True}
The posterior probabilities are calculated for both "Play = yes" and "Play = no", and the class with the highest probability is predicted.

Output: This output indicates that given the weather conditions in new_data, the classifier predicts that tennis will be played (Play = yes) with a 75% probability.


## 3.

1. Key points:
Generalized Data with Count:
Each row now contains a "count" that indicates how many data instances share the same attribute values. For example, the first row represents 30 records with the combination of department=sales, status=senior, age=31-40, and salary=Medium.

2. Efficient Decision Tree Modification:
In a regular decision tree, we calculate measures like entropy or Gini index by evaluating each instance. However, with the "count" column, you can weight the contribution of each row by the count value.
Instead of iterating through each individual instance, we can perform the same calculations by multiplying the effect of each row's attributes by its count. This reduces the number of operations and makes the process more efficient.

* Example Solution Steps:
1. Modify Entropy/Information Gain Calculations:
When calculating entropy for a particular split (e.g., splitting by status), instead of considering each record individually, weight the entropy contribution by the count for each row. For example, when considering how the "status" attribute affects salary, the row sales, senior, 31-40, Medium, 30 should contribute 30 times as much as a single instance would.

2. Weighted Entropy Formula:
The weighted entropy for a split would be calculated as:
Weighted Entropy = ∑ (count/total count) × Entropy of subset

where "count" is the number of records sharing the same attributes in that row.
Advantages:
This approach reduces the number of calculations significantly because instead of computing entropy for each individual record, we compute it once per row and adjust for the count, making the decision tree algorithm more efficient.
