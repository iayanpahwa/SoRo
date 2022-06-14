# tweet-block

tweet-block is a simple RESTfull API to schedule and post on twitter.
## Usage instructions

Include this snippet in your docker-compose.yml file under 'services':

    ```

    tweet-block:
      image: bh.cr/g_ayan_pahwa/tweet-block
    
    ```
    
  Add following environment varibales obtained from twitter developer portal to this block container env varibales on balenaCloud:

  ```
  - ENV CONSUMER_KEY
  - ENV CONSUMER_SECRET
  - ENV ACCESS_TOKEN
  - ENV ACCESS_TOKEN_SECRET
  ```

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