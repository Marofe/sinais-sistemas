import os

output_dir = r"G:\My Drive\Disciplinas\Graduação\SEL0383-Sinais e Sistemas\slides\apostila"
os.makedirs(output_dir, exist_ok=True)

# ----------------- CAPÍTULO 16 -----------------
cap16_content = r"""\chapter{Análise de Sistemas e Resposta ao Impulso}
\label{cap:16}

Neste capítulo, estudaremos a modelagem de Sistemas Lineares Invariantes no Tempo (SLIT) no domínio do tempo. Mostraremos que qualquer SLIT contínuo é completamente caracterizado pela sua Resposta ao Impulso $h(t)$. Investigaremos as propriedades dinâmicas fundamentais dos sistemas (Memória, Causalidade e Estabilidade BIBO) e apresentaremos as demonstrações matemáticas rigorosas associadas.

---

\section{Caracterização por Resposta ao Impulso}

No Capítulo \ref{cap:4}, derivamos de forma intuitiva que a resposta de um SLIT a qualquer sinal de entrada $x(t)$ é dada pela integral de convolução com a resposta ao impulso do sistema $h(t)$:
\begin{equation}
y(t) = x(t) * h(t) = \intParenthesisex(\tau) h(t - \tau) \dtau
\end{equation}
Isto significa que todo o comportamento dinâmico de um sistema linear e invariante no tempo é completamente conhecido se conhecemos a sua resposta ao sinal de impulso unitário $\delta(t)$ (Figura \ref{fig:h_t_sys}).

\begin{figure}[H]
    \centering
    \includegraphics[width=0.55\textwidth]{resposta_impulso_sistema.png}
    \caption{Caracterização completa de um SLIT a partir de sua assinatura temporal $h(t)$.}
    \label{fig:h_t_sys}
\end{figure}

---

\section{Propriedades dos Sistemas LTI}

A partir do comportamento analítico de $h(t)$, podemos avaliar importantes propriedades físicas do sistema:

\subsection{1. Sistemas Sem Memória (Memoryless)}
Um sistema é considerado sem memória se a sua saída no instante $t$ depende unicamente da entrada no mesmo instante $t$.
\begin{teorema}[Sistema Sem Memória]
Um SLIT é sem memória se e somente se sua resposta ao impulso for um impulso concentrado na origem escalonado:
\begin{equation}
h(t) = K \delta(t)
\end{equation}
onde $K$ é uma constante real. Neste caso, a saída simplifica-se para a relação puramente algébrica: $y(t) = K x(t)$.
\end{teorema}

\subsection{2. Causalidade}
Um sistema é causal se sua saída em qualquer instante $t$ depende apenas dos valores presentes e passados da entrada $x(t)$.
\begin{teorema}[Causalidade de SLIT]
Um SLIT é causal se e somente se sua resposta ao impulso for identicamente nula para instantes de tempo negativos:
\begin{equation}
h(t) = 0 \quad \text{para todo } t < 0
\end{equation}
\end{teorema}
Neste caso, os limites da integral de convolução reduzem-se para a faixa causal, como mostrado graficamente nas Figuras \ref{fig:causalidade_slit_all}:
\begin{equation}
y(t) = \int_{0}^{\infty} h(\tau) x(t-\tau) \dtau = \int_{-\infty}^{t} x(\tau) h(t-\tau) \dtau
\end{equation}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{causalidade_SLIT0.png}
        \caption{A resposta ao impulso causal iniciando estritamente em $t=0$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{causalidade_SLIT2.png}
        \caption{Integração causal limitada ao passado do sinal.}
    \end{subfigure}
    \caption{Propriedade de causalidade dinâmica em sistemas LTI.}
    \label{fig:causalidade_slit_all}
\end{figure}

\subsection{3. Estabilidade BIBO}
Um sistema é considerado estável no sentido BIBO (*Bounded-Input, Bounded-Output*) se qualquer entrada limitada em amplitude gera uma resposta que também é limitada.
\begin{teorema}[Estabilidade BIBO]
Um SLIT é BIBO estável se e somente se sua resposta ao impulso for absolutamente integrável sobre todo o domínio real:
\begin{equation}
\int_{-\infty}^{\infty} |h(t)| \dt < \infty
\end{equation}
\end{teorema}

\begin{proof}
Mostraremos primeiro a condição de suficiência (estabilidade $\Leftarrow$ integrabilidade).
Assumimos que a entrada é limitada por um valor real positivo $M_x < \infty$, ou seja, $|x(t)| \le M_x$ para todo $t \in \R$. Calculamos o módulo do sinal de saída $y(t)$:
\begin{align*}
|y(t)| &= \left| \int_{-\infty}^{\infty} h(\tau) x(t-\tau) \dtau \right|
\end{align*}
Utilizando a desigualdade de Jensen para integrais:
\begin{align*}
|y(t)| &\le \int_{-\infty}^{\infty} |h(\tau) x(t-\tau)| \dtau = \int_{-\infty}^{\infty} |h(\tau)| \cdot |x(t-\tau)| \dtau
\end{align*}
Como $|x(t-\tau)| \le M_x$:
\begin{align*}
|y(t)| &\le M_x \int_{-\infty}^{\infty} |h(\tau)| \dtau
\end{align*}
Se a integral for absolutamente finita, ou seja, $\int_{-\infty}^{\infty} |h(t)| \dt = I_h < \infty$:
\[
|y(t)| \le M_x I_h < \infty
\]
provando que a saída é limitada ($y(t)$ estável BIBO). A prova de necessidade ($\Rightarrow$) é obtida de forma análoga definindo uma entrada limitada específica $x(t-\tau) = \text{sign}\{h(\tau)\}$.
\end{proof}

Esta propriedade fundamental de decaimento de amplitude e limites é mostrada na Figura \ref{fig:bibo_estabilidade}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.65\textwidth]{BIBO_estabilidade.png}
    \caption{Sinal de entrada limitado gerando uma saída estável limitada sob o critério BIBO.}
    \label{fig:bibo_estabilidade}
\end{figure}
"""

