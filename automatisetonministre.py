import random
import numpy as np
import panel as pn


def click_cb(event):
    
    #text_input.link(generated_text, value='object')
    #generated_text = pn.pane.Markdown(object=text_input)
    taxes = ["les éviers", 
             "les mouchoirs", 
             "la crème solaire",
            "les avirons",
            "les citernes",
            "les édredons",
            "les moustaches",
            "le fil à coudre",
             "les monosourcils",
             "les animaux de compagnie",
             "la peinture bio",
             "les scies",
             "les crèpes",
             "le parquet",
             "les douches",
             "les patins",
             "les vélos",
             "l'herbe",
             "les pauvres"
            ]
    pred = random.choice(taxes)
    generated_text.object = "Je veux taxer " + pred

pn.extension() # loading panel's extension for jupyter compatibility 

text_input = "Je veux taxer ..."
generated_text = pn.pane.Markdown(object=text_input,sizing_mode='stretch_both')

button = pn.widgets.Button(name="Que va-t-on taxer aujourd'hui?",button_type="primary")

button.on_click(click_cb)

app = pn.Column(button, generated_text,sizing_mode='stretch_both', align='center'); app
title = pn.pane.Markdown("# **Générateur automatique de taxes belges**")
desc = pn.pane.HTML("<marquee scrollamount='10'><b>Bienvenue sur le  générateur automatique de taxes! Pour trouver des idées de nouvelles taxes, cliquez simplement sur le bouton pour générer de nouvelles taxes créatives et faire le travail d'un ministre belge pendant 3 ou 6 mois, plus qu'à regarder l'argent tomber!</b></marquee>")
final_app = pn.Column(title, desc ,app)


vpage = pn.Column(
    pn.Row(pn.layout.HSpacer(width=100), final_app, pn.layout.HSpacer(width=100), height=64),
    align='center',sizing_mode='stretch_both')


vpage.show()

