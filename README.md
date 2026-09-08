# Spark — evento Goiânia (21/09)

Landing do evento presencial **"O que é hype e o que é real na IA?"** — palestra do
Oliver Cunningham, com mediação de Marcelo Aquino, no HUB Cerrado, Goiânia/GO,
21 de setembro, das 08h30 às 10h30. Realização Ganplo · Ionix.

Reconstrução da landing anterior (`papaya-squirrel-5dc4d7.netlify.app`) na
**identidade visual canônica da Ionix**: violeta `#A855F7`, fundo `#0A0A0A`,
faixa gradient violeta→magenta→ciano, Montserrat + JetBrains Mono nos eyebrows.
O conteúdo é o mesmo da versão anterior — só o design mudou.

Página estática (HTML/CSS/JS vanilla, sem build), pra carregar rápido no wifi de evento.

## Estrutura

```
index.html    landing + widget de inscrição (TechConversa)
styles.css    identidade Ionix
assets/       arte do evento, retrato do palestrante, logos e favicons
arte/         fonte da arte do evento (HTML) + os formatos exportados
netlify.toml  config de deploy
```

## Arte do evento

A peça original (Ganplo) está preservada em `arte/original-ganplo.jpg`. A versão
em uso é refeita na identidade Ionix, com a foto real do Oliver recortada do
fundo de estúdio — `arte/oliver_arte.png`.

A arte é desenhada em HTML (`arte/arte.html`) e exportada com Chrome headless.
Para regerar os três formatos:

```
cd arte && python gerar_artes.py
```

Sai `arte-feed-4x5.jpg` (1080×1350, feed), `arte-quadrada-1x1.jpg` (1080×1080)
e `arte-story-9x16.jpg` (1080×1920, stories). O feed 4:5 é o que alimenta
`assets/evento-goiania.jpg` no hero da landing — ao trocar a arte, copiar o novo
export por cima desse arquivo.

Os logos Ganplo e HUB Cerrado foram extraídos da peça original (branco sobre
transparente). Se aparecerem os arquivos vetoriais, substituir
`arte/logo_ganplo.png` e `arte/logo_hubcerrado.png`.

## Deploy em produção

Site estático, sem build e sem dependência. O `netlify.toml` já traz
`publish = "."` e build vazio.

**Opção A — conectar este repo no Netlify (recomendado)**

Add new site → Import an existing project → GitHub → `Ionix-Tech/spark-evento-goiania`.
Não precisa preencher build command nem publish directory: vêm do `netlify.toml`.
A partir daí, todo push na `main` republica sozinho.

**Opção B — deploy manual pela CLI**

```
npm i -g netlify-cli
netlify deploy --prod --dir=.
```

### Formulário de inscrição

As novas inscrições usam o widget **TechConversa** configurado pela Maeli,
formulário `Pr4lBjSN`. Os dois botões abrem o popup; caso o script não carregue,
levam ao formulário direto: https://app.techconversa.com.br/form/Pr4lBjSN.
Há também um link direto independente no rodapé. Links antigos com
`#inscricao` são convertidos para `#form-Pr4lBjSN`.

Campos, obrigatoriedade, mensagem de sucesso e automações são geridos no
TechConversa. A configuração aprovada mantém nome, WhatsApp, e-mail, empresa,
setor e cargo obrigatórios; faturamento opcional; sem checkbox de consentimento.
A mensagem do provedor anuncia comunicação por e-mail e WhatsApp.

O envio antigo ao Netlify Forms foi removido da página. Nenhum registro antigo
foi apagado ou migrado: consultar o histórico no Netlify separadamente.
Após publicar, fazer uma inscrição real e confirmar o recebimento com a Maeli;
abrir o popup não comprova gravação nem entrega das automações.

### Sobre o site que já está no ar

O site atual é https://eventoionixgoiania.netlify.app, conectado à main.
Para atualização manual, usar a pasta `deploys/eventoionixgoiania-manual`
do workspace, no projeto Netlify existente.

## Assets

- `evento-goiania.jpg` — arte do hero na identidade Ionix, com a foto do PPT,
  Oliver como palestrante e Marcelo Aquino como mediador
- `oliver-cunningham-ppt.png` — foto indicada pela Maeli e extraída do mini-CV
  `OEC Mini CV.pptx`; usada na seção do palestrante com recorte responsivo em CSS.
- `oliver-cunningham.jpg` — foto anterior, preservada no repo como referência e
  sem uso na landing atual.
- `ionix-logo-dark.png` — logo Ionix negativo (fundo escuro)
- `ionix-logo-light.png` — logo Ionix positivo (fundo claro), não usado hoje
