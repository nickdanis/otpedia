import os, sys

chapters = [f for f in os.listdir('./src') if f.endswith(".md")]

print(chapters)