from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chapati_recipe():
    steps = [
        "Mix 2 cups of whole wheat flour and 1 teaspoon of salt in a bowl.",
        "Gradually add water and knead into a soft, elastic dough.",
        "Cover and let the dough rest for 20–30 minutes.",
        "Divide dough into small balls.",
        "Roll out each ball into a thin circle.",
        "Heat a tawa (griddle) over medium-high heat.",
        "Cook each chapati for about 30 seconds on each side, until golden and puffed.",
        "Optionally, brush with ghee for extra flavor.",
        "Serve warm and enjoy!"
    ]
    return render_template('recipe.html', steps=steps)

if __name__ == '__main__':
    app.run(debug=True)
