Introduction to Machine Learning
Fall 2016
ASSIGNMENT <ASSIGNMENT 5> README FILE

Due Date: <ASSIGNMENT DUE DATE,  Wednesday, November 30, 2016>
Submission Date: <DATE SUBMITED, Wednesday, November 30, 2016>
Author(s): <SAGAR KALE> 
e-mail(s): <skale4@binghamton.edu> 

FILES:
[
	driver.py
]

TO COMPILE:
[
	
]

TO RUN: 
[	
	FROM CURRENT DIRECTORY
	remote07: python src/driver.py <input_file> <Number of Clusters> <Random Seed>
	Eg.
	remote07: python src/driver.py GaussianMixture-unlabeled.txt 3 5
]

TO CLEAN:
[
	remote07: rm *~ *.png
]

EXPLAINATION:
[
	The histogram of data is generated with name as histogram.png. The histogram can be generated again by different value of bins.
	Histogram of data is Generated successfully #By Default, it will generate histogram25.png file for bins=25
	Do you want to generate histogram of data with different bins count (yes/no)? yes
	Enter bins count (Eg.25): 15
	Histogram of data is Generated successfully #It will generate histogram15.png file for bins=15
	Do you want to generate histogram of data with different bins count (yes/no)? no
]