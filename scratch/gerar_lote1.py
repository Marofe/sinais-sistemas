import os

output_dir = r"G:\My Drive\Disciplinas\Graduação\SEL0383-Sinais e Sistemas\slides\apostila"
os.makedirs(output_dir, exist_ok=True)

# ----------------- CAPÍTULO 4 -----------------
cap4_content = r"""\chapter{Função Impulso e Operação de Convolução}
\label{cap:4}

Neste capítulo, estudaremos em profundidade a função impulso unitário (Delta de Dirac) e a operação fundamental de convolução contínua. Estas ferramentas matemáticas são o alicerce para a caracterização de Sistemas Lineares e Invariantes no Tempo (SLIT) no domínio do tempo, permitindo determinar a saída de um sistema a partir de qualquer excitação genérica.

---

\section{Propriedades Matemáticas do Delta de Dirac}

Relembrando a definição do Delta de Dirac $\delta(t)$ introduzida no Capítulo \ref{cap:1}, esta distribuição possui propriedades singulares de extrema importância prática:

\subsection{Propriedade de Filtragem (Sifting Property)}
O impulso unitário é capaz de isolar ou extrair o valor de um sinal contínuo no instante de ocorrência do impulso:

\begin{teorema}[Filtragem]
Seja $f(t)$ uma função contínua no instante $t=t_0$. Então:
\begin{equation}
\int_{-\infty}^{\infty} f(t) \delta(t - t_0) \dt = f(t_0)
\end{equation}
\end{teorema}

\begin{proof}
Como $\delta(t-t_0) = 0$ para todo $t \neq t_0$, o integrando é nulo em todo o domínio, exceto no ponto $t = t_0$. Portanto, podemos substituir o valor da função $f(t)$ pelo seu valor constante $f(t_0)$ na integral:
\begin{align*}
\int_{-\infty}^{\infty} f(t) \delta(t - t_0) \dt &= \int_{-\infty}^{\infty} f(t_0) \delta(t - t_0) \dt
\end{align*}
Pela linearidade da integral, podemos retirar a constante $f(t_0)$:
\begin{align*}
&= f(t_0) \int_{-\infty}^{\infty} \delta(t - t_0) \dt
\end{align*}
Como a integral do Delta deslocado continua possuindo área unitária, ou seja, $\int_{-\infty}^{\infty} \delta(t - t_0) \dt = 1$, obtemos:
\[
= f(t_0) \cdot 1 = f(t_0)
\]
Provando a propriedade.
\end{proof}

\subsection{Propriedade de Amostragem (Produto por Delta)}
Da mesma forma, o produto direto de um sinal contínuo pelo Delta resulta no próprio Delta escalonado pela amplitude do sinal naquele instante:
\begin{equation}
f(t) \delta(t - t_0) = f(t_0) \delta(t - t_0)
\end{equation}

\subsection{Propriedade de Mudança de Escala (Scaling Property)}
A escala temporal no argumento do Delta altera a sua área de forma inversamente proporcional:

\begin{teorema}[Mudança de Escala]
Para qualquer constante real não nula $a$:
\begin{equation}
\delta(at) = \frac{1}{|a|} \delta(t)
\end{equation}
\end{teorema}

\begin{proof}
Avaliamos a integral da distribuição sob uma mudança de variável $u = at \implies \dd u = a \dt \implies \dt = \frac{1}{a} \dd u$.
Se $a > 0$, os limites de integração permanecem inalterados ($-\infty$ a $\infty$):
\begin{align*}
\int_{-\infty}^{\infty} f(t) \delta(at) \dt &= \int_{-\infty}^{\infty} f\left(\frac{u}{a}\right) \delta(u) \frac{1}{a} \dd u = \frac{1}{a} f(0)
\end{align*}
Se $a < 0$, os limites de integração invertem-se ($\infty$ a $-\infty$), e a correção de inversão de sinal da integral compensa o sinal negativo de $a$:
\begin{align*}
\int_{-\infty}^{\infty} f(t) \delta(at) \dt &= \int_{\infty}^{-\infty} f\left(\frac{u}{a}\right) \delta(u) \frac{1}{a} \dd u = -\frac{1}{a} \int_{-\infty}^{\infty} f\left(\frac{u}{a}\right) \delta(u) \dd u = \frac{1}{-a} f(0)
\end{align*}
Unindo ambos os casos usando o valor absoluto:
\[
\int_{-\infty}^{\infty} f(t) \delta(at) \dt = \frac{1}{|a|} f(0)
\]
Isto demonstra que $\delta(at) = \frac{1}{|a|}\delta(t)$ no sentido das distribuições.
\end{proof}

---

\section{Decomposição de Sinais e a Integral de Convolução}

O conceito físico de convolução surge diretamente ao tentarmos representar um sinal contínuo genérico $x(t)$ como uma soma (integral) infinita de impulsos unitários deslocados e ponderados. 

As Figuras \ref{fig:base_canonica} e \ref{fig:base_impulsos} mostram essa analogia: assim como um vetor em $\R^n$ é escrito como soma de projeções na base canônica de coordenadas discretas, qualquer sinal contínuo $x(t)$ pode ser decomposto em uma base contínua de impulsos deslocados $\delta(t-\tau)$:
\begin{equation}
x(t) = \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \dtau
\end{equation}
Esta equação é denominada a representação de amostragem integral de $x(t)$.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.45\textwidth]{base_canonica.png}
    \caption{Analogia discreta: vetor decomposto em termos das bases canônicas.}
    \label{fig:base_canonica}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.45\textwidth]{base_impulsos.png}
    \caption{Analogia contínua: sinal $x(t)$ decomposto como uma integral de impulsos infinitesimalmente densos.}
    \label{fig:base_impulsos}
\end{figure}

Suponha agora que passamos este sinal $x(t)$ por um sistema operador linear $H\{\cdot\}$. Pela linearidade do sistema, a transformação atua diretamente dentro da integral sobre os elementos de base $\delta(t-\tau)$:
\begin{align*}
y(t) &= H\{x(t)\} = H\left\{ \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \dtau \right\} \\
&= \int_{-\infty}^{\infty} x(\tau) H\{\delta(t - \tau)\} \dtau
\end{align*}
Se o sistema for além disso \textbf{Invariante no Tempo}, sua resposta a um impulso deslocado $\delta(t-\tau)$ é simplesmente a resposta do sistema ao impulso na origem $h(t) = H\{\delta(t)\}$ deslocada temporalmente de $\tau$:
\begin{equation}
H\{\delta(t - \tau)\} = h(t - \tau)
\end{equation}
onde $h(t)$ é chamada de **Resposta ao Impulso** do sistema, como mostrado conceitualmente na Figura \ref{fig:resposta_ao_impulso} e no diagrama físico das Figuras \ref{fig:resposta_impulso_sistema_all}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\textwidth]{resposta_ao_impulso.png}
    \caption{O sinal de resposta ao impulso $h(t)$ como a assinatura dinâmica temporal do sistema.}
    \label{fig:resposta_ao_impulso}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{resposta_impulso_sistema.png}
        \caption{Um impulso $\delta(t)$ gerando a resposta $h(t)$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{resposta_impulso_sistema2.png}
        \caption{Um impulso deslocado $\delta(t-\tau)$ gerando a resposta $h(t-\tau)$.}
    \end{subfigure}
    \caption{Princípio da Invariância no Tempo atuando sobre a resposta ao impulso.}
    \label{fig:resposta_impulso_sistema_all}
\end{figure}

Substituindo essa relação na integral, obtemos a monumental **Integral de Convolução**:

\begin{teorema}[Integral de Convolução]
A resposta de qualquer Sistema Linear Invariante no Tempo (SLIT) a uma entrada genérica $x(t)$ é dada pela convolução temporal entre a entrada e a resposta ao impulso $h(t)$:
\begin{equation}
y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \dtau
\end{equation}
\end{teorema}

---

\section{Interpretação Geométrica e Gráfica da Convolução}

A convolução descreve a mistura física das duas formas de onda ao longo do tempo. Matematicamente, a integral envolve quatro passos gráficos fundamentais para cada instante $t$:
\begin{enumerate}
    \item \textbf{Inversão} (Flip): Refletir $h(\tau)$ em relação à origem para obter $h(-\tau)$.
    \item \textbf{Deslocamento} (Shift): Deslocar o sinal refletido de $t$ para obter $h(t-\tau)$.
    \item \textbf{Multiplicação} (Multiply): Multiplicar $x(\tau)$ por $h(t-\tau)$ ponto a ponto.
    \item \textbf{Integração} (Integrate): Calcular a área sob a curva resultante da multiplicação.
\end{enumerate}

As Figuras \ref{fig:conv_gate} e \ref{fig:conv_exp} exibem este processo para diferentes combinações clássicas de sinais físicos: pulsos quadrados (gate), funções exponenciais e rampas lineares.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{conv_gate.png}
    \caption{Processo de convolução entre dois pulsos retangulares de largura unitária, resultando em um pulso triangular.}
    \label{fig:conv_gate}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conv_exp_exp.png}
        \caption{Convolução entre duas funções exponenciais causais decrescentes.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conv_exp_gate.png}
        \caption{Convolução de pulso retangular com exponencial decrescente.}
    \end{subfigure}
    \caption{Exemplos práticos de formas de onda geradas por convolução.}
    \label{fig:conv_exp}
\end{figure}

As Figuras \ref{fig:conv_reta_gate_all} mostram o progresso passo a passo de uma convolução entre um pulso rampa e um pulso quadrado (gate) conforme a janela desliza no tempo.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conv_reta_gate01.png}
        \caption{Antes do contato ($t < 0$).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conv_reta_gate02.png}
        \caption{Contato parcial inicial ($0 < t < 1$).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conv_reta_gate03.png}
        \caption{Sobreposição completa da janela.}
    \end{subfigure}
    
    \vspace{0.2cm}
    
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conv_reta_gate04.png}
        \caption{Saída gradual da janela.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conv_reta_gate05.png}
        \caption{Após o contato ($t > 2$).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conv_reta_gate06.png}
        \caption{O sinal convoluído final completo.}
    \end{subfigure}
    \caption{Estudo de caso gráfico passo a passo da operação de convolução contínua.}
    \label{fig:conv_reta_gate_all}
\end{figure}

---

\section{Propriedades da Convolução}

A operação de convolução contínua atende a importantes propriedades algébricas de fácil demonstração:

\subsection{Propriedade Comutativa}
A ordem dos sinais na convolução não altera a resposta do sistema:
\begin{equation}
x(t) * h(t) = h(t) * x(t)
\end{equation}

\begin{proof}
Iniciamos com a definição $\int_{-\infty}^{\infty} x(\tau)h(t-\tau)\dtau$. Fazemos uma mudança de variável $u = t - \tau \implies \tau = t - u \implies \dtau = -\dd u$.
Os limites de integração mudam de $(\infty, -\infty)$.
\begin{align*}
\int_{-\infty}^{\infty} x(\tau) h(t - \tau) \dtau &= \int_{\infty}^{-\infty} x(t - u) h(u) (-\dd u) \\
&= \int_{-\infty}^{\infty} h(u) x(t - u) \dd u = h(t) * x(t)
\end{align*}
Comprovando a comutatividade.
\end{proof}

\subsection{Propriedade Distributiva}
A convolução é linear em relação à adição de sinais:
\begin{equation}
x(t) * [h_1(t) + h_2(t)] = x(t) * h_1(t) + x(t) * h_2(t)
\end{equation}
Geometricamente, esta propriedade representa a equivalência entre dois sistemas em paralelo e um único sistema cuja resposta ao impulso é a soma das respostas individuais.

\subsection{Propriedade Associativa}
A convolução em cascata de múltiplos sistemas é associativa:
\begin{equation}
x(t) * [h_1(t) * h_2(t)] = [x(t) * h_1(t)] * h_2(t)
\end{equation}
Esta propriedade prova a equivalência física de sistemas LTI em cascata (série): a ordem de ligação em série de dois blocos dinâmicos LTI não altera em nada o sinal de saída final.
"""

