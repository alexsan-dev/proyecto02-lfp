def grammar_dict_to_HTML(grammar_dict, grammar_name):
    # LEER LINEAS DE TEMPLATE
    lfp_stream = open('./templates/digraph.html', encoding='utf-8')
    lfp_lines = lfp_stream.read()

    # ESCRIBIR
    lfp_stream_write = open('./out/reports/digraph.html', 'w')
    lfp_stream_write.write(lfp_lines)

    # CERRAR
    lfp_stream_write.close()
    lfp_stream.close()