# ----------------- CAPÍTULO 17 -----------------
cap17_content = r"""\chapter{Transformada de Laplace}
\label{cap:17}

Neste capítulo, estudaremos a Transformada de Laplace unilateral e bilateral. Esta poderosa ferramenta estende a análise espectral de Fourier para sinais instáveis que crescem exponencialmente com o tempo, mapeando a dinâmica de sistemas no plano complexo $s$. Analisaremos detalhadamente a Região de Convergência (ROC) e suas propriedades matemáticas fundamentais.

---

\section{Definição de Transformada de Laplace}

A Transformada de Fourier Contínua exige que os sinais sejam absolutamente integráveis, impossibilitando a análise direta de sistemas instáveis (cujas respostas crescem exponencialmente). Para contornar esta limitação matemática, multiplicamos o sinal original $x(t)$ por um fator de decaimento exponencial amortecedor $e^{-\sigma t}$ antes de aplicar a Transformada de Fourier.

\begin{definicao}[Transformada de Laplace Bilateral]
A Transformada de Laplace Bilateral de um sinal contínuo $x(t)$ é definida pela integral complexa:
\begin{equation}
X(s) = \Lap\{x(t)\} = \intParenthesisex(t) e^{-st} \dt
\end{equation}
onde $s = \sigma + j\omega \in \C$ é a variável de frequência complexa de Laplace.
\end{definicao}

A respectiva fórmula da transformada de Laplace inversa realiza a integração ao longo de um contorno vertical no plano complexo:
\begin{equation}
x(t) = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} X(s) e^{st} \text{d}s
\end{equation}

A correlação física direta entre as formulações de Laplace e Fourier é evidente ao avaliarmos a variável complexa na fronteira imaginária nula $\sigma = 0 \implies s = j\omega$:
\begin{equation}
X(s)|_{s = j\omega} = \Lap\{x(t)\}|_{s = j\omega} = \F\{x(t)\} = X(j\omega)
\end{equation}
Esta relação de eixos e projeção entre o plano-s e a Transformada de Fourier é mostrada esquematicamente nas Figuras \ref{fig:planos_s_all}.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s.png}
        \caption{O plano complexo $s$ com eixos real $\sigma$ e imaginário $j\omega$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_laplace.png}
        \caption{Amostragem dinâmica no plano-s de Laplace.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_fourier.png}
        \caption{Fronteira de Fourier contida sobre o eixo imaginário.}
    \end{subfigure}
    \caption{Mapeamento de frequências reais e complexas no plano-s.}
    \label{fig:planos_s_all}
\end{figure}

---

\section{Região de Convergência (ROC)}

Como o integrando de Laplace contém o fator $e^{-st}$, a convergência da integral contínua de $-\infty$ a $\infty$ depende estritamente da escolha dos valores da parte real $\sigma = \text{Re}\{s\}$.

\begin{definicao}[Região de Convergência - ROC]
A \textbf{Região de Convergência} (ROC) é o conjunto de todos os valores de $s$ no plano complexo para os quais a integral de Laplace de $x(t)$ converge de forma absoluta:
\begin{equation}
\text{ROC} = \left\{ s \in \C : \intParenthesize|x(t) e^{-st}| \dt < \infty \right\}
\end{equation}
\end{definicao}

A ROC possui importantes propriedades geométricas que definem a natureza temporal do sinal de forma unívoca, ilustradas em detalhes nas Figuras \ref{fig:roc_planes_all} e \ref{fig:roc_planes_all2}:
\begin{enumerate}
    \item A ROC de $X(s)$ consiste em faixas ou listras verticais paralelas ao eixo imaginário $j\omega$ no plano-s (Figura \ref{fig:roc_banda}).
    \item Para sinais de duração finita, a ROC é todo o plano complexo $s$, exceto possivelmente no ponto de origem $s=0$ ou infinito $s=\infty$.
    \item Para sinais de tempo à direita (causais, isto é, $x(t) = 0$ para $t < t_0$), a ROC consiste no semiplano à direita do polo mais à direita (Figura \ref{fig:roc_right}).
    \item Para sinais de tempo à esquerda (anticausais), a ROC é o semiplano à esquerda do polo mais à esquerda (Figura \ref{fig:roc_left}).
    \item Para sinais bilaterais, a ROC consiste em uma faixa vertical limitada por polos em ambos os lados (Figura \ref{fig:roc_bilateral}).
    \item A ROC de um sistema não pode conter absolutamente nenhum polo de $X(s)$.
\end{enumerate}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_ROC.png}
        \caption{A ROC como faixa vertical de convergência.}
        \label{fig:roc_banda}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_ROC_exp_desc.png}
        \caption{ROC à direita do polo para um sinal causal exponencial decrescente.}
        \label{fig:roc_right}
    \end{subfigure}
    \caption{Visualização geométrica da Região de Convergência (ROC) de Laplace.}
    \label{fig:roc_planes_all}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_ROC_leftsided.png}
        \caption{ROC à esquerda para sinal anticausal.}
        \label{fig:roc_left}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_ROC_leftsided_rightsided.png}
        \caption{ROC de faixa interna para sinal de natureza bilateral.}
        \label{fig:roc_bilateral}
    \end{subfigure}
    \caption{Diferentes geometrias de ROC dependentes da causalidade do sinal.}
    \label{fig:roc_planes_all2}
\end{figure}

As Figuras \ref{fig:planos_s_sigma_all} marcam de forma exata o comportamento de integrabilidade da exponencial para diferentes seções verticais $\sigma$.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_ROC_exp_desc_sigma1.png}
        \caption{$\sigma < a$: Integral diverge.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_ROC_exp_desc_sigma2.png}
        \caption{$\sigma > a$: Integral converge.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{plano_s_ROC_intersec.png}
        \caption{Intersecção de ROC de sinais compostos.}
    \end{subfigure}
    \caption{Processo de análise e determinação física dos contornos da ROC.}
    \label{fig:planos_s_sigma_all}
\end{figure}
"""