# ----------------- CAPÍTULO 5 -----------------
cap5_content = r"""\chapter{Sinais Periódicos e Série de Fourier}
\label{cap:5}

Neste capítulo, estudaremos a representação clássica de Fourier para sinais periódicos. A Série de Fourier decompõe qualquer forma de onda periódica contínua em uma soma infinita de senos e cossenos (Série Trigonométrica) ou em uma soma de exponenciais complexas (Série Exponencial). Esta representação permite transitar a análise de sinais do domínio do tempo para o domínio da frequência.

---

\section{Contexto Histórico}

O físico e matemático francês Jean-Baptiste Joseph Fourier (retratado na Figura \ref{fig:joseph_fourier}) propôs em 1807 que qualquer função periódica poderia ser decomposta como soma de harmônicos senoidais, no âmbito do estudo da equação de transferência de calor em placas metálicas (mostrado esquematicamente nas Figuras \ref{fig:fourier_heat_all}). Embora contestada na época por gigantes como Lagrange e Laplace pela falta de rigor analítico, a formulação de Fourier revolucionou a matemática moderna e a física de ondas.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.3\textwidth]{joseph_fourier.webp}
    \caption{Jean-Baptiste Joseph Fourier (1768--1830).}
    \label{fig:joseph_fourier}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_heat_transfer.png}
        \caption{Difusão unidimensional de calor.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_heat_transfer2.png}
        \caption{Grade térmica bidimensional de contorno.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_heat_transfer3.png}
        \caption{Equilíbrio de temperatura em placas.}
    \end{subfigure}
    \caption{Estudo de difusão térmica que levou à criação da Série de Fourier.}
    \label{fig:fourier_heat_all}
\end{figure}

---

\section{Série Trigonométrica de Fourier}

A Série Trigonométrica de Fourier representa um sinal periódico real $x(t)$ de período fundamental $T_0$ (e frequência angular fundamental $\omega_0 = 2\pi/T_0$) por meio de um termo médio contínuo e harmônicos senoidais puros.

\begin{definicao}[Série Trigonométrica]
A representação trigonométrica da Série de Fourier é expressa por:
\begin{equation}
x(t) = a_0 + \sum_{n=1}^{\infty} a_n \cos(n\omega_0 t) + \sum_{n=1}^{\infty} b_n \sin(n\omega_0 t)
\end{equation}
onde:
\begin{itemize}
    \item $a_0$ é o valor médio (nível DC) do sinal.
    \item $a_n$ são os coeficientes harmônicos associados ao cosseno (componentes pares).
    \item $b_n$ são os coeficientes harmônicos associados ao seno (componentes ímpares).
\end{itemize}
\end{definicao}

\begin{teorema}[Fórmulas de Euler-Fourier]
Os coeficientes da série trigonométrica são calculados de forma analítica por:
\begin{equation}
a_0 = \frac{1}{T_0} \int_{T_0} x(t) \dt
\end{equation}
\begin{equation}
a_n = \frac{2}{T_0} \int_{T_0} x(t) \cos(n\omega_0 t) \dt
\end{equation}
\begin{equation}
b_n = \frac{2}{T_0} \int_{T_0} x(t) \sin(n\omega_0 t) \dt
\end{equation}
onde a notação $\int_{T_0}$ representa a integração realizada ao longo de um período completo qualquer (ex: de $0$ a $T_0$, ou de $-T_0/2$ a $T_0/2$).
\end{teorema}

\begin{proof}
Para derivar a fórmula do coeficiente cossenoidal $a_n$, multiplicamos ambos os lados da equação da série por $\cos(m\omega_0 t)$ e integramos sobre um período fundamental $[0, T_0]$:
\begin{align*}
\int_0^{T_0} x(t)\cos(m\omega_0 t)\dt &= \int_0^{T_0} \left[ a_0 + \sum_{n=1}^{\infty} a_n \cos(n\omega_0 t) + \sum_{n=1}^{\infty} b_n \sin(n\omega_0 t) \right] \cos(m\omega_0 t)\dt
\end{align*}
Pelas propriedades de ortogonalidade dos harmônicos trigonométricos sobre o período fundamental $[0, T_0]$:
\begin{equation}
\int_0^{T_0} \cos(n\omega_0 t) \cos(m\omega_0 t) \dt = \frac{T_0}{2} \delta_{nm}
\end{equation}
\begin{equation}
\int_0^{T_0} \sin(n\omega_0 t) \cos(m\omega_0 t) \dt = 0
\end{equation}
\begin{equation}
\int_0^{T_0} \cos(m\omega_0 t) \dt = 0 \quad (\text{para } m \neq 0)
\end{equation}
Apenas o termo correspondente a $n = m$ no primeiro somatório sobrevive à integração:
\begin{align*}
\int_0^{T_0} x(t)\cos(m\omega_0 t)\dt &= a_m \cdot \frac{T_0}{2}
\end{align*}
Isolando $a_m$, obtemos exatamente:
\[
a_m = \frac{2}{T_0} \int_0^{T_0} x(t) \cos(m\omega_0 t) \dt
\]
A demonstração para $b_n$ é perfeitamente análoga, multiplicando-se por $\sin(m\omega_0 t)$.
\end{proof}

---

\section{Série Exponencial de Fourier}

A forma mais elegante e compacta da Série de Fourier surge ao utilizarmos a Base de Fourier complexa ortogonal $\{e^{jn\omega_0 t}\}$ apresentada no Capítulo \ref{cap:3}.

\begin{definicao}[Série Exponencial]
A representação em Série Exponencial de Fourier é dada por:
\begin{equation}
x(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}
\end{equation}
onde os coeficientes complexos de Fourier $c_n$ são expressos por:
\begin{equation}
c_n = \frac{1}{T_0} \int_{T_0} x(t) e^{-jn\omega_0 t} \dt
\end{equation}
\end{definicao}

Os coeficientes complexos carregam simultaneamente informações sobre a amplitude e a fase de cada componente harmônica. A relação matemática direta entre os coeficientes complexos ($c_n$) e os trigonométricos ($a_n, b_n$) deriva das fórmulas de Euler:
\begin{equation}
c_0 = a_0
\end{equation}
\begin{equation}
c_n = \frac{a_n - jb_n}{2}, \quad c_{-n} = c_n^* = \frac{a_n + jb_n}{2} \quad (\text{para } n > 0)
\end{equation}

---

\section{Exemplo Resolvido Detalhado: Onda Quadrada Simétrica}

Para ilustrar o processo analítico de cálculo, determinaremos a representação em Série de Fourier de uma onda quadrada periódica simétrica de período $T_0$ e amplitude $A$.

As Figuras \ref{fig:fourier_exemplo1_all} exibem graficamente como a soma progressiva dos harmônicos senoidais ($N=1, N=2, N=3, N=4$) converge de forma notável em direção ao formato de degrau da onda quadrada.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_exemplo1_N1.png}
        \caption{Aproximação harmônica para $N=1$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_exemplo1_N2.png}
        \caption{Aproximação harmônica para $N=2$ (harmônicos superiores).}
    \end{subfigure}
    
    \vspace{0.2cm}
    
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_exemplo1_N3.png}
        \caption{Aproximação harmônica para $N=3$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_exemplo1_N4.png}
        \caption{Aproximação harmônica para $N=4$ exibindo ripple nas bordas.}
    \end{subfigure}
    \caption{Processo físico-trigonométrico de síntese de onda quadrada a partir de Série de Fourier.}
    \label{fig:fourier_exemplo1_all}
\end{figure}

\begin{exemplo}[Coeficientes Complexos da Onda Quadrada]
Seja a onda quadrada periódica alternada de amplitude $A$ e período $T_0$, definida no intervalo de um período $[-T_0/2, T_0/2]$ por:
\[
x(t) = \begin{cases}
    A,  & -T_0/4 < t < T_0/4 \\
   -A,  & -T_0/2 < t < -T_0/4 \quad \text{e} \quad T_0/4 < t < T_0/2
\end{cases}
\]
Calculamos os coeficientes complexos $c_n$:
\begin{align*}
c_n &= \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} x(t) e^{-jn\omega_0 t} \dt \\
&= \frac{1}{T_0} \left[ \int_{-T_0/2}^{-T_0/4} (-A) e^{-jn\omega_0 t} \dt + \int_{-T_0/4}^{T_0/4} A e^{-jn\omega_0 t} \dt + \int_{T_0/4}^{T_0/2} (-A) e^{-jn\omega_0 t} \dt \right]
\end{align*}
Avaliando as integrais exponenciais (para $n \neq 0$):
\begin{align*}
c_n &= \frac{A}{T_0} \left[ \left. \frac{e^{-jn\omega_0 t}}{jn\omega_0} \right|_{-T_0/2}^{-T_0/4} - \left. \frac{e^{-jn\omega_0 t}}{jn\omega_0} \right|_{-T_0/4}^{T_0/4} + \left. \frac{e^{-jn\omega_0 t}}{jn\omega_0} \right|_{T_0/4}^{T_0/2} \right] \\
&= \frac{A}{jn2\pi} \left[ (e^{jn\pi/2} - e^{jn\pi}) - (e^{-jn\pi/2} - e^{jn\pi/2}) + (e^{-jn\pi} - e^{-jn\pi/2}) \right]
\end{align*}
Utilizando o fato de que $e^{jn\pi} = e^{-jn\pi} = (-1)^n$:
\begin{align*}
c_n &= \frac{A}{jn2\pi} \left[ 2 e^{jn\pi/2} - 2 e^{-jn\pi/2} \right] = \frac{2A}{n\pi} \left[ \frac{e^{jn\pi/2} - e^{-jn\pi/2}}{2j} \right] \\
&= \frac{2A}{n\pi} \sin\left(\frac{n\pi}{2}\right)
\end{align*}
Avaliando os valores para diferentes valores de $n$:
\begin{itemize}
    \item Para $n$ par: $\sin(n\pi/2) = 0 \implies c_n = 0$.
    \item Para $n = 1, 5, 9, \dots$: $\sin(n\pi/2) = 1 \implies c_n = \frac{2A}{n\pi}$.
    \item Para $n = 3, 7, 11, \dots$: $\sin(n\pi/2) = -1 \implies c_n = -\frac{2A}{n\pi}$.
\end{itemize}
Para $n=0$, o valor médio é $c_0 = a_0 = 0$ pela óbvia simetria de área da onda.
\end{exemplo}

A distribuição de energia e componentes espectrais resultante deste exemplo clássico de engenharia elétrica é representada geometricamente nas linhas de espectro mostradas na Figura \ref{fig:espectro_exponencial}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{espectro_exponencial.png}
    \caption{O espectro de linha discreto de amplitude da onda quadrada simétrica.}
    \label{fig:espectro_exponencial}
\end{figure}
"""

