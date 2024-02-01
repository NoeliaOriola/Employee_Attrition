# Attrition | impact attrition and prediction
This dataset was created to explore the diverse factors impacting employee performance and satisfaction in a typical organization. It spans a variety of fields from personal demographics to performance metrics and job details, offering a comprehensive view into the dynamics of the workplace.

# What is Attrition?

Attrition in the workplace, a persistent challenge for many organizations. 
It represents the rate at which employees employees leaving the workforce of an organization, which can occur through voluntary means like resignations and retirements, as well as involuntary actions such as terminations and layoffs.

This phenomenon poses significant problems for companies like IBM and others in the tech industry. When experienced employees depart, companies face not only the loss of valuable institutional knowledge and skills but also the high costs and resource-intensive process associated with recruiting, hiring, and training new personnel.

Moreover, a high attrition rate can tarnish a company's reputation as an employer, making it increasingly difficult to attract top talent in a competitive job market. Understanding and addressing the root causes of attrition is thus crucial for maintaining a skilled, stable, and motivated workforce.
<img width="1005" alt="Screenshot 2024-01-30 at 15 26 12" src="https://github.com/NoeliaOriola/Employee_Attrition/assets/151629602/e808c5cd-1474-461d-8486-f55c691a9d61">

# What's our Goal?
The main goal for this topic is to predict attrition by implementing machine learning so it helps us to compare correlated patterns from our dataset to identify tendency from our employees to stay or leave the organisation. 

Also we want  to ensure we want to retain employees, especially our top performers that are leaving voluntary and address HR strategies to retain them.

![5-Types-of-Attrition](https://github.com/NoeliaOriola/Employee_Attrition/assets/151629602/ee523236-3745-4459-a71d-639a740bf336)

# Context | Business Impact
Understanding when and why employees are likely to leave can inform strategies to boost employee retention and facilitate preemptive hiring planning. I will be using a systematic, step-by-step approach suitable for various machine learning problems. This project would fall under what is commonly known as "HR Anlytics", "People Analytics".

In this study, we will attempt to solve the following problem statement is:

What is the likelihood of an active employee leaving the company?
What are the key indicators of an employee leaving the company?
What policies or strategies can be adopted based on the results to improve employee retention?
What are the patters associated to employee productivity and attrition?
How can we predict employee turnover?
External factors that reflects job satisfaction? 

![image](https://github.com/NoeliaOriola/Employee_Attrition/assets/151629602/7048497c-da50-4feb-af0f-dd7399aa81d3)

# Scoring values (1 to 5)
Education 1 'Below College' 2 'College' 3 'Bachelor' 4 'Master' 5 'Doctor'

EnvironmentSatisfaction 1 'Low' 2 'Medium' 3 'High' 4 'Very High'

JobInvolvement 1 'Low' 2 'Medium' 3 'High' 4 'Very High'

JobSatisfaction 1 'Low' 2 'Medium' 3 'High' 4 'Very High'

PerformanceRating 1 'Low' 2 'Good' 3 'Excellent' 4 'Outstanding'

RelationshipSatisfaction 1 'Low' 2 'Medium' 3 'High' 4 'Very High'

WorkLifeBalance 1 'Bad' 2 'Good' 3 'Better' 4 'Best'

# Conclusion 
After finalizing the analysis using Machine Learning Prediction Models. We came to the conclusion to select the Machine Learning Model of KNN classifier with oversampling that demonstrated promising performance metrics, showcasing robustness in classifying employee attrition with balanced precision and recall scores. 

![image](https://github.com/NoeliaOriola/Employee_Attrition/assets/151629602/48582848-b7cc-4517-8223-0631e92fbf75)

By using our prediction ML model, we could have identified in an early stage the 79% of our 237 attrited employees (187employees).
Considering the employee attrition cost average (average 10-20K), by predicting the 187 employees, we could have saved approximately 1,870,00EUR/$.
However we must identify if those attrited employees left voluntary or involuntary, if we could prevent them to leave.  

After our analysis we came with some suggestions for our HR team, by reflecing on the missing data that would be crucial to enhance our prediciton accuracy as well as come up with some HR strategies to increase employees retention and save costs. 
