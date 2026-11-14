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

## v4.0 — Capital & Ownership
Novo, seminovo e usado; depreciação inicial distinta para novo; manutenção crescente, garantia indicativa, estacionamento, financiamento amortizado, património líquido e capital remanescente. Prioridades pessoais ponderadas e emissões opcionais introduzidas pelo utilizador. O saldo de capital não inclui rendimentos familiares e pode ser negativo; comparação exige igual orçamento inicial. Taxas e reservas são pressupostos, não previsões. Dados de motor provisórios. A chave OpenRouter não é persistida. Dados v2 locais mantidos; avaliações antigas usam valores de fallback para novos campos. Teste de sintaxe JS realizado; browser e API não testados.

## v5 — Market Intelligence
Indicadores IHPC Eurostat para novos/usados, PT/UE, variações 1/3/6/12/60 meses. O cache inicial está vazio (sem valores inventados). Em Actions > Update market data > Run workflow, executar a primeira recolha; depois corre diariamente. Se necessário autorizar escrita em Settings > Actions. A atualização valida os rótulos e preserva o cache se faltar uma série. Os códigos e endpoints necessitam de validação em produção; caso a classificação Eurostat mude, ajustar market.py. Commits por GITHUB_TOKEN podem não disparar a publicação Pages: usar publicação manual ou workflow Pages próprio. Em modo file:// o fetch pode ser bloqueado; servir via HTTP. Buy or Wait usa cenário editável, não previsão.

## v5.1
Consulta direta ao Eurostat (prc_hicp_minr, ECOICOP 2, I25), com cache e diagnóstico de erros. O workflow usa o mesmo dataset. Se o browser bloquear CORS, executar Update market data em Actions e aguardar publicação. Não foram efetuados testes de rede neste ambiente.

## v5.2
Parâmetros de compra primeiro; mercado no final. Tentativas alternativas de índice I25/I15; cache parcial preservado. Consulte os logs de Actions se a API falhar. A integração ao vivo não foi testada neste ambiente.
