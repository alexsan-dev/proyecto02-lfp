# IMPORTS
import re

# TOOLS
from tools.dictionaries import dict_to_json

def parse_file(lines):
    grammars_dict = {}
    grammars_names = []
    current_grammar_index = 0
    grammars_invalid_dict = {}
    is_context_free_grammar = False
    
    # RECORRER LINEAS
    for line in lines.split("\n"):
        # NOMBRES DE GRAMÁTICAS
        if re.match("^\s*\w{2,}\s*$", line):
            grammars_names.append(line.strip())

        # NO TERMINALES ; TERMINALES ; TERMINAL INICIAL
        if re.match("^\s*(\w[,;]+)+\w*\s*$", line):
            symbols = line.split(";")

            # AGREGAR A DICCIONARIO
            grammars_dict[grammars_names[current_grammar_index]] = {
                "noTerminals":symbols[0].split(','),
                "terminals": symbols[1].split(','),
                "initialTerminal": symbols[2].split(',')
            }

        # PRODUCCIONES
        if re.match("^\s*\w\-\>(\w\s*)+", line):
            order = line.split('->')
            current_name = grammars_names[current_grammar_index]

            # COPIA DE DICCIONARIO
            transitions = order[1].split(" ")
            productions = grammars_dict[current_name].get('productions', [])
            productions.append({"entry": order[0], "transitions": transitions})

            # VERIFICAR SI ES LIBRE DE CONTEXTO
            if len(transitions) == 3:
                is_context_free_grammar = True 

            # AGREGAR A DICCIONARIO
            grammars_dict[current_name]['productions'] = productions


        # FINAL DE GRAMÁTICA
        if re.match("^\s*\*\s*", line):
            # ELIMINAR SI NO ES LIBRE DE CONTEXTO
            if not is_context_free_grammar:
                # COPIAR
                grammar_name = grammars_names[current_grammar_index] 
                grammars_invalid_dict[grammar_name] = grammars_dict[grammar_name]

                # BORRAR Y SALIDA
                del grammars_dict[grammar_name]

            # AUMENTAR POSICIÓN DE GRAMÁTICAS
            current_grammar_index += 1
            is_context_free_grammar = False
        

    # DICCIONARIO DE SALIDA
    return {
        "validGrammars": grammars_dict,
        "invalidGrammars": grammars_invalid_dict
    }
