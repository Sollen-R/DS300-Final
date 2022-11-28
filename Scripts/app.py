import tkinter as tk
import joblib

root = tk.Tk()

canvas = tk.Canvas(root, height=250, width=600, bg='#152659')
canvas.create_text(300, 50, text='Phishing Link Detector', fill='white', font=('Times', '24', 'bold'))
canvas.pack()

def predict_phishing():
	#url = entry.get()
	#model = joblib.load('phishing_model.sav')
	#print(model.predict(url))
	pass

checkButton = tk.Button(root, text='Check Link', padx=10, pady=5, fg='black', bg='white', command=predict_phishing)
checkButton.pack()

entry = tk.Entry(root, width=88, justify='center')
canvas.create_window(300, 150, window=entry)

root.mainloop()