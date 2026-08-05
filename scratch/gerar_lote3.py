import os

output_dir = r"G:\My Drive\Disciplinas\Graduação\SEL0383-Sinais e Sistemas\slides\apostila"
os.makedirs(output_dir, exist_ok=True)

# ----------------- CAPÍTULO 12 -----------------
cap12_content = r"""\chapter{Solução de Integrais com a Transformada de Fourier}
\label{cap:12}

Neste capítulo, estudaremos a aplicação da Transformada de Fourier Contínua como uma poderosa ferramenta para resolver integrais definidas complexas, que seriam de extrema dificuldade usando métodos de integração clássica. Mostraremos como as propriedades de Duidade (Simetria) e o Teorema de Parseval convertem integrais complexas em avaliações de amplitude diretas.

---

\section{Resolução de Integrais via Propriedade de Duidade}

A propriedade de Duidade (Simetria) da CTFT estabelece uma ponte direta de troca de argumentos entre os domínios do tempo e da frequência:
\begin{equation}
\F\{X(t)\} = 2\pi x(-\omega)
\end{equation}
Isto significa que, se conhecemos um par de transformadas $x(t) \xleftrightarrow{\F} X(j\omega)$, podemos calcular de forma imediata a integral de uma função temporal com a forma de $X(t)$.

As Figuras \ref{fig:sinc_transf_all} exibem o par de transformadas clássico entre o pulso retangular e a função sinc.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{sinc_transf_pulso.png}
        \caption{Pulso retangular no tempo gerando a função sinc na frequência.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{sinc_transf_pulso_par.png}
        \caption{A simetria de fase cossenoidal associada ao par.}
    \end{subfigure}
    \caption{Par fundamental de transformadas de Fourier: Pulso e Sinc.}
    \label{fig:sinc_transf_all}
\end{figure}

\begin{exemplo}[Cálculo da Integral da Função Sinc]
Desejamos calcular a integral clássica definida de $-\infty$ a $\infty$ da função sinc:
\[
I = \int_{-\infty}^{\infty} \frac{\sin(\pi t)}{\pi t} \dt = \int_{-\infty}^{\infty} \sinc(t) \dt
\]
\textbf{Passo 1: Identificar o Par de Transformadas de Referência}
Sabemos que a transformada de um pulso retangular $x(t) = \text{rect}(t)$ é dada por:
\[
X(j\omega) = \sinc\left(\frac{\omega}{2\pi}\right)
\]
Pela equação de análise da CTFT no instante de frequência angular nulo $\omega = 0$:
\begin{align*}
X(j\omega) &= \intParenthesizex(t) e^{-j\omega t} \dt \implies X(j0) = \intParenthesizex(t) \dt
\end{align*}
Substituindo $x(t) = \text{rect}(t)$:
\[
\int_{-1/2}^{1/2} 1 \dt = 1
\]
Portanto, a área sob o pulso retangular é unitária: $X(j0) = 1$.

\textbf{Passo 2: Aplicar a Transformada Inversa}
Escrevemos a equação de síntese (transformada inversa) para $x(t)$:
\begin{align*}
x(t) &= \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) e^{j\omega t} \dw \\
\text{rect}(t) &= \frac{1}{2\pi} \intParenthesizesinc\left(\frac{\omega}{2\pi}\right) e^{j\omega t} \dw
\end{align*}
Avaliamos a equação no instante de tempo nulo $t = 0$ (sabendo que $\text{rect}(0) = 1$ e $e^{j0} = 1$):
\begin{align*}
1 &= \frac{1}{2\pi} \intParenthesizesinc\left(\frac{\omega}{2\pi}\right) \dw
\end{align*}
Efetuamos a mudança de variável de integração $u = \frac{\omega}{2\pi} \implies \dw = 2\pi \dd u$.
Os limites permanecem de $-\infty$ a $\infty$:
\begin{align*}
1 &= \frac{1}{2\pi} \int_{-\infty}^{\infty} \sinc(u) (2\pi \dd u) \\
1 &= \int_{-\infty}^{\infty} \sinc(u) \dd u
\end{align*}
Desta forma, provamos com extrema simplicidade que a integral da função sinc é unitária:
\[
I = \int_{-\infty}^{\infty} \sinc(t) \dt = 1
\]
\end{exemplo}

---

\section{Resolução de Integrais via Teorema de Parseval}

Dualmente, se a integral envolve o produto quadrático de funções complexas, podemos utilizar o **Teorema de Parseval** para a CTFT para converter o problema em uma integral muito mais simples na frequência:
\begin{equation}
\intParenthesize|x(t)|^2 \dt = \frac{1}{2\pi} \intParenthesize|X(j\omega)|^2 \dw
\end{equation}

\begin{exemplo}[Cálculo da Integral de $\text{sinc}^2(t)$]
Desejamos calcular a integral da função sinc ao quadrado:
\[
I_2 = \intParenthesize\sinc^2(t) \dt
\]
Pelo Teorema de Parseval, sabendo que $\text{sinc}(t) \xleftrightarrow{\F} \text{rect}\left(\frac{\omega}{2\pi}\right)$:
\begin{align*}
\intParenthesize\sinc^2(t) \dt &= \frac{1}{2\pi} \intParenthesize\left|\text{rect}\left(\frac{\omega}{2\pi}\right)\right|^2 \dw
\end{align*}
Como a função retangular assume apenas valor unitário no intervalo de frequência angular $[-\pi, \pi]$ e zero fora dele:
\begin{align*}
&= \frac{1}{2\pi} \int_{-\pi}^{\pi} (1)^2 \dw = \frac{1}{2\pi} \left. \omega \right|_{-\pi}^{\pi} \\
&= \frac{1}{2\pi} [\pi - (-\pi)] = \frac{2\pi}{2\pi} = 1
\end{align*}
Portanto, a integral de $\sinc^2(t)$ também é igual a 1:
\[
\intParenthesize\sinc^2(t) \dt = 1
\]
\end{exemplo}

As Figuras \ref{fig:sinc_duality} mostram graficamente o mapeamento espectral e cossenoidal da dualidade das formas de onda.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{sinc_transf_pulso2.png}
        \caption{Transformada de Fourier direta.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{sinc_transf_fourier_dualidade.png}
        \caption{Troca geométrica de eixos sob Duidade.}
    \end{subfigure}
    \caption{Simetria de Duidade entre funções de tempo e frequência.}
    \label{fig:sinc_duality}
\end{figure}
"""

