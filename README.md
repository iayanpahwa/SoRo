# SoRo
SocialRobot a.ka SoRo is a simple RESTfull API to schedule and post on various social media channels

---
## Features
- Tweets text content ✔️
- Tweets text with media content (tbd)
- Scheduling tweets (tbd)

## Usage
Obtain following from twitter developer portal and set them as Environment varibales in block container
```
CONSUMER_KEY
CONSUMER_SECRET
ACCESS_TOKEN
ACCESS_TOKEN_SECRET
```
## Test
The default API runs on port 5000, endpoint *tweet* can be tested using cURL : 
```curl -X POST -H "Content-Type: application/json" -d '{"CONTENT OF TWEET"}' http://127.0.0.1:5000/tweet```