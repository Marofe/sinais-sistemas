import os
import re
from html.parser import HTMLParser

class RevealHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.current_slide = None
        self.current_tag = None
        self.tag_stack = []
        self.in_title = False
        self.in_content = False
        self.list_depth = 0
        self.in_math = False
        self.text_accumulator = ""
        
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        attrs_dict = dict(attrs)
        
        if tag == "section":
            # New slide
            self.current_slide = {
                "title": "",
                "elements": [],
                "has_math": False
            }
            self.slides.append(self.current_slide)
            self.list_depth = 0
            
        elif tag in ["h1", "h2", "h3"] or "slide-title" in attrs_dict.get("class", ""):
            self.in_title = True
            self.text_accumulator = ""
            
        elif tag == "img":
            src = attrs_dict.get("src", "")
            # Clean up paths
            src = os.path.basename(src)
            if self.current_slide is not None:
                self.current_slide["elements"].append(("image", src))
                
        elif tag in ["p", "li", "span", "div", "center"]:
            self.text_accumulator = ""
            if tag == "li":
                self.list_depth += 1
                
    def handle_endtag(self, tag):
        if self.tag_stack:
            self.tag_stack.pop()
            
        if tag == "section":
            self.current_slide = None
            
        elif tag in ["h1", "h2", "h3"] or self.in_title:
            if self.in_title and self.current_slide is not None:
                title_text = self.clean_text(self.text_accumulator)
                if not self.current_slide["title"]:
                    self.current_slide["title"] = title_text
                else:
                    self.current_slide["elements"].append(("subheading", title_text))
            self.in_title = False
            self.text_accumulator = ""
            
        elif tag in ["p", "li", "span", "div", "center"]:
            text = self.clean_text(self.text_accumulator)
            if text and self.current_slide is not None:
                if tag == "li":
                    self.current_slide["elements"].append(("item", text))
                else:
                    self.current_slide["elements"].append(("text", text))
            
            if tag == "li":
                self.list_depth = max(0, self.list_depth - 1)
            self.text_accumulator = ""
            
    def handle_data(self, data):
        self.text_accumulator += data
        
    def clean_text(self, text):
        # Clean double spaces, newlines, tabs
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

def convert_html_math_to_latex(text):
    # Reveal.js slides use $...$ or $$...$$ for KaTeX.
    # We will keep these but escape normal LaTeX characters that are outside $...$
    
    # Simple regex to split text by math delimiters $ or $$
    parts = re.split(r'(\$\$.*?\$\$|\$.*?\$)', text)
    
    for i in range(len(parts)):
        # If it's not a math block, escape special LaTeX characters
        if not (parts[i].startswith('$') and parts[i].endswith('$')):
            # Escape LaTeX characters: %, &, _, #, {, }
            p = parts[i]
            p = p.replace('&nbsp;', ' ')
            p = p.replace('&amp;', '\\&')
            p = p.replace('&lt;', '<')
            p = p.replace('&gt;', '>')
            p = p.replace('%', '\\%')
            p = p.replace('_', '\\_')
            p = p.replace('&', '\\&')
            p = p.replace('#', '\\#')
            parts[i] = p
        else:
            # Inside math, clean up any HTML entities if present
            m = parts[i]
            m = m.replace('&nbsp;', ' ')
            m = m.replace('&amp;', '&')
            m = m.replace('&lt;', '<')
            m = m.replace('&gt;', '>')
            m = m.replace('\\\\', '\\cr') # Katex new line to standard latex cr or keep as \\
            parts[i] = m
            
    return "".join(parts)

def parse_aula_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # Extract only the slides div content to avoid outer templates
    slides_match = re.search(r'<div class="slides">(.*?)</div>\s*</div>', html_content, re.DOTALL)
    if slides_match:
        html_content = slides_match.group(1)
        
    parser = RevealHTMLParser()
    parser.feed(html_content)
    return parser.slides