# ----------------- CAPÍTULO 13 -----------------
cap13_content = r"""\chapter{Sinais Periódicos e Filtros Ideais}
\label{cap:13}

Neste capítulo, estudaremos a Transformada de Fourier de sinais periódicos genéricos (modelados como somas de deltas de Dirac), o impacto do janelamento temporal (truncamento) em sinais práticos de duração finita, o vazamento spectral (*spectral leakage*) e a resposta no tempo e frequência de filtros ideais analógicos.

---

\section{Transformada de Fourier de Sinais Periódicos}

Um sinal periódico genérico $x(t) = \sum c_n e^{jn\omega_0 t}$ possui potência finita e energia infinita, o que impede a convergência da integral clássica de Fourier. Contudo, podemos expressar sua transformada no sentido distribucional utilizando impulsos de Dirac na frequência.

\begin{teorema}[Transformada de Sinal Periódico]
A Transformada de Fourier de um sinal periódico de período $T_0$ com coeficientes complexos de Fourier $c_n$ é dada por um trem de impulsos na frequência:
\begin{equation}
X(j\omega) = 2\pi \sum_{n=-\infty}^{\infty} c_n \delta(\omega - n\omega_0)
\end{equation}
\end{teorema}

\begin{proof}
Aplicamos a transformada de Fourier inversa na expressão contendo os Deltas na frequência:
\begin{align*}
x(t) &= \frac{1}{2\pi} \int_{-\infty}^{\infty} \left[ 2\pi \sum_{n=-\infty}^{\infty} c_n \delta(\omega - n\omega_0) \right] e^{j\omega t} \dw \\
&= \sum_{n=-\infty}^{\infty} c_n \int_{-\infty}^{\infty} \delta(\omega - n\omega_0) e^{j\omega t} \dw
\end{align*}
Pela propriedade de filtragem do Delta de Dirac, a integral isola o valor da exponencial no ponto $\omega = n\omega_0$:
\[
x(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}
\]
o que resulta na Série de Fourier original do sinal, validando a transformada.
\end{proof}

As Figuras \ref{fig:trem_pulsos_all} trazem a evolução espectral do trem de pulsos periódicos de duração finita.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{trem_pulsos.png}
        \caption{Trem de pulsos periódicos no tempo.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{trem_pulsos_c0.png}
        \caption{Espectro harmônico de amplitude.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{trem_pulsos_c100.png}
        \caption{Espectro de linha densamente concentrado.}
    \end{subfigure}
    \caption{Trem de pulsos e sua representação espectral discreta sob deltas de Fourier.}
    \label{fig:trem_pulsos_all}
\end{figure}

---

\section{Janelamento Temporal e Vazamento Espectral}

Na prática de engenharia, nunca podemos processar ou coletar um sinal por um tempo infinito. Nós necessariamente truncamos o sinal multiplicando-o por uma janela temporal de duração finita $\text{rect}(t/T_w)$, como ilustrado na Figura \ref{fig:janelamento}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{janelamento2.png}
    \caption{Processo de truncamento (janelamento) de uma senoide infinita por um pulso retangular.}
    \label{fig:janelamento}
\end{figure}

Pela propriedade da modulação de Fourier, a multiplicação no tempo por uma janela retangular equivale a uma convolução na frequência com uma função sinc:
\begin{equation}
x_{janelado}(t) = x(t) w(t) \xleftrightarrow{\F} X_{janelado}(j\omega) = \frac{1}{2\pi} X(j\omega) * W(j\omega)
\end{equation}

Esta convolução faz com que as raias espectrais discretas (deltas puros) espalhem-se nas vizinhanças da frequência de interesse. Esse fenômeno é chamado de **Vazamento Espectral** (*spectral leakage*), e é exibido de forma nítida na Figura \ref{fig:leakage_cos}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{janelamento_cosseno.png}
    \caption{O espectro da senoide janelada, exibindo lóbulos secundários espalhados gerados pelo vazamento espectral.}
    \label{fig:leakage_cos}
\end{figure}

Para reduzir a amplitude dos lóbulos secundários e suavizar as transições nas bordas, utilizamos janelas suaves alternativas, como a **Janela de Hanning** (ou janela de cosseno elevado), ilustrada na Figura \ref{fig:hanning}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{janelamento_cosseno_hanning.png}
    \caption{A janela de Hanning suavizando as extremidades do sinal e atenuando de forma significativa os lóbulos secundários na frequência.}
    \label{fig:hanning}
\end{figure}

---

\section{Definição e Resposta de Filtros Ideais}

Filtros são sistemas LTI projetados para alterar de forma seletiva a amplitude e a fase de componentes harmônicas de sinais de acordo com faixas de frequência de interesse. As Figuras \ref{fig:filtros_ideais_all} e \ref{fig:filtros_positivos_all} exibem a resposta de amplitude dos quatro filtros ideais clássicos:

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=0.85\textwidth]{filtro_passa_baixa.png}
        \caption{Filtro Passa-Baixas (FPB).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=0.85\textwidth]{filtro_passa_alta.png}
        \caption{Filtro Passa-Altas (FPA).}
    \end{subfigure}
    
    \vspace{0.2cm}
    
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=0.85\textwidth]{filtro_passa_faixa.png}
        \caption{Filtro Passa-Faixa (FPF).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=0.85\textwidth]{filtro_rejeita_faixa.png}
        \caption{Filtro Rejeita-Faixa (FRF).}
    \end{subfigure}
    \caption{Os quatro filtros ideais definidos em todo o domínio de frequências bilaterais.}
    \label{fig:filtros_ideais_all}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.24\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_passa_baixa_positivo.png}
        \caption{FPB unilateral.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.24\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_passa_alta_positivo.png}
        \caption{FPA unilateral.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.24\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_passa_faixa_positivo.png}
        \caption{FPF unilateral.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.24\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rejeita_faixa_positiva.png}
        \caption{FRF unilateral.}
    \end{subfigure}
    \caption{Espectro de ganho em frequências físicas positivas.}
    \label{fig:filtros_positivos_all}
\end{figure}

A resposta ao impulso de um Filtro Passa-Baixas ideal com ganho unitário e frequência de corte $\omega_c$ é obtida pela transformada de Fourier inversa de sua janela retangular na frequência $H(j\omega) = \text{rect}(\omega/2\omega_c)$:
\begin{equation}
h(t) = \frac{1}{2\pi} \int_{-\omega_c}^{\omega_c} 1 \cdot e^{j\omega t} \dw = \frac{\omega_c}{\pi} \sinc\left(\frac{\omega_c t}{\pi}\right)
\end{equation}

Esta resposta ao impulso de filtro ideal é exibida graficamente na Figura \ref{fig:fpb_phase}. Note que $h(t) \neq 0$ para $t < 0$, o que significa que o filtro passa-baixas ideal é **não causal**, sendo impossível de ser implementado fisicamente em tempo real.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{filtro_passa_baixa_fase.png}
    \caption{Resposta ao impulso não causal $h(t)$ na forma de sinc associada ao filtro passa-baixas ideal.}
    \label{fig:fpb_phase}
\end{figure}
"""

