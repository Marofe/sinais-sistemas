import os

directory = r"G:\My Drive\Disciplinas\Graduação\SEL0383-Sinais e Sistemas\slides\apostila"

def fix_file(filename):
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # 1. Correção dos \end{align编}
    content = content.replace(r'\end{align编}', r'\end{align*}')
    
    # 2. Correção de \end{entr} no cap7
    content = content.replace(r'\end{entr}', r'\]')
    
    # 3. Correção de </figure> no cap14
    content = content.replace(r'</figure>', r'\end{figure}')
    
    # 4. Correção do \end{align*} indevido na linha 331 do cap2
    # Procuramos o trecho específico:
    # \lambda = \frac{4 \pm \sqrt{(-4)^2 - 4(1)(3)}}{2} = \frac{4 \pm \sqrt{16 - 12}}{2} = \frac{4 \pm 2}{2}
    # \end{align*}
    # E trocamos por \].
    content = content.replace(
        "\\lambda = \\frac{4 \\pm \\sqrt{(-4)^2 - 4(1)(3)}}{2} = \\frac{4 \\pm \\sqrt{16 - 12}}{2} = \\frac{4 \\pm 2}{2}\n\\end{align*}",
        "\\lambda = \\frac{4 \\pm \\sqrt{(-4)^2 - 4(1)(3)}}{2} = \\frac{4 \\pm \\sqrt{16 - 12}}{2} = \\frac{4 \\pm 2}{2}\n\\]"
    )
    
    # 5. Correção dos placeholders de integral 'intParenthesize' e 'intParenthesis'
    # Cap 9: \intParenthesizex(t) -> \int_{-\infty}^{\infty} x(t)
    content = content.replace(r'\intParenthesizex(t)', r'\int_{-\infty}^{\infty} x(t)')
    content = content.replace(r'\intParenthesize', r'\int_{-\infty}^{\infty}')
    
    # Cap 12: \intParenthesize
    # Cap 16: \intParenthesisex(\tau) -> \int_{-\infty}^{\infty} x(\tau)
    content = content.replace(r'\intParenthesisex(\tau)', r'\int_{-\infty}^{\infty} x(\tau)')
    
    # Cap 17: \intParenthesisex(t) -> \int_{-\infty}^{\infty} x(t)
    content = content.replace(r'\intParenthesisex(t)', r'\int_{-\infty}^{\infty} x(t)')
    
    # Caso geral de limpeza
    content = content.replace(r'\intParenthesisex', r'\int_{-\infty}^{\infty} x')
    content = content.replace(r'\intParenthesis', r'\int_{-\infty}^{\infty}')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Corrigido: {filename}")
        return True
    return False

def main():
    print("Iniciando correções...")
    for i in range(1, 21):
        filename = f"cap{i}.tex"
        fix_file(filename)
    print("Correções concluídas!")

if __name__ == "__main__":
    main()
