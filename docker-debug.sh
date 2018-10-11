# docker run assumes that you have built the image before using:
# docker build -t jcito/praw .

docker run -ti --rm \
    -e REDDIT_CLIENT_ID=$REDDIT_CLIENT_ID \
    -e REDDIT_CLIENT_SECRET=$REDDIT_CLIENT_SECRET \
    -v $PWD/src:/home --name reddit_extract_debug jcito/praw sh