# ----------------- CAPÍTULO 14 -----------------
cap14_content = r"""\chapter{Filtros Analógicos Realizáveis}
\label{cap:14}

Neste capítulo, estudaremos a análise e projeto de filtros passivos realizáveis (analógicos) implementados por circuitos elétricos contendo resistores ($R$), capacitores ($C$) e indutores ($L$). Analisaremos os circuitos de 1ª e 2ª ordem, derivando suas Funções de Transferência $H(j\omega)$, os Diagramas de Bode de módulo (em dB) e fase, o conceito de frequência de corte de meia potência ($-3$ dB) e filtros de ordens superiores em cascata.

---

\section{Impedância Complexa de Elementos Passivos}

Para modelar circuitos elétricos excitados por fontes senoidais no domínio da frequência, usamos o conceito de **Impedância Complexa** $Z(j\omega)$ (mostrado esquematicamente nas Figuras \ref{fig:impedancia_passiva_all}), que estende a lei de Ohm para correntes alternadas:
\begin{equation}
V(j\omega) = Z(j\omega) I(j\omega)
\end{equation}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=0.5\textwidth]{resistor.png}
        \caption{Resistor: $Z_R = R$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=0.5\textwidth]{capacitor.png}
        \caption{Capacitor: $Z_C = \frac{1}{j\omega C}$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=0.5\textwidth]{indutor.png}
        \caption{Indutor: $Z_L = j\omega L$.}
    \end{subfigure}
    \caption{Símbolos elétricos e expressões de impedância complexa.}
    \label{fig:impedancia_passiva_all}
\end{figure}

As Figuras \ref{fig:circuitos_passivos_all} exibem circuitos elétricos clássicos de malha única formados por estes componentes, atuando sob divisores de tensão (Figura \ref{fig:divisor_tensao}) para processar sinais.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.24\textwidth}
        \centering
        \includegraphics[width=\textwidth]{circuito_R.png}
        \caption{Malha puramente resistiva.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.24\textwidth}
        \centering
        \includegraphics[width=\textwidth]{circuito_RC.png}
        \caption{Circuito em série RC.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.24\textwidth}
        \centering
        \includegraphics[width=\textwidth]{circuito_RLC.png}
        \caption{Circuito ressonante RLC.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.24\textwidth}
        \centering
        \includegraphics[width=\textwidth]{circuito_RLC_rejeita.png}
        \caption{Circuito RLC paralelo.}
    \end{subfigure}
    \caption{Configurações elétricas de circuitos analógicos passivos.}
    \label{fig:circuitos_passivos_all}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.45\textwidth]{divisor_tensao.png}
    \caption{Diagrama de um divisor de tensão genérico com impedâncias complexas.}
    \label{fig:divisor_tensao}
\end{figure}

---

\section{Filtro Passa-Baixas RC de 1ª Ordem}

Considere o circuito elétrico da Figura \ref{fig:circuito_rc_filter}, onde o sinal de entrada $v_e(t)$ é a fonte de tensão e o sinal de saída $v_s(t)$ é a tensão medida sobre o capacitor $C$.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.45\textwidth]{filtro_RC.png}
    \caption{Circuito elétrico do Filtro Passa-Baixas RC.}
    \label{fig:circuito_rc_filter}
\end{figure}

Aplicando a regra do divisor de tensão complexa:
\begin{align*}
H(j\omega) &= \frac{V_s(j\omega)}{V_e(j\omega)} = \frac{Z_C}{Z_R + Z_C} = \frac{\frac{1}{j\omega C}}{R + \frac{1}{j\omega C}}
\end{align*}
Multiplicando o numerador e o denominador por $j\omega C$, obtemos a Função de Transferência clássica:
\begin{equation}
H(j\omega) = \frac{1}{1 + j\omega RC}
\end{equation}

\subsection{Análise de Módulo e Fase}
Escrevemos a função em termos de seu módulo e sua fase complexa:
\begin{equation}
|H(j\omega)| = \frac{1}{\sqrt{1 + (\omega RC)^2}}
\end{equation}
\begin{equation}
\angle H(j\omega) = -\text{arctg}(\omega RC)
\end{equation}

Esta resposta em frequência é representada geometricamente nas curvas contínuas exibidas na Figura \ref{fig:bode_rc}. Na escala logarítmica (dB), o módulo é dado por:
\begin{equation}
|H(j\omega)|_{dB} = 20\log_{10}|H(j\omega)| = -10\log_{10}(1 + (\omega RC)^2)
\end{equation}
A Figura \ref{fig:bode_rc_db} exibe o Diagrama de Bode de magnitude correspondente, mostrando a queda assintótica linear com inclinação constante de $-20$ dB/década para altas frequências.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\textwidth]{filtro_rc_espectro.png}
    \caption{Curvas de módulo e fase lineares do filtro passa-baixas RC.}
    \label{fig:bode_rc}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\textwidth]{filtro_rc_espectro_db.png}
    \caption{Diagrama de Bode de magnitude em decibéis (dB) do filtro RC.}
    \label{fig:bode_rc_db}
\end{figure}

\subsection{Frequência de Corte de Meia Potência}
A frequência limite que divide a banda de passagem da banda de rejeição é convencionada como a frequência em que a potência da saída cai para exatamente **metade** da potência máxima de entrada. Isto equivale a dizer que a magnitude do ganho elétrico cai para $1/\sqrt{2} \approx 0.707$ (ou queda de $-3$ dB na escala logarítmica).

\begin{teorema}[Frequência de Corte RC]
A frequência de corte $\omega_c$ do filtro passa-baixas RC é dada por:
\begin{equation}
\omega_c = \frac{1}{RC} \quad (\text{rad/s}) \implies f_c = \frac{1}{2\pi RC} \quad (\text{Hz})
\end{equation}
\end{teorema}

\begin{proof}
Buscamos a frequência angular $\omega_c$ tal que $|H(j\omega_c)| = 1/\sqrt{2}$:
\begin{align*}
\frac{1}{\sqrt{1 + (\omega_c RC)^2}} &= \frac{1}{\sqrt{2}} \implies \sqrt{1 + (\omega_c RC)^2} = \sqrt{2} \\
1 + (\omega_c RC)^2 &= 2 \implies (\omega_c RC)^2 = 1 \\
\omega_c RC &= 1 \implies \omega_c = \frac{1}{RC}
\end{align*}
Provando de forma elegante a equação.
\end{proof}

As Figuras \ref{fig:rc_meia_potencia_all} trazem em detalhe a marcação gráfica da frequência de corte de meia potência sobre as curvas de ganho linear e em dB.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_RC_meia_potencia.png}
        \caption{Marcação de $0.707$ em gráfico de ganho linear.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_RC_meia_potencia2.png}
        \caption{Queda exata de $-3$ dB em escala logarítmica.}
    \end{subfigure}
    \caption{Identificação da frequência de corte de meia potência do filtro RC.}
    \label{fig:rc_meia_potencia_all}
</figure>

---

\section{Filtro Passa-Altas RL de 1ª Ordem}

Considere agora o circuito elétrico da Figura \ref{fig:circuito_rl_filter}, onde o sinal de saída $v_s(t)$ é a tensão medida diretamente sobre o indutor $L$.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.45\textwidth]{filtro_RL.png}
    \caption{Circuito elétrico do Filtro Passa-Altas RL.}
    \label{fig:circuito_rl_filter}
\end{figure}

Aplicando a regra de divisor de tensão:
\begin{equation}
H(j\omega) = \frac{Z_L}{Z_R + Z_L} = \frac{j\omega L}{R + j\omega L} = \frac{j\omega (L/R)}{1 + j\omega (L/R)}
\end{equation}
O módulo e a fase associados são representados nas Figuras \ref{fig:bode_rl_all}. A frequência de corte do filtro RL é dada por:
\begin{equation}
\omega_c = \frac{R}{L} \quad (\text{rad/s})
\end{equation}

As Figuras \ref{fig:rl_meia_potencia_all} marcam de forma exata a queda de meia potência no comportamento passa-altas.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rl_espectro.png}
        \caption{Módulo e fase lineares do filtro RL.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rl_espectro_db.png}
        \caption{Diagrama de Bode de magnitude em dB.}
    \end{subfigure}
    \caption{Resposta em frequência do Filtro Passa-Altas RL.}
    \label{fig:bode_rl_all}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rl_meia_potencia.png}
        \caption{Frequência de corte de $0.707$ em gráfico linear.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rl_meia_potencia2.png}
        \caption{Queda de $-3$ dB no ganho do filtro RL.}
    \end{subfigure}
    \caption{Marcação de corte de meia potência do filtro RL.}
    \label{fig:rl_meia_potencia_all}
\end{figure}

---

\section{Filtros de 2ª Ordem RLC (Passa-Faixa e Rejeita-Faixa)}

Ao utilizarmos três elementos passivos em série ($R, L, C$), formamos circuitos ressonantes de 2ª ordem. As respostas destes sistemas dependem da frequência de ressonância natural do circuito $\omega_0 = 1/\sqrt{LC}$.

\subsection{Filtro Passa-Faixa RLC}
Se a tensão de saída é medida sobre o resistor $R$ (Figura \ref{fig:circuito_rlc_filter}):
\begin{equation}
H(j\omega) = \frac{Z_R}{Z_R + Z_L + Z_C} = \frac{R}{R + j\omega L + \frac{1}{j\omega C}} = \frac{j\omega RC}{(j\omega)^2 LC + j\omega RC + 1}
\end{equation}
Este filtro exibe ganho máximo de valor unitário ($0$ dB) na frequência exata de ressonância $\omega_0$, caindo para zero em baixas e altas frequências. As curvas espectrais completas e as frequências de corte superior e inferior são ilustradas nas Figuras \ref{fig:bode_rlc_all} e \ref{fig:rlc_meia_potencia_all}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.45\textwidth]{filtro_RLC.png}
    \caption{Circuito elétrico do Filtro Passa-Faixa RLC.}
    \label{fig:circuito_rlc_filter}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rlc_espectro.png}
        \caption{Comportamento passa-faixa com pico na ressonância.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rlc_meia_potencia.png}
        \caption{Corte linear de meia potência bilateral.}
    \end{subfigure}
    \caption{Resposta em frequência do Filtro Passa-Faixa RLC.}
    \label{fig:bode_rlc_all}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.55\textwidth]{filtro_rlc_meia_potencia2.png}
    \caption{Largura de banda ($B$) medida a $-3$ dB do pico de ressonância.}
    \label{fig:rlc_meia_potencia_all}
\end{figure}

\subsection{Filtro Rejeita-Faixa RLC}
Se a saída é medida sobre a associação em série do capacitor e indutor (Figura \ref{fig:circuito_rlc_rejeita}):
\begin{equation}
H(j\omega) = \frac{Z_L + Z_C}{Z_R + Z_L + Z_C} = \frac{(j\omega)^2 LC + 1}{(j\omega)^2 LC + j\omega RC + 1}
\end{equation}
Este filtro atenua de forma completa a componente em $\omega_0$, deixando passar sinais de baixa e alta frequência. Suas curvas são mostradas nas Figuras \ref{fig:bode_rlc_rejeita_all}.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rlc_rejeita_espectro.png}
        \caption{Entalhe acentuado na frequência de rejeição.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{filtro_rlc_rejeita_meia_potencia.png}
        \caption{Curva de ganho com rejeição na ressonância.}
    \end{subfigure}
    \caption{Resposta em frequência do Filtro Rejeita-Faixa RLC.}
    \label{fig:bode_rlc_rejeita_all}
\end{figure}

---

\section{Filtros de Ordens Superiores em Cascata}

Para obter transições muito mais íngremes e próximas ao comportamento retangular do filtro ideal, realizamos a ligação em cascata (série) de múltiplos filtros básicos (Figura \ref{fig:rc_cascata} e Figura \ref{fig:high_order_rc}).

\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\textwidth]{filtros_rc_cascata.png}
    \caption{Ligação em cascata de dois estágios de filtros RC passa-baixas.}
    \label{fig:rc_cascata}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{high_orderm_lowpass_rc_filter.png}
    \caption{Estrutura de filtro RC de ordem superior em série isolada.}
    \label{fig:high_order_rc}
\end{figure}

A passagem para sistemas ativos e o comportamento de ganho de filtros planos na banda de passagem, como o clássico **Filtro de Butterworth**, são detalhados nas Figuras \ref{fig:butterworth_all}.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{lowpass_ideal_vs_RC.png}
        \caption{Comparativo: Filtro ideal vs. RC de 1ª ordem.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{butterworth.png}
        \caption{Filtros de Butterworth de ordens crescentes ($N=2, 3, 4$).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{butter_6.png}
        \caption{Comportamento plano ideal de ordem 6.}
    \end{subfigure}
    \caption{Aproximação e síntese de filtros de ordens superiores.}
    \label{fig:butterworth_all}
\end{figure}
"""

