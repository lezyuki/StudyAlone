## var
Escopo: Escopo de função. Se declarada fora de uma função, a variável é global.
Hoisting: Variáveis declaradas com var são "hoisted" para o topo do seu escopo, mas a inicialização não é. Isso significa que elas podem ser referenciadas antes da sua declaração, mas terão valor undefined até a linha de inicialização.
Reatribuição e Redefinição: Pode ser reatribuída e redefinida.

## let
Escopo: Escopo de bloco. Está disponível apenas dentro do bloco onde foi declarada.
Hoisting: Variáveis declaradas com let também são "hoisted", mas diferentemente de var, não podem ser acessadas antes da declaração, resultando em um erro de referência se tentarem ser acessadas antes de sua inicialização.
Reatribuição e Redefinição: Pode ser reatribuída, mas não redefinida no mesmo escopo.

## const
Escopo: Escopo de bloco, assim como let.
Hoisting: Mesmo comportamento de hoisting que let. Não pode ser acessada antes da declaração.
Reatribuição e Redefinição: Não pode ser reatribuída nem redefinida. A constante deve ser inicializada na declaração.

## var: Escopo de função, hoisting, pode ser reatribuída e redefinida.

## let: Escopo de bloco, hoisting, pode ser reatribuída mas não redefinida.

## const: Escopo de bloco, hoisting, não pode ser reatribuída nem redefinida.


Essas diferenças fazem com que let e const sejam preferidos em JavaScript moderno para evitar bugs relacionados a escopo e hoisting que são comuns com var.









