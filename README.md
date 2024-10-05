# run this in order

git clone https://github.com/nikolasdoan/dustin-gpt

conda create --name dustin_gpt python=3.8

conda activate dustin_gpt 

sudo apt-get install portaudio19-dev

sudo apt-get install python3-dev

pip install pyaudio

pip install -r requirements.txt

# create .env file for API key in the dustin-gpt folder
echo "OPENAI_API_KEY=<your-secret-api-key>" > .env

# run the main file
python gpt.py

