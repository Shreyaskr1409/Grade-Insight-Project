# ML Model Training

> This segment of the documentation acts as a plan which might be changed as per our requirements as we progress.

## Understanding the Training Process

To predict **CG (Cumulative Grade)** based on the 20 identified factors, we followed a systematic approach to train our machine learning model. The process involved:

1. **Preparing the data**
2. **Selecting the best features**
3. **Training the model**
4. **Evaluating its performance**

---

## Data Preparation

The first step was to prepare the data so the model could understand it:

- **Handling Missing Data**:
    - Filled missing numerical values (e.g., study hours) with averages.
    - Used the most common value for categorical data (e.g., branch or school type).

- **Scaling the Data**:
    - Scaled features with different ranges (e.g., attendance, previous scores) to ensure uniformity.

- **Splitting Data**:
    - Divided the dataset into (Planned):
        - **70% Training Set**
        - **30% Testing Set**

---

## Feature Selection

Not all 20 factors contributed equally to CG prediction. We identified and focused on the most impactful ones:

### Key Features
- **Study hours**
- **Attendance**
- **Motivation**
- **Previous scores**
- **Family income**

### Behavioral and Categorical Factors
- Extracurricular activities
- Peer influence
- Interest in the subject

### Transforming Data
Categorical data (e.g., school type, branch) was converted into numerical form using **encoding**.

---

## Choosing the Right Model

Multiple machine learning algorithms were tested to identify the best fit for this problem:

| **Algorithm**            | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Linear Regression**     | A starting point to understand basic relationships between factors and CG.     |
| **Random Forest Regressor** | Advanced model for handling complex, non-linear relationships.                 |
| **Gradient Boosting**     | Known for high accuracy by learning from its own mistakes.                     |
| **Support Vector Machines (SVM)** | Suitable for high-dimensional, less structured data.                          |

### Observations
- **Random Forest** and **Gradient Boosting** emerged as the most balanced in terms of accuracy and interpretability.

---

## Preliminary Observations

During the initial phase:
- Strong correlation observed between **study hours**, **previous scores**, and **CG**.
- Behavioral factors like **motivation** and **extracurricular participation** significantly influenced academic performance.

---

## Training the Model

### Random Forest Training
- Adjusted key parameters such as:
    - Number of trees (**n_estimators**)
    - Tree depth
- Ensured the model didn’t overfit the data.

### Cross-Validation
- Used cross-validation to evaluate performance on new data by splitting the data into multiple subsets.

---

## Model Evaluation

To assess model performance, the following metrics were used:

| **Metric**             | **Purpose**                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------|
| **Mean Squared Error (MSE)** | Measures prediction error. Lower values indicate better performance.                      |
| **R-squared (R²)**      | Explains the variance in CG. Values closer to 1 indicate higher prediction accuracy.        |

### Results:
- **Random Forest**:
    - **MSE**: (TBD)
    - **R²**: (TBD)
- **Gradient Boosting**:
    - (TBD).

---

## Feature Importance

Using the Random Forest model, the top contributing factors were identified:

| **Feature**                  | **Importance (%)** |
|------------------------------|--------------------|
| **Study Hours**              | (TBD)              |
| **Previous Exam Scores**     | (TBD)              |
| **Motivation**               | (TBD)              |
| **Attendance**               | (TBD)              |
| **Extracurricular Activities** | (TBD)              |

### Insights:
These results can guide students to focus on areas that matter most for improving their grades.

---

## Challenges and Solutions

| **Challenge**               | **Solution**                                                                                      |
|------------------------------|--------------------------------------------------------------------------------------------------|
| **Data Imbalance**           | Applied techniques to balance datasets for features with fewer data points (e.g., low attendance).|
| **Overfitting**              | Fine-tuned the Random Forest model to generalize well beyond the training data.                 |
| **Outliers**                 | Identified and addressed unusual data points (e.g., 0 study hours but high CG).                 |

---

This structured approach helped create a reliable model capable of predicting CG accurately and providing actionable insights for students.