# ----------------- CAPÍTULO 6 -----------------
cap6_content = r"""\chapter{Espectro de Fourier e Fenômenos Físicos}
\label{cap:6}

Neste capítulo, aprofundaremos a análise do Espectro de Frequência discreto dos sinais periódicos, abordando o Teorema de Parseval para conservação de energia/potência, o Fenômeno de Gibbs gerado por descontinuidades e a correlação direta entre o comportamento temporal e espectral.

---

\section{Análise do Espectro de Módulo e Fase}

Como os coeficientes $c_n$ da Série Exponencial de Fourier são números complexos, eles podem ser escritos em sua forma polar:
\begin{equation}
c_n = |c_n| e^{j\angle c_n}
\end{equation}
Isso divide a nossa análise do domínio de frequência em dois espectros discretos de linha (como ilustrado na Figura \ref{fig:espectros_mag_fase_all}):
\begin{enumerate}
    \item \textbf{Espectro de Módulo}: Gráfico de $|c_n|$ versus a frequência angular $n\omega_0$. Mostra a distribuição de amplitude de cada componente harmônica. É uma função sempre par para sinais reais ($|c_{-n}| = |c_n|$).
    \item \textbf{Espectro de Fase}: Gráfico de $\angle c_n$ versus a frequência angular $n\omega_0$. Mostra o alinhamento temporal (defasagem) de cada harmônico. É uma função sempre ímpar para sinais reais ($\angle c_{-n} = -\angle c_n$).
\end{enumerate}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{espectro_fourier_mag.png}
        \caption{Espectro bilateral típico de módulo (par).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{espectro_fourier_fase.png}
        \caption{Espectro bilateral típico de fase (ímpar).}
    \end{subfigure}
    \caption{Visualização gráfica clássica da representação em frequência bilateral de Fourier.}
    \label{fig:espectros_mag_fase_all}
\end{figure}

As Figuras \ref{fig:espectros_exemplos_all} trazem espectros de linha calculados para sinais experimentais reais, exibindo a energia concentrada em harmônicos ímpares ou decaindo suavemente.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{espectro_fourier_mod_ex.png}
        \caption{Módulo discreto real calculado.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{espectro_fourier_fase_ex.png}
        \caption{Fase correspondente discreta.}
    \end{subfigure}
    \caption{Espectros de linha medidos empiricamente.}
    \label{fig:espectros_exemplos_all}
\end{figure}

---

\section{O Teorema de Parseval}

O Teorema de Parseval estabelece que a potência média total calculada no domínio do tempo é exatamente igual à soma das potências de cada uma das componentes harmônicas no domínio da frequência. Trata-se do princípio físico da conservação da energia estendido para espaços vetoriais funcionais.

\begin{teorema}[Teorema de Parseval]
Seja $x(t)$ um sinal periódico de período fundamental $T_0$ com coeficientes complexos de Fourier $c_n$. A sua potência média total $P_x$ é dada por:
\begin{equation}
P_x = \frac{1}{T_0} \int_{T_0} |x(t)|^2 \dt = \sum_{n=-\infty}^{\infty} |c_n|^2
\end{equation}
\end{teorema}

\begin{proof}
Iniciamos com a definição clássica de potência média:
\begin{align*}
P_x &= \frac{1}{T_0} \int_{T_0} x(t) x^*(t) \dt
\end{align*}
Substituímos o sinal conjugado $x^*(t)$ usando a sua representação em Série Exponencial de Fourier:
\begin{align*}
x^*(t) &= \left( \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t} \right)^* = \sum_{n=-\infty}^{\infty} c_n^* e^{-jn\omega_0 t}
\end{align*}
Substituindo essa expansão na integral de potência:
\begin{align*}
P_x &= \frac{1}{T_0} \int_{T_0} x(t) \left( \sum_{n=-\infty}^{\infty} c_n^* e^{-jn\omega_0 t} \right) \dt
\end{align*}
Permutando de forma analítica a ordem de integração e soma:
\begin{align*}
P_x &= \sum_{n=-\infty}^{\infty} c_n^* \left[ \frac{1}{T_0} \int_{T_0} x(t) e^{-jn\omega_0 t} \dt \right]
\end{align编}
Reconhecendo que a expressão entre colchetes é a própria definição clássica do coeficiente de Fourier complexo $c_n$:
\begin{align*}
P_x &= \sum_{n=-\infty}^{\infty} c_n^* c_n = \sum_{n=-\infty}^{\infty} |c_n|^2
\end{align*}
Isto demonstra o teorema de Parseval.
\end{proof}

---

\section{O Fenômeno de Gibbs}

Ao tentar aproximar funções periódicas que contêm descontinuidades abruptas por meio de uma série de Fourier truncada em $N$ harmônicos:
\begin{equation}
x_N(t) = \sum_{n=-N}^{N} c_n e^{jn\omega_0 t}
\end{equation}
surge um comportamento oscilatório singular nas vizinhanças dos pontos de descontinuidade. Este efeito é conhecido como o **Fenômeno de Gibbs**, em homenagem ao físico americano Willard Gibbs.

\begin{alerta}[Pitfall do Fenômeno de Gibbs]
O Fenômeno de Gibbs estabelece que, não importa o quão alto seja o número de harmônicos $N$ utilizados na aproximação, a amplitude do sobressinal (*overshoot*) nas bordas da descontinuidade não desaparece. Ela converge para um valor limite constante de aproximadamente \textbf{9\%} da amplitude do salto de descontinuidade.
\end{alerta}

O aumento do número de termos $N$ apenas estreita a largura das oscilações, aproximando o pico oscilatório cada vez mais do ponto exato da transição, contudo, a amplitude do pico permanece inalterada em ~9\%. A Figura \ref{fig:gibbs_pulse} exibe graficamente esse sobressinal característico.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{trem_pulsos_gibbs.png}
    \caption{Aproximação de Fourier truncada de um pulso periódico evidenciando o sobressinal do Fenômeno de Gibbs nas transições.}
    \label{fig:gibbs_pulse}
\end{figure}
"""

