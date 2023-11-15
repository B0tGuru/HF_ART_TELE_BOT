# HF_ART_TELE_BOT
Using Hugging face stability AI inference to generate art and send back to the user using pooling
got to hugging face: https://huggingface.co/stabilityai/stable-diffusion-2-1, sign up or signin, generate your hugging face token.
create a .env file with the contents:
BOT_TOKEN = "YOUR TELEGRAM BOT TOKEN"
HF_API_TOKEN = "YOUR HUGGING FACE TOKEN"

you can use the command line generator using python artman.py or use the telegram bot generator using python xbot.py...
it uses pooling.

i added a default watermark but u can change it in the hugface.py genArt method, by modifying the text variable. You can also change the initial auto prompt.

if u don't want a water mark, you can use the genArt_noWM method or just remove the water mark lines in getArt method.

### GOODLUCK