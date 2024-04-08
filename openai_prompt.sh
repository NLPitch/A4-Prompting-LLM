curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "task:Is this text a compliment or backhanded compliment?, input:You are the only person who can always make me laugh"}], 
     "temperature": 0.7
   }'
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "task:Is this text a compliment or backhanded compliment?, input: Your ideas were good for an intern."}],                 
     "temperature": 0.7
   }'
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "task:Is this text a compliment or backhanded compliment?, input:Your Instagram makes you seem so fun!"}],               
     "temperature": 0.7
   }'
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "task:Is this text a compliment or backhanded compliment?, input:You are Amazing For Going Back To Work. I Could Never Let A Stranger Watch My Kids"}],
     "temperature": 0.7
   }'
   
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "task:Is this text a compliment or backhanded compliment?, input: You are like a breath of fresh air."}],
     "temperature": 0.7
   }'