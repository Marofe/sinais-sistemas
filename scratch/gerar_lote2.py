import os

output_dir = r"G:\My Drive\Disciplinas\Graduação\SEL0383-Sinais e Sistemas\slides\apostila"
os.makedirs(output_dir, exist_ok=True)

# ----------------- CAPÍTULO 8 -----------------
cap8_content = r"""\chapter{Sinais em Tempo Discreto e Amostragem}
\label{cap:8}

Neste capítulo, estudaremos a amostragem de sinais e as sequências em tempo discreto. Compreenderemos a ponte que une o domínio analógico contínuo ao mundo computacional discreto. Analisaremos o Teorema da Amostragem de Nyquist-Shannon, o fenômeno de sobreposição spectral (aliasing) e a representação matemática de sequências discretas fundamentais.

---

\section{O Processo de Amostragem Ideal}

O processamento digital exige a conversão de sinais contínuos $x(t)$ em sequências de números discretos $x[n]$. Como mostrado na Figura \ref{fig:conversor_adc}, este processo é realizado por um Conversor Analógico-Digital (ADC), compreendendo a amostragem temporal, a quantização de amplitude e a codificação binária. O fluxo contínuo versus quantizado de sinais é representado detalhadamente nas Figuras \ref{fig:conversao_all}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.65\textwidth]{conversor_adc.png}
    \caption{Etapas completas de processamento e digitalização de sinais analógicos.}
    \label{fig:conversor_adc}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{conversao_amostragem_quantizacao.png}
        \caption{Amostragem em instantes discretos e quantização de níveis.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=0.9\textwidth]{PCM_Stpes_600x600.webp}
        \caption{Sinal modulado por código de pulso quantizado final (PCM).}
    \end{subfigure}
    \caption{Processo de digitalização física e amostragem.}
    \label{fig:conversao_all}
\end{figure}

Matematicamente, modelamos a amostragem ideal como a multiplicação direta do sinal contínuo $x(t)$ por um **Trem de Impulsos periódicos** $p(t)$ com período de amostragem $T_s$:
\begin{equation}
p(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT_s)
\end{equation}
O sinal amostrado resultante no tempo contínuo, denotado por $x_s(t)$, é dado por:
\begin{equation}
x_s(t) = x(t) p(t) = \sum_{n=-\infty}^{\infty} x(nT_s) \delta(t - nT_s)
\end{equation}
Este processo gera uma representação discreta direta $x[n] = x(nT_s)$, exibida na Figura \ref{fig:sinal_amostrado}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.55\textwidth]{sinal_amostrado.png}
    \caption{Sinal amostrado contendo a envelope dinâmica original.}
    \label{fig:sinal_amostrado}
\end{figure}

---

\section{Análise em Frequência e o Teorema de Nyquist}

Como a multiplicação no domínio do tempo equivale a uma convolução no domínio da frequência, podemos avaliar o espectro do sinal amostrado $X_s(j\omega)$ a partir da transformada de Fourier do trem de impulsos $P(j\omega) = \frac{2\pi}{T_s} \sum \delta(\omega - k\omega_s)$, onde $\omega_s = 2\pi/T_s$ é a frequência angular de amostragem:
\begin{equation}
X_s(j\omega) = \frac{1}{2\pi} X(j\omega) * P(j\omega) = \frac{1}{T_s} \sum_{k=-\infty}^{\infty} X(j(\omega - k\omega_s))
\end{equation}

Esta elegante relação prova que o espectro do sinal amostrado é uma soma infinita de réplicas periódicas deslocadas do espectro do sinal original $X(j\omega)$, espaçadas pela frequência de amostragem $\omega_s$.

\begin{teorema}[Teorema da Amostragem de Nyquist-Shannon]
Seja $x(t)$ um sinal de banda limitada cuja maior componente de frequência é $\omega_{max}$ (ou $f_{max}$). O sinal $x(t)$ pode ser perfeitamente reconstruído a partir de suas amostras discretas $x(nT_s)$ se a frequência de amostragem $\omega_s$ for estritamente maior que o dobro da frequência máxima:
\begin{equation}
\omega_s > 2\omega_{max} \implies f_s > 2f_{max}
\end{equation}
A frequência limite $f_N = 2f_{max}$ é chamada de **Taxa de Nyquist**.
\end{teorema}

Se $f_s \le 2f_{max}$, as réplicas adjacentes do espectro sobrepõem-se, distorcendo irreversivelmente a informação original. Esse fenômeno é conhecido como \textbf{Aliasing} (sobreposição spectral).

---

\section{Sinais Discretos Fundamentais}

As sequências discretas $x[n]$ possuem uma representação gráfica em forma de ramos (hastes) discretos. As Figuras \ref{fig:discretos_all} trazem os principais sinais no domínio discreto estudados na engenharia:

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{degrau_unitario_discreto.png}
        \caption{Degrau discreto $u[n]$.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{gate_discreto.png}
        \caption{Pulso retangular discreto.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{cossenoide_discreta.png}
        \caption{Cossenoide amostrada.}
    \end{subfigure}
    
    \vspace{0.2cm}
    
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{senoide_discreta.png}
        \caption{Senoide discreta periódica.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{dente_serra_discreto.png}
        \caption{Dente de serra discreto.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{impulso_discreto.png}
        \caption{Impulso unitário discreto $\delta[n]$.}
    \end{subfigure}
    \caption{Galeria de sequências em tempo discreto fundamentais.}
    \label{fig:discretos_all}
\end{figure}
"""

