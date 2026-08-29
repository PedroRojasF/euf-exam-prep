import katex from 'katex';

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

/**
 * High-precision Portuguese-to-Spanish Physics Text Translator.
 * Translates academic physics prompts while keeping all LaTeX formulas $...$ and math expressions untouched.
 */
export function translatePortuguesePhysicsToSpanish(text: string): string {
  if (!text) return '';

  // 1. Temporarily replace math blocks ($...$ or $$...$$) with placeholders
  const mathTokens: string[] = [];
  let tokenized = text.replace(/(\$\$[\s\S]*?\$\$|\$[^\$\r\n]+?\$)/g, (match) => {
    mathTokens.push(match);
    return `___MATH_TOKEN_${mathTokens.length - 1}___`;
  });

  // 2. Physics & Academic Translation Dictionary (Portuguese -> Spanish)
  const replacements: [RegExp, string][] = [
    // Classical Mechanics Specific Translations
    [/\bUma configuração central é aquela em que a atração gravitacional total sobre cada corpo aponta diretamente para o centro de massa do sistema\b/gi, 'Una configuración central es aquella en la que la atracción gravitacional total sobre cada cuerpo apunta directamente hacia el centro de masa del sistema'],
    [/\bConsidere 3 corpos de massas iguais a\b/gi, 'Considere 3 cuerpos de masas iguales a'],
    [/\bConsidere 4 corpos de massas iguais a\b/gi, 'Considere 4 cuerpos de masas iguales a'],
    [/\blocalizados nos vértices de um triângulo equilátero de lado\b/gi, 'ubicados en los vértices de un triángulo equilátero de lado'],
    [/\blocalizados nos vértices de um quadrado de lado\b/gi, 'ubicados en los vértices de un cuadrado de lado'],
    [/\bgirando em torno do centro de massa com velocidade angular constante\b/gi, 'girando alrededor del centro de masa con velocidad angular constante'],
    [/\bO valor de (.+?) para que o sistema mantenha sua configuração de equilíbrio dinâmico é:\b/gi, 'El valor de $1 para que el sistema mantenga su configuración de equilibrio dinámico es:'],
    [/\bO valor de (.+?) para que o sistema mantenha a configuração rígida é:\b/gi, 'El valor de $1 para que el sistema mantenga la configuración rígida es:'],
    [/\bUma balança de braços iguais de comprimento total\b/gi, 'Una balanza de brazos iguales de longitud total'],
    [/\bpossui um ponteiro indicador vertical de massa\b/gi, 'posee un puntero indicador vertical de masa'],
    [/\bcujo centro de massa está a uma distância (.+?) abaixo do ponto de articulação\b/gi, 'cuyo centro de masa está a una distancia $1 por debajo del punto de articulación'],
    [/\bQuando massas desiguais (.+?) e (.+?) são colocadas nos pratos\b/gi, 'Cuando masas desiguales $1 y $2 se colocan en los platos'],
    [/\bo ponteiro inclina-se de um ângulo\b/gi, 'el puntero se inclina un ángulo'],
    [/\bA sensibilidade da balança, definida por (.+?), é proporcional a:\b/gi, 'La sensibilidad de la balanza, definida por $1, es proporcional a:'],
    [/\bse o comprimento do braço (.+?) é aumentado em\b/gi, 'si la longitud del brazo $1 se incrementa en'],
    [/\ba sensibilidade angular da balança:\b/gi, 'la sensibilidad angular de la balanza:'],
    [/\bAumenta proporcionalmente a\b/gi, 'Aumenta proporcionalmente a'],
    [/\bPermanece inalterada\b/gi, 'Permanece inalterada'],
    [/\bDiminui proporcionalmente a\b/gi, 'Disminuye proporcionalmente a'],
    [/\bUma pessoa em pé sobre o centro de uma plataforma giratória horizontal livre de atrito segura dois halteres de massa\b/gi, 'Una persona de pie sobre el centro de una plataforma giratoria horizontal libre de fricción sostiene dos mancuernas de masa'],
    [/\bcom os braços estendidos\b/gi, 'con los brazos extendidos'],
    [/\bO momento de inércia inicial do conjunto é (.+?) e a velocidade angular é\b/gi, 'El momento de inercia inicial del conjunto es $1 y la velocidad angular es'],
    [/\bAo recolher os braços para junto do corpo, o momento de inércia cai para\b/gi, 'Al recoger los brazos junto al cuerpo, el momento de inercia disminuye a'],
    [/\bA nova velocidade angular (.+?) e a energia cinética rotacional final (.+?) satisfazem:\b/gi, 'La nueva velocidad angular $1 y la energía cinética rotacional final $2 satisfacen:'],
    [/\bO aumento na energia cinética rotacional (.+?) do sistema giratório ocorre porque:\b/gi, 'El aumento en la energía cinética rotacional $1 del sistema giratorio ocurre porque:'],
    [/\bA pessoa realiza trabalho interno contra a força centrífuga ao puxar os halteres para dentro\b/gi, 'La persona realiza trabajo interno contra la fuerza centrífuga al atraer las mancuernas hacia el cuerpo'],
    [/\bUm pêndulo físico é formado por uma barra rígida delgada de massa (.+?) e comprimento (.+?), articulada sem atrito em uma de suas extremidades\b/gi, 'Un péndulo físico está formado por una barra rígida delgada de masa $1 y longitud $2, articulada sin fricción en uno de sus extremos'],
    [/\bO período de pequenas oscilações do pêndulo físico é:\b/gi, 'El período de pequeñas oscilaciones del péndulo físico es:'],
    [/\bSe uma massa pontual (.+?) for fixada na extremidade inferior da barra delgada de comprimento (.+?) e massa\b/gi, 'Si una masa puntual $1 se fija en el extremo inferior de la barra delgada de longitud $2 y masa'],
    [/\bO novo período de pequenas oscilações (.+?) do conjunto é:\b/gi, 'El nuevo período de pequeñas oscilaciones $1 del conjunto es:'],
    [/\bUm pêndulo simples de massa (.+?) e comprimento (.+?) é solto a partir do repouso de uma altura\b/gi, 'Un péndulo simple de masa $1 y longitud $2 se suelta desde el reposo desde una altura'],
    [/\bNo ponto mais baixo, ele colide elasticamente e frontalmente com um bloco de massa (.+?) inicialmente em repouso sobre uma superfície horizontal sem atrito\b/gi, 'En el punto más bajo, colisiona elástica y frontalmente con un bloque de masa $1 inicialmente en reposo sobre una superficie horizontal sin fricción'],
    [/\bA velocidade (.+?) adquirida pelo bloco de massa (.+?) imediatamente após a colisão é:\b/gi, 'La velocidad $1 adquirida por el bloque de masa $2 inmediatamente después de la colisión es:'],
    [/\bA fração de energia cinética transferida para a massa (.+?) na colisão elástica é:\b/gi, 'La fracción de energía cinética transferida a la masa $1 en la colisión elástica es:'],
    [/\bUm satélite de massa (.+?) move-se em uma órbita circular de raio (.+?) ao redor da Terra\b/gi, 'Un satélite de masa $1 se mueve en una órbita circular de radio $2 alrededor de la Tierra'],
    [/\bPara transferir o satélite para uma órbita circular de raio maior (.+?), a variação de energia mecânica total (.+?) que deve ser fornecida pelos motores é:\b/gi, 'Para transferir el satélite a una órbita circular de mayor radio $1, el cambio de energía mecánica total $2 que deben suministrar los motores es:'],
    [/\bSe o raio da órbita for quadruplicado (.+?), a sua velocidade orbital (.+?) e o seu período orbital (.+?) tornam-se, respectivamente:\b/gi, 'Si el radio de la órbita se cuadruplica ($1), su velocidad orbital $2 y su período orbital $3 se convierten, respectivamente, en:'],
    [/\bUm sistema é composto por uma massa (.+?) em um plano horizontal conectada em paralelo a três molas idênticas de constante elástica\b/gi, 'Un sistema está compuesto por una masa $1 en un plano horizontal conectada en paralelo a tres resortes idénticos de constante elástica'],
    [/\bUm sistema é composto por uma massa (.+?) conectada em paralelo a quatro molas idênticas de constante elástica\b/gi, 'Un sistema está compuesto por una masa $1 conectada en paralelo a cuatro resortes idénticos de constante elástica'],
    [/\bA frequência angular de oscilação do sistema é:\b/gi, 'La frecuencia angular de oscilación del sistema es:'],
    [/\bA energia potencial intermolecular entre dois átomos a uma distância (.+?) é descrita pelo potencial\b/gi, 'La energía potencial intermolecular entre dos átomos a una distancia $1 es descrita por el potencial'],
    [/\bA distância interatômica de equilíbrio (.+?) e a constante de mola efetiva (.+?) valem:\b/gi, 'La distancia interatómica de equilibrio $1 y la constante de resorte efectiva $2 valen:'],
    [/\ba energia de ligação molecular \(profundidade do poço de potencial (.+?)\) vale:\b/gi, 'la energía de enlace molecular (profundidad del pozo de potencial $1) vale:'],
    [/\bUm disco uniforme de momento de inércia (.+?) gira livremente com velocidade angular (.+?) em torno de um eixo vertical sem atrito\b/gi, 'Un disco uniforme de momento de inercia $1 gira libremente con velocidad angular $2 alrededor de un eje vertical sin fricción'],
    [/\bDeixa-se cair suavemente sobre ele um segundo disco uniforme inicialmente em repouso de momento de inércia\b/gi, 'Se deja caer suavemente sobre él un segundo disco uniforme inicialmente en reposo de momento de inercia'],
    [/\bDevido ao atrito entre as superfícies dos discos, eles passam a girar juntos com velocidade angular final comum\b/gi, 'Debido a la fricción entre las superficies de los discos, pasan a girar juntos con velocidad angular final común'],
    [/\bA velocidade angular final (.+?) do conjunto e a fração de energia mecânica perdida (.+?) valem:\b/gi, 'La velocidad angular final $1 del conjunto y la fracción de energía mecánica perdida $2 valen:'],
    [/\bUma esfera maciça homogênea de massa (.+?) e raio (.+?) é abandonada a partir do repouso no topo de um plano inclinado de ângulo (.+?), rolando para baixo sem deslizar\b/gi, 'Una esfera maciza homogénea de masa $1 y radio $2 se suelta desde el reposo en la parte superior de un plano inclinado de ángulo $3, rodando hacia abajo sin deslizar'],
    [/\bA aceleração linear (.+?) do centro de massa da esfera maciça é:\b/gi, 'La aceleración lineal $1 del centro de masa de la esfera maciza es:'],
    [/\bUma esfera oca homogênea de casca fina de massa (.+?) e raio (.+?) desce o mesmo plano inclinado de ângulo (.+?) rolando sem deslizar\b/gi, 'Una esfera hueca homogénea de capa delgada de masa $1 y radio $2 desciende el mismo plano inclinado de ángulo $3 rodando sin deslizar'],
    [/\bA aceleração linear (.+?) do centro de massa da esfera oca é:\b/gi, 'La aceleración lineal $1 del centro de masa de la esfera hueca es:'],
    [/\bO módulo da força resultante (.+?) exercida sobre um objeto é calculado a partir das medidas de sua massa (.+?) e de sua aceleração\b/gi, 'El módulo de la fuerza resultante $1 ejercida sobre un objeto se calcula a partir de las medidas de su masa $2 y de su aceleración'],
    [/\bcom incertezas experimentais (.+?) e (.+?), respectivamente\. Pela Segunda Lei de Newton (.+?), a incerteza (.+?) é dada por:\b/gi, 'con incertidumbres experimentales $1 y $2, respectivamente. Por la Segunda Ley de Newton ($3), la incertidumbre $4 está dada por:'],
    [/\bO módulo da aceleração (.+?) é calculado a partir de (.+?), com incertezas (.+?) e (.+?)\. A incerteza experimental (.+?) é:\b/gi, 'El módulo de la aceleración $1 se calcula a partir de $2, con incertidumbres $3 y $4. La incertidumbre experimental $5 es:'],

    // Problem Introductions & Geometry
    [/\bConsidere um anel fino de raio\b/gi, 'Considere un anillo delgado de radio'],
    [/\bConsidere um anel de raio\b/gi, 'Considere un anillo de radio'],
    [/\buniformemente carregado com carga total\b/gi, 'uniformemente cargado con carga total'],
    [/\bfixo no plano\b/gi, 'fijo en el plano'],
    [/\be centrado na origem do sistema de coordenadas\b/gi, 'y centrado en el origen del sistema de coordenadas'],
    [/\bé colocada sobre o eixo\b/gi, 'se coloca sobre el eje'],
    [/\bao longo do eixo de simetria do sistema\b/gi, 'a lo largo del eje de simetría del sistema'],
    [/\bacima do centro do anel\b/gi, 'por encima del centro del anillo'],
    [/\bAlém da força elétrica exercida pelo anel sobre a partícula\b/gi, 'Además de la fuerza eléctrica ejercida por el anillo sobre la partícula'],
    [/\batua também a força peso\b/gi, 'actúa también la fuerza peso'],
    [/\bassociada à aceleração da gravidade\b/gi, 'asociada a la aceleración de la gravedad'],
    [/\bdirigida no sentido negativo do eixo\b/gi, 'dirigida en el sentido negativo del eje'],
    [/\bSabendo que a partícula está posicionada a uma altura igual ao raio do anel\b/gi, 'Sabiendo que la partícula está posicionada a una altura igual al radio del anillo'],
    [/\bSabendo que a partícula está posicionada a uma altura igual a metade do raio do anel\b/gi, 'Sabiendo que la partícula está posicionada a una altura igual a la mitad del radio del anillo'],
    [/\bqual deve ser o valor da massa\b/gi, '¿cuál debe ser el valor de la masa'],
    [/\bpara que a partícula permaneça em equilíbrio nessa posição\?/gi, 'para que la partícula permanezca en equilibrio en esa posición?'],
    [/\bDuas cascas cilíndricas longas e concêntricas possuem raios\b/gi, 'Dos cascarones cilíndricos largos y concéntricos poseen radios'],
    [/\bA casca interna possui uma densidade linear de carga igual a\b/gi, 'El cascarón interno posee una densidad lineal de carga igual a'],
    [/\benquanto a casca externa possui uma densidade linear de carga igual a\b/gi, 'mientras que el cascarón externo posee una densidad lineal de carga igual a'],
    [/\bDetermine a diferença de potencial elétrico entre as cascas\b/gi, 'Determine la diferencia de potencial eléctrico entre los cascarones'],
    [/\bdefinida por\b/gi, 'definida por'],
    [/\bno caso em que\b/gi, 'en el caso en que'],
    [/\bUma carga puntiforme\b/gi, 'Una carga puntual'],
    [/\bUma carga pontual\b/gi, 'Una carga puntual'],
    [/\bestá fixa na origem de um sistema de coordenadas\b/gi, 'está fija en el origen de un sistema de coordenadas'],
    [/\bConsidere uma superfície esférica de raio\b/gi, 'Considere una superficie esférica de radio'],
    [/\btambém centrada na origem\b/gi, 'también centrada en el origen'],
    [/\bQual é o fluxo de campo elétrico\b/gi, '¿Cuál es el flujo de campo eléctrico'],
    [/\bque atravessa a porção da superfície esférica que corresponde\b/gi, 'que atraviesa la porción de la superficie esférica que corresponde'],
    [/\bem coordenadas esféricas\b/gi, 'en coordenadas esféricas'],
    [/\bà região angular definida por\b/gi, 'a la región angular definida por'],
    [/\bConsidere um cilindro que carrega uma magnetização permanente\b/gi, 'Considere un cilindro que porta una magnetización permanente'],
    [/\bparalela à direção de seu eixo de simetria\b/gi, 'paralela a la dirección de su eje de simetría'],
    [/\bDenotando a direção deste eixo por\b/gi, 'Denotando la dirección de este eje por'],
    [/\bpodemos escrever\b/gi, 'podemos escribir'],
    [/\bAs densidades de correntes ligadas na superfície\b/gi, 'Las densidades de corrientes ligadas en la superficie'],
    [/\be no volume\b/gi, 'y en el volumen'],
    [/\bassociadas a essa magnetização são dadas por\b/gi, 'asociadas a esa magnetización son dadas por'],
    [/\bna superfície lateral do cilindro\b/gi, 'en la superficie lateral del cilindro'],
    [/\bnas tampas inferior e superior do cilindro\b/gi, 'en las tapas inferior y superior del cilindro'],
    [/\bnas tampas superior e inferior do cilindro\b/gi, 'en las tapas superior e inferior del cilindro'],
    [/\bem todo o volume do cilindro\b/gi, 'en todo el volumen del cilindro'],
    [/\bem toda a superfície do cilindro\b/gi, 'en toda la superficie del cilindro'],
    [/\bA figura representa um corte transversal perpendicular ao eixo comum de dois cilindros condutores coaxiais\b/gi, 'La figura representa un corte transversal perpendicular al eje común de dos cilindros conductores coaxiales'],
    [/\bOs raios internos e externos de cada um dos cilindros estão indicados na figura\b/gi, 'Los radios internos y externos de cada uno de los cilindros están indicados en la figura'],
    [/\bOs cilindros estão em equilíbrio eletrostático\b/gi, 'Los cilindros están en equilibrio electrostático'],
    [/\bSobre a superfície condutora de raio\b/gi, 'Sobre la superficie conductora de radio'],
    [/\bexiste uma densidade superficial de carga\b/gi, 'existe una densidad superficial de carga'],
    [/\bA densidade superficial de carga na superfície\b/gi, 'La densidad superficial de carga en la superficie'],
    [/\bUm feixe de luz não polarizada, correspondente a uma onda plana de intensidade\b/gi, 'Un haz de luz no polarizada, correspondiente a una onda plana de intensidad'],
    [/\bviaja ao longo da direção\b/gi, 'viaja a lo largo de la dirección'],
    [/\bincide sobre um conjunto de dois polarizadores lineares\b/gi, 'incide sobre un conjunto de dos polarizadores lineales'],
    [/\bO eixo de transmissão do primeiro polarizador está ao longo do eixo\b/gi, 'El eje de transmisión del primer polarizador está a lo largo del eje'],
    [/\benquanto o eixo de transmissão do segundo polarizador faz um ângulo\b/gi, 'mientras que el eje de transmisión del segundo polarizador forma un ángulo'],
    [/\bcom o eixo\b/gi, 'con el eje'],
    [/\bSabendo que a intensidade final do feixe após atravessar ambos os polarizadores é\b/gi, 'Sabiendo que la intensidad final del haz tras atravesar ambos polarizadores es'],
    [/\bO ângulo (\w+) é\b/gi, 'El ángulo $1 es'],
    [/\bConsidere duas espiras circulares, concêntricas e coplanares, de raios\b/gi, 'Considere dos espiras circulares, concéntricas y coplanares, de radios'],
    [/\bA espira de raio\b/gi, 'La espira de radio'],
    [/\bé percorrida por uma corrente elétrica\b/gi, 'es recorrida por una corriente eléctrica'],
    [/\bcujo sentido é oposto ao da corrente\b/gi, 'cuyo sentido es opuesto al de la corriente'],
    [/\bque percorre a espira de raio\b/gi, 'que recorre la espira de radio'],
    [/\bQual é a relação entre\b/gi, '¿Cuál es la relación entre'],
    [/\bpara que o campo magnético (.+?) no centro das espiras seja nulo\?\b/gi, 'para que el campo magnético $1 en el centro de las espiras sea nulo?'],
    [/\bUm cubo condutor maciço possui uma cavidade esférica cujo centro coincide com o centro do cubo\b/gi, 'Un cubo conductor macizo posee una cavidad esférica cuyo centro coincide con el centro del cubo'],
    [/\bNo centro da cavidade há uma carga pontual\b/gi, 'En el centro de la cavidad hay una carga puntual'],
    [/\bAlém da carga no centro da cavidade, o condutor maciço está carregado com uma carga total líquida\b/gi, 'Además de la carga en el centro de la cavidad, el conductor macizo está cargado con una carga total neta'],
    [/\ba carga (.+?) na superfície da cavidade esférica\b/gi, 'la carga $1 en la superficie de la cavidad esférica'],
    [/\ba carga (.+?) em cada uma das (.+?) faces externas do cubo\b/gi, 'la carga $1 en cada una de las $2 caras externas del cubo'],
    [/\bPartículas de carga (.+?) e massa (.+?) são aceleradas a partir do repouso\b/gi, 'Partículas de carga $1 y masa $2 son aceleradas a partir del reposo'],
    [/\bpor uma diferença de potencial\b/gi, 'por una diferencia de potencial'],
    [/\bEm seguida, as partículas entram numa região com campo magnético uniforme\b/gi, 'A continuación, las partículas entran en una región con campo magnético uniforme'],
    [/\bperpendicular à velocidade das mesmas\b/gi, 'perpendicular a su velocidad'],
    [/\be passam a descrever uma trajetória circular de raio\b/gi, 'y pasan a describir una trayectoria circular de radio'],
    [/\bO gráfico apresenta os resultados para os valores de (.+?) obtidos variando-se a diferença de potencial\b/gi, 'El gráfico presenta los resultados para los valores de $1 obtenidos al variar la diferencia de potencial'],
    [/\bQual é o valor da razão q\/m dessas partículas\?\b/gi, '¿Cuál es el valor de la razón q/m de esas partículas?'],
    [/\bUma barra condutora de comprimento (.+?), resistência elétrica (.+?) e massa (.+?) pode deslizar sem atrito sobre um par de trilhos\b/gi, 'Una barra conductora de longitud $1, resistencia eléctrica $2 y masa $3 puede deslizar sin fricción sobre un par de rieles'],
    [/\bcondutores paralelos e horizontais de resistência desprezível\b/gi, 'conductores paralelos y horizontales de resistencia despreciable'],
    [/\bUm campo magnético uniforme (.+?) é perpendicular ao plano dos trilhos e a barra encontra-se inicialmente em repouso\b/gi, 'Un campo magnético uniforme $1 es perpendicular al plano de los rieles y la barra se encuentra inicialmente en reposo'],
    [/\bUma bateria de força eletromotriz (.+?) e resistência interna nula é conectada entre os dois trilhos no instante\b/gi, 'Una batería de fuerza electromotriz $1 y resistencia interna nula se conecta entre los dos rieles en el instante'],
    [/\bgerando uma corrente inicial\b/gi, 'generando una corriente inicial'],
    [/\ba força (.+?) que age sobre a barra em função da sua velocidade\b/gi, 'la fuerza $1 que actúa sobre la barra en función de su velocidad'],
    [/\ba velocidade (.+?) da barra quando a corrente for igual a\b/gi, 'la velocidad $1 de la barra cuando la corriente sea igual a'],
    [/\bdo seu valor inicial\b/gi, 'de su valor inicial'],
    [/\bRadiação eletromagnética monocromática, de intensidade uniforme, incide perpendicularmente sobre uma placa metálica polida\b/gi, 'Radiación electromagnética monocromática, de intensidad uniforme, incide perpendicularmente sobre una placa metálica pulida'],
    [/\bde formato quadrado e de área\b/gi, 'de forma cuadrada y de área'],
    [/\bde formato circular e de área\b/gi, 'de forma circular y de área'],
    [/\bA placa reflete (.+?) da intensidade da radiação incidente e absorve o restante na superfície\b/gi, 'La placa refleja $1 de la intensidad de la radiación incidente y absorbe el resto en la superficie'],
    [/\bOs campos elétrico e magnético da radiação incidente são dados, respectivamente, pelas partes reais das seguintes expressões:\b/gi, 'Los campos eléctrico y magnético de la radiación incidente están dados, respectivamente, por las partes reales de las siguientes expresiones:'],
    [/\bQual é a força média (.+?) que a radiação exerce sobre a placa metálica\?\b/gi, '¿Cuál es la fuerza media $1 que la radiación ejerce sobre la placa metálica?'],

    // General mechanics & physics terminology
    [/\bUm recipiente muito longo de massa\b/gi, 'Un recipiente muy largo de masa'],
    [/\bUm recipiente de massa\b/gi, 'Un recipiente de masa'],
    [/\bUm recipiente\b/gi, 'Un recipiente'],
    [/\bUma partícula\b/gi, 'Una partícula'],
    [/\bUma esfera homogênea\b/gi, 'Una esfera homogénea'],
    [/\bUma esfera sólida\b/gi, 'Una esfera sólida'],
    [/\bUma esfera condutora\b/gi, 'Una esfera conductora'],
    [/\bUma esfera\b/gi, 'Una esfera'],
    [/\bUm cilindro condutor\b/gi, 'Un cilindro conductor'],
    [/\bUm cilindro\b/gi, 'Un cilindro'],
    [/\bUm disco homogêneo\b/gi, 'Un disco homogéneo'],
    [/\bUm disco\b/gi, 'Un disco'],
    [/\bUm bloco\b/gi, 'Un bloque'],
    [/\bUm vagão\b/gi, 'Un vagón'],
    [/\bUm feixe de luz não polarizada\b/gi, 'Un haz de luz no polarizada'],
    [/\bUm feixe de luz\b/gi, 'Un haz de luz'],
    [/\bUm feixe de nêutrons\b/gi, 'Un haz de neutrones'],
    [/\bUm feixe de elétrons\b/gi, 'Un haz de electrones'],
    [/\bUm elétron\b/gi, 'Un electrón'],
    [/\bUm próton\b/gi, 'Un protón'],
    [/\bUm gás ideal\b/gi, 'Un gas ideal'],
    [/\bUm oscilador harmônico quântico\b/gi, 'Un oscilador armónico cuántico'],
    [/\bUm oscilador harmônico\b/gi, 'Un oscilador armónico'],
    [/\bUm circuito constituído por\b/gi, 'Un circuito constituido por'],
    [/\bDuas partículas\b/gi, 'Dos partículas'],
    [/\bUma haste muito fina e homogênea\b/gi, 'Una varilla muy fina y homogénea'],
    [/\bUma haste\b/gi, 'Una varilla'],
    [/\bConsidere que\b/gi, 'Considere que'],
    [/\bConsidere um\b/gi, 'Considere un'],
    [/\bConsidere uma\b/gi, 'Considere una'],
    [/\bConsidere dois\b/gi, 'Considere dos'],
    [/\bConsidere as seguintes\b/gi, 'Considere las siguientes'],
    [/\bConsidere as afirmações a seguir\b/gi, 'Considere las siguientes afirmaciones'],
    [/\bConsidere\b/gi, 'Considere'],
    [/\bSuponha que\b/gi, 'Suponga que'],

    // Motion & Mechanics Terms
    [/\bmove-se sobre um plano horizontal sem atrito com velocidade constante\b/gi, 'se mueve sobre un plano horizontal sin fricción con velocidad constante'],
    [/\bmove-se sobre um plano horizontal sem atrito\b/gi, 'se mueve sobre un plano horizontal sin fricción'],
    [/\bmove-se sobre um plano horizontal\b/gi, 'se mueve sobre un plano horizontal'],
    [/\bmove-se com velocidade constante\b/gi, 'se mueve con velocidad constante'],
    [/\bmove-se ao longo de\b/gi, 'se mueve a lo largo de'],
    [/\bmove-se\b/gi, 'se mueve'],
    [/\bdesliza sem rolar\b/gi, 'desliza sin rodar'],
    [/\brola sem deslizar\b/gi, 'rueda sin deslizar'],
    [/\bcom velocidade constante\b/gi, 'con velocidad constante'],
    [/\binicialmente em repouso\b/gi, 'inicialmente en reposo'],
    [/\bem repouso\b/gi, 'en reposo'],
    [/\bno instante\b/gi, 'en el instante'],
    [/\ba partir do instante\b/gi, 'a partir del instante'],
    [/\ba partir do repouso\b/gi, 'a partir del reposo'],
    [/\badentra uma região onde\b/gi, 'entra en una región donde'],
    [/\bé despejado verticalmente\b/gi, 'se vierte verticalmente'],
    [/\ba uma taxa constante\b/gi, 'a una tasa constante'],
    [/\bmassa por unidade de tempo\b/gi, 'masa por unidad de tiempo'],
    [/\bcomo ilustra a figura\b/gi, 'como ilustra la figura'],
    [/\bcomo indicado na figura\b/gi, 'como se indica en la figura'],
    [/\bmostrado na figura\b/gi, 'mostrado en la figura'],
    [/\bveja a figura\b/gi, 'ver la figura'],
    [/\bna figura abaixo\b/gi, 'en la figura de abajo'],
    [/\bchoque perfeitamente inelástico\b/gi, 'choque perfectamente inelástico'],
    [/\bchoque perfeitamente elástico\b/gi, 'choque perfectamente elástico'],
    [/\bcolisão elástica\b/gi, 'colisión elástica'],
    [/\bcolisão inelástica\b/gi, 'colisión inelástica'],
    [/\bSendo (.+?) a posição do recipiente e (.+?) sua velocidade\b/gi, 'Siendo $1 la posición del recipiente y $2 su velocidad'],
    [/\bSendo\b/gi, 'Siendo'],
    [/\be sua velocidade\b/gi, 'y su velocidad'],
    [/\ba posição\b/gi, 'la posición'],
    [/\bo coeficiente de atrito\b/gi, 'el coeficiente de fricción'],
    [/\ba aceleração da gravidade\b/gi, 'la aceleración de la gravedad'],
    [/\bdesprezando a resistência do ar\b/gi, 'despreciando la resistencia del aire'],
    [/\bdesprezando o atrito\b/gi, 'despreciando la fricción'],
    [/\bpequenas amplitudes\b/gi, 'pequeñas amplitudes'],

    // Electromagnetism, Quantum & Thermal Terms
    [/\bcampo elétrico\b/gi, 'campo eléctrico'],
    [/\bcampo magnético\b/gi, 'campo magnético'],
    [/\bpotencial elétrico\b/gi, 'potencial eléctrico'],
    [/\bdiferença de potencial\b/gi, 'diferencia de potencial'],
    [/\bdensidade de carga\b/gi, 'densidad de carga'],
    [/\bdensidade superficial de carga\b/gi, 'densidad superficial de carga'],
    [/\bdensidade volumétrica de carga\b/gi, 'densidad volumétrica de carga'],
    [/\bdensidade linear de carga\b/gi, 'densidad linear de carga'],
    [/\bforça eletromotriz\b/gi, 'fuerza electromotriz'],
    [/\bonda eletromagnética plana\b/gi, 'onda electromagnética plana'],
    [/\bno vácuo\b/gi, 'en el vacío'],
    [/\bpropagando-se na direção\b/gi, 'propagándose en la dirección'],
    [/\bvetor de Poynting\b/gi, 'vector de Poynting'],
    [/\bmédia temporal do módulo\b/gi, 'media temporal del módulo'],
    [/\bcapacitor de capacitância\b/gi, 'condensador de capacitancia'],
    [/\bindutor de indutância\b/gi, 'inductor de inductancia'],
    [/\bcapacitor encontra-se inicialmente carregado\b/gi, 'el condensador se encuentra inicialmente cargado'],
    [/\bchave do circuito é fechada\b/gi, 'el interruptor del circuito se cierra'],
    [/\bgráfico que melhor representa\b/gi, 'gráfico que mejor representa'],
    [/\bestão representados possíveis gráficos\b/gi, 'se representan posibles gráficos'],
    [/\bem função do tempo\b/gi, 'en función del tiempo'],
    [/\bnível fundamental\b/gi, 'nivel fundamental'],
    [/\bestado fundamental\b/gi, 'estado fundamental'],
    [/\bpoço de potencial infinito\b/gi, 'pozo de potencial infinito'],
    [/\bfunção de onda\b/gi, 'función de onda'],
    [/\bfunção de partição\b/gi, 'función de partición'],
    [/\bensemble canônico\b/gi, 'ensamble canónico'],
    [/\bensemble microcanônico\b/gi, 'ensamble microcanónico'],
    [/\bgrande canônico\b/gi, 'gran canónico'],
    [/\bcalor específico\b/gi, 'calor específico'],
    [/\bcapacidade térmica\b/gi, 'capacidad térmica'],

    // Question Actions & Prompts
    [/\bindique a alternativa que contém a equação correta do movimento\b/gi, 'indique la alternativa que contiene la ecuación correcta del movimiento'],
    [/\bindique a alternativa correta\b/gi, 'indique la alternativa correcta'],
    [/\bAssinale a alternativa correta quanto ao efeito\b/gi, 'Marque la alternativa correcta respecto al efecto'],
    [/\bAssinale a alternativa correta\b/gi, 'Marque la alternativa correcta'],
    [/\bAssinale abaixo a alternativa que melhor representa\b/gi, 'Marque abajo la alternativa que mejor representa'],
    [/\bSelecione a alternativa verdadeira\b/gi, 'Seleccione la alternativa verdadera'],
    [/\bQual é o valor de\b/gi, '¿Cuál es el valor de'],
    [/\bQual é a energia\b/gi, '¿Cuál es la energía'],
    [/\bQual é o módulo de\b/gi, '¿Cuál es el módulo de'],
    [/\bQual das alternativas abaixo é a correta\b/gi, '¿Cuál de las siguientes alternativas es la correcta'],
    [/\bDetermine o valor de\b/gi, 'Determine el valor de'],
    [/\bDetermine a frequência\b/gi, 'Determine la frecuencia'],
    [/\bDetermine o trabalho\b/gi, 'Determine el trabajo'],
    [/\bApenas as afirmações I e II são corretas\b/gi, 'Solo las afirmaciones I y II son correctas'],
    [/\bApenas as afirmações II e III são corretas\b/gi, 'Solo las afirmaciones II y III son correctas'],
    [/\bApenas as afirmações I e III são corretas\b/gi, 'Solo las afirmaciones I y III son correctas'],
    [/\bApenas as afirmações I e II são verdadeiras\b/gi, 'Solo las afirmaciones I y II son verdaderas'],
    [/\bApenas a afirmação I é correta\b/gi, 'Solo la afirmación I es correcta'],
    [/\bApenas a afirmação II é correta\b/gi, 'Solo la afirmación II es correcta'],
    [/\bApenas a afirmação III é correta\b/gi, 'Solo la afirmación III es correcta'],
    [/\bApenas a afirmação I é verdadeira\b/gi, 'Solo la afirmación I es verdadera'],
    [/\bApenas a afirmação II é verdadeira\b/gi, 'Solo la afirmación II es verdadera'],
    [/\bApenas a afirmação III é verdadeira\b/gi, 'Solo la afirmación III es verdadera'],
    [/\bAs afirmações I, II e III são verdadeiras\b/gi, 'Las afirmaciones I, II y III son verdaderas'],
    [/\bTodas as afirmações são corretas\b/gi, 'Todas las afirmaciones son correctas'],
    [/\bNenhuma das outras alternativas\b/gi, 'Ninguna de las otras alternativas'],
    [/\bonde o momento canônico é\b/gi, 'donde el momento canónico es'],
    [/\bonde (.+?) e (.+?) são constantes\b/gi, 'donde $1 y $2 son constantes'],
    [/\bonde (.+?) é uma constante\b/gi, 'donde $1 es una constante'],
    [/\bonde\b/gi, 'donde'],
    [/\bdado por\b/gi, 'dado por'],
    [/\bé dada por\b/gi, 'es dada por'],
    [/\bsão dadas por\b/gi, 'son dadas por'],
    [/\bisto é\b/gi, 'es decir'],
    [/\bPede-se:\b/gi, 'Se pide:']
  ];

  for (const [pattern, repl] of replacements) {
    tokenized = tokenized.replace(pattern, repl);
  }

  // 3. Restore math tokens
  return tokenized.replace(/___MATH_TOKEN_(\d+)___/g, (_, idx) => {
    return mathTokens[parseInt(idx, 10)] || '';
  });
}

