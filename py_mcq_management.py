import tkinter as tk
from random import shuffle
 
a = """Q]What is the core objective of the World Bank supported STRIVE project in India?
[A] Skill Develop 
[B] Elimination of HIV/ AIDS
[C] Elimination of Malaria
[D] none of the above
,Q]Which among the following is the most important role played by Ribosome in the cells?
[A] Synthesis of Proteins
[B] Synthesis of DNA
[C] Synthesis of RNA
[D] none
""".split(",")
 
b = """Q]Deficiency of Vitamin D causes?
[A] Night blindness
[B] Rickets
[C] Goitre
[D] None of the above
,Q]Animal without RBC?
[A] Frog
[B] Earthworm
[C] Snake
[D] Peacock 
""".split(",")

c="""Q]Opium is obtained from which part of the Papaver somniferum Plant?
[A] Stem
[B] Leaves
[C] latex
[D] Stem joints
,Q]Spermology is the study of
[A] Leaf
[B] Fruit
[C] Seeds
[D] Pollen grains
,Q] 13 chambered heart is present in-
[A] Earthworm
[B] Snail
[C] cockroach
[D] Leech
""".split(",")

d="""Q]Plasmodium falciparum which causes malaria in humans is kept in which among the following groups?
[A] Bacteria
[B] Viruses
[C] Fungi
[D] Protozoans
,Q]The phenomenon of summer sleep by animals is called as
[A] Hibernation
[B] Laziness
[C] Lethargic
[D] Aestivation
,Q]Bones deformities occur due to the excess intake of-
[A] Phosphorus
[B] Potassium
[C] Fatty acid
[D] Fluorine
""".split(",")
 
num_questions = len(a)+len(b)+len(c)+len(d)
 
ans = a + b + c + d
shuffle(ans)
 
 
answer = []
for q in ans:
        if q in a:
                answer.append("a")
        elif q in b:
                answer.append("b")
        elif q in c:
                answer.append("c")
        else:
                answer.append("d")
quest = []
for n in range(num_questions):
	quest.append((ans[n], answer[n]))
 
print(quest)
 
 
numdom = len(quest)
score = 0
num = 0
def d1():
	global num, score, entry
	if num == numdom:
		text.pack_forget()
		entry.pack_forget()
		entry1.pack_forget()
		score = score / num * 100
		button['text'] = f"your Score is: {score}%\n Click here to Close this window"
		button['command'] = game_over
		button.pack()
		return
 
	if num == 0:
		answer_widget()
	text['height'] = 7
	text['bg'] = "LightPink1"
	text['width'] = 80
	text.delete("1.0",tk.END)
	text.insert("1.0",quest[num][0] + "\n enter the correct option a/b/c/d  below:")
	button.pack_forget()
	num+=1
 
def game_over():
	global score
	print("Roll number {} answered {} questions correctly ".format(entry1,score))
	root.destroy()
def answer_widget():
	global entry
	entry1.pack_forget()
	entry = tk.Entry(root, textvariable=solution, bg="RosyBrown1", font="Helvetica" )
	entry.pack()
	entry.bind("<Return>", lambda x: check())
	entry.focus()
 
def empty_textbox():
		solution.set("")
		d1()
 
def check():
	global n, score
	text.delete("1.0",tk.END)
	if solution.get() == quest[num-1][1]:
		text.insert(tk.END, "Right +1")
		score+=1
		text['bg'] = "green"
	else:
		text.insert(tk.END, "Wrong 0 points")
		text['bg'] = "red"
	label['text'] = score
	text.after(1000, empty_textbox)
 
root = tk.Tk()
label = tk.Label(root, text = """PRACTICE BIOLOGY TEST""", bg="firebrick1", font="Arial 48")
label.pack()
rules = """Multiple Choice Questions:

Q] Write the correct option in the box and press Enter







ENTER YOUR ROLL NUMBER BELOW:
"""

text = tk.Text(root, height=12 ,bg="navajo white",font="Arial 20")
text.insert("1.0", rules)

text.pack()


Rollno =tk.StringVar()
entry1 = tk.Entry(root, textvariable=Rollno, bg="old lace", font="Arial 20")
entry1.pack()
entry1.focus()

button = tk.Button(root, text="CLICK TO START TEST", bg="grey22", fg="white", command=d1, font="bold")
button.pack()
solution = tk.StringVar()

root.mainloop()