# ----------------- CAPÍTULO 18 -----------------
cap18_content = r"""\chapter{Estabilidade de SLIT no Domínio s}
\label{cap:18}

Neste capítulo, estudaremos a análise de estabilidade e o comportamento transitório de Sistemas Lineares Invariantes no Tempo utilizando a Transformada de Laplace. Definiremos a Função de Transferência $H(s)$, a representação gráfica de polos e zeros e demonstraremos a correlação direta entre a ROC, a causalidade e a estabilidade BIBO. Analisaremos também as respostas a sistemas de 1ª e 2ª ordem.

---

\section{A Função de Transferência H(s)}

A Função de Transferência $H(s)$ de um SLIT contínuo é definida como a Transformada de Laplace de sua Resposta ao Impulso $h(t)$:
\begin{equation}
H(s) = \Lap\{h(t)\} = \int_{-\infty}^{\infty} h(t) e^{-st} \dt
\end{equation}

Para sistemas físicos práticos descritos por equações diferenciais ordinárias de coeficientes constantes, a função de transferência é expressa como uma função racional (razão de polinômios):
\begin{equation}
H(s) = \frac{B(s)}{A(s)} = \frac{b_m s^m + b_{m-1} s^{m-1} + \dots + b_0}{a_n s^n + a_{n-1} s^{n-1} + \dots + a_0}
\end{equation}
\begin{itemize}
    \item As raízes do numerador $B(s) = 0$ são os \textbf{Zeros} do sistema.
    \item As raízes do denominador $A(s) = 0$ são os \textbf{Polos} do sistema.
\end{itemize}

---

\section{Condição de Causalidade e Estabilidade no Plano-s}

A localização de polos e a geometria da ROC no plano-s determinam de forma única a causalidade e a estabilidade dinâmica do sistema.

\begin{teorema}[Estabilidade de SLIT Causal]
Um SLIT causal contínuo é BIBO estável se e somente se todos os polos de sua função de transferência $H(s)$ estiverem localizados estritamente no semiplano esquerdo (LHP - Left Half Plane) do plano-s, ou seja:
\begin{equation}
\text{Re}\{p_k\} < 0 \quad \text{para todos os polos } p_k
\end{equation}
\end{teorema}

\begin{proof}
Sabemos do Capítulo \ref{cap:16} que um sistema é BIBO estável se e somente se sua resposta ao impulso for absolutamente integrável. Isto implica diretamente que a Transformada de Fourier de $h(t)$ deve convergir.
Como a Transformada de Fourier equivale a avaliar a Transformada de Laplace sobre o eixo imaginário ($s = j\omega$), o eixo imaginário $j\omega$ deve necessariamente pertencer à Região de Convergência (ROC) do sistema estável:
\begin{equation}
j\omega \in \text{ROC}
\end{equation}
Como assumimos que o sistema é causal, a ROC consiste em todo o plano à direita do polo mais à direita.
Para que o eixo imaginário (que possui parte real $\text{Re}\{s\} = 0$) esteja contido nesta ROC causal estendida à direita, todos os polos do sistema devem residir à esquerda do eixo imaginário:
\[
\text{Re}\{p_k\} < 0
\]
o que prova o teorema fundamental de estabilidade dinâmica.
\end{proof}

---

\section{Análise de Resposta Temporal de 2ª Ordem}

Sistemas de 2ª ordem desempenham papel crucial na engenharia de controle e dinâmica física (ex: sistema massa-mola-amortecedor e circuitos RLC). A função de transferência padrão de 2ª ordem é dada por:
\begin{equation}
H(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}
\end{equation}
onde:
\begin{itemize}
    \item $\omega_n$ é a frequência natural não amortecida do sistema.
    \item $\zeta$ é o coeficiente de amortecimento.
\end{itemize}

O comportamento da resposta transitória do sistema a um degrau unitário varia drasticamente de acordo com o valor de $\zeta$:
\begin{itemize}
    \item \textbf{Subamortecido} ($0 \le \zeta < 1$): Os polos são complexos conjugados localizados no LHP. A resposta exibe oscilações senoidais amortecidas com sobre-sinal (*overshoot*), como exibido nas curvas temporais das Figuras \ref{fig:step_underdamped_all}.
    \item \textbf{Criticamente Amortecido} ($\zeta = 1$): Polos reais idênticos. É a resposta sem oscilação mais rápida possível.
    \item \textbf{Superamortecido} ($\zeta > 1$): Polos reais distintos. A resposta é lenta e dominada por decaimentos exponenciais puros.
\end{itemize}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{subamortecido_step.png}
        \caption{Resposta ao degrau unitário exibindo oscilações e overshoot.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{subamortecido_step_wn.png}
        \caption{Impacto do aumento da frequência natural $\omega_n$ na velocidade da resposta.}
    \end{subfigure}
    \caption{Curvas dinâmicas temporais de sistemas subamortecidos de 2ª ordem.}
    \label{fig:step_underdamped_all}
\end{figure}
"""

