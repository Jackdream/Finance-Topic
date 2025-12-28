import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO


response = requests.get('http://localhost:5030/api/v1/chatlog?time=2025-12-24&talker=%E9%B8%BF%E5%AD%A6%E9%99%A2%E7%9F%AD%E7%BA%BF%E4%BA%A4%E6%B5%81%E7%BE%A4&format=csv')


with open('./output/chat_2025_12_24.csv', 'w', encoding='utf-8') as file:
    file.write(response.text)