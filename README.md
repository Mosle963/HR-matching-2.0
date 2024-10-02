**Under Development**

HR – web application 
  
  Objective: Matches company’s job-posts with job-seekers based on their resumes.       
       
  Methodology: Employing Django MVT architecture to create a web application with the     
  following features:

  User Types: Three types of users, each with different permissions and functions:
	  -  Companies: Can create, delete, and update job posts, and browse job seekers’ profiles.
	  -  Job Seekers: Can update their information and browse job posts.
	  -  Admin: Can use the API to manage the model from a dedicated control panel.

  Job Matching: Suggested job posts are shown to job seekers using a Kmeans clustering model.

to do:
- update clusters after applying new model
- add tests
- configure admin panel
- add suggested job-posts to home page
- deploy
