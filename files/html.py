# GRAMÁTICA A HTML
def grammar_dict_to_HTML(grammar_dict, grammar_name):
    # LEER LINEAS DE TEMPLATE
    stream = open('./templates/digraph.html', encoding='utf-8')
    lines = stream.read()

    # REMPLAZAR VARIABLES
    lines = lines.replace('{{ grammar_name }}', grammar_name).replace(
        '{{ terminals }}', ', '.join(grammar_dict['terminals'])).replace('{{ alphabet }}', ', '.join(grammar_dict['terminals'] + grammar_dict['noTerminals']))

    # ESCRIBIR
    stream_write = open('./out/reports/digraph.html', 'w')
    stream_write.write(lines)

    # CERRAR
    stream_write.close()
    stream.close()


def get_automaton_html_route(grammar_dict, grammar_name, word):
    # LEER LINEAS DE TEMPLATE
    stream = open('./templates/route.html', encoding='utf-8')
    lines = stream.read()

    # LEER AUTOMATA
    stream_svg = open(f'./out/reports/assets/AP_{grammar_name}.dot.svg')

    # REMPLAZAR VARIABLES
    svg_lines = stream_svg.read()
    svg_lines = svg_lines[svg_lines.index('<!-- Title: G Pages: 1 -->'):].replace(
        '<polygon fill="#ffffff"', '<polygon fill="transparent"')
    lines = lines.replace('{{ grammar_name }}', grammar_name).replace(
        '{{ grammar }}', str(grammar_dict)).replace("{{ word }}", word).replace("{{ svg }}", svg_lines)

    # ESCRIBIR
    stream_write = open('./out/reports/route.html', 'w')
    stream_write.write(lines)

    # CERRAR
    stream_write.close()
    stream.close()
