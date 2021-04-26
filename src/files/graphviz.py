# IMPORTS
from graphviz import Digraph

# GENERAR GRAFO DE AUTOMATA


def get_automaton_graph(grammar_dict, grammar_name):
    """Crea un svg utilizando Graphviz

    Args:
       grammar_dict (dict): Diccionario de gramática
       grammar_name (str): Nombre de gramática
    """
    # GRAPHVIZ
    g = Digraph('G', directory='./out/reports/assets',
                filename=f'AP_{grammar_name}.dot', format="svg")

    # --------- AUTOMATA ---------
    # ATRIBUTOS DE GRAFO
    g.attr(rankdir='LR')
    g.attr('node', shape='circle')

    # NODOS
    g.node('i', label="<<B>i</B>>", **
           {'width': '1', 'height': '1'}, fontsize='25')
    g.node('p', label="<<B>p</B>>", **
           {'width': '1', 'height': '1'}, fontsize='25')
    g.node('q', label="<<B>q</B>>",  **
           {'width': '1.5', 'height': '1.5'}, fontsize='25')
    g.node('f', label="<<B>f</B>>", **{'width': '1', 'height': '1'},
           shape="doublecircle", fontsize='25')

    # UNIR NODOS
    g.edge("i", "p", label="λ,λ;#", fontsize='19')
    g.edge(
        "p", "q", label=f"λ,λ;{grammar_dict['initialNoTerminal']}", fontsize='19')
    g.edge("q", "f", label="λ,#;λ", fontsize='19')

    # PRODUCCIONES
    break_line = "\n"
    g.edge(
        "q", "q", label=f'{break_line.join(map(lambda production: "λ," + production["entry"] + ";" + "".join(production["transitions"]),grammar_dict["productions"]))}\n\n{break_line.join(map(lambda terminal: terminal + "," + terminal + ";" + "λ" ,grammar_dict["terminals"]))}')

    # GENERAR SVG
    g.render()