# ----------------- CAPÍTULO 9 -----------------
cap9_content = r"""\chapter{Transformada de Fourier Contínua}
\label{cap:9}

Neste capítulo, estudaremos a transição analítica das Séries de Fourier (que representam sinais periódicos) em direção à Transformada de Fourier Contínua (CTFT), aplicável a sinais aperiódicos de energia finita. Derivaremos rigorosamente as fórmulas diretas e inversas a partir do limite matemático do período tendendo ao infinito.

---

\section{A Transição de Sinais Periódicos para Aperiódicos}

Seja um sinal de pulso único e aperiódico $x(t)$. Podemos construir uma aproximação periódica de $x(t)$, denotada por $\tilde{x}(t)$, repetindo o pulso a cada intervalo de tempo $T_0$. Conforme aumentamos o período de repetição artificial $T_0$ em direção ao infinito, o sinal periódico $\tilde{x}(t)$ aproxima-se perfeitamente do sinal aperiódico original $x(t)$:
\begin{equation}
x(t) = \lim_{T_0 \to \infty} \tilde{x}(t)
\end{equation}

As Figuras \ref{fig:fourier_pulses_all} exibem esse processo conceitual no domínio da frequência: à medida que o período fundamental $T_0$ cresce, as linhas discretas de amplitude do espectro harmônico aproximam-se cada vez mais, tornando-se uma curva contínua e densa no limite $T_0 \to \infty$.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_periodic_pulse2.png}
        \caption{Espectro discreto para período $T_0$ curto.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_periodic_pulse12.png}
        \caption{Espectro com densidade duplicada (período duplo).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.31\textwidth}
        \centering
        \includegraphics[width=\textwidth]{fourier_periodic_pulse32.png}
        \caption{O limite de espectro contínuo conforme $T_0 \to \infty$.}
    \end{subfigure}
    \caption{Visualização conceitual da transição espectral da série para a transformada de Fourier.}
    \label{fig:fourier_pulses_all}
\end{figure}

---

\section{Derivação Analítica Rigorosa da CTFT}

\begin{teorema}[Transformada de Fourier e Par de Inversão]
O par de equações da Transformada de Fourier Contínua (CTFT) de um sinal $x(t)$ é definido por:
\begin{equation}
X(j\omega) = \intParenthesizex(t) e^{-j\omega t} \dt \quad (\text{Equação de Análise})
\end{equation}
\begin{equation}
x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) e^{j\omega t} \dw \quad (\text{Equação de Síntese})
\end{equation}
\end{teorema}

\begin{proof}
Partimos da representação em Série Exponencial de Fourier do sinal periódico $\tilde{x}(t)$:
\begin{equation}
\tilde{x}(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}
\end{equation}
onde:
\begin{equation}
c_n = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} \tilde{x}(t) e^{-jn\omega_0 t} \dt
\end{equation}
Substituindo $c_n$ diretamente no somatório, e usando a relação $1/T_0 = \omega_0/2\pi$:
\begin{align*}
\tilde{x}(t) &= \sum_{n=-\infty}^{\infty} \left[ \frac{\omega_0}{2\pi} \int_{-T_0/2}^{T_0/2} \tilde{x}(\tau) e^{-jn\omega_0 \tau} \dd\tau \right] e^{jn\omega_0 t} \\
&= \frac{1}{2\pi} \sum_{n=-\infty}^{\infty} \left[ \int_{-T_0/2}^{T_0/2} \tilde{x}(\tau) e^{-jn\omega_0 \tau} \dd\tau \right] e^{jn\omega_0 t} \omega_0
\end{align*}
Agora, avaliamos o limite conforme $T_0 \to \infty$. Neste cenário de limite contínuo:
\begin{itemize}
    \item A frequência fundamental discreta $\omega_0$ torna-se um incremento diferencial de frequência $\dw$.
    \item A frequência harmônica discreta $n\omega_0$ passa a ser uma variável contínua de frequência $\omega$.
    \item O somatório infinito $\sum_{n=-\infty}^{\infty}$ transforma-se na integral contínua de Riemann $\int_{-\infty}^{\infty}$.
    \item O sinal periódico $\tilde{x}(t)$ torna-se o sinal aperiódico $x(t)$.
\end{itemize}
Substituindo estas transições na equação:
\begin{align*}
x(t) &= \frac{1}{2\pi} \int_{-\infty}^{\infty} \left[ \int_{-\infty}^{\infty} x(\tau) e^{-j\omega \tau} \dd\tau \right] e^{j\omega t} \dw
\end{align*}
Definindo o termo interno dos colchetes como a Transformada de Fourier $X(j\omega)$:
\[
X(j\omega) = \int_{-\infty}^{\infty} x(\tau) e^{-j\omega \tau} \dd\tau
\]
obtemos a equação de síntese da transformada de Fourier inversa:
\[
x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) e^{j\omega t} \dw
\]
o que demonstra perfeitamente o par de transformadas.
\end{proof}
"""

