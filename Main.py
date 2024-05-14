import praw
import pandas as pd

id1 = input("Enter your client id:")
secret = input("Enter your client secret:")

reddit_read_only = praw.Reddit(
    client_id = id1,
    client_secret = secret,
    user_agent = "Rescraper",
)

subr = input("Enter the subreddit name that you want to scrape: ")
when = input("Choose between(All,Year,Month,Week,Day):")
#Gives Information about the subreddit
 
subreddit = reddit_read_only.subreddit(subr)

print("Display Name:", subreddit.display_name)
print("Title:", subreddit.title)
print("Description:", subreddit.description)


#Top 5 Posts

subreddit = reddit_read_only.subreddit(subr)
for post in subreddit.hot(limit = 5):
    print(post.title)
    print() 

#Using pandas

posts = subreddit.top(time_filter = when,limit = 5)
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
			"ID": [], "Score": [],
			"Total Comments": [], "Post URL": []
			}

for post in posts:
	# Title of each post
	posts_dict["Title"].append(post.title)
	
	# Text inside a post
	posts_dict["Post Text"].append(post.selftext)
	
	# Unique ID of each post
	posts_dict["ID"].append(post.id)
	
	# The score of a post
	posts_dict["Score"].append(post.score)
	
	# Total number of comments inside the post
	posts_dict["Total Comments"].append(post.num_comments)
	
	# URL of each post
	posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv("Top Posts.csv", index=True)

