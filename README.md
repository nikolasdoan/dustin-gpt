# if there is no git, install git
sudo apt install git 

git clone https://github.com/nikolasdoan/dustin-gpt

# install conda
https://www.taki.com.tw/blog/how-to-install-anaconda-on-ubuntu/?srsltid=AfmBOopzLE0wh7tKA4E3sE056G_rdSC6NmAlR_BnIcY3l8N6cnCvf-R9

conda create --name dustin_gpt python=3.8

conda activate dustin_gpt 

# install port audio, python3_dev, and pyaudio
sudo apt-get install portaudio19-dev

sudo apt-get install python3-dev

pip install pyaudio


# install requirements in the (dustin_gpt) venv
pip install -r requirements.txt

# in the dustin-gpt folder create a .env file and paste
OPENAI_API_KEY=<your-secret-api-key>

# run gpt.py