# ----------------- CAPÍTULO 10 -----------------
cap10_content = r"""\chapter{Propriedades da Transformada de Fourier}
\label{cap:10}

Neste capítulo, estudaremos e demonstraremos de forma detalhada e rigorosa todas as propriedades operacionais da Transformada de Fourier Contínua. Estas propriedades são fundamentais para simplificar a análise espectral de sistemas LTI e para modelar processos de comunicação de alta complexidade.

---

\section{Tabela e Demonstração das Propriedades}

Denotaremos o par de transformadas de Fourier por $x(t) \xleftrightarrow{\F} X(j\omega)$.

\subsection{1. Linearidade}
\begin{equation}
\F\{\alpha x(t) + \beta y(t)\} = \alpha X(j\omega) + \beta Y(j\omega)
\end{equation}
A prova é direta a partir da propriedade de linearidade intrínseca da operação de integração.

\subsection{2. Deslocamento no Tempo (Time Shifting)}
A translação no tempo gera uma alteração de fase linear na frequência, mantendo o espectro de magnitude inalterado:
\begin{equation}
\F\{x(t - t_0)\} = X(j\omega) e^{-j\omega t_0}
\end{equation}

\begin{proof}
Aplicamos a definição da CTFT ao sinal deslocado:
\begin{align*}
\F\{x(t - t_0)\} &= \int_{-\infty}^{\infty} x(t - t_0) e^{-j\omega t} \dt
\end{align*}
Efetuamos a mudança de variável $u = t - t_0 \implies t = u + t_0 \implies \dt = \dd u$. Os limites de integração continuam $-\infty$ a $\infty$:
\begin{align*}
&= \int_{-\infty}^{\infty} x(u) e^{-j\omega (u + t_0)} \dd u = \int_{-\infty}^{\infty} x(u) e^{-j\omega u} e^{-j\omega t_0} \dd u \\
&= e^{-j\omega t_0} \int_{-\infty}^{\infty} x(u) e^{-j\omega u} \dd u = X(j\omega) e^{-j\omega t_0}
\end{align*}
Provando o teorema.
\end{proof}

\subsection{3. Deslocamento na Frequência (Modulação)}
O deslocamento no domínio da frequência equivale a multiplicar o sinal no tempo por uma exponencial complexa:
\begin{equation}
\F\{x(t) e^{j\omega_0 t}\} = X(j(\omega - \omega_0))
\end{equation}
Esta propriedade é a base de todos os sistemas de telecomunicações de modulação de portadora.

\subsection{4. Mudança de Escala Temporal (Time Scaling)}
Comprimir o tempo expande o espectro na frequência e vice-versa:
\begin{equation}
\F\{x(at)\} = \frac{1}{|a|} X\left(j\frac{\omega}{a}\right)
\end{equation}

\begin{proof}
Calculamos a integral de Fourier para $x(at)$:
\begin{align*}
\F\{x(at)\} &= \int_{-\infty}^{\infty} x(at) e^{-j\omega t} \dt
\end{align编}
Fazemos a mudança de variável $u = at \implies t = u/a \implies \dt = \frac{1}{a} \dd u$.
Se $a > 0$:
\begin{align*}
\F\{x(at)\} &= \int_{-\infty}^{\infty} x(u) e^{-j\omega (u/a)} \frac{1}{a} \dd u = \frac{1}{a} X\left(j\frac{\omega}{a}\right)
\end{align*}
Se $a < 0$, a inversão dos limites compensa o sinal de $a$, resultando no termo geral usando o módulo $|a|$:
\[
\F\{x(at)\} = \frac{1}{|a|} X\left(j\frac{\omega}{a}\right)
\]
Demonstrando a propriedade.
\end{proof}

\subsection{5. Duidade (Simetria)}
A dualidade matemática entre as equações de síntese e análise de Fourier gera uma simetria notável de pares:
\begin{equation}
\F\{X(t)\} = 2\pi x(-\omega)
\end{equation}

\subsection{6. Diferenciação no Tempo}
Derivar o sinal no tempo equivale a multiplicar seu espectro por $j\omega$:
\begin{equation}
\F\left\{\frac{\dd x(t)}{\dd t}\right\} = j\omega X(j\omega)
\end{equation}

\begin{proof}
Usamos a equação de síntese da transformada de Fourier inversa para expressar $x(t)$:
\begin{align*}
x(t) &= \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) e^{j\omega t} \dw
\end{align*}
Derivando ambos os lados em relação ao tempo $t$, e passando o operador de derivada para dentro da integral contínua:
\begin{align*}
\frac{\dd x(t)}{\dd t} &= \frac{\dd}{\dd t}\left[ \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) e^{j\omega t} \dw \right] \\
&= \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) \left( \frac{\partial e^{j\omega t}}{\partial t} \right) \dw \\
&= \frac{1}{2\pi} \int_{-\infty}^{\infty} [j\omega X(j\omega)] e^{j\omega t} \dw
\end{align*}
A expressão acima é, por definição, a transformada inversa de $[j\omega X(j\omega)]$. Portanto, $\F\{\frac{\dd x(t)}{\dd t}\} = j\omega X(j\omega)$.
\end{proof}

\subsection{7. Propriedade da Convolução no Tempo}
Esta é uma das propriedades mais importantes da engenharia: a convolução complexa no domínio do tempo é mapeada em uma multiplicação algébrica direta na frequência:
\begin{equation}
\F\{x(t) * h(t)\} = X(j\omega) H(j\omega)
\end{equation}
Isto reduz o cálculo dinâmico de saídas de SLITs a simples multiplicações de polinômios e funções racionais de ganho.

\subsection{8. Propriedade da Modulação (Convolução na Frequência)}
Dualmente, a multiplicação direta no domínio do tempo equivale à convolução no domínio da frequência escalonada por $2\pi$:
\begin{equation}
\F\{x(t) y(t)\} = \frac{1}{2\pi} X(j\omega) * Y(j\omega)
\end{equation}
As Figuras \ref{fig:espectro_transformada_all} trazem os espectros contínuos calculados a partir de sinais especiais aplicando estas propriedades.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{espectro_fourier_transform.png}
        \caption{Módulo de transformada contínua típica (par).}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{espectro_fourier_transform_fase.png}
        \caption{Fase contínua calculada (ímpar).}
    \end{subfigure}
    \caption{Visualização espectral contínua sob o domínio da Transformada de Fourier.}
    \label{fig:espectro_transformada_all}
\end{figure}
"""

