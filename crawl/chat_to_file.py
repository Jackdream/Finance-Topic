import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO


response = requests.get('http://localhost:5030/api/v1/chatlog?time=2025-01-01%7E2026-04-02&talker=%E9%B8%BF%E5%AD%A6%E9%99%A2%E7%9F%AD%E7%BA%BF%E4%BA%A4%E6%B5%81%E7%BE%A4&sender=%E8%90%8C%E6%96%B0%E6%8E%A2%E7%8F%AD%E6%99%BA%E5%BA%93%E4%B9%8B%E6%97%85')


with open('./output/chat_2026_04_02.csv', 'w', encoding='utf-8') as file:
    file.write(response.text)