def generate_chapter_latex(chapter_num, slides):
    latex_lines = []
    
    # Find main title from slides or default
    main_title = f"Aula {chapter_num}"
    for slide in slides:
        if slide["title"] and "Aula" in slide["title"]:
            main_title = slide["title"]
            # Clean up the "Aula X:" label if needed, or keep it
            main_title = re.sub(r'Aula\s+\d+:\s*(<br>)?', '', main_title, flags=re.IGNORECASE)
            main_title = main_title.replace("<br>", " ").replace("<br/>", " ")
            main_title = re.sub(r'\s+', ' ', main_title).strip()
            break
            
    latex_lines.append(f"\\chapter{{{main_title}}}")
    latex_lines.append(f"\\label{{cap:{chapter_num}}}")
    latex_lines.append("\n% --- INTRODUÇÃO E CONTEXTO ---")
    latex_lines.append(f"Neste capítulo, abordaremos os conceitos apresentados na Aula {chapter_num} da disciplina de Sinais e Sistemas. ")
    latex_lines.append("Expandiremos a teoria apresentada nos slides, adicionando demonstrações matemáticas passo a passo, ")
    latex_lines.append("descrições detalhadas dos fenômenos físicos envolvidos e análise das ilustrações correspondentes.\n")
    
    in_itemize = False
    
    for slide in slides:
        slide_title = slide["title"].replace("<br>", " ").replace("<br/>", " ")
        slide_title = re.sub(r'\s+', ' ', slide_title).strip()
        
        # Skip intro/evaluation slides for core theory or include them
        if not slide_title or "dúvidas" in slide_title.lower() or "objetivos" in slide_title.lower() or "avaliação" in slide_title.lower():
            if not slide_title:
                pass # Unnamed slide, we still parse elements
            else:
                continue # Skip standard administrative slides
                
        latex_lines.append(f"\n\\section{{{slide_title}}}")
        
        for elem_type, content in slide["elements"]:
            content_clean = convert_html_math_to_latex(content)
            
            if elem_type == "subheading":
                if in_itemize:
                    latex_lines.append("\\end{itemize}")
                    in_itemize = False
                latex_lines.append(f"\n\\subsection{{{content_clean}}}")
                
            elif elem_type == "text":
                if in_itemize:
                    latex_lines.append("\\end{itemize}")
                    in_itemize = False
                # If it's pure block math (e.g. $$...$$), center it or place in \[ \]
                if content_clean.startswith('$$') and content_clean.endswith('$$'):
                    math_expr = content_clean[2:-2].strip()
                    latex_lines.append(f"\n\\[\n{math_expr}\n\\]\n")
                else:
                    latex_lines.append(f"\n{content_clean}")
                    
            elif elem_type == "item":
                if not in_itemize:
                    latex_lines.append("\n\\begin{itemize}")
                    in_itemize = True
                latex_lines.append(f"    \\item {content_clean}")
                
            elif elem_type == "image":
                if in_itemize:
                    latex_lines.append("\\end{itemize}")
                    in_itemize = False
                latex_lines.append("\n\\begin{figure}[H]")
                latex_lines.append("    \\centering")
                latex_lines.append(f"    \\includegraphics[width=0.75\\textwidth]{{{content}}}")
                latex_lines.append(f"    \\caption{{Representação de {content.replace('_', ' ')}.}}")
                latex_lines.append(f"    \\label{{fig:{content.split('.')[0]}}}")
                latex_lines.append("\\end{figure}")
                
        if in_itemize:
            latex_lines.append("\\end{itemize}")
            in_itemize = False
            
    return "\n".join(latex_lines)

def main():
    slides_dir = r"G:\My Drive\Disciplinas\Graduação\SEL0383-Sinais e Sistemas\slides\2025\SEL0383"
    output_dir = r"G:\My Drive\Disciplinas\Graduação\SEL0383-Sinais e Sistemas\slides\apostila"
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("Iniciando extração das aulas...")
    for i in range(1, 21):
        filename = f"aula{i}.html"
        filepath = os.path.join(slides_dir, filename)
        if not os.path.exists(filepath):
            print(f"Aviso: arquivo {filename} não encontrado. Pulando...")
            continue
            
        print(f"Processando {filename}...")
        slides = parse_aula_file(filepath)
        latex_content = generate_chapter_latex(i, slides)
        
        out_filepath = os.path.join(output_dir, f"cap{i}.tex")
        with open(out_filepath, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        print(f"Capítulo {i} gerado em {out_filepath}")
        
if __name__ == "__main__":
    main()