/**
 * Renders mathematical expressions using KaTeX.
 */
export function renderMathInString(text: string): string {
  if (!text) return '';

  let processed = text;

  // 1. Render Block Math: $$ ... $$
  processed = processed.replace(/\$\$([\s\S]*?)\$\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: true, throwOnError: false });
    } catch {
      return `<div class="katex-block my-2 overflow-x-auto text-center font-serif">$$${escapeHtml(math)}$$</div>`;
    }
  });

  // 2. Render Inline Math: $ ... $
  processed = processed.replace(/\$([^\$\r\n]+?)\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: false, throwOnError: false });
    } catch {
      return `<span class="katex-inline font-serif font-semibold">$${escapeHtml(math)}$</span>`;
    }
  });

  // 3. Auto-render isolated LaTeX commands without $ like \frac{...}{...}, \sqrt{...}, \omega, \hbar, etc.
  processed = processed.replace(/(\\(?:frac|sqrt|vec|hat|dot|ddot|hbar|varepsilon|mu|omega|alpha|beta|gamma|theta|lambda|sigma|phi|psi|nabla|int|oint|sum|prod|partial|pm|mp|approx|le|ge|ne|times|cdot|in|to|infty)\b(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}|\[[^\[\]]*\]|[a-zA-Z0-9_\^\{\}])*)/g, (match) => {
    try {
      return katex.renderToString(match, { displayMode: false, throwOnError: false });
    } catch {
      return match;
    }
  });

  // 4. Convert line breaks
  return processed.replace(/\n/g, '<br/>');
}

