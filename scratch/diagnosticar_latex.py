import os
import re

directory = r"G:\My Drive\Disciplinas\Graduação\SEL0383-Sinais e Sistemas\slides\apostila"

def check_latex_environments(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    stack = []
    errors = []
    
    # Simple regex to find \begin{...} and \end{...}
    begin_re = re.compile(r'\\begin\{([a-zA-Z*]+)\}')
    end_re = re.compile(r'\\end\{([a-zA-Z*]+)\}')
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        
        # Check for malformed integral placeholders
        if 'intParenthesize' in line:
            errors.append(f"LINHA {line_num}: Encontrado 'intParenthesize' malformado.")
            
        begins = begin_re.findall(line)
        for env in begins:
            stack.append((env, line_num))
            
        ends = end_re.findall(line)
        for env in ends:
            if not stack:
                errors.append(f"LINHA {line_num}: \\end{{{env}}} sem correspondente \\begin.")
            else:
                last_env, last_line = stack.pop()
                if last_env != env:
                    errors.append(f"LINHA {line_num}: \\end{{{env}}} fecha \\begin{{{last_env}}} na linha {last_line}.")
                    
    for env, line_num in stack:
        errors.append(f"LINHA {line_num}: \\begin{{{env}}} não foi fechado.")
        
    return errors

def main():
    for i in range(1, 21):
        filename = f"cap{i}.tex"
        filepath = os.path.join(directory, filename)
        if not os.path.exists(filepath):
            continue
            
        errors = check_latex_environments(filepath)
        if errors:
            print(f"\n--- ERROS EM {filename} ---")
            for err in errors:
                print(err)

if __name__ == "__main__":
    main()