# ----------------- CAPÍTULO 19 -----------------
cap19_content = r"""\chapter{Resposta em Frequência de SLIT}
\label{cap:19}

Neste capítulo, estudaremos o comportamento dinâmico de regime permanente de Sistemas Lineares Invariantes no Tempo excitados por entradas senoidais puras no tempo. Mostraremos como avaliar a função de resposta em frequência $H(j\omega)$ diretamente a partir da função de transferência de Laplace $H(s)$ e como obter insights geométricos profundos e qualitativos baseados unicamente na localização de polos e zeros no plano complexo.

---

\section{Resposta a Entradas Senoidais de Regime}

Se excitamos um SLIT estável com um sinal senoidal puro real de frequência angular $\omega_0$:
\begin{equation}
x(t) = A \cos(\omega_0 t + \theta)
\end{equation}
a resposta de regime permanente do sistema, após o decaimento de todos os transientes associados às condições iniciais, é descrita por uma senoide com a exata mesma frequência, alterada unicamente em magnitude e fase pelo valor da resposta em frequência avaliada em $\omega_0$:
\begin{equation}
y(t) = A |H(j\omega_0)| \cos(\omega_0 t + \theta + \angle H(j\omega_0))
\end{equation}
onde:
\begin{equation}
H(j\omega_0) = H(s)|_{s = j\omega_0} = \int_{-\infty}^{\infty} h(t) e^{-j\omega_0 t} \dt
\end{equation}

---

\section{Interpretação Geométrica de Polos e Zeros}

Podemos determinar a forma de $H(j\omega)$ de forma puramente geométrica e qualitativa no plano-s. Seja a função de transferência racional escrita em termos de polos e zeros fatorados:
\begin{equation}
H(s) = K \frac{\prod_{i=1}^m (s - z_i)}{\prod_{k=1}^n (s - p_k)}
\end{equation}
A resposta em frequência é obtida avaliando $H(s)$ no eixo imaginário $s = j\omega$:
\begin{equation}
H(j\omega) = K \frac{\prod_{i=1}^m (j\omega - z_i)}{\prod_{k=1}^n (j\omega - p_k)}
\end{equation}

Cada termo da forma $(j\omega - z_i)$ ou $(j\omega - p_k)$ representa um vetor complexo que parte do zero $z_i$ ou polo $p_k$ apontando em direção ao ponto de interesse $j\omega$ sobre o eixo imaginário.
\begin{itemize}
    \item Módulo: O ganho $|H(j\omega)|$ é proporcional ao produto das magnitudes dos vetores partindo dos zeros dividido pelo produto das magnitudes dos vetores partindo dos polos.
    \item Fase: A fase total $\angle H(j\omega)$ é a soma dos ângulos dos vetores dos zeros subtraída da soma dos ângulos dos vetores dos polos.
\end{itemize}

Esta elegante propriedade visual nos permite esboçar a resposta em frequência de qualquer filtro apenas olhando para o diagrama de polos e zeros:
\begin{itemize}
    \item Polos próximos ao eixo $j\omega$ provocam picos acentuados de ganho na frequência correspondente (comportamento de ressonância ou passa-faixa).
    \item Zeros localizados sobre o eixo $j\omega$ ou muito próximos a ele anulam completamente o ganho na respectiva frequência (comportamento de rejeição).
\end{itemize}

As Figuras \ref{fig:freq_resp_poles_zeros_all} ilustram esse mapeamento qualitativo no plano complexo e em gráficos 3D associados.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{resposta_frequencia.png}
        \caption{Avaliação de vetores complexos do polo ao eixo imaginário.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{resposta_frequencia3.png}
        \caption{Superfície 3D de magnitude de Laplace evidenciando o pico infinito no polo.}
    \end{subfigure}
    \caption{Interpretação geométrica da resposta em frequência a partir do plano-s.}
    \label{fig:freq_resp_poles_zeros_all}
\end{figure}

As Figuras \ref{fig:freq_responses_1st_2nd_all} trazem a resposta em frequência calculada para diferentes sistemas de 1ª ordem, 2ª ordem e integradores puros (polos na origem ou zeros complexos conjugados).

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{resposta_frequencia_1ordem.png}
        \caption{Resposta de módulo e fase para sistema de 1ª ordem.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{resposta_frequencia_2ordem.png}
        \caption{Pico de ressonância acentuado para polos subamortecidos de 2ª ordem.}
    \end{subfigure}
    
    \vspace{0.2cm}
    
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{resposta_frequencia_polo_origem.png}
        \caption{Comportamento integrador com polo na origem.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{resposta_frequencia_zeros_conjugados.png}
        \caption{Comportamento rejeita-faixa com zeros no plano complexo.}
    \end{subfigure}
    \caption{Curvas de resposta em frequência típicas para diferentes localizações de polos e zeros.}
    \label{fig:freq_responses_1st_2nd_all}
\end{figure}
"""