# ----------------- CAPÍTULO 7 -----------------
cap7_content = r"""\chapter{Aplicações de Séries de Fourier em SLIT}
\label{cap:7}

Neste capítulo, estudaremos a aplicação das Séries de Fourier na análise de Sistemas Lineares Invariantes no Tempo (SLIT). Mostraremos a propriedade de autofunção das exponenciais complexas e como determinar a resposta de regime permanente de um sistema linear excitado por qualquer sinal periódico genérico, convertendo problemas diferenciais complexos em multiplicações algébricas diretas.

---

\section{A Exponencial Complexa como Autofunção}

Em Álgebra Linear (Capítulo \ref{cap:2}), estudamos que um autovetor $\vec{x}$ de um operador $A$ satisfaz a relação $A\vec{x} = \lambda \vec{x}$. No domínio contínuo, as funções que mantêm sua estrutura fundamental de onda inalterada ao passar por um sistema dinâmico LTI são chamadas de **Autofunções** do sistema.

\begin{teorema}[Autofunção de SLIT]
A exponencial complexa $x(t) = e^{st}$ (onde $s = \sigma + j\omega \in \C$) é uma autofunção de qualquer Sistema Linear Invariante no Tempo (SLIT). A resposta de regime do sistema é dada por:
\begin{equation}
y(t) = H(s) e^{st}
\end{equation}
onde $H(s)$ é o autovalor complexo associado (chamado de Função de Transferência do sistema).
\end{teorema}

\begin{proof}
Seja $h(t)$ a resposta ao impulso do SLIT. O sinal de saída $y(t)$ é a integral de convolução com a entrada $x(t) = e^{st}$:
\begin{align*}
y(t) &= \int_{-\infty}^{\infty} h(\tau) x(t-\tau) \dtau = \int_{-\infty}^{\infty} h(\tau) e^{s(t-\tau)} \dtau
\end{align*}
Pelas propriedades da exponencial, podemos decompor o termo $e^{s(t-\tau)} = e^{st}e^{-s\tau}$:
\begin{align*}
y(t) &= \int_{-\infty}^{\infty} h(\tau) e^{st} e^{-s\tau} \dtau
\end{align*}
Como o termo $e^{st}$ não depende da variável de integração $\tau$, ele pode ser retirado da integral:
\begin{align*}
y(t) &= e^{st} \left[ \int_{-\infty}^{\infty} h(\tau) e^{-s\tau} \dtau \right]
\end{align*}
Definindo o termo contido entre colchetes como a Função de Transferência do sistema:
\begin{equation}
H(s) = \int_{-\infty}^{\infty} h(\tau) e^{-s\tau} \dtau
\end{equation}
obtemos exatamente:
\[
y(t) = H(s) e^{st}
\]
provando que a exponencial complexa propaga-se no sistema LTI mantendo sua assinatura cossenoidal pura, modificada unicamente em magnitude e fase pelo ganho complexo $H(s)$.
\end{proof}

Esta elegante propriedade e o correspondente diagrama de autovalor contínuo são ilustrados geometricamente nas Figuras \ref{fig:sistema_autofuncao} e \ref{fig:sistema_cos_all}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{sistema_autofuncao.png}
    \caption{Visualização do princípio de autofunção: exponencial complexa entrando e saindo multiplicada pelo ganho $H(s)$.}
    \label{fig:sistema_autofuncao}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{sistema_cos.png}
        \caption{Senoides propagando-se em circuitos LTI.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{sistema_cos2.png}
        \caption{Sinal senoidal sofrendo defasagem e ganho de amplitude.}
    \end{subfigure}
    \caption{Resposta de regime permanente senoidal de um sistema dinâmico LTI.}
    \label{fig:sistema_cos_all}
\end{figure}

---

\section{Resposta de Regime a Entradas Periódicas}

Seja um sinal periódico arbitrário $x(t)$ representado em Série Exponencial de Fourier:
\[
x(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}
\end{entr}
Pelo princípio da superposição e da linearidade do SLIT, se a resposta para cada exponencial individual $e^{jn\omega_0 t}$ é dada por $H(jn\omega_0)e^{jn\omega_0 t}$, a resposta do sistema à soma total será a soma das respostas individuais.

\begin{teorema}[Resposta de Fourier em SLIT]
A saída de regime permanente de um SLIT a uma entrada periódica $x(t)$ é descrita pela Série de Fourier:
\begin{equation}
y(t) = \sum_{n=-\infty}^{\infty} c_n H(jn\omega_0) e^{jn\omega_0 t}
\end{equation}
onde os novos coeficientes complexos da saída $d_n$ são dados por:
\begin{equation}
d_n = c_n H(jn\omega_0)
\end{equation}
\end{teorema}

---

\section{Resolução de Equações Diferenciais Lineares}

Esta representação espectral simplifica de forma monumental a resolução de equações diferenciais que descrevem sistemas mecânicos ou circuitos elétricos excitados por fontes periódicas não senoidais (ex: trem de pulsos, ondas triangulares).

\begin{exemplo}[Resolução de EDO via Série de Fourier]
Considere um sistema dinâmico LTI de 1ª ordem descrito pela Equação Diferencial Ordinária (EDO):
\[
\frac{\dd y(t)}{\dd t} + 2y(t) = x(t)
\]
Desejamos determinar a resposta $y(t)$ a uma entrada periódica genérica representada por $x(t) = \sum c_n e^{jn\omega_0 t}$.

\textbf{Passo 1: Determinar a Resposta em Frequência $H(j\omega)$ do Sistema}
Substituímos $x(t) = e^{j\omega t}$ e $y(t) = H(j\omega)e^{j\omega t}$ na EDO:
\begin{align*}
\frac{\dd}{\dd t}\left( H(j\omega) e^{j\omega t} \right) + 2 H(j\omega) e^{j\omega t} &= e^{j\omega t} \\
j\omega H(j\omega) e^{j\omega t} + 2 H(j\omega) e^{j\omega t} &= e^{j\omega t}
\end{align*}
Dividindo ambos os lados pelo termo exponencial comum $e^{j\omega t}$:
\begin{align*}
(j\omega + 2) H(j\omega) &= 1 \implies H(j\omega) = \frac{1}{2 + j\omega}
\end{align*}

\textbf{Passo 2: Montar a Solução da Saída}
Para o harmônico $n$, a frequência angular correspondente é $n\omega_0$. O autovalor complexo associado é:
\[
H(jn\omega_0) = \frac{1}{2 + jn\omega_0}
\]
Desta forma, a resposta temporal de regime do sistema é dada diretamente por:
\[
y(t) = \sum_{n=-\infty}^{\infty} \left( \frac{c_n}{2 + jn\omega_0} \right) e^{jn\omega_0 t}
\]
Isso demonstra que a EDO complexa no domínio do tempo foi convertida em uma simples divisão algébrica no domínio da frequência!
\end{exemplo}
"""

with open(os.path.join(output_dir, "cap4.tex"), "w", encoding="utf-8") as f:
    f.write(cap4_content)
with open(os.path.join(output_dir, "cap5.tex"), "w", encoding="utf-8") as f:
    f.write(cap5_content)
with open(os.path.join(output_dir, "cap6.tex"), "w", encoding="utf-8") as f:
    f.write(cap6_content)
with open(os.path.join(output_dir, "cap7.tex"), "w", encoding="utf-8") as f:
    f.write(cap7_content)

print("Lote 1 (cap4 a cap7) gerado com sucesso!")
