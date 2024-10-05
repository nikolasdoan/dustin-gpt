# run this in order

git clone --branch ubuntu-24.04 https://github.com/nikolasdoan/dustin-gpt

conda create --name dustin_gpt python=3.8

conda activate dustin_gpt 

conda install -c conda-forge libstdcxx-ng

strings $(g++ -print-file-name=libstdc++.so.6) | grep GLIBCXX # check installation of libstdcxx-ng

sudo apt upgrade libstdc++6

sudo apt-get install portaudio19-dev

sudo apt-get install python3-dev

pip install pyaudio

pip install -r requirements.txt

# create .env file for API key in the dustin-gpt folder
echo "OPENAI_API_KEY=<your-secret-api-key>" > .env

# run the main file
python gpt.py