# ----------------- CAPÍTULO 20 -----------------
cap20_content = r"""\chapter{Diagrama de Blocos e Espaço de Estados}
\label{cap:20}

Neste capítulo, estudaremos a representação interna de sistemas dinâmicos lineares e invariantes no tempo. Analisaremos as conexões por diagramas de blocos clássicas (série, paralelo e malha fechada) e introduziremos a modelagem moderna em Espaço de Estados, demonstrando as equações matriciais fundamentais e sua conexão matemática rigorosa com a Função de Transferência clássica.

---

\section{Representações por Diagrama de Blocos}

Sistemas complexos são construídos interconectando subsistemas mais simples. As três configurações clássicas de diagramas de blocos e suas reduções matemáticas são mostradas nas Figuras \ref{fig:diagramas_blocos_all}:

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{sistema_serie.png}
        \caption{Associação em Série (Cascata): $H(s) = H_1(s)H_2(s)$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{sistema_paralelo.png}
        \caption{Associação em Paralelo: $H(s) = H_1(s) + H_2(s)$.}
    \end{subfigure}
    
    \vspace{0.3cm}
    
    \begin{subfigure}[b]{0.65\textwidth}
        \centering
        \includegraphics[width=\textwidth]{sistema_realimentacao.png}
        \caption{Malha Fechada (Realimentação clássica).}
    \end{subfigure}
    \caption{Três estruturas clássicas de conexão e simplificação de diagramas de blocos.}
    \label{fig:diagramas_blocos_all}
\end{figure}

\begin{teorema}[Fórmula de Realimentação Clássica]
A função de transferência de malha fechada $H(s) = Y(s)/X(s)$ de um sistema com caminho direto $G(s)$ e malha de realimentação $H_{fb}(s)$ é dada por:
\begin{equation}
H(s) = \frac{G(s)}{1 + G(s)H_{fb}(s)}
\end{equation}
onde o sinal no denominador assume o caractere $+$ para realimentação negativa e $-$ para positiva.
\end{teorema}

---

\section{Modelagem em Espaço de Estados}

Diferente da Função de Transferência (que é uma representação externa baseada estritamente na relação de entrada-saída sob condições iniciais nulas), a modelagem em **Espaço de Estados** é uma representação interna de 1ª ordem baseada em variáveis internas chamadas variáveis de estado.

\begin{definicao}[Equações de Estado]
A representação matemática em espaço de estados de um SLIT contínuo linear é expressa por um par de equações matriciais:
\begin{equation}
\dot{\mathbf{x}}(t) = A \mathbf{x}(t) + B \mathbf{u}(t) \quad (\text{Equação de Estado})
\end{equation}
\begin{equation}
\mathbf{y}(t) = C \mathbf{x}(t) + D \mathbf{u}(t) \quad (\text{Equação de Saída})
\end{equation}
onde:
\begin{itemize}
    \item $\mathbf{x}(t) \in \R^n$ é o vetor de variáveis de estado (estados internos).
    \item $\mathbf{u}(t) \in \R^m$ é o vetor de sinais de entrada (excitações).
    \item $\mathbf{y}(t) \in \R^p$ é o vetor de sinais de saída (respostas).
    \item $A$ é a matriz de dinâmica interna ($n \times n$).
    \item $B$ é a matriz de entrada ($n \times m$).
    \item $C$ é a matriz de saída ($p \times n$).
    \item $D$ é a matriz de transmissão direta ($p \times m$).
\end{itemize}
\end{definicao}

---

\section{Conexão entre Espaço de Estados e H(s)}

Existe uma equivalência matemática exata entre a representação matricial interna e a função de transferência clássica de Laplace.

\begin{teorema}[Transição de Estados para Laplace]
Seja um sistema LTI descrito pelas matrizes de estado $\{A, B, C, D\}$. A sua correspondente Função de Transferência racional $H(s)$ é dada de forma única por:
\begin{equation}
H(s) = C(sI - A)^{-1}B + D
\end{equation}
onde $I$ representa a matriz identidade de dimensão correspondente.
\end{teorema}

\begin{proof}
Partimos da Equação de Estado no domínio do tempo:
\[
\dot{\mathbf{x}}(t) = A \mathbf{x}(t) + B \mathbf{u}(t)
\]
Aplicamos a Transformada de Laplace unilateral sob condições iniciais estritamente nulas ($\mathbf{x}(0) = \mathbf{0}$):
\begin{align*}
s \mathbf{X}(s) &= A \mathbf{X}(s) + B \mathbf{U}(s)
\end{align*}
Agrupamos os termos contendo $\mathbf{X}(s)$ no lado esquerdo da igualdade, e usamos a matriz identidade $I$:
\begin{align*}
s I \mathbf{X}(s) - A \mathbf{X}(s) &= B \mathbf{U}(s) \\
(sI - A)\mathbf{X}(s) &= B \mathbf{U}(s)
\end{align*}
Isolamos o vetor de estado $\mathbf{X}(s)$ multiplicando pela matriz inversa $(sI - A)^{-1}$:
\begin{equation}
\mathbf{X}(s) = (sI - A)^{-1} B \mathbf{U}(s)
\end{equation}

Agora aplicamos a Transformada de Laplace na Equação de Saída:
\begin{align*}
\mathbf{Y}(s) &= C \mathbf{X}(s) + D \mathbf{U}(s)
\end{align*}
Substituímos o vetor de estado isolado $\mathbf{X}(s)$ na equação:
\begin{align*}
\mathbf{Y}(s) &= C \left[ (sI - A)^{-1} B \mathbf{U}(s) \right] + D \mathbf{U}(s) \\
\mathbf{Y}(s) &= \left[ C(sI - A)^{-1}B + D \right] \mathbf{U}(s)
\end{align*}
Como a função de transferência define a relação de amplitude direta $\mathbf{Y}(s) = H(s) \mathbf{U}(s)$:
\[
H(s) = C(sI - A)^{-1}B + D
\]
o que demonstra perfeitamente o teorema fundamental.
\end{proof}
"""

with open(os.path.join(output_dir, "cap16.tex"), "w", encoding="utf-8") as f:
    f.write(cap16_content)
with open(os.path.join(output_dir, "cap17.tex"), "w", encoding="utf-8") as f:
    f.write(cap17_content)
with open(os.path.join(output_dir, "cap18.tex"), "w", encoding="utf-8") as f:
    f.write(cap18_content)
with open(os.path.join(output_dir, "cap19.tex"), "w", encoding="utf-8") as f:
    f.write(cap19_content)
with open(os.path.join(output_dir, "cap20.tex"), "w", encoding="utf-8") as f:
    f.write(cap20_content)

print("Lote 4 (cap16 a cap20) gerado com sucesso!")
