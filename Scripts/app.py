import tkinter as tk
import pandas as pd
import random
import joblib
import pickle

root = tk.Tk()

canvas = tk.Canvas(root, height=250, width=600, bg='#152659')
canvas.create_text(300, 50, text='Phishing Link Detector', fill='white', font=('Times', '24', 'bold'))
canvas.pack()

def predict_phishing():
	#url = entry.get
	#dict = {}
	useless = ['nb_or', 'ratio_nullHyperlinks', 'ratio_intRedirection', 'ratio_intErrors', 'submit_email', 'sfh']
	prediction_data = pd.read_csv('https://raw.githubusercontent.com/Sollen-R/DS300-Final/main/Datasets/initial_dataset.csv')
	prediction_data.drop(useless, axis='columns', inplace=True)
	url = prediction_data.iloc[int(random.random() * len(prediction_data))].to_frame().T
	model = joblib.load('phishing_model.sav')
	pred = model.predict(url.drop(['url', 'status'], axis='columns'))
	print(url['url'], pred)
	print(url['status'])

checkButton = tk.Button(root, text='Check Link', padx=10, pady=5, fg='black', bg='white', command=predict_phishing)
checkButton.pack()

entry = tk.Entry(root, width=88, justify='center')
canvas.create_window(300, 150, window=entry)

root.mainloop()