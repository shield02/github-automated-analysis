### Github Automated Analysis
Congratulations on being selected to complete a Mercor project! We conduct final-round interviews for applicants with successful submissions to be a Mercor engineer. 

In this project, you will build a Python-based tool which, when given a GitHub users URL, returns the most technically complex and challenging repository from that users profile. The tool will use GPT and LangChain to assess each repository individually before determining the most technically challenging one. 

### Requirements: 

1. Fetch a user’s repositories from their GitHub user URL. 

2. Preprocess the code in repositories before passing it into GPT. Specifically, implement memory management techniques for large repositories and the files within them. Consider that repositories may contain large Jupyter notebooks or package files which, if passed raw through GPT, would greatly exceed token limits. 

3. Implement prompt engineering when passing code through GPT for evaluation to determine its technical complexity. 

4. Identify which of the repositories is the most technically complex. Use GPT to justify the selection of the repository. 

5. Deploy your solution on a hosting platform like Vercel, Netlify, or GitHub pages. The interface should include a simple text box where users can input a GitHub user URL for analysis. Then, the interface should display a link to the most complex repository as well as GPT analysis justifying the selection. 

6. Record a YouTube video demonstrating your tool in action, showcasing its ability to evaluate and compare repositories complexity. 

### Grading: 

1. Projects will only be evaluated if they meet all requirements and contain links to a deployed site and YouTube video. 

2. Only the backend logic will be evaluated. No part of the frontend is graded. 

3. Solutions with more accurate complexity scoring based on GPT and creative memory management techniques will receive higher grades. 

4. Code should be well-structured and documented. 