export interface ParsedQuestionResult {
  statementHtml: string;
  options: { letter: string; html: string }[];
}

/**
 * Robust two-pass question statement and multiple choice options extractor.
 * Completely prevents any nested options or false-matching of Portuguese articles.
 */
export function parseAndRenderQuestion(rawText: string, lang: 'pt' | 'es' | 'en' = 'pt'): ParsedQuestionResult {
  if (!rawText) {
    return { statementHtml: '', options: [] };
  }

  const lines = rawText.split('\n').map(l => l.trim()).filter(l => l.length > 0);

  // Find the exact line index where options A, B, C, D, E start
  let optStartIdx = -1;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Check if line matches an option header like 'A ', 'A.', '(A)', 'A)'
    const isOptHeader = /^(?:\([A-E]\)|[A-E][\.\:\)]|[A-E])\s+(?:[A-Za-z0-9\$\\\+\-\/\(\)]|\=)/.test(line) || /^[A-E]$/.test(line);

    if (isOptHeader) {
      // Guard against false positive Portuguese sentences starting with "A ..."
      const isArticleStart = /^[A-E]\s+(?:lagrangiana|partícula|haste|esfera|placa|figura|amostra|barra|carga|corrente|tensão|velocidade|função|energia|diferença|área|distribuição|constante|massa|posição|força|intensidade|radiação|frequência)\b/i.test(line);

      if (!isArticleStart) {
        // Verify subsequent lines contain B, C, or D
        const rest = lines.slice(i).join(' ');
        const hasB = /(?:^|\n|\s)(?:\(B\)|B[\.\:\)]|B\s+)/.test(rest);
        const hasC = /(?:^|\n|\s)(?:\(C\)|C[\.\:\)]|C\s+)/.test(rest);
        const hasD = /(?:^|\n|\s)(?:\(D\)|D[\.\:\)]|D\s+)/.test(rest);

        if ((hasB && hasC) || (hasC && hasD)) {
          optStartIdx = i;
          break;
        }
      }
    }
  }

  let statementRaw = '';
  let optionsRaw = '';

  if (optStartIdx !== -1) {
    statementRaw = lines.slice(0, optStartIdx).join('\n');
    optionsRaw = lines.slice(optStartIdx).join('\n');
  } else {
    statementRaw = lines.join('\n');
  }

  // 1. Process Statement
  const statementToRender = lang === 'es' ? translatePortuguesePhysicsToSpanish(statementRaw) : statementRaw;
  const statementHtml = renderMathInString(statementToRender);

  // 2. Process Options (Isolated & strictly non-nested)
  const options: { letter: string; html: string }[] = [];
  if (optionsRaw) {
    const optPattern = /(?:^|\n)\s*(?:\(([A-E])\)|([A-E])[\.\:\)]|([A-E]))\s+/g;
    const matches = Array.from(optionsRaw.matchAll(optPattern));

    for (let i = 0; i < matches.length; i++) {
      const match = matches[i];
      const letter = match[1] || match[2] || match[3];
      const start = match.index! + match[0].length;
      const end = i + 1 < matches.length ? matches[i + 1].index! : optionsRaw.length;
      const optText = optionsRaw.slice(start, end).trim();

      const translatedOptText = lang === 'es' ? translatePortuguesePhysicsToSpanish(optText) : optText;
      options.push({
        letter,
        html: renderMathInString(translatedOptText)
      });
    }
  }

  return { statementHtml, options };
}

export function mathAction(node: HTMLElement, textContent: string | { text: string; lang?: 'pt' | 'es' | 'en' }) {
  function update(content: string | { text: string; lang?: 'pt' | 'es' | 'en' }) {
    if (!content) {
      node.innerHTML = '';
      return;
    }
    if (typeof content === 'string') {
      node.innerHTML = renderMathInString(content);
    } else {
      const rendered = parseAndRenderQuestion(content.text, content.lang || 'pt');
      let combined = `<div class="statement-part mb-3">${rendered.statementHtml}</div>`;
      if (rendered.options && rendered.options.length > 0) {
        combined += `<div class="options-part space-y-2 mt-3 pt-3 border-t border-slate-200 dark:border-slate-800">`;
        for (const o of rendered.options) {
          combined += `<div class="flex items-start gap-2 text-sm"><span class="font-bold text-sky-500">${o.letter})</span> <div>${o.html}</div></div>`;
        }
        combined += `</div>`;
      }
      node.innerHTML = combined;
    }
  }

  update(textContent);

  return {
    update(newContent: string | { text: string; lang?: 'pt' | 'es' | 'en' }) {
      update(newContent);
    }
  };
}