# ----------------- CAPÍTULO 11 -----------------
cap11_content = r"""\chapter{Modulação de Sinais e Telecomunicações}
\label{cap:11}

Neste capítulo, estudaremos a aplicação direta das propriedades da Transformada de Fourier (deslocamento em frequência e modulação) nos sistemas modernos de telecomunicações. Analisaremos a modulação em amplitude com portadora suprimida (AM-DSB-SC) e modulação convencional (AM-DSB), o processo de demodulação síncrona/envelope e a multiplexação de sinais por divisão de frequência.

---

\section{O Princípio Físico da Modulação}

Sinais de áudio e voz possuem espectros concentrados em baixas frequências (banda base, tipicamente de $20$ Hz a $20$ kHz). A transmissão direta destes sinais no ar por ondas eletromagnéticas exigiria antenas com dimensões impraticáveis (de dezenas de quilômetros, pois o comprimento da antena deve ser proporcional ao comprimento de onda $\lambda = c/f$).

Para viabilizar a transmissão e evitar a interferência mútua, realizamos o processo de \textbf{Modulação}: deslocamos o espectro de banda base para altas frequências multiplicando o sinal de informação $m(t)$ (mensagem) por uma oscilação de alta frequência $c(t)$ (portadora), como mostrado no diagrama de circuito transmissor da Figura \ref{fig:am_mod_tx} e no sistema completo da Figura \ref{fig:am_mod_tx_rx}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{AM_modulation_TX.png}
    \caption{Esquema básico do modulador transmissor (multiplicador) de sinais AM.}
    \label{fig:am_mod_tx}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{AM_modulation_TX_RX.png}
    \caption{Diagrama de enlace completo: modulação no transmissor e recepção por demodulador.}
    \label{fig:am_mod_tx_rx}
\end{figure}

---

\section{Modulação AM-DSB-SC (Portadora Suprimida)}

Na modulação de amplitude em banda lateral dupla com portadora suprimida (AM-DSB-SC), o sinal transmitido $s(t)$ é simplesmente o produto da mensagem $m(t)$ pela portadora senoidal $\cos(\omega_c t)$:
\begin{equation}
s(t) = m(t) \cos(\omega_c t)
\end{equation}

Pela propriedade da modulação de Fourier, como $\F\{\cos(\omega_c t)\} = \pi [\delta(\omega - \omega_c) + \delta(\omega + \omega_c)]$, o espectro resultante $S(j\omega)$ é dado por:
\begin{equation}
S(j\omega) = \frac{1}{2} [M(j(\omega - \omega_c)) + M(j(\omega + \omega_c))]
\end{equation}

Geometricamente, o espectro original $M(j\omega)$ da mensagem é duplicado e deslocado de $\pm\omega_c$, como exibido no espectro da Figura \ref{fig:espectro_AM}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.55\textwidth]{espectro_fourier_AM.png}
    \caption{Espectro do sinal modulado em amplitude com suas bandas laterais superior e inferior.}
    \label{fig:espectro_AM}
\end{figure}

---

\section{Processo de Demodulação Síncrona (Recepção)}

Para recuperar a mensagem original no receptor (Figura \ref{fig:am_mod_rx}), multiplicamos o sinal recebido novamente pela portadora local em perfeita sincronia de fase $\cos(\omega_c t)$:
\begin{align*}
r(t) &= s(t) \cos(\omega_c t) = [m(t) \cos(\omega_c t)] \cos(\omega_c t) \\
&= m(t) \cos^2(\omega_c t) = m(t) \left[ \frac{1 + \cos(2\omega_c t)}{2} \right] \\
&= \frac{1}{2} m(t) + \frac{1}{2} m(t) \cos(2\omega_c t)
\end{align*}

Avaliando o espectro $R(j\omega)$ do sinal multiplicado no receptor:
\begin{equation}
R(j\omega) = \frac{1}{2} M(j\omega) + \frac{1}{4} [M(j(\omega - 2\omega_c)) + M(j(\omega + 2\omega_c))]
\end{equation}
Este espectro (Figura \ref{fig:espectro_demodulated}) exibe uma réplica da mensagem original centrada na origem (banda base) e duas réplicas espúrias de alta frequência em $\pm 2\omega_c$.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{AM_modulation_RX.png}
    \caption{Estrutura do circuito receptor: multiplicador seguido por um filtro passa-baixas (FPB).}
    \label{fig:am_mod_rx}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.55\textwidth]{espectro_fourier_AM_demodulated.png}
    \caption{Espectro do sinal após multiplicação no receptor, exibindo a banda base e as réplicas em alta frequência.}
    \label{fig:espectro_demodulated}
\end{figure}

Como ilustrado nas Figuras \ref{fig:am_rx_nofilter} e \ref{fig:espectro_demodulated_FPB}, a passagem deste sinal por um **Filtro Passa-Baixas (FPB) ideal** com frequência de corte $\omega_c$ elimina completamente as réplicas espúrias de alta frequência, restando perfeitamente apenas a mensagem de interesse original $m(t)$ amplificada por $1/2$.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.55\textwidth]{AM_modulation_RX_no_filter.png}
    \caption{Sinal recebido distorcido no tempo antes da filtragem passa-baixas.}
    \label{fig:am_rx_nofilter}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.55\textwidth]{espectro_fourier_AM_demodulated_FPB.png}
    \caption{Espectro do sinal recuperado purificado após a passagem pelo filtro passa-baixas ideal.}
    \label{fig:espectro_demodulated_FPB}
\end{figure}

---

\section{Multiplexação por Divisão de Frequência (FDM)}

A multiplexação FDM permite que múltiplas estações de rádio transmitam simultaneamente pelo ar sem interferirem umas nas outras. Cada transmissor modula sua respectiva mensagem em uma frequência de portadora distinta ($\omega_1, \omega_2, \dots$), enviando a soma total dos sinais pelo canal comum (Figura \ref{fig:am_multistation}).

\begin{figure}[H]
    \centering
    \includegraphics[width=0.65\textwidth]{AM_modulation_multistation.png}
    \caption{Esquema de multiplexação FDM somando e transmitindo múltiplos canais de rádio.}
    \label{fig:am_multistation}
\end{figure}

O espectro total somado no ar (Figura \ref{fig:espectro_AM_multistation}) exibe canais organizados de forma ordenada em diferentes frequências. No receptor (Figura \ref{fig:am_multistation_dem}), o usuário sintoniza um filtro passa-faixa (FPF) na portadora de interesse ($\omega_i$), isolando-a perfeitamente dos demais canais para posterior demodulação (como ilustrado conceitualmente nas Figuras \ref{fig:espectros_multistation_filter_all}).

\begin{figure}[H]
    \centering
    \includegraphics[width=0.65\textwidth]{AM_modulation_multistation_dem.png}
    \caption{Demultiplexador e demodulador sintonizável para seleção de canais específicos.}
    \label{fig:am_multistation_dem}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.55\textwidth]{espectro_fourier_AM_multistation.png}
    \caption{O espectro total compartilhado contendo canais adjacentes organizados na frequência.}
    \label{fig:espectro_AM_multistation}
\end{figure}

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{espectro_fourier_AM_multistation_filter.png}
        \caption{Filtro passa-faixa sintonizado no canal central.}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{espectro_fourier_AM_multistation_filter_w2.png}
        \caption{O sinal sintonizado isolado pronto para demodulação.}
    \end{subfigure}
    \caption{Processo físico-espectral de sintonia e seleção de canais via FDM.}
    \label{fig:espectros_multistation_filter_all}
\end{figure}
"""

with open(os.path.join(output_dir, "cap8.tex"), "w", encoding="utf-8") as f:
    f.write(cap8_content)
with open(os.path.join(output_dir, "cap9.tex"), "w", encoding="utf-8") as f:
    f.write(cap9_content)
with open(os.path.join(output_dir, "cap10.tex"), "w", encoding="utf-8") as f:
    f.write(cap10_content)
with open(os.path.join(output_dir, "cap11.tex"), "w", encoding="utf-8") as f:
    f.write(cap11_content)

print("Lote 2 (cap8 a cap11) gerado com sucesso!")
