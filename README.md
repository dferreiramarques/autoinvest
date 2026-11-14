# Auto / Investimento v3
Simulador independente de compra de usados em Portugal. Sem dependências.

## Executar
Abrir index.html com engines.js na mesma pasta, ou `python -m http.server 8000`. No GitHub Pages, publicar a raiz do repositório (Settings → Pages → Deploy from a branch).

## Dados
15 famílias iniciais ilustrativas, não verificadas documentalmente. Não representam frequências de avaria. Confirmar código e versão. Catálogo local, sem ligação ao Standvirtual. engines.json é a fonte editável; executar `python build_db.py` após alterações. Reserva é pressuposto editável, não previsão.

## IA
Opcional, OpenRouter: introduzir chave pessoal e ID de modelo disponível. A chave não é persistida; informações do veículo são transmitidas ao fornecedor. Limites, disponibilidade e custos dependem do modelo; escolher explicitamente um modelo gratuito. Não publicar chaves. Respostas não verificadas, sem integração automática no cálculo.

## Modelo financeiro
TCO = preço − residual + custos iniciais + custos correntes. Cenários variam apenas a reserva anual. Sem inflação nem portagens.

## Validação
Verificação de sintaxe JS e dados JSON; teste de browser e API pendente.
