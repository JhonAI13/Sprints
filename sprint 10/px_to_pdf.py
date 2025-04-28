# convert_ipynb_to_pdf.py
# Script para converter um notebook Jupyter (.ipynb) em PDF,
# substituindo gráficos interativos do Plotly por imagens estáticas.

import os
import json
import nbformat
from nbconvert import PDFExporter
from nbconvert.preprocessors import Preprocessor
import plotly.io as pio

class PlotlyStaticPreprocessor(Preprocessor):
    """
    Pré-processador que converte saídas interativas do Plotly em imagens PNG estáticas
    usando o engine "kaleido".
    """
    def preprocess_cell(self, cell, resources, index):
        if cell.cell_type == 'code' and 'outputs' in cell:
            new_outputs = []
            for output in cell.outputs:
                data = getattr(output, 'data', {})
                if 'application/vnd.plotly.v1+json' in data:
                    fig_dict = data['application/vnd.plotly.v1+json']
                    fig = pio.from_json(json.dumps(fig_dict))
                    img_bytes = pio.to_image(fig, format='png', engine='kaleido')
                    new_output = nbformat.v4.new_output(
                        output_type='display_data',
                        data={'image/png': img_bytes},
                        metadata={}
                    )
                    new_outputs.append(new_output)
                else:
                    new_outputs.append(output)
            cell.outputs = new_outputs
        return cell, resources


def convert_notebook_to_pdf(input_nb: str, output_pdf: str):
    """
    Lê o notebook, aplica o pré-processador e exporta para PDF.
    """
    nb = nbformat.read(input_nb, as_version=4)
    exporter = PDFExporter()
    exporter.register_preprocessor(PlotlyStaticPreprocessor, enabled=True)
    pdf_bytes, _ = exporter.from_notebook_node(nb)
    with open(output_pdf, 'wb') as f:
        f.write(pdf_bytes)


if __name__ == '__main__':
    # Caminhos fixos conforme solicitado
    input_nb = r'C:\Users\jonat\Documents\GitHub\Sprints\sprint 10\sprint10.ipynb'
    output_dir = r'C:\Users\jonat\Documents\GitHub\Sprints\sprint 10'

    # Garante que o diretório de saída exista
    os.makedirs(output_dir, exist_ok=True)

    # Define nome do PDF com mesmo nome do notebook
    base_name = os.path.splitext(os.path.basename(input_nb))[0]
    output_pdf = os.path.join(output_dir, f'{base_name}.pdf')

    # Converte e informa ao usuário
    convert_notebook_to_pdf(input_nb, output_pdf)
    print(f'PDF gerado em: {output_pdf}')

# Dependências:
# pip install nbformat nbconvert plotly kaleido