# ----------------- CAPÍTULO 15 -----------------
cap15_content = r"""\chapter{Transformada de Fourier Discreta}
\label{cap:15}

Neste capítulo, estudaremos a formulação da Transformada de Fourier para Sinais Discretos. Definiremos a Transformada de Fourier em Tempo Discreto (DTFT) e sua periodicidade inerente, a sua contraparte computacional finita, a Transformada Discreta de Fourier (DFT), e o algoritmo eficiente de cálculo Fast Fourier Transform (FFT).

---

\section{Transformada de Fourier em Tempo Discreto (DTFT)}

Se dispomos de uma sequência em tempo discreto $x[n]$, a sua representação no domínio da frequência contínua é descrita pela DTFT.

\begin{definicao}[DTFT]
O par de equações da Transformada de Fourier em Tempo Discreto (DTFT) é definido por:
\begin{equation}
X(e^{j\Omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\Omega n} \quad (\text{Equação de Análise})
\end{equation}
\begin{equation}
x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\Omega}) e^{j\Omega n} \dd\Omega \quad (\text{Equação de Síntese})
\end{equation}
onde $\Omega$ é a frequência angular discreta expressa em radianos por amostra (rad/amostra).
\end{definicao}

A propriedade mais importante da DTFT é a sua **periodicidade inerente** de período fundamental $2\pi$:
\begin{equation}
X(e^{j(\Omega + 2\pi)}) = X(e^{j\Omega})
\end{equation}
Isto ocorre porque a exponencial complexa discreta de período $2\pi$ é idêntica à original, ou seja, $e^{-j(\Omega + 2\pi)n} = e^{-j\Omega n}e^{-j2\pi n} = e^{-j\Omega n}$ para todo $n \in \Z$.

---

\section{Transformada Discreta de Fourier (DFT e FFT)}

Como computadores não conseguem operar com somas infinitas (DTFT) ou frequências contínuas $\Omega$, realizamos a amostragem do espectro da DTFT em $N$ pontos discretos ao longo de um período de $2\pi$. Isto nos leva à **Transformada Discreta de Fourier (DFT)**.

\begin{definicao}[DFT]
Para uma sequência finita de $N$ amostras $x[n]$ com $n = 0, 1, \dots, N-1$, a sua DFT de $N$ pontos é a sequência de amostras espectrais $X[k]$ definida por:
\begin{equation}
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N} kn}, \quad k = 0, 1, \dots, N-1
\end{equation}
A respectiva transformada inversa (IDFT) é expressa por:
\begin{equation}
x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j\frac{2\pi}{N} kn}, \quad n = 0, 1, \dots, N-1
\end{equation}
\end{definicao}

O cálculo direto da DFT exige $O(N^2)$ operações aritméticas complexas. Para otimizar este processo em computadores reais, utilizamos o algoritmo **Fast Fourier Transform (FFT)**, que explora a simetria e a periodicidade dos coeficientes de fase (fatores de rotação) para reduzir a complexidade computacional para apenas $O(N\log_2 N)$ operações.

As Figuras \ref{fig:discretas_fourier_all} exibem o mapeamento discreto de coeficientes harmônicos periódicos calculados de forma digital.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{serie_fourier_discreta_1.png}
        \caption{Sequência periódica discreta original.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{serie_fourier_discreta_3.png}
        \caption{Os coeficientes discretos da DFT (FFT) mostrando a periodicidade em frequência.}
    \end{subfigure}
    \caption{Processo de análise espectral discreta computacional.}
    \label{fig:discretas_fourier_all}
\end{figure}
"""

with open(os.path.join(output_dir, "cap12.tex"), "w", encoding="utf-8") as f:
    f.write(cap12_content)
with open(os.path.join(output_dir, "cap13.tex"), "w", encoding="utf-8") as f:
    f.write(cap13_content)
with open(os.path.join(output_dir, "cap14.tex"), "w", encoding="utf-8") as f:
    f.write(cap14_content)
with open(os.path.join(output_dir, "cap15.tex"), "w", encoding="utf-8") as f:
    f.write(cap15_content)

print("Lote 3 (cap12 a cap15) gerado com sucesso!")
