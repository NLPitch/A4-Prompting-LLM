curl --request POST \
  --url https://api.cohere.ai/v1/generate \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer " \
  --data '{
    "prompt": "task: Is this text a compliment or backhanded compliment?, input: You are the only person who can always make me laugh."
  }'

curl --request POST \
  --url https://api.cohere.ai/v1/generate \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer " \
  --data '{
    "prompt": "task: Is this text a compliment or backhanded compliment?, input: Your ideas were good for an intern. "
  }'

curl --request POST \
  --url https://api.cohere.ai/v1/generate \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer " \
  --data '{
    "prompt": "task: Is this text a compliment or backhanded compliment?, input: Your Instagram makes you seem so fun! "
  }'
curl --request POST \
  --url https://api.cohere.ai/v1/generate \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer " \
  --data '{
    "prompt": "task: Is this text a compliment or backhanded compliment?, input: You are Amazing For Going Back To Work. I Could Never Let A Stranger Watch My Kids!"
  }'
curl --request POST \
  --url https://api.cohere.ai/v1/generate \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer " \
  --data '{
    "prompt": "task: Is this text a compliment or backhanded compliment?, input: You are like a breath of fresh air."
  }'